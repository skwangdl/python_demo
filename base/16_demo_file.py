
def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

if __name__ == '__main__':
    msg = "abccba"
    print(is_palindrome(msg))