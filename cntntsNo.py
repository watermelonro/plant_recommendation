import requests
from bs4 import BeautifulSoup

cntnts_no_list = [] 
pageNo = 1

try:
    while True:
        # Send GET request to the API URL
        url = 'http://api.nongsaro.go.kr/service/garden/gardenList'
        params = {
            'apiKey': '20230522VOBNQFUDC7WSEYSSB8QZQ',
            'pageNo': pageNo
        }
        response = requests.get(url, params=params)

        # Check if the request was successful
        response.raise_for_status()

        # Parse the XML response
        soup = BeautifulSoup(response.content, 'xml')

        # Extract the contents within the <cntntsNo> tags
        current_cntnts_no_list = [tag.text for tag in soup.find_all('cntntsNo')]
        cntnts_no_list.extend(current_cntnts_no_list)

        # Check if there are more pages
        if len(current_cntnts_no_list) == 0:
            print("END")
            break

        # Increase pageNo by 1 for the next request
        pageNo += 1

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)

# Print the retrieved contents

    # Save to a text file
with open('list.txt', 'a', newline='') as r:
    r.write('\n'.join(cntnts_no_list) + '\n')





