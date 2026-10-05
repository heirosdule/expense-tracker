# Project: Expense Tracker - Installment 2
# Author: Heirosdule Nadala
# Simple expense tracker that asks the user for two expenses

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
item1 = input("First expense? ")
amount1 = float(input("Amount? "))
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print()
print("-" * 40)
print("SUMMARY")
print("  -", item1 + ":" + " " * (12 - len(item1)), "$" + str(amount1))
print("  -", item2 + ":" + " " * (12 - len(item2)), "$" + str(amount2))
print("Total spent:" + " " * 4, "$" + str(total))
print("Average:" + " " * 8, "$" + str(average))
print("-" * 40)
print("Made by:", name, "|  Installment 2")