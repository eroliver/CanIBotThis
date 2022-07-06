
with open('word_list.txt') as text:
    words = text.read()
    stripped = words.strip('[]')
    replaced = stripped.replace("'","")
    word_list = replaced.split(', ')
    
