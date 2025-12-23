# print("Symbols :  🍒 🍉 🥭 🔔 ⭐")
import random
import time


def spin_row():
    symbols = ['🍒', '🍉', '🥭', '🔔', '⭐']

    # NOTE list comperhension
    return [random.choice(symbols) for _ in range(3)]


def print_spinning(row):
    print(" | ".join(row))


def betting(row, client_bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return client_bet * 3
        elif row[0] == '🍉':
            return client_bet * 4
        elif row[0] == '🥭':
            return client_bet * 5
        elif row[0] == '🔔':
            return client_bet * 10
        elif row[0] == '⭐':
            return client_bet * 20

    return 0


def client_cash():
    balance = 0
    is_running = True

    while is_running:
        input_balance = input("Enter your cash: ")

        if not input_balance.isdigit():
            print("Please enter a valid positive number.")
            continue

        input_balance = int(input_balance)

        if input_balance <= 0:
            print("Amount must be greater than zero.")
            continue

        client_confirm = input(f"Do you want to transfer this amount ${input_balance}?"
                               '(Press ENTER to confirm, type anything to cancel): ')

        if client_confirm == "":
            balance += input_balance
            print(f"${balance} is your balance now.")
            is_running = False   # stop after successful transfer
        else:
            print("Request denied!")

    return balance


def main():
    balance = client_cash()  # returning balance
    print()

    print("****************************")
    print("Welcome to Python Slots Game")
    print("Symbols :  🍒 🍉 🥭 🔔 ⭐")
    print("****************************")

    print()
    print(f"Now you have this amount ${balance}")

    while True:
        while balance > 0:
            print(f"Current balance: ${balance}")

            client_bet = input("Place your bet amount: ")

            if not client_bet.isdigit():
                print("ERROR!! YOU CAN'T DO THAT!!!!!")
                continue

            # <<<<< doing int to the client betting
            client_bet = int(client_bet)

            if client_bet > balance:
                print("INSUFFICIENT BALANCE :( ")
                continue

            if client_bet <= 0:
                print("BET must be greater than zero.")
                continue

            balance -= client_bet

            row = spin_row()
            print("Spinning.....\n")
            time.sleep(2)
            print_spinning(row)

            payout = betting(row, client_bet)

            if payout > 0:
                print(f"You won ${payout}")
            else:
                print("Sorry you lost this round.")

            balance += payout

            play_again = input("Do you want to spin again? (y/n): ").lower()

            if play_again != 'y':
                break
        print()
        print(f"Game over! Your final balance is ${balance}")
        print()
        
        if balance <= 0:
            print("Your balance is $0. You need to deposit more to play again.")
            deposit_more = input(
                "Do you want to deposit again? (y/n): ").lower()
            if deposit_more == 'y':
                balance = client_cash()
                continue
            else:
                print("Thanks for playing")
                break
        else:
            print("TY bro") #user quit with money left
            break


if __name__ == '__main__':
    main()


# wanna deposit again? then run again if they fill their charge
