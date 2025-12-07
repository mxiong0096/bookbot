def get_book_text(filepath):
    book_content = ""
    with open(filepath) as f:
        book_content = f.read()
    return book_content

def get_num_words(book):
    words_in_book = book.split()
    num_words = 0
    for words in words_in_book:
        num_words += 1
    return num_words

def get_char_count(book):
    book_characters = {}
    for char in book:
        if char.lower() in book_characters:
            book_characters[char.lower()] += 1
        else:
            book_characters[char.lower()] = 1
    return book_characters

def sort_on(items):
    return items["num"]

def sorts_dict_to_list(book_dic):
    my_list = []

    for key in book_dic:
        my_list.append({"char": key, "num": book_dic[key]})

    my_list.sort(reverse=True, key=sort_on)
    return my_list


# book1 = get_book_text("./books/frankenstein.txt")
# char_count_in_book = get_char_count(book1)
# print(char_count_in_book)
# sorts_dict_to_list(char_count_in_book)
# print(sorts_dict_to_list(char_count_in_book))

