## Bank2CSV Test Python Script
# Each test will go through the models
# and evaluate the accuracy of each one

from Bank2CSV import process_transaction_file
import pandas as pd

def accuracy(correct, total):
    return 100*(correct/total)

## First Test: IF-ELSE BLOCKS (Original)
input_file = 'Test1.txt'  # Replace with your text file name
output_file = 'Test1.csv'
process_transaction_file(input_file, output_file)

# Check Accuracy

# Load CSV files into DataFrames
test1 = pd.read_csv('Test1.csv')
test1_exp = pd.read_csv('Test1_expected.csv')

# # Compare DataFrames and identify differences
differences = test1['Category'].compare(test1_exp['Category'])

# # Output the differences
test1_tot = len(test1) 
test1_cor = test1_tot - len(differences)
print("Test1 Accuracy: {:.2f}%".format(accuracy(test1_cor, test1_tot)))
