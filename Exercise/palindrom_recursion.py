def isPalindrom(str) :
    if len(str) < 1 :
        return True
    else :
        if str[0] == str[-1] :
            return isPalindrom(str[1:-1])
        else :
            return False

inp  = input() 
if isPalindrom(inp) :
    print("it's palindrom")
else :
    print("not palindrom")