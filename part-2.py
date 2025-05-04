# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(list, query):
    if list == []:
        return False
    
    if list[0] == query:
        return True 
    
    return search(list[1:], query)

# is_palindrome

def is_palindrome(text):
    if len(text) == 0 or len(text) == 1:
        return True
    
    if text[0] != text[-1]:
        return False
        
    return is_palindrome(text[1: -1])


# digit_match

def digit_match(num1, num2):
    return helper(num1, num2, 0)
    
def helper(n1, n2, count):
    if n1 == 0 and n2 == 0:
        return 1
    
    if n1 == 0 or n2 == 0:
        return count
        
    if n1 % 10 == n2 % 10:
        count += 1
        
    return helper(n1 // 10, n2 // 10, count)

# digit_match(another impementation, but with help)

def digit_match(apples, oranges):
    if apples == 0 and oranges == 0:
        return 1
    if apples < 10 or oranges < 10:
        return 1 if (apples % 10) == (oranges % 10) else 0

    match = 1 if (apples % 10) == (oranges % 10) else 0
    return match + digit_match(apples // 10, oranges // 10)