from stats import get_book_text,get_word_count,get_letter_count,get_sorted_letter_count
from sys import argv

def main():
    print("============ BOOKBOT ============")
    
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    book_path = argv[1]


    print(f"Analyzing book found at {book_path}")
    
    text = get_book_text(book_path)
    count = get_word_count(text)
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    letter_count = get_letter_count(text)
    
    sorted_letter_count = get_sorted_letter_count(letter_count)
    print("--------- Character Count -------")
    for item in sorted_letter_count:
        print(f"{item['char']}: {item['num']}")

main()