def calculate_bill(units):
    if units <= 100:
        return 0, ["0 - 100 Units", "0"], 0
    elif units <= 200:
        cost = (units - 100) * 2.35
        return cost, ["0 - 100 Units", "0"], [f"101 - {units} Units", cost]
    elif units <= 400:
        cost = (units - 200) * 4.70 + (100 * 2.35)
        return cost, ["0 - 100 Units", "0"], ["101 - 200 Units", 225], [f"201 - {units} Units", cost]
    elif units <= 600:
        cost = (units - 400) * 6.30 + (200 * 4.70) + (100 * 2.35)
        return cost, ["0 - 100 Units", "0"], ["101 - 200 Units", 225], ["201 - 400 Units", 900], [f"401 - {units} Units", cost]
    elif units <= 800:
        cost = (units - 600) * 9.45 + (100 * 8.40) + (300 * 4.70) + (100 * 6.30)
        return cost, ["0 - 100 Units", "0"], ["101 - 400 Units", 1350], ["401 - 500 Units", 600], ["501 - 600 Units", 800], [f"601 - {units} Units", cost]
    elif units <= 1000:
        cost = (units - 800) * 10.50 + (200 * 9.45) + (100 * 8.40) + (300 * 4.70) + (100 * 6.30)
        return cost, ["0 - 100 Units", "0"], ["101 - 400 Units", 1350], ["401 - 500 Units", 600], ["501 - 600 Units", 800], ["601 - 800 Units", 1800], [f"801 - {units} Units", cost]
    else:
        cost = (units - 1000) * 11.55 + (200 * 10.50) + (200 * 9.45) + (100 * 8.40) + (300 * 4.70) + (100 * 6.30)
        return cost, ["0 - 100 Units", "0"], ["101 - 400 Units", 1350], ["401 - 500 Units", 600], ["501 - 600 Units", 800], ["601 - 800 Units", 1800], ["801 - 1000 Units", 2000], [f"1001 - {units} Units", cost]

def print_table(units, rows, total):
    print("\n" + "Consumed Units".ljust(20) + "Amount")
    for row in rows:
        print(row[0].ljust(20) + str(row[1]))
    print("Total".ljust(20) + str(total))
    
def main():
    while True:
        user_input = input("Enter the number of units consumed (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        try:
            units = float(user_input)
            total, *rows = calculate_bill(units)
            print_table(units, rows, total)
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
