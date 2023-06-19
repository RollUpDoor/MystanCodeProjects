"""
File: complement.py
Name: 皓暄
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    This program finds the complement strand of a DNA sequence.
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
    param dna: str with upper case
    return ans: str
    """
    ans = ''
    if dna == '':
        return "DNA strand is missing"
    else:
        for i in range(len(dna)):
            if dna[i] == "A":
                ans = ans + "T"
            elif dna[i] == "T":
                ans = ans + "A"
            elif dna[i] == "C":
                ans = ans + "G"
            else:
                ans = ans + "C"
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
