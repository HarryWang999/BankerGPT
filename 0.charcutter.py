import json

# load from files
inputfilename = "datasets/EXTRACTED_FILINGS/320193_10K_2013_0001193125-13-416534.json"

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