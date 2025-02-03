def main():

    book_path = "books/frankenstein.txt" # Definies variables needed by the main() function that are the products of other nested functions.
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_report = alpha_dict_list(text)    

    char_report.sort(reverse=True, key=sort_on) # Sorts the list of dictionaries by key that is gathered from the sort_on function and goes from high to low.
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    for char_dict in char_report: # Since char_report is a list of dictionaries, looping through each entry of the list and printing the line which calls the name and key of each.
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")

    print("--- End report ---")
def get_num_words(text): ## Function that splits the text into words and returns the length of the list
    words = text.split()
    return len(words)


def get_book_text(path): ## Function that reads the file from the path provided and returns
    with open(path) as f:
        return f.read()


## Trying to combine character count and alpha count into one function that loops through.

def alpha_dict_list(text): # Function that takes the text input and converts it to lower case, loops through and if the character is in the alphabet it will add to the dictionary,
                        # if its already in the dictionary it increases the key value by 1
    char_lower = text.lower()
    alpha_char = {}
    
    for char in char_lower:
        if char.isalpha():
            alpha_char[char] = alpha_char.get(char, 0) + 1
            
    dict_list = [{"char": character, "num": count} for character, count in alpha_char.items()]
    return dict_list


def sort_on(dict): # A function to return the key value for a dictonary input? Its how the .sort() knows how to sort the list.
    return dict["num"]



    
   

main()