var=input("enter string ")
def reverse_string(var):
    result = ""
    for c in var:
        
        result = c + result
    return result

def is_palindrome(var):
    return var == var[::-1]

a= reverse_string(var)
if is_palindrome(var):
    print("palindrome")
else:
    print("not palindrome ")
