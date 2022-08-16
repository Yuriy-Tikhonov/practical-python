# sears.py
bill_t = 0.11 * 0.001
total_t = 442

current_bills = 1
total_bills = 0
current_day = 1

while total_bills*bill_t < total_t :
    total_bills = total_bills + current_bills
    print( current_day, current_bills, total_bills, total_bills*bill_t)

    current_day = current_day + 1
    current_bills = current_bills * 2

# if and elif test

a = 30

if a < 30:
    print('<')
elif a == 30 :
    print('==')
else:
    print(">")


name = input('Name?')
age = input('Age?')

print(type(age))

print('Name: ', name, end=' ')
print('Age: ', age)

if age != '10':
    pass
else:
    print('== 10')


# sears2.py

bill_thickness = 0.11 * 0.001    # Meters (0.11 mm)
sears_height   = 442             # Height (meters)
num_bills      = 1
day            = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)