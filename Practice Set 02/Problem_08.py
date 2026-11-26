applicant_age = int(input("Applicant Age: "))
monthly_salary = float(input("Monthly Salary: "))
existing_monthly_emi = float(input("Existing EMI: "))
credit_score = int(input("Credit Score: "))
employment_type = input("Employment Type (Salaried/Self-employed): ")

emi_ratio = (existing_monthly_emi / monthly_salary) * 100

if applicant_age < 21 or applicant_age > 60:
    loan_status = "Not Eligible"

elif credit_score < 600:
    loan_status = "Rejected"

elif emi_ratio > 40:
    loan_status = "High Financial Risk"

elif credit_score >= 600 and credit_score <= 699:
    loan_status = "Manual Review"

elif employment_type == "Salaried" and monthly_salary < 25000:
    loan_status = "Not Eligible"

elif employment_type == "Self-employed" and monthly_salary < 40000:
    loan_status = "Not Eligible"

elif employment_type == "Salaried" or employment_type == "Self-employed":
    loan_status = "ELIGIBLE"

else:
    loan_status = "Invalid Employment Type"

print("Loan Status:", loan_status)
print("EMI Ratio:", emi_ratio, "%")
