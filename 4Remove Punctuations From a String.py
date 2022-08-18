# 4. Python Program to Remove Punctuations From a String

def punc_removal(teststring):
    print(teststring)
    initialstring = teststring
    # initializing punctuations string
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    # Removing punctuations in string
    # Using loop + punctuation string

    for stringchar in initialstring: # G, f ,G
        for puncelement in punc:
            initialstring = initialstring.replace(puncelement, "")

    # printing result
    print("The string after punctuation filter : " + initialstring)


# Driving code

# initializing string
test_str = "Gfg, is best : for ! Geeks ;"
punc_removal(test_str)
