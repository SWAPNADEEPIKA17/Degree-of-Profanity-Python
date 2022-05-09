# -*- coding: utf-8 -*-
"""
Created on Fri May  6 09:06:31 2022

@author: animi
"""



import re
import pandas as pd

# Input csv file with tweets.
tweet_input_file = input("Provide the name of the input file: ")
input_file = pd.read_csv(tweet_input_file)
# List of racial slurs
input_slurs = input("Enter name separated by space: ")
# Split string into words
list_of_slurs = input_slurs.split(" ")

# Adding headers to the file
num_cols = input_file.shape[1]
old_col0 = input_file.columns.to_list()[0]
input_file = input_file.rename(columns={old_col0: "Tweets"})
# Separating user 
input_file["User"] = input_file["Tweets"].apply(lambda x: [x for x \
    in x.split(" ") if x.startswith("@")])
input_file["User"] = input_file["User"].apply(lambda x: str(x)) 

input_file["Tweets"] = input_file["Tweets"].apply(lambda x: [x for x \
    in x.split(" ") ][1:])
input_file["Tweets"] = input_file["Tweets"].apply(lambda x: " ".join(x))
def search_slurs(x):     
    tmp_list = []
    for y in list_of_slurs: 
        if re.search(y, x, re.IGNORECASE) is not None:   
            tmp_list.append(y) 
        else: 
            pass
        another_tmp_list = []
        for item in tmp_list: 
            if len(item) == 0:
                pass 
            else:
                another_tmp_list.append(item)
            
            foul_words = ", ".join(another_tmp_list)
            return foul_words            
                              
input_file["Slur Words"] = input_file["Tweets"].apply(search_slurs)
input_file['Total Word Count'] = input_file['Tweets'].apply(lambda x: \
            len(re.findall(r'\w+', x)))
    
input_file['Slurs Count'] = input_file['Slur Words'].apply(lambda y: \
            len(re.findall(r'\w+', y)))

                
input_file["Deg. Profanity"] = input_file["Slurs Count"]/input_file["Total Word Count"]
input_file.to_csv(r"degree_of_profanity.csv", index=False)