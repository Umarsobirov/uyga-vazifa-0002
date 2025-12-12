print("2-VAZIFALAR")

# task 1
with open("info.txt", "w") as file:
    file.write("Salom, Dunyo!")


# task 2
with open("info.txt", "r") as file:
    f = file.read()
    print(f)


# task 3
with open("info.txt", "a") as file:
    file.write("\nBu matn append orqali yozildi.")


# task 4
# ism = input("Ismingizni Kiriting: ")

# with open("ism.txt", "w") as file:
#     file.write(f"Kiritilgan ism: {ism}")



# task 5
meva = ["Olma", "Anor", "Behi", "Xurmo"]

with open("mevalar.txt", "w") as file:
    for i in meva:
        file.write(f"{i}\n") 


# task 6
with open("mevalar.txt", "r") as file:
    mev = []
    for i in meva:
        mev.append(i)

print(mev)




# task 7
with open("manba.txt", "r") as file:
    mn = file.read()


with open("yangi.txt", "w") as file:
    file.write(mn)




# task 8
with open("matn.txt", "r") as file:
    uzunligi = file.read()
    print(f"({uzunligi})-> Uzunligi: {len(uzunligi)}")



# task 9
def read_specific_lines(tekst, line_numbers):
    result = []
    with open("tekst.txt", "r") as file:
        for i, line in enumerate(file, start=1):
            if i in line_numbers:
                result.append(line.strip())
    return result

print(read_specific_lines("info.txt", [2, 4, 6]))



# task 10
import os

filename = "temp.txt"

try:
    os.remove(filename)
    print(f"{filename} fayl o'chirildi.")
except FileNotFoundError:
    print("Bunday fayl mavjud emas!")





