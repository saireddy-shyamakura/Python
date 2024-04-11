import random 

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

def get_slot_machine_spin(rows ,cols ,symbols) :
    all_symbols =[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol) 
    columns = []
    for _ in range(cols):
        column =[]
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machines(columns):
    for row in range(len(columns[0])) :
        for i, column in enumerate(columns) :
            if  i != len(columns) -1 :
                print(column[row], end = " | ")
            else :
                 print(column[row],end="")
        print()

def deposit() :
    while True :
        amount = input("deposit your amount? : ")
        if amount.isdigit() :
            amount = int(amount)
            if amount > 0 :
                break
            else:
                print("enter amount greater than zero")
        else:
            print("please enter a number")
    return amount

def get_number_of_lines():
    while True :
        lines = input("enter the number of lines 1 to "+ str(MAX_LINES) + " : ")
        if lines.isdigit() :
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("enter a vaild number")
        else:
            print("please enter a number")
    return lines

def get_bet() :
    while True :
        amount = input("give your bet on each line : ")
        if amount.isdigit() :
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET :
                break
            else:
                print(f"enter amount betwen {MIN_BET} - {MAX_BET}.")
        else:
            print("please enter a number")
    return amount 

def main():
    balance = deposit() 
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet > balance :
            print("you dont have enough of balance and your current balance is ", balance)
        else :
            break
    print(f"you are betting {bet} on {lines} lines. your total bet is  ",lines*bet)
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machines(slots)

main()