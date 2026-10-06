# Project: Expense Tracker - Installment 3
# Author: Your Full Name
# Expense tracker that does math (subtotal, tax, budget)

print("=" * 40)
print(" " * 10 + "EXPENSE TRACKER")
print(" " * 5 + "Know where your money goes.")
print("=" * 40)

print()
print("MAIN MENU")
print("  [1] Add an expense" + " " * 12 + "(coming soon)")
print("  [2] View all expenses" + " " * 9 + "(coming soon)")
print("  [3] Show total spent" + " " * 10 + "(coming soon)")
print("  [4] Exit" + " " * 22 + "(coming soon)")
print()

name = input("What's your name? ")
print("Welcome,", name + "! Let's log two expenses.")

subtotal = 0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal = subtotal + amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal = subtotal + amount2

average = subtotal / 2

tax_percent = float(input("Tax rate %? "))
tax = subtotal * (tax_percent / 100)
total = subtotal + tax

budget = float(input("Your budget? "))
over_budget = total > budget
left = budget - total

print()
print("-" * 40)
print("SUMMARY")
print("  -", item1 + ":\t$" + str(amount1))
print("  -", item2 + ":\t$" + str(amount2))
print("Subtotal:\t$" + str(subtotal))
print("Average:\t$" + str(average))
print("Tax (" + str(tax_percent) + "%):\t$" + str(tax))
print("Grand total:\t$" + str(total))
print("Over budget?\t" + str(over_budget))
print("Left in budget:\t$" + str(left))
print("-" * 40)
print("Made by:", name, "|  Installment 3")