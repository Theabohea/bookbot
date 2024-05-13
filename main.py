def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print(count_words(text))
    character_counts = count_characters(text)
    print(character_counts)
    sort_dict(character_counts)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    wordcount = len(text.split())
    return(wordcount) 
    

def count_characters(text):
    strings_integers = {}
    lower_text = text.lower()
    for letter in lower_text:
        if letter.isalpha():
            if letter in strings_integers:
                strings_integers[letter] +=1
            else: 
                strings_integers[letter]= 1
    return(strings_integers)

def sort_dict(strings_integers):
    print("--- Begin report of books/frankenstein.txt ---" + "\n77986 words found in the document")
    ind_lists = list(strings_integers.items())
    sorted_ind_lists = sorted(ind_lists, key =lambda x: x[1], reverse=True)
    for item in sorted_ind_lists:
        character = item[0]
        count = item[1]
        print("The '" + character + "' character was found " + str(count) + " times\n")
    print("--- End report ---")




if __name__ == "__main__":
    main()