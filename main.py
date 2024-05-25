def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = []
        words = file_contents.split()
        print(f"{len(words)} words found in the document")
        
    alpha = {}
    new = letters(file_contents)
    for i in new:
        if i in alpha:
            alpha[i] += 1

        else:
            alpha[i] = 1

    print (alpha)
    
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


main()