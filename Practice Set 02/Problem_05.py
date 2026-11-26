annual_income = int(input("Enter annual income: "))

first_slab_tax = 0
second_slab_tax = 0
third_slab_tax = 0
fourth_slab_tax = 0
fifth_slab_tax = 0

if annual_income > 300000:
    second_slab_tax = (min(annual_income, 600000) - 300000) * 0.05

if annual_income > 600000:
    third_slab_tax = (min(annual_income, 900000) - 600000) * 0.10

if annual_income > 900000:
    fourth_slab_tax = (min(annual_income, 1200000) - 900000) * 0.15

if annual_income > 1200000:
    fifth_slab_tax = (annual_income - 1200000) * 0.20

total_tax = second_slab_tax + third_slab_tax + fourth_slab_tax + fifth_slab_tax

income_after_tax = annual_income - total_tax

if annual_income > 0:
    effective_tax_rate = (total_tax / annual_income) * 100
else:
    effective_tax_rate = 0

print("Annual Income:", annual_income)
print("Tax on First Slab:", first_slab_tax)
print("Tax on Second Slab:", second_slab_tax)
print("Tax on Third Slab:", third_slab_tax)
print("Tax on Fourth Slab:", fourth_slab_tax)
print("Tax on Fifth Slab:", fifth_slab_tax)
print("Total Tax:", total_tax)
print("Income After Tax:", income_after_tax)
print("Effective Tax Rate:", effective_tax_rate, "%")
