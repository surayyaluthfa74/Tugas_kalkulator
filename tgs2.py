player = int(input("Masukkan poin player : "))
musuh = int(input("Masukkan poin musuh : "))

while player > musuh:
    print("Player menang")

    player += musuh

    print("Poin player sekarang :", player)

    musuh = int(input("Masukkan poin musuh : "))

print("======================")
print("Game Over")