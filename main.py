from stats import word_count, count_characters, list_of_dicts
import sys



def main():
    try: 
        book_path = sys.argv[1]
    except IndexError as e: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    number = word_count(text)  
    character_dict = count_characters(text)
    print(f"{number} words found in the document")
    print(character_dict)
    dicts = list_of_dicts(text)
    char_report = ""
    for char_dict in dicts:
        char_report += f"{char_dict["char"]}: {char_dict["count"]}\n"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {number} total words")
    print("--------- Character Count -------")
    print(f"{char_report}") 
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()


