num = int(input("Этот год: "))

if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
    print(f"{num} - високосный год")
else:
    print(f"{num} - не високосный год")