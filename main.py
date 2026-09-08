def ohms_law():
    print("\nOhm's Law: V = I × R")
    print("Leave exactly one value blank.")
    v = input("Voltage (V): ").strip()
    i = input("Current (A): ").strip()
    r = input("Resistance (Ω): ").strip()

    values = [v, i, r]
    if sum(x == "" for x in values) != 1:
        print("Enter exactly two values.\n")
        return

    try:
        if v == "":
            result = float(i) * float(r)
            print(f"Voltage = {result:.4f} V\n")
        elif i == "":
            if float(r) == 0:
                print("Resistance cannot be zero.\n")
                return
            result = float(v) / float(r)
            print(f"Current = {result:.4f} A\n")
        else:
            if float(i) == 0:
                print("Current cannot be zero.\n")
                return
            result = float(v) / float(i)
            print(f"Resistance = {result:.4f} Ω\n")
    except ValueError:
        print("Please enter valid numbers.\n")


def power_calculator():
    print("\nPower Calculator: P = V × I")
    try:
        voltage = float(input("Voltage (V): "))
        current = float(input("Current (A): "))
        print(f"Power = {voltage * current:.4f} W\n")
    except ValueError:
        print("Please enter valid numbers.\n")


def frequency_converter():
    print("\nFrequency Converter")
    try:
        hz = float(input("Frequency in Hz: "))
        print(f"kHz = {hz / 1_000:.6f}")
        print(f"MHz = {hz / 1_000_000:.9f}")
        print(f"GHz = {hz / 1_000_000_000:.12f}\n")
    except ValueError:
        print("Please enter a valid number.\n")


def resistor_calculator():
    print("\nResistor Calculator")
    print("Enter resistor bands using these colors:")
    colors = {"black": 0, "brown": 1, "red": 2, "orange": 3,
              "yellow": 4, "green": 5, "blue": 6, "violet": 7,
              "grey": 8, "gray": 8, "white": 9}
    try:
        first = input("1st band: ").lower().strip()
        second = input("2nd band: ").lower().strip()
        multiplier = input("Multiplier band: ").lower().strip()
        if first not in colors or second not in colors or multiplier not in colors:
            print("Invalid color.\n")
            return
        value = (colors[first] * 10 + colors[second]) * (10 ** colors[multiplier])
        print(f"Resistance = {value:g} Ω\n")
    except ValueError:
        print("Invalid input.\n")


def dbm_to_watts():
    print("\ndBm → Watts")
    try:
        dbm = float(input("Power (dBm): "))
        watts = 10 ** ((dbm - 30) / 10)
        print(f"Power = {watts:.10g} W\n")
    except ValueError:
        print("Please enter a valid number.\n")


def main():
    while True:
        print("╔══════════════════════════════╗")
        print("║         ⚡ ECE TOOLKIT       ║")
        print("╠══════════════════════════════╣")
        print("║ 1. Ohm's Law                 ║")
        print("║ 2. Power Calculator          ║")
        print("║ 3. Frequency Converter       ║")
        print("║ 4. Resistor Calculator       ║")
        print("║ 5. dBm → Watts               ║")
        print("║ 0. Exit                      ║")
        print("╚══════════════════════════════╝")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            ohms_law()
        elif choice == "2":
            power_calculator()
        elif choice == "3":
            frequency_converter()
        elif choice == "4":
            resistor_calculator()
        elif choice == "5":
            dbm_to_watts()
        elif choice == "0":
            print("Thanks for using ECE Toolkit!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
