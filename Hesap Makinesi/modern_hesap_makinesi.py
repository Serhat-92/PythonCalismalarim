def calc(x, y, ops):
    if ops not in "+-/*":
        return "Only +-/* !!!"

    if ops == "+":
        return str(x) + " " + ops + " " + str(y) + " = " + str(x + y)
    elif ops == "-":
        return str(x) + " " + ops + " " + str(y) + " = " + str(x - y)
    elif ops == "/":
        if y == 0:
            return "Sıfıra bölme hatası!"
        return str(x) + " " + ops + " " + str(y) + " = " + str(x / y)
    elif ops == "*":
        return str(x) + " " + ops + " " + str(y) + " = " + str(x * y)


while True:
    print("\n--- Yeni Hesap ---")

    # Çıkış seçeneği
    cikis = input("Çıkmak için 'q', devam etmek için Enter'a bas: ").strip().lower()
    if cikis == "q":
        print("Programdan çıkılıyor. Görüşürüz!")
        break

    try:
        x = int(input("Please enter first number: "))
        y = int(input("Please enter second number: "))
        ops = input("Choose between +,-,*,/: ").strip()

        print(calc(x, y, ops))

    except ValueError:
        print("Lütfen geçerli bir tam sayı giriniz!")