import easygui as e

while True:
    nz_word = e.enterbox("Please enter the NZ word", "Word to check ")
    word = nz_word
    word = word.replace("s", "z")
    word = word.replace("u", "")
    if word == nz_word:
        e.msgbox("No changes made")
    else:
        e.msgbox(f"The american spelling of {nz_word} is {word}", "Result")