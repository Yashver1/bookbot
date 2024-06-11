from collections import Counter

def main() -> int:
    with open("./books/frankenstein.txt") as file:
        contents = file.read()
        print("--- Begin report of books/frankenstein.txt ---\n")
        word_count = wordcount(contents)
        print(f"{word_count} words found in the document\n\n")
        char_dict = str_to_dict(contents)
        char_list = convert_dict(char_dict)
        char_list.sort(reverse = True, key=sort_on)
        for pair in char_list:
            if pair.get("char").isalpha():
                print(f"The {pair.get("char")} character was found {pair.get("num")} times")
        print("--- End report ---")


    return 0

def wordcount(words : str) -> int:
    word_list = words.split()
    return len(word_list)

def str_to_dict(words: str) -> dict:
    words = words.lower()
    return(Counter(words))

def convert_dict(word_dict: dict) -> list:
    dict_list = []
    for key,value in word_dict.items():
        dict_list.append({"char": key, "num":value})
    return dict_list

def sort_on(dict):
    return dict["num"]


if __name__ == '__main__':
    main()
