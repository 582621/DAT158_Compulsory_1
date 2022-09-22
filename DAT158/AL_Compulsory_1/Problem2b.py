# Problem 2b
def BMMatch(Text, Pattern):
    m = len(Pattern)
    n = len(Text)
    i = m-1
    j = m-1
    comparisons = 0

    while i <= n-1:
        comparisons += 1
        if Pattern[j] == Text[i]:
            if j == 0:
                return "Found the given pattern in index: {} after {:.2f} comparisons per character".format(i, comparisons/n)
            else:
                i -= 1
                j -= 1
        else:
            i = i+m - min(j, 1 + last(Text[i], Pattern))
            j = m-1

    return "There is no substring in T matching P"


def last(Character, Pattern):
    return Pattern.find(Character)


if __name__ == '__main__':
    Text = "Oldtidsbyen Palmyra lå i nåværende Syria. Her styrte blant annet dronning Zenobia. Hun ledet en blomstrende storby i den syriske ørkenen fra år 267 " \
        "etter moderne tidsregning. Zenobia våget til og med i sin tid å utfordre Romerriket. Ikke at det gikk særlig bra. Det endte med at byen ble beseiret, " \
        "og dronningen og folket mistet både friheten og riket. Palmyra ble plyndret og redusert til en ubetydelig småby. De pittoreske ruinene ble «gjenoppdaget» av " \
        "vestlige reisende på slutten av 1600-tallet. Historien om oldtidsbyen har fasinert og forundret folk i lang tid. Men nå mener norske og danske forskere at den " \
        "historiske fortellingen skurrer. Var det egentlig romerne som hadde skylden for Palmyras fall i år 273?"
    Pattern = "Romer"
    print(BMMatch(Text, Pattern))
