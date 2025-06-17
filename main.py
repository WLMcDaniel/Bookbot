import sys
def get_book_text(filepath):
    with open(filepath) as f:
    #Do something with f (The file) here   
    # f is a file object
        file_contents = f.read() 
    return file_contents 

def check_fun():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        pass

check_fun()

def main():
    book_text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    words_in_doc(book_text)
    print("--------- Character Count -------")
    char_counts = character_appear(book_text)
    sorted_chars = sort_dict(char_counts)
    for item in sorted_chars:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")  
    print("============= END ===============")
    
    

from stats import words_in_doc
from stats import character_appear
from stats import sort_dict




main()