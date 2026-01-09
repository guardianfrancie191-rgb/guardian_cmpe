
'''''
welcome_messages():
card_reader(isCardInserted):
input_and_validate_pin_number(pinNumber): return isValid
transaction_selection(transaction):
amount_and_account_selection(amount):
transaction_validation(transaction):
amount_and_account_validation(amount, balance): return isValid
card_ejection():
cash_dispensing():
print_receipt(amount, balance):
'''



import time
amount = 0
balance = 1000
pin_number = "1414"

def welcome_messages():
    time.sleep(1)
    print("WELCOME TO FRNC BANK ")
    time.sleep(1)
    print("............................")
    time.sleep(1)
    print("Please enter your card")

def card_reader(isCardInserted):
    if isCardInserted == "YES":
        print("Card is inserted")
        return True
    else:
        return False

def input_and_validate_pin_number():
    for i in range(4):
        inputPin = input("Please enter your pin number: ")

        if inputPin == pin_number:
            print("Correct PIN")
            return True
        else:
            print("Incorrect pin number")

    print("Card Blocked")
    return False



def transaction_selection():
    transaction = input ("Please enter your transaction: ")
    return transaction


def transaction_validation(amount, balance):
     if balance > amount:
         return True
     else:
         print ("Insufficient Fund. Please contact your sugar mom")
         return False

def print_receipt(amount):
    global balance
    balance = balance - amount
    print("Remaining Balance: " + str(balance))
    print("Please get your receipt")



def card_ejection():
    print("Please get your card, Card is ejected")


def cash_dispensing():
    print("Please get your cash")

while True:
    welcome_messages()
    isCardInserted = input("Is Card Inserted?")  # SENSOR
    if not card_reader(isCardInserted):  # FALSE
        continue

    print("Next Step")

    if not input_and_validate_pin_number():
        break

    print("Next Steps")

    amount = int(input("Please enter your amount: "))

    transaction = transaction_selection()

    if transaction == "withdraw":
        if transaction_validation(amount, balance):
            print("Withdraw Operation Started..")
            time.sleep(3)
            card_ejection()
            time.sleep(2)
            cash_dispensing()
            time.sleep(2)
            print_receipt(amount)
            time.sleep(1)


    elif transaction == "check balance":
        print("Check Balance Operation Started ...")
        break
    else:
        continue