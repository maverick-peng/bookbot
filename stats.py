
def count_words(text):
    return len(text.split())

def gen_dictionary(text):
    dict = {}
    for c in text:
        if c.lower() in dict:
            dict[c.lower()] += 1
        else:
            dict[c.lower()] = 1
    return dict

def sort_on(dict):
    return dict["num"]

def dict_to_sorted_list(dict):
    list = []
    for key in dict:
        list.append({"name": key, "num": dict[key]})
    list.sort(reverse=True, key=sort_on)
    return list