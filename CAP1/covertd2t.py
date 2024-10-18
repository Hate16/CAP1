import docx2txt as d2t

dfile = 'dictionary.docx'
tfile = 'dictionary.txt'

doc = d2t.process(dfile)

file = open(tfile, 'w', encoding='utf-8')
file.write(doc)
file.close()

print('file coverted')