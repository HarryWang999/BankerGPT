import json
import openai 
import nltk
import openpyxl
from bs4 import BeautifulSoup
# up for checking libraries 

# load from file's name
inputfilename = "datasets/EXTRACTED_FILINGS/"+"320193_10K_2020_0000320193-20-000096.json"

# functions to read from JSON file
def js_r(filename: str):
    with open(filename) as f_in:
        return json.load(f_in)


# call functions, get dict output
my_data = js_r(inputfilename)

# print dict output
# print (my_data)

# 
final_input = my_data['item_8'][:20000]

print (final_input)

# string1 = "hello, this is apple google meta amazon!"
# string2 = string1[:10]

# print (string2)