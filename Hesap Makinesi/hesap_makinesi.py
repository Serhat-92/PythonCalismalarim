while True:

	sayi1 = float(input("sayi1: "))
	sayi2 = float(input("sayi2: "))

	islem = input("islem (+,-,*,/): ")	


	if islem == "+":
		sonuc = sayi1 + sayi2
		print(sonuc)

	elif islem == "-":
		sonuc = sayi1 - sayi2
		print(sonuc)

	elif islem == "*":
		sonuc = sayi1 * sayi2
		print(sonuc)

	elif islem == "/":
		if sayi2 == 0:
			print("Bölünemez")
		else:
			sonuc = sayi1 / sayi2
			print(sonuc)
	else:
		print("islem geçersiz")

	cevap = input("devam? (e/h): ")
	if cevap == "h":
		break