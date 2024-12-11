tangalar = 0

while True:
    tanga = int(input("Tanga kirit: "))

    if tanga == 25 or tanga == 10 or tanga == 5:
        tangalar += tanga

        if tangalar >= 50:
            qaytim = tangalar - 50

            print(f"Coca-Cola berildi\nQaytim: {qaytim}!")
            tangalar = 0
            break

        print(f"Yana {50 - tangalar} so'm qoldi!")
