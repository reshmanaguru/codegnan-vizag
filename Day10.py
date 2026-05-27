Program for ATM machine:

---------------------------------

user_information = {"Name":"Reshma",
                    "Mobile Number": "",
                    "ATM PIN": "3008",
                    "Balance": 50000,
                    "Transaction History" : []
                    }
print("Please insert your ATM card")
remaining_attempts = 3
while remaining_attempts > 0:
    user_pin = input("Enter 4 digits pin:")
    if len(user_pin) ==4:
        if user_pin in user_information["ATM PIN"]:
            a = int(input("enter \n1.withdrawl \n2.check balance \n3.mini statement \n4.deposit"))
            if a == 1:
                w_a = int(input("enter withdrawl amount:"))
                if w_a > user_information["Balance"]:
                    print("insufficient balance")
                elif w_a < 100:
                    print("please enter minimum amount")
                elif w_a %100 !=0:
                    print("enter amount without chnage:")
                else:
                    print("take you amount")
                    break
            elif a == 2:
                print("your balance amount is :")
                break
            elif a == 3:
                print("your mini statement :")
                break
            elif a == 4:
                print("enter withdraw amount:")
                break
            else:
                remaining_attempts -= 1
                if remaining_attempts > 0 :
                    print(f" you have {remaining_attempts} chances left.please enter correct pin")
                else:
                    print("your card has been temporarily blocked")



            
            
