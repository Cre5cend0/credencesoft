from utilities.logger import logger
from utilities.setup import setup_bs

log = logger()


def pagination_size(url):
    """
    requires one parameter: a webpage url with a pagination object -> str
    returns number of pages of products in a given category -> int
    """
    soup = setup_bs(url)  # setting up soup object for the given url
    size = 1  # for categories with just one page worth of products
    try:
        log.info('Searching for pagination item')
        pages = soup.select('.cw-pagination__list-item')[-2]  # identify the last but one'th item in the pagination list
        size = int(pages.text)  # extracting text as a string and converting it to an integer for iterative purposes
    except IndexError:
        log.warning("No pagination item in the provided URL")

    finally:
        return size
