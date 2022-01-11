###Stop gninnipS My sdroW!###

#Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). 
#Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
#Examples: 
#spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
#spinWords( "This is a test") => returns "This is a test" 
#spinWords( "This is another test" )=> returns "This is rehtona test"

def spin_words(sentence):
    res = ""
    list = sentence.split(" ")
    for i in range(len(list)):
        if len(list[i]) >= 5:
            list[i] = list[i][::-1]
    arr = [str(a) for a in list]
    return " ".join(arr)
    
________________________________________________________________________________________________________________________
###Does my number look big in this?###

#A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. 
#In this Kata, we will restrict ourselves to decimal (base 10).
#For example, take 153 (3 digits), which is narcisstic:

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    
#and 1652 (4 digits), which isn't:

    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938

def narcissistic( value ):
    result = 0
    narc = [int(a) for a in str(value)]
    N = len(narc)
    for i in range(N):
        result += narc[i]**N
    if result == value: return True
    else: return False

________________________________________________________________________________________________________________________
