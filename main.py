def main():
    with open("books/frankenstein.txt") as f:
        file_contents = str(f.read())
        words = []
        words = file_contents.split()
        print(len(words))

        


main()