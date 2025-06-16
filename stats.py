def words_in_doc(doc):
    new_list = doc.split()
    words = len(new_list)
    print(f"{words} words found in the document")
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

