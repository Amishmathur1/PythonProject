import csv

def calculate_bill(units, slabs):
    total_bill = 0
    breakdown = []

    for slab in slabs:
        min_u = int(slab['from_unit'])

        if slab['to_unit'].lower() == "above":
            max_u = units
        else:
            max_u = int(slab['to_unit'])

        rate = float(slab['rate_(rs.)'])

        if units >= min_u:
            applicable_units = min(units, max_u) - min_u + 1
            cost = applicable_units * rate
            total_bill += cost

            breakdown.append({
                "range": f"{min_u} - {slab['to_unit']}",
                "units": applicable_units,
                "rate": rate,
                "cost": cost
            })

        if units <= max_u:
            break

    return total_bill, breakdown


try:
    slabs = []

    with open('/home/amish/Documents/Coding Stuff/Python/ElecBill.csv', 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            clean_row = {
                key.strip().lower().replace(" ", "_"): value.strip()
                for key, value in row.items()
            }
            slabs.append(clean_row)

    # User inputs
    prev_reading = int(input("Enter previous meter reading: "))
    curr_reading = int(input("Enter current meter reading: "))

    if curr_reading < prev_reading:
        raise ValueError("Current reading cannot be less than previous reading!")

    units = curr_reading - prev_reading

    bill, breakdown = calculate_bill(units, slabs)

    # 🧾 FORMATTED BILL PRINT
    print("\n" + "="*50)
    print("           ELECTRICITY BILL")
    print("="*50)

    print(f"{'Previous Reading':<25}: {prev_reading}")
    print(f"{'Current Reading':<25}: {curr_reading}")
    print(f"{'Units Consumed':<25}: {units}")

    print("-"*50)
    print(f"{'Range':<15}{'Units':<10}{'Rate (₹)':<12}{'Cost (₹)':<12}")
    print("-"*50)

    for item in breakdown:
        print(f"{item['range']:<15}{item['units']:<10}{item['rate']:<12}{item['cost']:<12.2f}")

    print("-"*50)
    print(f"{'TOTAL BILL':<37}₹{bill:.2f}")
    print("="*50)

except FileNotFoundError:
    print("Error: CSV file not found.")

except ValueError as ve:
    print(f"Input Error: {ve}")

except Exception as e:
    print(f"Unexpected Error: {e}")

finally:
    print("\nThank you for using the Electricity Bill Calculator.")
