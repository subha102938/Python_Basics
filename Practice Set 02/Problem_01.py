electricity_units = int(input("Enter electricity units: "))

base_bill = 0
surcharge = 0
service_charge = 0

if electricity_units <= 100:
    base_bill = electricity_units * 3

elif electricity_units <= 200:
    base_bill = (100 * 3) + ((electricity_units - 100) * 5)

elif electricity_units <= 400:
    base_bill = (100 * 3) + (100 * 5) + ((electricity_units - 200) * 7)

else:
    base_bill = (100 * 3) + (100 * 5) + (200 * 7) + ((electricity_units - 400) * 10)

if base_bill > 2000:
    surcharge = base_bill * 0.05

elif base_bill < 500:
    service_charge = 50

final_bill = base_bill + surcharge + service_charge

print("Units Consumed:", electricity_units)
print("Base Bill:", base_bill)
print("Surcharge:", surcharge)
print("Service Charge:", service_charge)
print("Final Electricity Bill:", final_bill)
