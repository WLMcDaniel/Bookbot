def words_in_doc(doc):
    new_list = doc.split()
    words = len(new_list)
    print(f"Found {words} total words")
    return words

def character_appear(doc):
    new_list = doc.lower()
    counts = {}
    for i in new_list:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts

def sort_on(dict_item):
    return dict_item["num"]


def sort_dict(char_dict):
    new_list = []
    for key, value in char_dict.items():
        new_dict = {"char": key, "num": value}
        new_list.append(new_dict)
    new_list.sort(reverse=True, key=sort_on)
    return new_list
  
    
