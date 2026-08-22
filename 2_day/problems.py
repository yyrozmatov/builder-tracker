# # Oddiy

# # 1 - musbat

# # 2 - juft

# # 3 - ikkalasidan kattasi

# # 4 - 18+ tekshirish

# # 5 - Parol tekshirish

# # 6 - Son 100 dan kattami

# son = int(input("Son kiriting: "))

# if son > 100:
# 	print("Son 100 dan katta")
# else:
# 	print("Son 100 dan katta emas")

# # 7 - Son 10-50 oralig'idami
# son = int(input("Son kiriting: "))

# if son >= 10 and son <= 50:
# 	print("Son 10-50 orasida")
# else:
# 	print("Son 10-50 orasida emas")

# # 8 - Ikki son tengmi?

# son_1 = int(input("Birinchi sonni kiriting: "))
# son_2 = int(input("Ikkinchi sonni kiriting: "))

# if son_1 == son_2:
# 	print("Sonlar teng")
# else:
# 	print("Sonlar teng emas")

# # 9 - Xona harorati

# harorat = int(input("Xona haroratini kiriting: "))

# if harorat >= 25:
# 	print("Xona harorati issiq")
# elif harorat < 25 and harorat >= 10:
# 	print("Xona harorati iliq")
# else:
# 	print("Xona harorati sovuq")

# # 10 - Ballga qarab o'tdi/yiqildi

# ball = float(input("Ball kiriting: "))

# if ball >= 80.0:
# 	print("Davlat grand")
# elif ball >= 70.0:
# 	print("To'lov shartnoma")
# else:
# 	print("Yiqildi")

# # 11 - Baho A/B/C/D/F

# baho = int(input("Baho kiriting: "))

# if baho == 100:
# 	print("A")
# elif baho > 89:
# 	print("B")
# elif baho > 79:
# 	print("C")
# elif baho > 69:
# 	print("D")
# else:
# 	print("F")

# # 12 - Yosh kategoriyasi

# yosh = int(input("Yoshingizni kiriting: "))

# if yosh >= 30:
# 	print("Kattalar")
# elif yosh >= 18:
# 	print("Yoshlar")
# else:
# 	print("Bolalar")

# # 13 - Daromadga qarab soliq

# daromad = int(input("Daromadingizni kiriting: "))

# if daromad >= 5000000:
# 	print("Soliq 500 000 so'm")
# elif daromad >= 3000000:
# 	print("Soliq 300 000 so'm")
# else:
# 	print("Soliq 100 000 so'm")

# # 14 - Tezlik: sekin/normal/tez

# tezlik = int(input("Tezlikni kiriting (km/soat): "))

# if tezlik >= 100:
# 	print("Tez")
# elif tezlik >= 60:
# 	print("Normal")
# else:
# 	print("Sekin")

# # 15 - Kun: Weekday/weekend

# day = input("Enter day: ")

# if day.capitalize() == "Monday" or day.capitalize() == "Tuesday" or day.capitalize() == "Wednesday" or day.capitalize() == "Thoursday" or day.capitalize() == "Friday":
# 	print("Today weekday")
# elif day.capitalize() == "Saturday" or day.capitalize() == "Sunday":
# 	print("Today weekend")
# else:
# 	print("Enter reset")

# # 16 - Oy raqamidan fasl

# oy_raqami = int(input("Oy raqamini kiriting: "))

# if oy_raqami <= 2 or oy_raqami == 12:
# 	print("Qish")
# elif oy_raqami <= 5:
# 	print("Bahor")
# elif oy_raqami <= 8:
# 	print("Yoz")
# elif oy_raqami <= 11:
# 	print("Kuz")
# else:
# 	print("12 gacha")

# # 18 - BMI

# boy = float(input("Bo'yingizni kiriting (m): "))
# vazn = int(input("Vazningizni kiriting (kg): "))

# bmi = vazn / (boy ** 2)

# if bmi >= 24:
# 	print(f"{int(bmi)} Normadan baland")
# elif bmi >= 18:
# 	print(f"{int(bmi)} Norma")
# else:
# 	print(f"{int(bmi)} Normadan past")

# # 19 - Xarid summasiga chegirma

# xarid_summa = int(input("Xarid summani kiriting: "))

# if xarid_summa >= 1000000:
# 	xarid_summa - xarid_summa * 0.2
# 	print("Sizga 20%  chegirma")
# elif xarid_summa >= 100000:
# 	xarid_summa - xarid_summa * 0.1
# 	print("Sizga 10%  chegirma")
# else:
# 	print("Afsuski chegirma uchun xarid summasi yetarli emas")

# # 20 - Imtihon natijasiga qarab status

# imtihon_natija = int(input("Imtihon natijasini kiriting: "))

# if imtihon_natija >= 80:
# 	print("Legend")
# elif imtihon_natija >= 70:
# 	print("Professional")
# else:
# 	print("Invincible")

# # 21 - Uchta sondan eng kattasini topish

# a = int(input())
# b = int(input())
# c = int(input())

# if a > b > c:
# 	print(a)
# elif b < a < c:
# 	print(b)
# else:
# 	print(c)

# # 22 - Uchta sondan eng kichigini top

# a = int(input())
# b = int(input())
# c = int(input())

# if a < b < c:
# 	print(a)
# elif b < a < c:
# 	print(b)
# else:
# 	print(C)

# # 23 - Login + password tekshir

# login = input()
# password = input()

# if login and password:
# 	print("True")
# elif login or password:
# 	print("One true")
# else:
# 	print("Is not defined")

# # 24 - Yosh va tarjibaga qarab kurs daraja

# yosh = int(input())
# tarjiba = int(input())

# if yosh >= 18:
# 	if tarjiba >= 1:
# 		print("Senior")
# 	else:
# 		print("War mode")
# else:
# 	if tarjiba >= 1:
# 		print("War mode")
# 	else:
# 		print("Foundation")

# # 25 - Real conditional problem:

# roza = input("Ro'za tutganmisiz?: ")

# if roza.lower() == "ha":
# 	print("Savob tarqatamiz")
# elif roza.lower() == "yo'q":
# 	print("Suv ichish mumkin")
# else:
# 	print("Ha yoki yo'q javob bering")




