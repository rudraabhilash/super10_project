import re
def main():
    get_word()

def get_word():
    word=input("enter the valid word:")
    if re.search(r"^[a-zA-Z0-9]+$",word):
        if len(word)>=3:
            if any(char in "AEIOUaeiou" for char in word) and any(char in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz" for char in word):
                print(True)
            else:
                print(False)
        else:
            print(False)        
    else: 
        print(False)
main()            