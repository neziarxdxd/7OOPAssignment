amount = (10000.00)
name = input("Enter your name: ")
print("Current Amount: ", amount)
choice = input("Choose transaction: [W]-withdraw [D]-deposit [E]-exit : ")
if choice == "w":
    withdraw_money = int(input("Enter the amount: "))
    amount=amount-withdraw_money
    print("Thank you for your withdrawal. Your current amount is :", amount)
elif choice == "d":
    deposit_money = int(input("Enter the amount: "))
    amount = amount-deposit_money
elif choice == "e":
    exit()
else:
    print("Please try again")



