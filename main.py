
def get_book_text(filepath):
    with open(filepath) as f:
    #Do something with f (The file) here   
    # f is a file object
        file_contents = f.read() 
    return file_contents  

def main():
    book_text = get_book_text("../bookbot/books/frankenstein.txt")
    print(book_text)

main()
    