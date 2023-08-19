def palendwom(chenn):
    chenn = chenn.lower()
    chenn = chenn.replace(" ", "")
    return chenn== chenn[::-1]



#Koman pouw itilizel
mot = "radar"
if palendwom(mot):
    print(f"{mot} se yon palendwom.")
else:
    print(f"{mot} se pa yon palendwom.")
