import openai 
import nltk
import openpyxl
import json
from nltk.tokenize import word_tokenize
nltk.download('punkt')  # Download the punkt tokenizer data if not already downloaded
  
with open('gpt_key.txt', 'r') as file:
    openai.api_key = file.read().replace('\n', '')

# openai.api_key = searchkey

# https://openai.com/pricing
model = "gpt-3.5-turbo-1106" #16k tokens ~= 60k char
# 
inputfilename = "datasets/EXTRACTED_FILINGS/"+"320193_10K_2020_0000320193-20-000096.json"


def js_r(filename: str):
    with open(filename) as f_in:
        return json.load(f_in)


load_data = js_r(inputfilename)
data = load_data['item_8'][:20000] # set 50-60k char


#  Income Statement Prompt
role1 = "You are the expert of Finance and Accounting, please tell me about several numbers precisly.Please tell me the financial numbers in this year: Revenue；Cost of Goods Sold；Selling, general and administrative Expense；R&D Expense； Operating Income； Interest Income； Interest Expense； Earnings Before Tax；Net Income (Use the currency from report and format with table )." + " Please generate output vertical in JSON format"

# Balance sheet Prompt
role2 = "You are the expert of Finance and Accounting, please tell me about several numbers precisly.Please tell me the financial numbers:Cash and Cash Equivalents; Accounts Receivable; Inventory; Prepaid Expense; Total current assets；Property and equipment, Goodwill, Intangible assets, Total non-current Asset；Short-term Borrowings, Accounts payable, Accrued Expenses，Total Current Liability；Total Non-current liability,Total Liabilities；Total Equity." + " Please generate output vertical in JSON format"

# additional_request = "please put output into csv format, with double quotation marks, use the column name as the name of each row on the left"
additional_request = "please generate output vertical in JSON format"


# Change the role number to different prompt tasks
messages = [ {"role": "system", "content": role1} ]



# initial run
message = '"'+data+'"' + additional_request
if message: 
    messages.append( 
        {"role": "user", "content": message}, 
    ) 
    chat = openai.ChatCompletion.create( 
        model=model, messages=messages 
    ) 
  
reply = chat.choices[0].message.content 
print(f"BankerGPT: {reply}") 
messages.append({"role": "assistant", "content": reply})

# write to output
outputfile = open("output.csv",'w')
outputfile.write(reply)
outputfile.close()


# input
# time period: 2022-2023, multiple pdfs
# currency: USD, RMB
# company name: apple, nio, etc.


#future suppliment 
while True: 
    message = input("User (good/quit/exit): ") 
    if message == "good" or message == "quit" or message == "exit":
        break
    if message: 
        messages.append( 
            {"role": "user", "content": message}, 
        ) 
        chat = openai.ChatCompletion.create( 
            model=model, messages=messages 
        ) 
      
    reply = chat.choices[0].message.content 
    print(f"BankerGPT: {reply}") 
    messages.append({"role": "assistant", "content": reply})

    #if previous format not correct, then ask for e.g."in csv format" to regenerate
    outputfile = open("output.csv",'w')
    outputfile.write(reply)
    outputfile.close()



# def write2excel():
#     # Replace 'existing_file.xlsx' with the path to your existing Excel file
#     file_path = 'BankerGPT_demo.xlsx'

#     # Load the existing workbook
#     workbook = openpyxl.load_workbook(file_path)
#     exist_sheet_name = 'Financial Numbers From AR'
#     replace_cell = workbook.get_sheet_by_name(exist_sheet_name)

#     # banker_json["FinancialNumbers"]["Revenue"]["2022"] = 394328

#     banker_json = {
#       "FinancialNumbers": {
#         "Revenue": {
#           "2022": 394328,
#           "2021": 365817,
#           "2020": 274515
#         },
#         "CostOfGoodsSold": {
#           "2022": 223546,
#           "2021": 212981,
#           "2020": 169559
#         },
#         "SellingGeneralAdministrativeExpense": {
#           "2022": 25394,
#           "2021": 21973,
#           "2020": 19916
#         },
#         "RDExpense": {
#           "2022": 26251,
#           "2021": 21914,
#           "2020": 18752
#         },
#         "OperatingIncome": {
#           "2022": 119437,
#           "2021": 108949,
#           "2020": 66288
#         },
#         "InterestIncome": -334,
#         "InterestExpense": 0,
#         "EarningsBeforeTax": {
#           "2022": 119103,
#           "2021": 109207,
#           "2020": 67091
#         },
#         "NetIncome": {
#           "2022": 99803,
#           "2021": 94680,
#           "2020": 57411
#         }
#       },
#       "Currency": "In millions USD"
#     }


#     # You can now modify the new sheet as needed
#     # For example, you can write data to the new sheet
# #2020
#     replace_cell['E2'] = 9456609
#     replace_cell['E3'] = 7907270
#     replace_cell['E4'] = 1118819
#     replace_cell['E5'] = 1099857
#     replace_cell['E6'] = 669337
#     replace_cell['E7'] = 41316
#     replace_cell['E8'] = 66916
#     replace_cell['E9'] = 188877
#     replace_cell['E10'] = 151657

#     #2021
#     replace_cell['F2'] = 27009779
#     replace_cell['F3'] = 21248325
#     replace_cell['F4'] = 3492385
#     replace_cell['F5'] = 3286389
#     replace_cell['F6'] = 1017320
#     replace_cell['F7'] = 740432
#     replace_cell['F8'] = 63244
#     replace_cell['F9'] = 152812
#     replace_cell['F10'] = 321455

#     #2022
#     replace_cell['G2'] = 45286816
#     replace_cell['G3'] = 36496360
#     replace_cell['G4'] = 5665301
#     replace_cell['G5'] = 6780032
#     replace_cell['G6'] = 3654877
#     replace_cell['G7'] = 976229
#     replace_cell['G8'] = 106340
#     replace_cell['G9'] = 2159355
#     replace_cell['G10'] = 2032348

#     # Save the changes to the existing workbook
#     workbook.save(file_path)

#     print(f'The sheet "{exist_sheet_name}" has been added to the existing Excel file.')

# write2excel()



