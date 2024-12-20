def main():
    get_word()

def get_word():
    word=input("enter the valid word:")
    if len(word)>=3:
        pass
        for i in range(len(word)):
            if word[i] in ("A","E","I","o","U","e","a","i","o","u"):
                pass
            else:
                print(False)
        for i in range(len(word)):
            if word[i] in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'):
                pass
            else:
                print(False)

            
            
    else: 
        print(False)

main()
                