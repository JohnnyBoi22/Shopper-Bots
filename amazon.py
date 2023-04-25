import bottlenose
import xml.etree.ElementTree as ET

# Define API credentials
AWS_ACCESS_KEY_ID = 'your_aws_access_key_id'
AWS_SECRET_ACCESS_KEY = 'your_aws_secret_access_key'
AWS_ASSOCIATE_TAG = 'your_aws_associate_tag'

# Initialize API client
amazon = bottlenose.Amazon(
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_ASSOCIATE_TAG,
    Region='US' # Change region if necessary
)

# Define keyword to search for
keyword = 'iphone'

# Send request to API
response = amazon.ItemSearch(
    Keywords=keyword,
    SearchIndex='All', # Change search index if necessary
    Sort='price',
    ItemPage=1, # Change page number if necessary
    ResponseGroup='Small'
)

# Parse XML response
root = ET.fromstring(response)
items = root.findall('.//Item')

# Print information for each item
for item in items:
    title = item.find('.//Title').text
    price = item.find('.//FormattedPrice').text
    url = item.find('.//DetailPageURL').text
    print(title, price, url)

