def get_word_count(filepath):
    with open(filepath) as f:
        return len(f.read().split())

def get_char_count(filepath):
    dict_character_count = {}
    with open(filepath) as read_file:
        for character in read_file.read().lower():
            dict_character_count[character] = dict_character_count.get(character, 0) + 1
    return dict_character_count

def dict_splitser(input_dict):
    character_list = [{"char": char, "num": count} for char, count in input_dict.items()]
    character_list.sort(key=lambda x: x["num"], reverse=True)
    return character_list