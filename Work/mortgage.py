# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month_count = 0

extra_paymet = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    if month_count >= extra_payment_start_month and month_count <= extra_payment_end_month :
        full_payment = payment + extra_paymet
    else:
        full_payment = payment
        
    principal = principal * (1+rate/12) - full_payment

    if principal < 0:
        full_payment = full_payment + principal
        principal = 0

    total_paid = total_paid + full_payment
    month_count = month_count + 1

    print(month_count, round(total_paid,2), round(principal, 2))