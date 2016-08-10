checker = (input("Welcome to the Great Palindrome Test!Please input a word or numbers. ")).lower() #converts all input to lower cases
#takes the value you choose to check for
def palin_check(checker):  #function that checks if it is a palindrome
    num = len(checker)
    x = 0
    if num % 2 == 0: #this helps increase efficiency - knowing if it is even or odd
        while x <= int((num/2) - 1):
            if checker[x] != checker[-x - 1]: #checks first and last number, progresses that way to successive ones
                print ("The word is not a palindrome")
                return checker #ends run
            x += 1
        print ("This is certainly a palindrome")
        print ("Thank you for using the Great Palindrome Test! :)")
        
    else:
        while x <= int(((num - 1)/2) - 1): #the middle number in an odd number is always the same both ways
            if checker[x] != checker[-x - 1]:
                print ("The word is not a palindrome")
                return checker #ends run
            x += 1
        print ("This is certainly a palindrome")
        print ("Thank you for using the Great Palindrome Test! :)")
        

palin_check(checker)
