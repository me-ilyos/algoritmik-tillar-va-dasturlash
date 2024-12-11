def main():
    n = raqam_olish()
    marta_chop(n)


def raqam_olish():
    while True:
        x = int(input("Raqam: "))

        if x > 0 and x <= 50:
            return x


def marta_chop(n):
    # while n > 0:
    #     print("Hello!")
    #     n -= 1
    for i in range(n):
        print("Hello")


main()
