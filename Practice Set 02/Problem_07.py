shopping_amount = float(input("Shopping Amount: "))
customer_category = input("Customer Category (Regular/Premium/VIP): ")
payment_method = input("Payment Method (UPI/Card/Cash): ")

customer_discount = 0
payment_discount = 0
flat_discount = 0

if shopping_amount < 500:
    print("Shopping amount must be at least 500")

else:
    if customer_category == "Regular":
        customer_discount = 5

    elif customer_category == "Premium":
        customer_discount = 10

    elif customer_category == "VIP":
        customer_discount = 15

    else:
        print("Invalid Customer Category")

    if payment_method == "UPI":
        payment_discount = 5

    elif payment_method == "Card":
        payment_discount = 2

    elif payment_method == "Cash":
        payment_discount = 0

    else:
        print("Invalid Payment Method")

    total_discount_percentage = customer_discount + payment_discount

    if total_discount_percentage > 20:
        total_discount_percentage = 20

    percentage_discount_amount = shopping_amount * total_discount_percentage / 100

    if shopping_amount > 10000:
        flat_discount = 500

    final_payable_amount = shopping_amount - percentage_discount_amount - flat_discount

    print("Original Amount:", shopping_amount)
    print("Customer Discount:", customer_discount, "%")
    print("Payment Discount:", payment_discount, "%")
    print("Total Discount:", total_discount_percentage, "%")
    print("Percentage Discount Amount:", percentage_discount_amount)
    print("Flat Discount:", flat_discount)
    print("Final Payable Amount:", final_payable_amount)
