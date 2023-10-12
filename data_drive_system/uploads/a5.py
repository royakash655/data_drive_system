from textblob import TextBlob


# please install "pip install textblob" in a command prompt ,otherwise correct spelling check function won't work.

print("orginal Sentence is:It was the blurst of tims . Where does does the cat go from here")

def correct_spelling_check():

    # sentance to   Spell  checkk!
    input1 = "It was the blurst of tims."
    sentence = TextBlob(input1)
    result = sentence.correct()
    print(result)


correct_spelling_check()


def remove_repeated_words():

    # Here you can give the input as repeated words into the sentence !
    input2 = "Where does does the cat go from here ?"

    sentence = input2.split()
    sentence2 = []
    for i in sentence:
        if i not in sentence2:
            sentence2.append(i)

    for j in sentence2:
        j = j+" "
        print(j, end="")


remove_repeated_words()