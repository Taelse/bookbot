def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    characters = get_character_count(text)
    print(characters)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_character_count(text):
    char_lower = text.lower()
    char_count = {}
    for char in char_lower:
        if char not in char_count:
            char_count[char] = 1
        else: 
            char_count[char] += 1
    return char_count 
   

main()