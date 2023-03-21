import easygui

while True
    #Get the word to check and convert it to a list
    nz_word=easygui.enterbox("Please enter the NZ word","Word to check")
    us_word=nz_word

    #Check for 3-character combinations and replace as required
    if "our" in nz_word:
        us_word = nz_word.replace("our","or")

    elif "ise" in nz_word:
        us_word = nz_word.replace("ise","ize")

    elif "yse" in nz_word:
        us_word = nz_word.replace("yse","yze")

    #Show results and ask if user wants to check another word
    new_word = easygui.buttonbox(f"The american spelling of '{nz_word}' is "
                                 f"'{us_word}'\n\nDo you want to check"
                                 f" another word?","Check another",
                                 choices=["Yes","No")
    if new_word == "No":
        break

easygui.msgbox("Good bye","Thanks for using this program ")