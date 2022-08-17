# Pattern 3 to print in python console.
#
# *
# ***
# *****
# *********


def pyramid(n):
    for i in range(0, n): # 0 1 2 3 4
        for j in range(0, i + 1): # 0 | 0 1 | 0 1 2
            # printing stars
            print("* ", end="")
        # ending line after each row
        print("\r")


# Driver Code
n = 5
pyramid(n)