def main():

    book_path = "books/frankenstein.txt" # Definies variables needed by the main() function that are the products of other nested functions.
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_report = alpha_dict(text)
    characters = get_character_count(text)
    

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

def get_character_count(text): # Function that takes the raw text input and sets a list with all text converted to lower case. Loops through the list and updates the empty dictionary. 
                               # If the entry isn't found it adds the entry, and if it does exist increases the count of the num key by 1 then returns the dictionary
    char_lower = text.lower()
    char_count = {}
    for char in char_lower:
        if char not in char_count:
            char_count[char] = 1
        else: 
            char_count[char] += 1
    return char_count 

def alpha_dict(text): # Function that takes the raw text input and creates a blank list of dictionaries. 
                        # Defines variables for a list of lower case characters in the alphabet and an empty dictionary for the name/key for each entry.
    dict_list = []
    char_lower_alpha = text.lower()
    char_count_alpha = {}

    for lowchar in char_lower_alpha: ## Loops through the list of lower case characters and if they are in alphabet adds them to the char_count_alpha dictionary.
        if lowchar.isalpha() == True:
            if lowchar not in char_count_alpha:
                char_count_alpha[lowchar] = 1
            else: 
                char_count_alpha[lowchar] += 1
    
    for character, count in char_count_alpha.items(): # Loops through each dictionary made by the loop above and defines the key pair then adds it to the list of dictionaries.
        char_dict = {"char": character, "num": count}
        dict_list.append(char_dict)
    return dict_list

def sort_on(dict): # A function to return the key value for a dictonary input? Its how the .sort() knows how to sort the list.
    return dict["num"]



    
   

main()