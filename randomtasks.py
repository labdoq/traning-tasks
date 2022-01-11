###Lucky number###
#№here are six-digit ticket numbers that can get lucky. 
#Lucky tickets are those in which the sum of the first three digits equals the sum of the other three digits.
#Write a function that determines whether the ticket is lucky or not.
#Example
#123456
#>>False
#
#123321
#>>True

def luckynum(num):
    return sum([int(item) for item in list(str(num))[:3]]) == sum([int(item) for item in list(str(num))[3:]])
