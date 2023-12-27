def calculate_years(principal, interest, tax, desired):
    sum = principal*interest - tax
    principal+=sum
    print(principal)
    if principal>desired:
        return principal
    else:
        calculate_years(principal,interest,tax,desired)

print(calculate_years(1000, 0.01, 0.18, 1200))