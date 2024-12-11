# CS50 Python Masalalari bo'yicha Qo'llanma

## Ro'yxatlar va Lug'atlar

### Ro'yxatlar (Lists)
Ro'yxatlar - bu o'zgaruvchan ketma-ketliklar. Ular kvadrat qavslar ichida yaratiladi.

```python
# Ro'yxat yaratish
sonlar = [1, 2, 3, 4, 5]
ismlar = ["Ali", "Vali", "Gani"]

# Elementga murojaat
print(sonlar[0])  # 1

# Element qo'shish
sonlar.append(6)

# Element o'chirish
sonlar.remove(3)

# Uzunlikni aniqlash
print(len(sonlar))
```

### Lug'atlar (Dictionaries)
Lug'atlar - kalit-qiymat juftliklarini saqlaydi.

```python
# Lug'at yaratish
talaba = {
    "ism": "Ali",
    "yosh": 20,
    "kurs": 2
}

# Qiymatga murojaat
print(talaba["ism"])

# Yangi juftlik qo'shish
talaba["fakultet"] = "IT"

# Juftlikni o'chirish
del talaba["yosh"]
```

## Masalalar

### 1. camelCase
#### Masala tavsifi
Foydalanuvchi kiritgan "kamel registr" formatidagi o'zgaruvchi nomini "ilon registr" formatiga o'zgartirish kerak.

Masalan:
- `nameOfVariable` → `name_of_variable`
- `firstName` → `first_name`

#### Yechim
```python
def main():
    camel = input("camelCase: ")
    snake = ""
    
    for char in camel:
        if char.isupper():
            snake += "_" + char.lower()
        else:
            snake += char
            
    if snake.startswith("_"):
        snake = snake[1:]
        
    print("snake_case:", snake)

main()
```

#### Tushuntirish
1. Har bir belgini tekshiramiz
2. Katta harf uchrasa, oldidan pastki chiziq qo'shib, kichik harfga o'tkazamiz
3. Agar natija pastki chiziq bilan boshlansa, uni olib tashlaymiz

### 2. Coke Machine
#### Masala tavsifi
Kola avtomati 50 sent turadi. Foydalanuvchi 25, 10 yoki 5 sentlik tangalar tashlashi mumkin. Qancha pul qolganini ko'rsatib borish kerak.

#### Yechim
```python
def main():
    amount_due = 50
    
    while amount_due > 0:
        print("Amount Due:", amount_due)
        coin = int(input("Insert Coin: "))
        
        if coin in [25, 10, 5]:
            amount_due -= coin
    
    print("Change Owed:", abs(amount_due))

main()
```

#### Tushuntirish
1. Boshlang'ich summa 50 sent
2. Foydalanuvchi tanga tashlaydi
3. Agar tanga to'g'ri qiymatda bo'lsa (25, 10, 5), summadan ayiramiz
4. Summa 0 dan kichik yoki teng bo'lguncha davom etamiz

### 3. Twttr
#### Masala tavsifi
Kiritilgan matndan unli harflarni (a, e, i, o, u) olib tashlash kerak.

#### Yechim
```python
def main():
    text = input("Input: ")
    vowels = "aeiouAEIOU"
    result = ""
    
    for char in text:
        if char not in vowels:
            result += char
            
    print("Output:", result)

main()
```

#### Tushuntirish
1. Unlilar ro'yxatini yaratamiz
2. Har bir belgini tekshiramiz
3. Agar belgi unli bo'lmasa, natijaga qo'shamiz

### 4. Vanity Plates
#### Masala tavsifi
Avtomobil raqamlarining to'g'riligini tekshirish:
- 2-6 ta belgi
- Kamida 2 ta harf bilan boshlanishi
- Raqamlar oxirida bo'lishi
- Birinchi raqam 0 bo'lmasligi
- Belgilar faqat harf va raqam

#### Yechim
```python
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    
    if not s[:2].isalpha():
        return False
        
    first_number = -1
    for i, char in enumerate(s):
        if char.isdigit():
            if first_number == -1:
                first_number = i
                if char == '0':
                    return False
            elif i < first_number:
                return False
        elif not char.isalpha():
            return False
            
    return True

main()
```

#### Tushuntirish
1. Uzunlikni tekshiramiz (2-6)
2. Birinchi ikki belgi harf ekanligini tekshiramiz
3. Birinchi raqamni topamiz va 0 emasligini tekshiramiz
4. Raqamlar ketma-ketligini tekshiramiz
5. Faqat harf va raqam ishlatilganligini tekshiramiz

### 5. Nutrition Facts
#### Masala tavsifi
Mevaning nomini kiritganda, undagi kalloriyani ko'rsatish kerak.

#### Yechim
```python
def main():
    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }
    
    fruit = input("Item: ").lower()
    if fruit in fruits:
        print("Calories:", fruits[fruit])

main()
```

#### Tushuntirish
1. Mevalar va ularning kalloriyalari lug'atini yaratamiz
2. Foydalanuvchi kiritgan mevani kichik harflarga o'tkazamiz
3. Agar meva lug'atda bo'lsa, kalloriyasini chiqaramiz