from utilities.setup import setup_bs
from utilities.logger import logger
import csv

log = logger()


def product_details(url):
    """
    requires one parameter: a webpage url -> str
    returns a dictionary object with product details -> dict
        - Product Name
        - Brand (Manufacturer)
        - Product Description
        - Ingredients
        - Key Benefits
        - Images (all image location hrefs)
        - Price (for default packaging size)
    """

    details = {}  # initialising an empty main_dict for all details
    soup = setup_bs(url)  # initialising a soup object

    '-------------------------******************------------------------------------'
    log.info('getting product name')
    name = soup.find('div', id='product-title').h1.text

    '-------------------------******************------------------------------------'
    log.info("Getting manufacturer's name")
    brand = soup.find('div', id="product-subtitle").span.text

    '-------------------------******************------------------------------------'
    log.info("getting product description paragraph")
    info = soup.find('section', class_='descriptions__content')
    desc = info.p.text

    '-------------------------******************------------------------------------'
    log.info("getting Ingredients details")
    constituents = soup.find('article', id='Nutritional-Info').p.text

    '-------------------------******************------------------------------------'
    log.info("getting list of items in Key Benefits")
    benefits_list = info.ul.find_all('li')
    key_benefits = []
    for item in benefits_list:
        key_benefits.append(item.text)

    '-------------------------******************------------------------------------'
    log.info("getting all high res product images")
    product_images = []
    image_block = soup.find('div', id='media-selector')
    images = image_block.find_all('a')

    for image in images:
        source = image.get('href')
        if source:
            if source == '#':
                continue
            link = "https:" + source
            product_images.append(link)

    '-------------------------******************------------------------------------'
    log.info("getting the price of a product for the default packaging size")
    cost = soup.find('span', class_='ga-eec__price').text

    '-------------------------******************------------------------------------'
    # Creating a dictionary with all the details
    log.info("Adding all values to the main_dict")
    details['Name'] = name.lstrip()  # product name
    details["Manufacturer"] = brand  # product manufacturer
    details["Description"] = desc  # product description
    details['Ingredients'] = constituents.lstrip()  # product ingredients
    details["Key Benefits"] = key_benefits  # product key benefits
    details["Product Images"] = product_images  # product high res images
    details['Price'] = cost.lstrip()  # product price

    '-------------------------******************------------------------------------'
    # generating csv file with the details
    csv_file = open("./reports/product_details.csv", "w")
    csv_writer = csv.writer(csv_file)

    columns = []
    rows = []
    for key, value in details.items():
        columns.append(key)
        rows.append(value)

    csv_writer.writerow(columns)
    csv_writer.writerow(rows)

    csv_file.close()

    return details
