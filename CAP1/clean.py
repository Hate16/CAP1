import re 
with open('dictionary.txt', 'r', encoding='utf-8') as file:
    content = file.read()
cleaned_content = re.sub(r'[a-zA-Z0-9.,!?\"()-]+', '', content).strip()

def clear_english(input_file, output_file):
    changes = []
    with open(input_file,"r",encoding = "utf-8") as files:
        for line in files:
            dzonkhas = line.split()
            if dzonkhas:
                word_dzo = dzonkhas[0]
                changes.append(word_dzo)
    with open(output_file, "w",encoding = "utf-8") as files:
        for dzonkhas in changes:
            files.write (dzonkhas + "\n")
        print(f"changed word saved to {output_file}")
input_file = "dictionary.txt"
output_file = "Cleaned_dictionary.txt"
clear_english(input_file, output_file)