fi = input("FI: ").lower()

a, b = fi.split(" ")
gender = False

if a.endswith("ov") or a.endswith("ova"):
    familya = a
    ism = b
else:
    ism = a
    familya = b

if a.endswith("ova"):
    gender = True

if gender:
    print(f"Yahshimiz {familya.title()} honim")
else:
    print(f"Yahshimiz janob {familya.title()}")
