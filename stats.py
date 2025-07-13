def get_num_words(text):
    words = text.split()
    return len(words)

def accptcha(text):
    okay = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    newl =""
    for i in text:
        if i in okay:
            newl += i
    return newl





def get_chars_dict(text):
    char = {}
    lowercase = text.lower()
    temp = accptcha(lowercase)
    
    for i in temp:
        if i in char:
            char[i] += 1

        else:
            char[i] = 1
    return char


def sort_on(dictt):
    return dictt["num"]
    
    
def chars_dict_to_sorted_list(num_chars_dict):
    temp_list = []
    for cha in num_chars_dict:
        temp_list.append({"char": cha, "num": num_chars_dict[cha]})
    temp_list.sort(reverse=True, key=sort_on)
    return temp_list
    