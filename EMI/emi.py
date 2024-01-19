# p=int(input("enter the principal amount"))
# r=float(input("enter the intrsrt"))
# n=float(input("year"))
# emi=(p * r * (1 + r) ** n) / ((1 + r) ** (n - 1))

# yea_mnth= 
# print(yea_mnth)
# print(emi)
def calculate_emi(p, r, n):
    emi = (p * r * (1 + r) ** n) / ((1 + r) ** (n - 1))
    return emi

# Input values
# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the monthly interest rate (in decimal): "))
# tenure = int(input("Enter the loan tenure in months: "))

# result_emi = calculate_emi(principal, rate, tenure)
# print(f"The Equated Monthly Installment (EMI) is: {result_emi:.2f}")
# def calculate_emi(principal, rate, time):
#     rate = rate / 12 / 100  # converting annual interest rate to monthly and to decimal
#     emi = principal * rate * ((1 + rate) ** time) / (((1 + rate) ** time) - 1)
#     return emi

def calculate_total_interest(emi, principal, time):
    total_interest = (emi * time) - principal
    return total_interest

# Input values
principal_amount = float(input("Enter the loan amount: "))
annual_interest_rate = float(input("Enter the annual interest rate: "))
loan_tenure_years = int(input("Enter the loan tenure in years: "))

loan_tenure_months = loan_tenure_years * 12

emi = calculate_emi(principal_amount, annual_interest_rate, loan_tenure_months)
total_interest = calculate_total_interest(emi, principal_amount, loan_tenure_months)
total_payable = principal_amount + total_interest

print(f"The Equated Monthly Installment (EMI) is: {emi:.2f}")
print(f"The total interest payable is: {total_interest:.2f}")
print(f"The total payable amount is: {total_payable:.2f}")
