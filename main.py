from stats import get_num_words
from stats import get_chars_dict
from stats import chars_dict_to_sorted_list
import sys

def main():

    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    else:
        with open(sys.argv[1]) as f:
            file_contents = f.read()
            num_words = get_num_words(file_contents)
            chars_sorted_list = chars_dict_to_sorted_list(get_chars_dict(file_contents))
            print_report(sys.argv[1], num_words, chars_sorted_list)
        
    
        
        
        
        
  


    #book_path = "books/frankenstein.txt"





def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")





    


main()