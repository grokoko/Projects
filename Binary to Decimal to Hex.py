#Converter

def main():
    choice = None
    while choice != "0":
        print \
            ("""
            Converter for hexadecimals, decimals and binary.
            
            0 - Quit
            1 - convert hex
            2 - convert binary
            3 - convert decimal
            """)

        choice = input("You choose: ")
        print()

        if choice == "0":
            print("Goodbye.")

        elif choice == "1":
            h = input("Input hex: ")
            dec = int(h, 16)
            b = format(dec, '0>42b')
            print(h, "hex = ", dec, "decimal and ", b, "binary.")

        elif choice == "2":
            b = input("Input binary: ")
            dec = int(b, 2)
            h = hex(dec)
            print(b, "binary = ", dec, "decimal and ", h, "hex.")

        elif choice == "3":
            dec = int(input("Input decimal: "))
            h = hex(dec)
            b = format(dec, '0>42b')
            print(dec, "decimal =", h, "hex and", b, "binary.")

        else:
            print("\nSorry,", choice, "is not a correct choice.")

main()
input("\n\nPress enter to quit.")