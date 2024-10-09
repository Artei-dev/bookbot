import os

def get_book_text(filepath: str) -> str:
    with open(filepath, 'r') as f:
        text = f.read()

    return text


def get_number_of_words(text: str) -> int:
    words = text.split()

    return len(words)

def get_characters_count(text: str) -> dict:
    characters = {}
    for char in text:
        char = char.lower()
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1

    return characters


def sort_on(characters: dict[str, int]) -> int:
    return characters['count']

def chars_dict_to_sorted_list(dict: dict[str, int]) -> list:
    list = []

    for ch in dict:
        list.append({"char": ch, "count": dict[ch]})

    list.sort(reverse=True, key=sort_on)

    return list

def generate_report(filename) -> None:
    path = os.path.join('books', filename)
    print(f'--- Begin report of {path} ---')

    text = get_book_text(path)
    print(f'{get_number_of_words(text)} words found in the document\n')

    character_count = get_characters_count(text)
    character_count_list_sorted = chars_dict_to_sorted_list(character_count)

    for pair in character_count_list_sorted:
        if pair['char'].isalpha():
            print(f"The '{pair['char']}' was found {pair['count']} times")

    print('--- End report ---')


if __name__ == "__main__":
    filename = "frankenstein.txt"

    generate_report(filename=filename)
