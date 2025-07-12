from stats import get_num_words

def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
        read = get_num_words(file_contents)
        print(f"--- Begin report of {file_path} ---")
        print(f"{read} words found in the document")
        print ()
        print ()
        
    alpha = {}
    new = letters(file_contents)
    for i in new:
        if i in alpha:
            alpha[i] += 1

        else:
            alpha[i] = 1

    end_report = chars_dict_to_sorted_list(alpha)

    for pri in end_report:
        #print (f"The {pri["char"]} character was found {pri["num"]} times")
        print (f"The {pri['char']} character was found {pri['num']} times")
    
    print ("--- End report ---")



def accptcha(text):
    okay = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    newl =""
    for i in text:
        if i in okay:
            newl += i
    return newl



def letters(sentence):
    lowercase = sentence.lower()
    temp = accptcha(lowercase)
    return temp


def sort_on(dictt):
    return dictt["num"]
    
    
def chars_dict_to_sorted_list(num_chars_dict):
    temp_list = []
    for cha in num_chars_dict:
        temp_list.append({"char": cha, "num": num_chars_dict[cha]})
    temp_list.sort(reverse=True, key=sort_on)
    return temp_list
    



    


main()