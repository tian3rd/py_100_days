import pandas as pd
import os.path

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

file_name = os.path.dirname(os.path.realpath(
    __file__)) + '/nato_phonetic_alphabet.csv'
nato_df = pd.read_csv(file_name)

nato_dic = {row.letter: row.code for (index, row) in nato_df.iterrows()}

while True:
    user_input = input("Type your word here (English letters only): ")
    if user_input.isalpha():
        break

user_nato_lst = [nato_dic[letter.upper()] for letter in user_input]
print(user_nato_lst)
