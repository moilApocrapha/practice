"""my solution to the isPalindrome challenge on leet Code. I wasn't cheap by converting the int to a string either. """

def isPalindrome(x: int) -> bool:

    orig = x
    reverse = 0
    while x >= 0:

        if x < 10:
            reverse += x
            x -= x
            break

        digit = (x % 10)
        reverse = (reverse + digit) * 10
        x = (x - digit)/10

    if orig == reverse:
        return True
    else:
        return False

if __name__ == "__main__":

    print(isPalindrome(1689), "expected False")
    print(isPalindrome(1), "expected True")
    print(isPalindrome(0), "expected True")
    print(isPalindrome(11), "expected True")
    print(isPalindrome(202), "expected True")
    print(isPalindrome(1120211))


