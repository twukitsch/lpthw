# Escape Sequences

print("\\ A slash") # \\ Escapes the slash
print("\" A double-quote") # \" Escapes a double-quote
print('\' A single-quote') # \' Escapes a single quote
print("\a An ASCII Bell") # \a Shows an ASCII bell (makes the alert or bell sound)
print("A backspace\bE") # \b Move cursor one position back in the console window but does not delete
print("This is a \f Formfeed") # \f Formfeed causes a printer to eject paper to the top of the next page, or a video terminal to clear the screen.
print("This is a\nLinefeed") # \n Starts a new line of text
#print("\N is a character named \"name\" in the Unicode database") # and will error out if used
print("This is a\rCarriage Return") # \r performs a return to the beginning of the current line
print("\t This is a Horizontal Tab") # \t prints a tab
#print("") # \uxxxx and \Uxxxxxxxx are for backward/forward compatability 
print("This is a \v Vertical Tab") # \v is a vertical tab
print("\"\114\117\114\041\" was written in octal") # \000 outputs a character with the assigned octal value
print("\"\x4C\x4D\x41\x4F\" was written in hex") # \xhh outputs a character with the assigned hex value

