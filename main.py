from stats import get_book_text, count_words, count_characters, sort_char_count
import sys

def main():
    if len(sys.argv) < 2:
        print("You have to provide a path to a book file!")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path: str = sys.argv[1]
    print("======== BOOKBOT ========")
    print(f"Analyzing book at path: {book_path}...")
    
    num_words = count_words(get_book_text(book_path))
    num_of_chars = count_characters(get_book_text(book_path))
    sorted_chars_report = sort_char_count(num_of_chars)
    print("-------- Word Count --------")
    print(f"Found {num_words} total words.")
    print("-------- Character Count --------")
    for item in sorted_chars_report:
        print(f"{item['char']}: {item['num']}")
    
main()