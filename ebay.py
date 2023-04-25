import requests
import xml.etree.ElementTree as ET

# Define API credentials
APP_ID = 'your_ebay_app_id'

# Define endpoint URL and request parameters
url = 'https://svcs.ebay.com/services/search/FindingService/v1'
params = {
    'OPERATION-NAME': 'findItemsByKeywords',
    'SERVICE-VERSION': '1.0.0',
    'SECURITY-APPNAME': APP_ID,
    'RESPONSE-DATA-FORMAT': 'XML',
    'REST-PAYLOAD': '',
    'keywords': 'iphone', # Change keyword if necessary
    'paginationInput': {
        'pageNumber': '1', # Change page number if necessary
        'entriesPerPage': '10' # Change number of results per page if necessary
    },
    'sortOrder': 'PricePlusShippingLowest' # Change sort order if necessary
}

# Send request to API
response = requests.get(url, params=params)

# Parse XML response
root = ET.fromstring(response.text)
items = root.findall('.//{http://www.ebay.com/marketplace/search/v1/services}item')

# Print information for each item
for item in items:
    title = item.find('.//{http://www.ebay.com/marketplace/search/v1/services}title').text
    price = item.find('.//{http://www.ebay.com/marketplace/search/v1/services}currentPrice').text
    url = item.find('.//{http://www.ebay.com/marketplace/search/v1/services}viewItemURL').text
    print(title, price, url)

