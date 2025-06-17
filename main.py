from stats import count_words, gen_dictionary, dict_to_sorted_list
from sys import argv, exit

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    path = argv[1]

    text = get_book_text(path)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")

    num_words = count_words(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    word_dict = gen_dictionary(text)
    sorted_list = dict_to_sorted_list(word_dict)
    for item in sorted_list:
        if  item["name"].isalpha():
            print(f"{ item["name"]}: {item["num"]}")

    print("============= END ===============")
main()