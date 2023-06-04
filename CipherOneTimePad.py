def oneTimePad(P1, KEY):
    C1 = ""
    for i in range(len(P1)):
        C1 += chr((ord(P1[i]) + ord(KEY[i])) % 26 + ord('A'))
    return C1


P1 = "CAT"
KEY = "ABA"

C1= oneTimePad(P1,KEY)

print("C1 = " + C1)

P2= oneTimePad(C1,KEY)
print("P2 = " + P2)
