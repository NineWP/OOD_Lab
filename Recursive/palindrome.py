def is_palindrome(str):
    if len(str) < 1 :
        return True
    else :
        if str[0] == str[-1] :
            return is_palindrome(str[1:-1])
        else :
            return False

inp = str(input("Enter Input : "))

if is_palindrome(inp) :
    print("'{}' is palindrome".format(inp))
else :
    print("'{}' is not palindrome".format(inp))