# Tech Assessment - Credencesoft

This document covers Get Started instructions, assessment questions, timeline and any concerns related to it.

---
## Getting started:

1. Git clone repository to your local machine
2. Run `pip install -r requirements.txt` to install dependencies
3. Run main.py

### Config:
>> 1. Navigate to utilities > setup.py to change headers for beautiful soup
>> 2. Navigate to utilities > logger.py and set file handler location
>> 3. navigate to utilities > config.py to change selenium web drivers locations or base URL (Optional)
___

### Question:
> 1. How do you extract categories of dog food from the page (https://www.chewy.com/b/dog-288). Explain and write a python script.
> 2. write a python script to get each product url in for dog food , wet-food category (https://www.chewy.com/b/dog-288)
> 3. write a function to detect how many pages of products in a category. So given the category url the function should output the number of pages
> 4. Write a python script for extracting the following attributes in a product url, for example https://www.chewy.com/pedigree-adult-complete-nutrition/dp/141438
>> - ProductName and Description
>> - Size
>> - Ingredients
>> - Images (all image location hrefs)
>> - Categories
>> - Key Benefits
>> - Brand (Manufacture)
>> - Price (for each packaging size)

### Answer:

All scripts are located in core_files directory with adequate comments. Some concerns are listed below

1. To extract the categories of dog food in the simplest way, I found the parent element which hosted all the category elements. 
I then extracted text from each child element by iterating over the list. 
I could also extract link if needed. Using a class to extract the categories was not an option 
here as there were other pet types using similar class name.

2. I extracted the URL from each product by visiting the product page and navigated to different pages using the 
BASE_URL + CATEGORY_PAGE variables set on top of the script. This way, if we need to extract products for a different 
category, all we need to do is change these variables.

3. Pretty straight forward. Could have used Requests-HTML - pagination method,
but decided against it and kept it 

4. This was fun to do: 
I extracted all attributes from the page and attached them to a csv file in a basic format for demonstration purposes. However, 
I could not extract "Categories" as there is no such section on the product page. It belongs to just one category.
I also could not extract the price for all package sizes as the packages are generated through javascript running on
the browser after and beautifulsoup could not locate the package size elements. 
I even used HTML-requests package, but got an error that I had no access. 
Something in my headers is probably missing or the page has not provided access to that section.  

___ 

### Timeline:

Overall, the project took me about 8 hours in total to complete as I was a beginner to using beautifulsoup.

- 30 minutes to Setting up the project files and structure
- 60 minutes of beautiful soup tutorials on youtube and freecodecamp
- 30 minutes to figure out what is headers, why is it needed and why my headers were incorrect initially
- 120 minutes to code all the core files
- 120 minutes to test different scenarios and debug code
- 120 minutes to optimise the code, documentation and improvements
