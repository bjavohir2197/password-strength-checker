import re
import string

def parol_mustahkamligini_tekshir(parol):
    # 1. Parol uzunligi kamida 8 belgidan iborat bo'lishi kerak
    if len(parol) < 8:
        return False

    # 2. Parolda kamida 1 harf, 1 raqam va 1 maxsus belgi bo'lishi kerak
    if not re.search("[a-z]", parol):
        return False
    if not re.search("[0-9]", parol):
        return False
    if not re.search("[!@#$%^&*()_+=-{};:'<>,./?]", parol):
        return False

    # 3. Parolda uchta bir xil belgi bo'lishi mumkin emas
    if len(set(parol)) == 1:
        return False

    # 4. Parolda uchta bir xil harf bo'lishi mumkin emas
    if len(set(c for c in parol if c in string.ascii_lowercase)) == 1:
        return False

    # 5. Parolda uchta bir xil raqam bo'lishi mumkin emas
    if len(set(c for c in parol if c in string.digits)) == 1:
        return False

    # 6. Parolda uchta bir xil maxsus belgi bo'lishi mumkin emas
    if len(set(c for c in parol if c in string.punctuation)) == 1:
        return False

    return True

# Test qilish
print(parol_mustahkamligini_tekshir("short"))  # False
print(parol_mustahkamligini_tekshir("short1"))  # False
print(parol_mustahkamligini_tekshir("short1!"))  # False
print(parol_mustahkamligini_tekshir("short1!a"))  # False
print(parol_mustahkamligini_tekshir("short1!aA"))  # False
print(parol_mustahkamligini_tekshir("short1!aA1"))  # False
print(parol_mustahkamligini_tekshir("short1!aA1!"))  # False
print(parol_mustahkamligini_tekshir("short1!aA1!a"))  # False
print(parol_mustahkamligini_tekshir("short1!aA1!aA"))  # False
print(parol_mustahkamligini_tekshir("short1!aA1!aA1"))  # False
print(parol_mustahkamligini_tekshir("short1!aA1!aA1!"))  # False
print(parol_mustahkamligini_tekshir("short1!aA1!aA1!a"))  # True
