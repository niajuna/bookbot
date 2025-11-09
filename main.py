def get_book_text(file_path):
    """ファイルパスから本の内容を読み取る関数
    Args:
        file_path (str): 本が含まれるテキストファイルのパス
    Returns:
        str: 本の内容を文字列として返す
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    print(book_text)

main()