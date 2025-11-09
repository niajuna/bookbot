import sys

from stats import count_words
from stats import count_characters
from stats import sort_character_counts

"""
ファイルパスから本の内容を読み取る関数
Args:
    file_path (str): 本が含まれるテキストファイルのパス
Returns:
    str: 本の内容を文字列として返す
"""
def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    char_counts = count_characters(book_text)
    sort_char_counts = sort_character_counts(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sort_char_counts:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()