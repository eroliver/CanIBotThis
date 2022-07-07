def import_word_list():
    with open('word_list.txt') as text:
        words = text.read()
        stripped = words.strip('[]')
        replaced = stripped.replace("'","")
        word_list = replaced.split(', ')
        return(word_list)

def import_words():
    with open('more_words.txt') as text:
        words = text.readlines()
        cleaned = [word.replace("\n", "") for word in words]
        not_dumb = [word for word in cleaned if len(word) == 5]
        return(not_dumb)

def words_to_wordlist(words_file: str) -> list:
    with open(words_file) as text:
        words = text.readlines()
        cleaned = [word.replace("\n", "") for word in words]
        not_dumb = [word for word in cleaned if len(word) == 5]
        return(not_dumb)

first_list = set(import_word_list())
second_list = import_words()
third_list = words_to_wordlist("so_many_words.txt")

print(len(first_list))
print(len(second_list))
print(len(third_list))

for word in second_list:
    first_list.add(word)

for word in third_list:
    first_list.add(word)

print(len(first_list))

new_file = open("all_words.txt", "w+")
new_file.write(str(list(first_list)))
new_file.close()