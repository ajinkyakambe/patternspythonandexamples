# Pattern 3 to print in python console.
#
# *
# ***
# *****
# *********


def pyramid(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")
        # ending line after each row
        print("\r")


# Driver Code
n = 5
pyramid(n)