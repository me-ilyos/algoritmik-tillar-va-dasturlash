# CS50 Python Laboratoriya Mashg'uloti

## Kirish
Ushbu laboratoriya mashg'ulotida siz Python dasturlash tilida 4 ta masalani yechishni o'rganasiz. Har bir masala input bilan ishlash, matn bilan ishlash va funksiyalar yaratish kabi asosiy Python konsepsiyalarini o'z ichiga oladi.
## Masalalar

### 1-Masala: Kichik Harflar (kichik_harf.py)

**Masala tarjimasi:**
Foydalanuvchidan matn kiritishni so'raydigan va kiritilgan matnni kichik harflarda qaytaradigan dastur yarating. Belgilari va bo'shliqlar o'zgarishsiz qolishi kerak.

**Faylni yaratish va ishga tushirish:**
1. `kichik_harf.py` nomli yangi fayl yarating
2. Quyidagi buyruq orqali dasturni ishga tushiring:
```bash
python kichik_harf.py
```

**Kutilgan natija:**
```
Kiriting: HELLO, WORLD
natija: hello, world
```

**Yechim va Tushuntirish:**
```python
# Foydalanuvchidan matn kiritishni so'raymiz
matn = input("Matn kiriting: ")

# lower() metodi yordamida barcha harflarni kichik harflarga o'zgartiramiz
# lower() metodi faqat harflarni o'zgartiradi, boshqa belgilar o'zgarmaydi
natija = matn.lower()

# Natijani ekranga chiqaramiz
print(natija)
```

**Tushuntirish:**
Bu dasturda biz uchta asosiy qadamni bajaramiz:
1. `input()` funksiyasi yordamida foydalanuvchidan matn qabul qilamiz
2. `lower()` metodi matndagi barcha katta harflarni kichik harflarga o'zgartiradi
3. Natijani `print()` orqali ekranga chiqaramiz

### 2-Masala: Sekinlashtirilgan Matn (sekin_matn.py)

**Masala tarjimasi:**
Foydalanuvchidan matn kiritishni so'raydigan va har bir bo'shliq o'rniga uch nuqta (...) qo'yib qaytaradigan dastur yarating.

**Faylni yaratish va ishga tushirish:**
1. `sekin_matn.py` nomli yangi fayl yarating
2. Quyidagi buyruq orqali dasturni ishga tushiring:
```bash
python sekin_matn.py
```
**Kutilgan natija:**
```
Kiriting: Bu test matni
natija: Bu...test...matni
```

**Yechim va Tushuntirish:**
```python
# Foydalanuvchidan matn kiritishni so'raymiz
matn = input("Matn kiriting: ")

# replace() metodi yordamida bo'shliqlarni "..." ga almashtiramiz
# replace() metodiga ikki parametr beriladi:
# 1. Qidirilayotgan belgi (" ")
# 2. O'rniga qo'yiladigan belgi ("...")
natija = matn.replace(" ", "...")

# Natijani ekranga chiqaramiz
print(natija)
```

**Tushuntirish:**
Bu dastur quyidagi qadamlardan iborat:
1. Foydalanuvchidan matn qabul qilinadi
2. `replace()` metodi yordamida har bir bo'shliq uch nuqta bilan almashtiriladi
3. O'zgartirilgan matn ekranga chiqariladi

### 3-Masala: Emotsiyalar (kayfiyat.py)

**Masala tarjimasi:**
Matndagi `:)` va `:(` belgilarini mos ravishda 🙂 va 🙁 emojilarga o'zgartiradigan dastur yarating.

**Faylni yaratish va ishga tushirish:**
1. `kayfiyat.py` nomli yangi fayl yarating
2. Quyidagi buyruq orqali dasturni ishga tushiring:
```bash
python kayfiyat.py
```
**Kutilgan natija:**
```
Kiriting: Salom :) Xayr :(
natija: Salom 🙂 Xayr 🙁
```

**Yechim va Tushuntirish:**
```python
def convert(matn):
    # Avval kulib turgan emojini o'zgartiramiz
    matn = matn.replace(":)", "🙂")
    # Keyin xafa emojini o'zgartiramiz
    matn = matn.replace(":(", "🙁")
    return matn

def main():
    # Foydalanuvchidan matn kiritishni so'raymiz
    user_input = input("Matn kiriting: ")
    
    # Kiritilgan matnni convert() funksiyasiga yuboramiz
    natija = convert(user_input)
    
    # Natijani ekranga chiqaramiz
    print(natija)

# Agar fayl to'g'ridan-to'g'ri ishga tushirilsa, main() funksiyasini chaqiramiz
if __name__ == "__main__":
    main()
```

**Tushuntirish:**
Bu dastur ikki qismdan iborat:
1. `convert()` funksiyasi:
   - Parametr sifatida matn qabul qiladi
   - Ikki bosqichda emoji belgilarini almashtiradi
   - O'zgartirilgan matnni qaytaradi

2. `main()` funksiyasi:
   - Foydalanuvchidan input oladi
   - `convert()` funksiyasini chaqiradi
   - Natijani ekranga chiqaradi

### 4-Masala: Choy puli kalkulyatori (choy_puli.py)

**Masala tarjimasi:**
Restoranda qoldirilishi kerak bo'lgan choy pulini hisoblaydigan dastur yarating. Dastur ikki funksiyadan iborat bo'lishi kerak:
- `dollars_to_float`: $XX.XX formatidagi stringni float tipiga o'zgartiradi
- `percent_to_float`: XX% formatidagi stringni o'nlik kasr (float) ko'rinishiga o'zgartiradi


**Faylni yaratish va ishga tushirish:**
1. `choy_puli.py` nomli yangi fayl yarating
2. Quyidagi buyruq orqali dasturni ishga tushiring:
```bash
python choy_puli.py
```

**Yechim va Tushuntirish:**
```python
def dollars_to_float(d):
    """
    Dollar belgisi bilan kelgan stringni float tipiga o'zgartiradi
    """
    # Dollar belgisini olib tashlaymiz va float ga o'tkazamiz
    return float(d.replace("$", ""))

def percent_to_float(p):
    """
    Foiz belgisi bilan kelgan stringni o'nlik kasrga o'zgartiradi
    """
    # Foiz belgisini olib tashlaymiz, float ga o'tkazib, 100 ga bo'lamiz
    return float(p.replace("%", "")) / 100

def main():
    # Ovqat narxini so'raymiz
    dollars = dollars_to_float(input("Ovqat narxi qancha? "))
    
    # Foiz miqdorini so'raymiz
    percent = percent_to_float(input("Necha foiz choy puli qoldirasiz? "))
    
    # Choy pulini hisoblaymiz
    tip = dollars * percent
    
    # Natijani ekranga chiqaramiz
    print(f"Choy puli: ${tip:.2f}")

if __name__ == "__main__":
    main()
```

**Tushuntirish:**
Bu dastur uch asosiy funksiyadan iborat:

1. `dollars_to_float()`:
   - Dollar belgisini ($) olib tashlaydi
   - Stringni float tipiga o'zgartiradi

2. `percent_to_float()`:
   - Foiz belgisini (%) olib tashlaydi
   - Stringni float tipiga o'zgartiradi
   - 100 ga bo'lib foizni o'nlik kasrga o'zgartiradi

3. `main()`:
   - Foydalanuvchidan ma'lumotlarni qabul qiladi
   - Boshqa funksiyalarni chaqiradi
   - Natijani hisoblab ekranga chiqaradi
   
## Qo'shimcha Manbalar
- [Python Documentation](https://docs.python.org/3/)
- [CS50's Python Documentation](https://cs50.harvard.edu/python/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)

## Muammolar yuzaga kelganda
Agar dasturingiz ishga tushirishda xatolik bersa, quyidagilarni tekshiring:
1. Python to'g'ri o'rnatilganligini
2. Fayl nomini to'g'ri yozganingizni
3. Fayl joylashgan papkada turganingizni
4. Sintaksis xatolar yo'qligini

Savollar bo'lsa, o'qituvchiga murojaat qiling.
