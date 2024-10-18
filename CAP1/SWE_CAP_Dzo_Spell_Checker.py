##################################

#Tshering Dendup
#A
#02240367

##################################

#Chat GPT, Youtube 
#https://www.python.org/
#Create a Dzongkha spell checker.
#https://www.youtube.com/results?search_query=dzo+spelling+checker++using+python

##################################

#Read the input file 
import request
link = "https://csf101-server-cap1.onrender.com/get/input/367"
request_file =request.get(link)
with open('367.txt', 'wb') as file:
    data = file.write(request_file.content)
print('Downloaded: 367.txt')
      
import re

def load_dzongkha_dictionary(file_path):
    """
    Load Dzongkha words from a file into a set.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(word.strip() for word in file.readlines())
    
# Read text from a file
with open('367.txt', 'r', encoding='utf-8') as file:
    input_text = file.read()
    
#Check spelling
def correct_word(word, dictionary):
    """
    Check if a word exists in the dictionary.
    """
    return word in dictionary

def spell_check(text, dictionary):
    """
    Check the spelling of words in the text against the dictionary.
    """
    words = re.findall(r'\b\w+\b', text)
    Incorrect_spellings = [word for word in words if not correct_word(word, dictionary)]
    return Incorrect_spellings

# Load the custom Dzongkha dictionary
dzongkha_dictionary = load_dzongkha_dictionary('Cleaned_dictionary.txt')

# Spell check
Incorrect_spellings = spell_check(input_text, dzongkha_dictionary)
if Incorrect_spellings:
    print("eorrs:", Incorrect_spellings)
else:
    print("No errors")