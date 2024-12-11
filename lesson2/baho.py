import sys

oraliq_baho = int(input("Nechi boldi:  "))

if oraliq_baho > 100:
    print("Notogri qiymat kiritildi!")
    sys.exit()

if 90 <= oraliq_baho:
    print("Baho: 5")
elif 75 <= oraliq_baho:
    print("Baho: 4")
elif 60 <= oraliq_baho:
    print("Baho: 3")
else:
    print("Hayr!")
