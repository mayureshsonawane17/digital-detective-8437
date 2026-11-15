
def main():
    print("=== Decimal to Binary and Hexadecimal Converter ===")
    user_input = input("Enter a positive decimal number: ")
    
    decimal_number = int(user_input)
    binary_representation = bin(decimal_number)
    hex_representation = hex(decimal_number)
    
    print("\nResults:")
    print(f"Decimal:     {decimal_number}")
    print(f"Binary:      {binary_representation}")
    print(f"Hexadecimal: {hex_representation}")

if __name__ == "__main__":
    main()
