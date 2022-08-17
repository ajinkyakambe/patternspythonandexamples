def counting_the_vovel(sentence):
    sentence = sentence.lower()
    character_count = [str(a) for a in str(sentence)]

    vovelcount = 0
    for singlechar in character_count:
        if singlechar == 'a' or singlechar == 'e' or singlechar == 'i' or singlechar == 'o' or singlechar == 'u':
            vovelcount += 1

    print(vovelcount)


# Driving code

# example no 1
counting_the_vovel("Number of vowels in the given sentence is ")

# example no 2
counting_the_vovel("nw wnt wrk ")
