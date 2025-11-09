"""
書籍のテキストを文字列として受け取り、その文字列に含まれる単語数を返す関数
Args:
    book_text (str): 本の内容を含む文字列
Returns:
    int: 本の内容に含まれる単語数
"""
def count_words(book_text):
    words = book_text.split()
    return len(words)

"""
本のテキストを文字列として受け取り、文字列内の各文字 (記号やスペースを含む) の出現回数を返す関数
小文字に変換してからカウントを行う
Use a dictionary of String -> Integer. The returned dictionary should look something like this:
    {'p': 6121, 'r': 20818, 'o': 25225, ...}
Args:
    book_text (str): 本の内容を含む文字列
Returns:
    dict: 各文字とその出現回数を含むdict
"""
def count_characters(book_text):
    char_count = {}
    for char in book_text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

"""
文字とその出現回数のdictを受け取り、ソートされたdictのリストを返す関数
Each dictionary should have two key-value pairs: one for the character itself and one for that character's count (e.g. {"char": "b", "num": 4868}).
Use the .sort() method:
Use a helper function to return the "num" key of each dictionary for comparison.
Sort the list from greatest to least by the count.
Args:
    char_count (dict): 各文字とその出現回数を含むdict
Returns:
    list: 出現回数でソートされた (文字, 出現回数)
"""
def sort_character_counts(char_count:dict):
    char_count_list = []
    for char, count in char_count.items():
        char_count_list.append({"char": char, "num": count})

    def get_count(item):
        return item["num"]
    
    char_count_list.sort(key=get_count, reverse=True)
    return char_count_list