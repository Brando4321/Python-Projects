import random


MAX_LINES = 3
MAX_BET= 100
MIN_BET= 1

ROWS= 3
COLS= 3

symbol_count= {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value= {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}
def check_winnings(columns, lines, bet, values):
    winnings= 0
    winning_lines=[]
    # This means we are looking at every row
    for line in range(lines):
        # We wanto to check the first symbol in the first column of the current row
        symbol = columns[0][line]
        # Look through every column
        for column in columns:
            symbol_to_check= column[line]
            # if the symbols are not the same we break out of the loop
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines
            
        
def get_slot_machine_spin(rows,cols,symbols):
    all_symbols =[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    # Here we are adding an empty list called column
    columns= []
    # Setting a for loop in the range of cols for every column that we have
    for _ in range(cols):
        # Column is an empty list
        column= []
        # Current_sybols is a copy of the original list all_symbols using : to represent a copy
        current_symbols= all_symbols[:]
        # Loop through the values we need to generate
        for _ in range(rows):
            # This gets a random value current_symbols which is a copy of all symbols
            value= random.choice(current_symbols)
            # Here removes the random selected value from the list 
            current_symbols.remove(value)
            # Here adds or appends the vale back into the empty column list
            column.append(value)
            
        columns.append(column)
        
        # Return the list columns with all the values
    return columns
            
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row],end="" )
                
        print()
    
def deposit():
    while True:
        amount = input("What would you like to deposit? $ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")
    return amount


def get_number_of_lines():
    while True:
        line = input("Enter a number of lines to bet on (1-"+str(MAX_LINES)+")? ")
        if line.isdigit():
            line = int(line)
            if 1 <= line <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")
    return line

def get_bet():
    while True:
        amount = input("Enter a number of lines to bet on each line? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number")
    return amount

def spin(balance):
    line = get_number_of_lines()
    while True:
        bet= get_bet()
        total_bet= bet * line
        
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {line} lines. Total bet is equal to: ${total_bet} ")
  
    slots= get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines= check_winnings(slots,line,bet, symbol_value)
    print(f"You won${winnings}.")
    print(f"You won on lines: ", * winnings_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current Balance is: ${balance}")
        answer= input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")
main()