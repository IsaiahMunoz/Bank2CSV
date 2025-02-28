import csv

# # importing all necessary modules
# from gensim.models import Word2Vec
# import gensim
# import nltk
# # nltk.download('punkt_tab')
# from nltk.tokenize import sent_tokenize, word_tokenize

# def create_model(sample_name):
#     with open(sample_name) as training_file:
#         sample = training_file.read()
#         f = sample.replace("\n"," ")
#         data = []
        
#         # iterate through each sentence in the file
#         for i in sent_tokenize(f):
#             temp = []
            
#             # tokenize the sentence into words
#             for j in word_tokenize(i):
#                 temp.append(j.lower())
            
#             data.append(temp)
        
#         # Create CBOW model
#         model1 = gensim.models.Word2Vec(data, min_count =  1, vector_size = 100, window = 5)
#         return model1 


def process_transaction_file(input_file, output_file):
    transactions = []  # List to store parsed transactions
    
    with open(input_file, 'r') as file:
        lines = file.readlines()  # Read all lines in the text file
    #print(lines)
    # Parse the lines
    for i in range(0, len(lines), 6):  # Transactions are grouped in 4 lines
        try:
            # Extract information
            date = lines[i].strip() + ", " + lines[i+1].strip()
            merchant = lines[i + 2].strip()  # Third line: Merchant
            category = lines[i + 3].strip()  # Fourth line: Category
            amount_line = lines[i + 4].strip()  # Fifth line: Amount

            # Skip if amount is a deposit (starts with '+')
            if amount_line.startswith('+'):
                continue
            
            amount = float(amount_line[3:].strip())
            
            method = None
            category = pred_recat(category, method)   
            
            # Append formatted transaction
            transactions.append(["",merchant, category, amount, date])
        except IndexError:
            # Handle cases where lines are incomplete
            continue
        # print(date, merchant, category, amount)

    transactions.reverse ()
        
    # Write to a CSV file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Descr', 'Merchant', 'Category', 'Price','Date'])  # Header row
        writer.writerows(transactions)  # Write all transactions

    print(f"Transactions successfully written to {output_file}.")

def pred_recat(category, method):
    # For Testing Purpose for now
    if category == "Gas":
        category = "Gas for Car"
    elif category == "Restaurants" or category == "Fast Food":
        category = "Dining"
    elif category == "Alcohol & Bars":
        category = "Alcohol and Bar"
    elif category == "Health & Fitness":
        category = "Gym"
    
    return category

# def load_metod(method):
#     if method == "IF Else Blocks":
#         return "IF Else Blocks"
#     else: 
#      raise ValueError(f"Unknown Method {method}")
        


# Example usage:
# input_file = 'Test1.txt'  # Replace with your text file name
# output_file = 'Test1.csv'
# process_transaction_file(input_file, output_file)



