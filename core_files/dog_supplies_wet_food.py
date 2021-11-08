from utilities.setup import setup_bs
from utilities.logger import logger
from utilities.config import MetaData
from core_files.category_pages import pagination_size

log = logger()
BASE = MetaData.URL + '/b/wet-food'

# change the numbers only in the below variables for accessing different categories
CATEGORY_PAGE_ONE = '-293'
CATEGORY_PAGES_REST = '_c293'


def dog_wet_food():
    """
    return: Every product's url in the given category -> list
    """
    URL = BASE + CATEGORY_PAGE_ONE
    soup = setup_bs(URL)  # setting up base page soup object
    pages = pagination_size(URL)  # getting the total number of pages with products in the category

    # looping through every page to get all product urls
    prod_urls = []
    for page in range(1, pages + 1):
        if page == 1:  # as page 1 is the base url. This 'if' block is executed just once
            log.info(f"Extracting all product's url from page {page}")
            products = soup.find_all('a', class_="product")
            for product in products:
                partial_link = product.get('href')  # acquiring partial link through href attribute
                link = MetaData.URL + partial_link  # concatenating partial link to the base url
                prod_urls.append(link)
        else:
            log.info(f"Extracting all product's url from page {page}")
            # since the url changes as we navigate to other pages when using pagination
            dynamic_url = URL + CATEGORY_PAGES_REST + f'_p{page}'  # passing page numbers to url as it changes
            soup = setup_bs(dynamic_url)
            products = soup.find_all('a', class_="product")  # listing all products in the given page

            # extracting html link for every product in the given page
            for product in products:
                partial_link = product.get('href')  # acquiring partial link through href attribute
                link = MetaData.URL + partial_link  # concatenating partial link to the base url
                prod_urls.append(link)

    return prod_urls
