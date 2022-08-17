# 4. Python Program to Trim Whitespace From a String

def trimwhitespaces(string):
    stringchars = [str(element) for element in string]
    print(stringchars)

    # final string without whitesapce
    resultstr = ""
    for singlechar in stringchars:
        if singlechar == " ":
            pass
        else:
            resultstr += singlechar

    print(resultstr)


# Driving code
trimwhitespaces("This is the string with whitesapce")
