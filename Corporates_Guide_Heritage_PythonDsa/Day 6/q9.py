balance = 50000.00
pin = "2004"

# 1. PIN Gate
if input("Enter PIN: ").strip() != pin:
    print("Incorrect PIN.")
else:
    # 2. Menu and Choice
    print("1.Balance | 2.Deposit | 3.Withdraw | 4.Exit")
    choice = input("Select option (1-4): ").strip()
    
    # 3. Operations Engine
    match choice:
        case "1":
            print(f"Balance: INR {balance:,.2f}")
        case "2":
            amt = float(input("Enter deposit amount: INR "))
            if amt > 0:
                balance += amt
                print(f"Updated Balance: INR {balance:,.2f}")
            else:
                print("Invalid amount.")
        case "3":
            amt = float(input("Enter withdrawal amount: INR "))
            if 0 < amt <= balance:
                balance -= amt
                print(f"Withdrew: INR {amt:,.2f}\nRemaining: INR {balance:,.2f}")
            else:
                print("Insufficient funds or invalid amount.")
        case "4":
            print("Session ended.")
        case _:
            print("Invalid selection.")