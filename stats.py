def get_book_text(file_path)-> str:
    with open(file_path) as file:
        file_content: str = file.read()
    return file_content

def count_words(text: str) -> int:
    word_count: int = len(text.split())
    return word_count

def count_characters(text: str) -> dict:
    counted_chars: dict[str, int] = {}
    for char in text:
        char_lower = char.lower()
        if char_lower in counted_chars:
            counted_chars[char_lower] += 1
        else:
            counted_chars[char_lower] = 1
    return counted_chars

def sort_on(items):
    return items["num"]

def sort_char_count(counted_chars: dict) -> list[dict]:
    sorted_chars_count: list[dict] = []
    for char in counted_chars:
        if char.isalpha():
            temp_dict: dict = {"char": char, "num": counted_chars[char]}
            sorted_chars_count.append(temp_dict)
    sorted_chars_count.sort(key=sort_on,  reverse=True)
    return sorted_chars_count