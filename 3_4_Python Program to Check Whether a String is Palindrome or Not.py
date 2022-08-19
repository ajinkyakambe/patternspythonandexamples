# 4. Python Program to Check Whether a String is Palindrome or Not

# here we are recursively checking for string to be palindrome or not.


# inner function
def isPalindromeRecursively(samplestring, start, end):
    # terminating condition
    if (start == end):
        return True

    # If first and last characters
    # do not match return false
    if (samplestring[start] != samplestring[end]):
        return False

    # If there are more than
    # two characters, check if
    # middle substring is also
    # palindrome or not. Two pointer approach
    if (start < end + 1):
        return isPalindromeRecursively(samplestring, start + 1, end - 1)

    return True


# Outer function for palindrome
def isPalindrome(samplestring):
    n = len(samplestring)

    # An empty string is
    # considered as palindrome
    if (n == 0):
        return True

    return isPalindromeRecursively(samplestring, 0, n - 1)


# Driving Code
stringtocompare = "geeg"
if (isPalindrome(stringtocompare)):
    print("Yes")
else:
    print("No")

# example 2
stringtocompare = "malayalam"
if (isPalindrome(stringtocompare)):
    print("Yes")
else:
    print("No")

# example 3
stringtocompare = "work it in"
if (isPalindrome(stringtocompare)):
    print("Yes")
else:
    print("No")