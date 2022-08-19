# 5. Python Program to Check if a Key is Already Present in a Dictionary

dict = {'A': 1, 'B': 2, 'C': 3}


def checkkeyindict(dict):
    key = input("Enter key to check:")
    if key in dict.keys():
        print("Key is present and value of the key is:")
        print(dict[key])
    else:
        print("Key isn't present!")

# Driving code
checkkeyindict(dict)