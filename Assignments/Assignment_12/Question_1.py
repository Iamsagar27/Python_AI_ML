# 1. Write a program which accepts one character and checks whether it is vowel or consonant. 
# Input: a 
# Output: Vowel 

def CheckVowelOrConsonant(char):
    if(char.lower() == 'a' or char.lower() == 'e' or char.lower() == 'i' or char.lower() == 'o' or char.lower() == 'u'):
        return True
    else :
        return False

def main():
    character = input("Enter a character :")

    Result = CheckVowelOrConsonant(character)

    if(Result):
        print("Vowel")
    else :
        print("Consonant")

if __name__ == "__main__":
    main()