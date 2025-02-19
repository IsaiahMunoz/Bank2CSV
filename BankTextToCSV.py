import csv

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
            amount = lines[i + 4].replace("â€“ ", "").replace("$", "").strip()
        

            # Fix Category Names
            if category == "Gas":
                category = "Gas for Car"
            elif category == "Restaurants" or category == "Fast Food":
                category = "Dining"
            elif category == "Alcohol & Bars":
                category = "Alcohol and Bar"
            elif category == "Health & Fitness":
                category = "Gym"
        
     
            #print(lines[i].strip())
            # Skip if amount is a deposit (starts with '+')
            if amount_line.startswith('+'):
                continue
            
            # Append formatted transaction
            transactions.append([merchant, category, amount, date])
        except IndexError:
            # Handle cases where lines are incomplete
            continue
        # print(date, merchant, category, amount)

    transactions.reverse ()
        
    # Write to a CSV file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        #writer.writerow(['Merchant', 'Category', 'Amount'])  # Header row
        writer.writerows(transactions)  # Write all transactions

    print(f"Transactions successfully written to {output_file}.")

# Example usage:
input_file = 'Test1.txt'  # Replace with your text file name
output_file = 'Test1.csv'
process_transaction_file(input_file, output_file)

