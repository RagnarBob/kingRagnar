non = input("antre nonw : ")
non_majikil = ""

komansman_mo = True
for lettre in non:
    if komansman_mo and lettre.isalpha():
        non_majikil += lettre.upper()
        komansman_mo = False
    else:
      non_majikil += lettre.lower()

    if lettre.isspace():
        komansman_mo = True

print( non_majikil )