balance = 945.70

while True:
    try:
        num = float(input("Deposit: "))
        break
    except ValueError:
        print("Must be a valid quantity")

balance += num
print(f"Balance: {balance}")