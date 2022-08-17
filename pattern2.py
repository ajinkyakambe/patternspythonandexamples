# Pattern 2 to print in python console.

# *****
# *****
# *****
# *****
# *****


def pattern(size):
    for i in range(size):  # Row
        for j in range(size):  # column
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print("*", end=" ")
            else:
                print("*", end=" ")
        print(" ")  # line break after every row


# Driving code for pattern with size
size = 5
pattern(size)

print(" ")

size2= 10
pattern(size2)