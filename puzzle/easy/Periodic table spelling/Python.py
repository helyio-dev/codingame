import sys

def solve():
    elements_str = "H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og"
    elements = set(elements_str.split())
    
    def find_spellings(word, current_spelling, results):
        if not word:
            results.append(current_spelling)
            return

        one_letter_symbol = word[0].upper()
        if one_letter_symbol in elements:
            find_spellings(word[1:], current_spelling + one_letter_symbol, results)

        if len(word) >= 2:
            two_letter_symbol = word[0].upper() + word[1].lower()
            if two_letter_symbol in elements:
                find_spellings(word[2:], current_spelling + two_letter_symbol, results)

    try:
        word_to_spell = sys.stdin.readline().strip().lower()
    except (IOError, IndexError):
        return

    possible_spellings = []
    find_spellings(word_to_spell, "", possible_spellings)
    
    if not possible_spellings:
        print("none")
    else:
        possible_spellings.sort()
        for spelling in possible_spellings:
            print(spelling)

solve()
