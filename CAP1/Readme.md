# Dzongkha Spell Checker

## Project Overview
Firstly, i had instsllled dictionary and anlysied it. After analysing it, we had to clean text, removing English words and other non-aplphanumeric characters. Using the cleaned ditcionary we compared mine index txt file with cleaned dictionary to check whether the spelling in mine txt using some algorithm.

## Table of content 
-[Usage](#usage)
-[implemention Details](#implementation-details)
-[Data Structures](#data-structures)
-[Algorithms](#algorithms)
-[Challenges and Solutions](#challenges-and-solutions)
-[Future imorvements](#future-improvemnets)
-[References](#references)

# Usage 
import re (regular expression)
Regular expression are tools used for searching and manipulating text.

def- To define the functions

re.findall- Function from the re module finds all occurences of patternn in a string and return them as a list.

'r'- To read the files

\b- Boundary to look for start and end of the word.

\w+- matches oen or more word characters.
Encoding='utf-8'- Character enncoding system to translate characters to numbers that computers can understand.

## Implementation Details
import re (regular expression)

def load_dzongkha_dictionary(file_path):
    """
    Load Dzongkha words from a file into a set.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(word.strip() for word in file.readlines())
Regular expression used for searching and manipulating text. Open specific file using file_path. And read the corresponding file.

def load_dzongkha_dictionary(file_path):
Defines function to load dzongkha word from specfic file located at file path.

def spell_check(text, dictionary):
    """
    Check the spelling of words in the text against the dictionary.
    """
    words = re.findall(r'\b\w+\b', text)
    Incorrect_spellings = [word for word in words if not correct_word(word, dictionary)]
    return Incorrect_spellings
Defines a function to comapare and see if the words in 367.txt exists in dictionary or not and if the words exists then it checks whether the spelling are correct or not. And if the spelling is incorrect then it will give incorrect spelling.

with open('367.txt', 'r', encoding='utf-8') as file:
    input_text = file.read()
Opens 367.txt file and reads the file.

Incorrect_spellings = spell_check(input_text, dzongkha_dictionary)
if Incorrect_spellings:
    print("eorrs:", Incorrect_spellings)
else:
    print("No errors")
Using the else functions to see if the spelling are correct or not, if the spelling is incorrect then it will give output saying incorrect spelling and else no errors. 

# Data Structure 
Set: The Dzongkha dictionary is stored in a set for quick lookup:
dzongkha_dictionary = load_dzongkha_dictionary('Cleaned_dictionary.txt')

String: Text from the file 367.txt is read and stored as a string:
input_text = file.read()

List: Words extracted from the text and incorrect spellings are stored in lists:
words = re.findall(r'\b\w+\b', text)
incorrect_spellings = [word for word in words if not correct_word(word, dictionary)]

# Chanllenges and Solutions
I couldn't entirely clear all  of the english words that exists in the dictionary. I couldn't link 

# Algorithms 
Loads Dzongkha words frm a file into a set:
def load_dzongkha_dictionary(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        return set(word.strip() for word in file.readlines())

Read text from a file:
with open('367.txt', 'r', encoding='utf-8') as file:
    input_text = file.read()

Check spelling:
def correct_word(word, dictionary):
    return word in dictionary

def spell_check(text, dictionary):

    words = re.findall(r'\b\w+\b', text)
    Incorrect_spellings = [word for word in words if not correct_word(word, dictionary)]
    return Incorrect_spellings

# Future Improvements 
Error Handling: Add more robust error handling, especially for the file download and reading processes.

User Interface: Develop a user interface (even a simple command-line one) for better usability.

Efficiency: Optimize your spell-check algorithm to handle larger texts more efficiently, maybe with concurrent processing.

Feedback: Integrate a feedback loop that suggests correct spellings for incorrect ones.

Additional Features: Consider adding grammar checks or more languages.

# References 
Chat GPT, Youtube 
https://www.python.org/
Create a Dzongkha spell checker.
https://www.youtube.com/results?search_query=dzo+spelling+checker++using+python
