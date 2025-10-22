def get_num_words(content):
    num_words = len(content.split())
    return f"Found {num_words} total words"

def get_char_count(content):
    char_count = {}
    for char in content:
        lowercase_char = char.lower()
        if lowercase_char in char_count:
            char_count[lowercase_char] += 1
        else:
            char_count[lowercase_char] = 1
    return char_count

def sort_on(dict_item):
    return dict_item["num"]

def get_sorted_char_count(char_count_dict):
    sorted_list = []
    for char, count in char_count_dict.items():
        sorted_list.append({"char": char, "num": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list