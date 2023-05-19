#Programa realizado por Bryan Leiva.
print("Welcome to bank Hispanoamericano!\n")
amount = float(input("Enter the amount of buy: "))
percentaje_interest = int(amount * 0.05)
mensuality = float(input("Enter the mensuality: "))
amortization = int(mensuality - percentaje_interest)
print(f"\n---INTEREST FEE---\nAmount = ₡{(amount)}\nInterest = ₡{percentaje_interest}\nMensuality = ₡{mensuality    }\nAmortización = ₡{amortization}\n")