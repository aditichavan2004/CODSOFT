# Simple Calculator using Python

print("===== 🧮 SIMPLE CALCULATOR =====")

# Take user inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect Operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1/2/3/4): ")

# Perform calculation based on user choice
if choice == '1' or choice == '+':
    result = num1 + num2
    print(f"\n✅ Result: {num1} + {num2} = {result}")

elif choice == '2' or choice == '-':
    result = num1 - num2
    print(f"\n✅ Result: {num1} - {num2} = {result}")

elif choice == '3' or choice == '*':
    result = num1 * num2
    print(f"\n✅ Result: {num1} × {num2} = {result}")

elif choice == '4' or choice == '/':
    if num2 == 0:
        print("\n⚠️ Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"\n✅ Result: {num1} ÷ {num2} = {result}")

else:
    print("\n❌ Invalid choice. Please select 1, 2, 3, or 4.")

print("\nThank you for using the calculator! 😊")
