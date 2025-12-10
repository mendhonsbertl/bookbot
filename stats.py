def get_num_words(text):
    split_text = text.split()
    return len(split_text)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def chars_dict_to_sorted_list(text):
    chars = get_chars_dict(text)
    list_chars =[]
    for key, value in chars.items():
        dictionary = {"char": key, "num": value}
        list_chars.append(dictionary)
    
    sorted_chars = sorted(list_chars, key=lambda d: d["num"], reverse=True)
    
    return sorted_chars