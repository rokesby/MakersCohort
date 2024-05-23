def calculate_tax_for_the_shire(grossPay):
    # The friendly Shire has a 20% tax rate
    return grossPay * 0.2


def calculate_tax_for_mirkwood(grossPay):
    # Dodgy Mirkwood has a 90% tax rate
    return grossPay * 0.9


def calculate_tax_for_mordor(grossPay):
    # Terrible Mordor has a 90% tax rate plus a fixed tax of £500.
    return grossPay * 0.9 + 500

def zero_tax(grossPay):
    return 0;



def report_pay(gross_pay, calculate_tax):
    # The `calculate_tax` argument is a function
    tax = calculate_tax(gross_pay)
    net_pay = gross_pay - tax
    return f"Your gross pay was {gross_pay}, minus {tax} makes your net pay {net_pay}"

print("Frodo's Pay:")
print(report_pay(5000.0, calculate_tax_for_the_shire))
# Your gross pay was 5000.0, minus 1000.0 makes your net pay 4000.0

print("Bombadil's Pay:")
print(report_pay(4320.0, calculate_tax_for_mirkwood))
# Your gross pay was 4320.0, minus 3888.0 makes your net pay 432.0

print("Mount Doom's Pay:")
print(report_pay(5000.0, calculate_tax_for_mordor))
# Your gross pay was 5000.0, minus 5000.0 makes your net pay 0.0

print("Reza's Pay:")
print(report_pay(5000.0, zero_tax))
# Your gross pay was 5000.0, minus 5000.0 makes your net pay 0.0

# ---------------------------



def as_sun_lover(temp):
    if temp>=25:
        return 'Great'
    else:
        return 'Not great'
    

def as_snow_lover(temp):
    if temp<0:
        return 'Great'
    else:
        return 'Not great' 

def report_weather(temp, mood):
    outcome = mood(temp)
    return f"Today's mood : {outcome}"


print(report_weather(24, as_sun_lover))
print(report_weather(26, as_sun_lover))
print(report_weather(-1, as_snow_lover))
print(report_weather(0, as_snow_lover))