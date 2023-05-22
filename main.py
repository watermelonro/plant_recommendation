import requests
from bs4 import BeautifulSoup
import csv

# Set authentication key
auth_key = '20230522VOBNQFUDC7WSEYSSB8QZQ'
cntNo = []

try:
    with open('list.txt', 'r', newline='') as cntNoList:
        lines = cntNoList.readlines()
        cntNo.extend([line.strip() for line in lines])

    # Create request object
    for num in cntNo:
        try:
            request = requests.get(f'http://api.nongsaro.go.kr/service/garden/gardenDtl?apiKey={auth_key}&cntntsNo={num}', verify=False)

            # Get response
            response = request.content

            # Parse the XML using BeautifulSoup.
            soup = BeautifulSoup(response, 'xml')

            item_element = soup.find('item')
            if item_element is None:
                continue
            tags = [tag.name for tag in item_element.find_all()]
            
            # Create or append to the CSV file
            with open('gardenDtl.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)

                # Check if the file is empty
                if csvfile.tell() == 0:
                    writer.writerow(tags)  # Write tags as the header row
                    csvfile.seek(0)  # Position file pointer at the beginning

                # Write data for each item
                for item in soup.find_all('item'):
                    row = [item.find(tag).text for tag in tags]
                    writer.writerow(row)
        except Exception as e:
            print(f"An error occurred for cntntsNo {num}: {e}")
except Exception as e:
    print("An error occurred:", e)
