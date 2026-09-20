# def energy_charge(units):
#     """Return the tiered energy charge in baht for `units` kWh.
#     Tier 1: first 150 units  @ 3.00 THB/unit
#     Tier 2: next 250 units   @ 4.00 THB/unit   (units 151-400)
#     Tier 3: everything above @ 4.50 THB/unit   (units 401+)
#     Raise ValueError if units is negative.
#     Hint: accumulate the charge tier by tier (Week 4)."""
#     if units < 0:
#         raise ValueError("raises ValueError")
#     else:
#         if units <= 150:
#             cost=units*3
#         elif units <= 400:
#             cost= 150 * 3 + (units-150) * 4
#         else:
#             cost= 150 * 3 + 250 * 4 + (units - 400) * 4.5
#         return(cost)
# u = float(input("Enter energy_charge(units): "))
# print(energy_charge(u))

# def service_charge(rate_type):
#     """Return the fixed monthly service fee for a customer type:
#        'residential'    -> 20.00
#        'small_business' -> 40.00
#        'large_business' -> 300.00
#     Raise ValueError for any other rate_type."""
#     if rate_type == 'residential':
#         return 20.0
#     elif rate_type == 'small_business':
#         return 40.0
#     elif rate_type == 'large_business':
#         return 300.0
#     else:
#         raise ValueError("raises ValueError")   
# rt = input("Enter the customer type:")
# print(service_charge(rt)) 

# def ft_charge(units, ft_rate):
#     """Return the fuel-adjustment (Ft) charge: units * ft_rate."""
#     if units < 0 or ft_rate < 0:
#         raise ValueError("raises ValueError")
#     else:
#         rate = units * ft_rate
#         return rate 
# un, ft = map(float, input("Enter the units and ft_rate: ").split( ))
# print(ft_charge(un,ft))

# def units_used(previous, current):
#     """Return the number of units consumed (current - previous).
#     Raise ValueError if either reading is negative, or if current < previous."""
#     if previous<0 or current<0 or current < previous:
#         raise ValueError('raises ValueError')
#         # return 'raises ValueError'
#     units_consumed=current-previous
#     return units_consumed   

# def energy_charge(units):
#     """Return the tiered energy charge in baht for `units` kWh.
#     Tier 1: first 150 units  @ 3.00 THB/unit
#     Tier 2: next 250 units   @ 4.00 THB/unit   (units 151-400)
#     Tier 3: everything above @ 4.50 THB/unit   (units 401+)
#     Raise ValueError if units is negative.
#     Hint: accumulate the charge tier by tier (Week 4)."""
#     if units < 0:
#         raise ValueError("raises ValueError")
#     else:
#         if units <= 150:
#             cost=units*3
#         elif units <= 400:
#             cost= 150 * 3 + (units-150) * 4
#         else:
#             cost= 150 * 3 + 250 * 4 + (units - 400) * 4.5
#         return cost

# def service_charge(rate_type):
#     """Return the fixed monthly service fee for a customer type:
#        'residential'    -> 20.00
#        'small_business' -> 40.00
#        'large_business' -> 300.00
#     Raise ValueError for any other rate_type."""
#     if rate_type == 'residential':
#         return 20.0
#     elif rate_type == 'small_business':
#         return 40.0
#     elif rate_type == 'large_business':
#         return 300.0
#     else:
#         raise ValueError("raises ValueError")   


# def ft_charge(units, ft_rate):
#     """Return the fuel-adjustment (Ft) charge: units * ft_rate."""
#     if units < 0 or ft_rate < 0:
#         raise ValueError("raises ValueError")
#     else:
#         rate = units * ft_rate
#         return rate 


# def subtotal(units, rate_type, ft_rate):
#     """Return energy_charge + service_charge + ft_charge (before VAT).
#     Reuse the functions above."""    
#     sub_total = energy_charge(units) + service_charge(rate_type) + ft_charge(units, ft_rate)
#     return sub_total

# un,rt,ft=input("Enter units, rate_type and ft_rate:").split( )
# un=float(un)
# ft=float(ft)
# print(subtotal(un,rt,ft))

# def vat(amount, rate=0.07):
#     """Return the VAT on `amount`. Default VAT rate is 7%."""
#     if amount<0 or rate<0:
#         raise ValueError("raises ValueError")
#     else:
#         vat_amount = amount * rate
#         return vat_amount

# def round_baht(amount):
#     """Return `amount` rounded to 2 decimal places."""
#     return f"{amount:.2f}"
# print(round_baht(115.084))

# def units_used(previous, current):
#     """Return the number of units consumed (current - previous).
#     Raise ValueError if either reading is negative, or if current < previous."""
#     if previous<0 or current<0 or current < previous:
#         raise ValueError('raises ValueError')
#         # return 'raises ValueError'
#     units_consumed=current-previous
#     return units_consumed   

# def energy_charge(units):
#     """Return the tiered energy charge in baht for `units` kWh.
#     Tier 1: first 150 units  @ 3.00 THB/unit
#     Tier 2: next 250 units   @ 4.00 THB/unit   (units 151-400)
#     Tier 3: everything above @ 4.50 THB/unit   (units 401+)
#     Raise ValueError if units is negative.
#     Hint: accumulate the charge tier by tier (Week 4)."""
#     if units < 0:
#         raise ValueError("raises ValueError")
#     else:
#         if units <= 150:
#             cost=units*3
#         elif units <= 400:
#             cost= 150 * 3 + (units-150) * 4
#         else:
#             cost= 150 * 3 + 250 * 4 + (units - 400) * 4.5
#         return cost

# def service_charge(rate_type):
#     """Return the fixed monthly service fee for a customer type:
#        'residential'    -> 20.00
#        'small_business' -> 40.00
#        'large_business' -> 300.00
#     Raise ValueError for any other rate_type."""
#     if rate_type == 'residential':
#         return 20.0
#     elif rate_type == 'small_business':
#         return 40.0
#     elif rate_type == 'large_business':
#         return 300.0
#     else:
#         raise ValueError("raises ValueError")   


# def ft_charge(units, ft_rate):
#     """Return the fuel-adjustment (Ft) charge: units * ft_rate."""
#     if units < 0 or ft_rate < 0:
#         raise ValueError("raises ValueError")
#     else:
#         rate = units * ft_rate
#         return rate 


# def subtotal(units, rate_type, ft_rate):
#     """Return energy_charge + service_charge + ft_charge (before VAT).
#     Reuse the functions above."""
#     sub_total = energy_charge(units) + service_charge(rate_type) + ft_charge(units, ft_rate)
#     return sub_total


# def vat(amount, rate=0.07):
#     """Return the VAT on `amount`. Default VAT rate is 7%."""
#     if amount<0 or rate<0:
#         raise ValueError("raises ValueError")
#     else:
#         vat_amount = amount * rate
#         return vat_amount


# def round_baht(amount):
#     """Return `amount` rounded to 2 decimal places."""
#     return f"{amount:.2f}"


# def total_due(units, rate_type, ft_rate, vat_rate=0.07):
#     """Return the final amount due, rounded to 2 decimals:
#        round_baht(subtotal + vat(subtotal))."""
#     total_due = round_baht(subtotal(units, rate_type, ft_rate) + vat(subtotal(units, rate_type, ft_rate), vat_rate))
#     return total_due

# print(total_due(420, 'residential', 0.20, vat_rate=0.10))
# print(total_due(420, 'residential', 0.20))
# print(total_due(100, 'residential', 0.20))

# def format_baht(amount):
#     """Return `amount` as a baht string with a thousands separator and
#     exactly 2 decimals, e.g. 1759.08 -> '฿1,759.08'.
#     Hint: f-string  f"฿{amount:,.2f}"."""
#     return f"฿{amount:.2f}"
# print(format_baht(1759.08))
# print(format_baht(363.8))

# def is_high_usage(units, threshold=400):
#     """Return True if `units` is strictly greater than `threshold`, else False."""
#     if units > threshold:
#         return True
#     else:
#         return False
# units_input=int(input("enter your units:"))
# option=int(input("enter 1 to type threshold(optional):"))
# if option == 1:
#     threshold_input=int(input("Enter your threshold: "))
#     print(is_high_usage(units_input,threshold_input))
# else:
#     print(is_high_usage(units_input))

# def months_until_over_budget(start_bill, monthly_increase, budget_cap):
#     """A bill starts at `start_bill` and rises by `monthly_increase` each month.
#     Return how many monthly increases are needed before the bill is strictly
#     greater than `budget_cap`. Return 0 if it already exceeds the cap.
#     Hint: use a while loop with a counter (Week 4)."""
#     counter=0
#     while start_bill <= budget_cap:
#         start_bill += monthly_increase
#         counter += 1
#     return counter
# sb, mi, bc = map(float, input("Enter the values:").split())
# print(months_until_over_budget(sb, mi, bc))

def units_used(previous, current):
    """Return the number of units consumed (current - previous).
    Raise ValueError if either reading is negative, or if current < previous."""
    if previous<0 or current<0 or current < previous:
        raise ValueError('raises ValueError')
        # return 'raises ValueError'
    units_consumed=current-previous
    return units_consumed   

def energy_charge(units):
    """Return the tiered energy charge in baht for `units` kWh.
    Tier 1: first 150 units  @ 3.00 THB/unit
    Tier 2: next 250 units   @ 4.00 THB/unit   (units 151-400)
    Tier 3: everything above @ 4.50 THB/unit   (units 401+)
    Raise ValueError if units is negative.
    Hint: accumulate the charge tier by tier (Week 4)."""
    if units < 0:
        raise ValueError("raises ValueError")
    else:
        if units <= 150:
            cost=units*3
        elif units <= 400:
            cost= 150 * 3 + (units-150) * 4
        else:
            cost= 150 * 3 + 250 * 4 + (units - 400) * 4.5
        return cost

def service_charge(rate_type):
    """Return the fixed monthly service fee for a customer type:
       'residential'    -> 20.00
       'small_business' -> 40.00
       'large_business' -> 300.00
    Raise ValueError for any other rate_type."""
    if rate_type == 'residential':
        return 20.0
    elif rate_type == 'small_business':
        return 40.0
    elif rate_type == 'large_business':
        return 300.0
    else:
        raise ValueError("raises ValueError")   


def ft_charge(units, ft_rate):
    """Return the fuel-adjustment (Ft) charge: units * ft_rate."""
    if units < 0 or ft_rate < 0:
        raise ValueError("raises ValueError")
    else:
        rate = units * ft_rate
        return rate 


def subtotal(units, rate_type, ft_rate):
    """Return energy_charge + service_charge + ft_charge (before VAT).
    Reuse the functions above."""
    sub_total = energy_charge(units) + service_charge(rate_type) + ft_charge(units, ft_rate)
    return sub_total


def vat(amount, rate=0.07):
    """Return the VAT on `amount`. Default VAT rate is 7%."""
    if amount<0 or rate<0:
        raise ValueError("raises ValueError")
    else:
        vat_amount = amount * rate
        return vat_amount


def round_baht(amount):
    """Return `amount` rounded to 2 decimal places."""
    return f"{amount:.2f}"


def total_due(units, rate_type, ft_rate, vat_rate=0.07):
    """Return the final amount due, rounded to 2 decimals:
       round_baht(subtotal + vat(subtotal))."""
    total_due = round_baht(subtotal(units, rate_type, ft_rate) + vat(subtotal(units, rate_type, ft_rate), vat_rate))
    return total_due


def format_baht(amount):
    """Return `amount` as a baht string with a thousands separator and
    exactly 2 decimals, e.g. 1759.08 -> '฿1,759.08'.
    Hint: f-string  f"฿{amount:,.2f}"."""
    return f"฿{float(amount):,.2f}"


def is_high_usage(units, threshold=400):
    """Return True if `units` is strictly greater than `threshold`, else False."""
    if units > threshold:
        return True
    else:
        return False


def months_until_over_budget(start_bill, monthly_increase, budget_cap):
    """A bill starts at `start_bill` and rises by `monthly_increase` each month.
    Return how many monthly increases are needed before the bill is strictly
    greater than `budget_cap`. Return 0 if it already exceeds the cap.
    Hint: use a while loop with a counter (Week 4)."""
    counter=0
    while start_bill <= budget_cap:
        start_bill += monthly_increase
        counter += 1

    return counter
    
    
def bill_receipt(previous, current, rate_type, ft_rate):
    """Build and return a multi-line receipt STRING by REUSING the functions
    above (decomposition, Week 5). It must include the text 'TOTAL DUE',
    the formatted total, and the number of units used.
    Suggested layout:

        MetroVolt - Electricity Bill
        Previous reading: <previous>
        Current reading:  <current>
        Units used:       <units>
        Rate type:        <rate_type>
        Energy charge:    <฿...>
        Service charge:   <฿...>
        Ft charge:        <฿...>
        Subtotal:         <฿...>
        VAT (7%):         <฿...>
        TOTAL DUE:        <฿...>
    """
    
    u = units_used(previous, current)
    e_charge = energy_charge(u)
    s_charge = service_charge(rate_type)
    f_charge = ft_charge(u, ft_rate)
    sub = subtotal(u, rate_type, ft_rate)
    v = vat(sub, rate=0.07)
    total = total_due(u, rate_type, ft_rate, vat_rate=0.07)

    receipt = (
        f"MetroVolt - Electricity Bill\n"
        f"Previous reading: {previous}\n"
        f"Current reading:  {current}\n"
        f"Units used:       {u}\n"
        f"Rate type:        {rate_type}\n"
        f"Energy charge:    {format_baht(e_charge)}\n"
        f"Service charge:   {format_baht(s_charge)}\n"
        f"Ft charge:        {format_baht(f_charge)}\n"
        f"Subtotal:         {format_baht(sub)}\n"
        f"VAT (7%):         {format_baht(v)}\n"
        f"TOTAL DUE:        {format_baht(total)}"
    )
    return receipt

print(bill_receipt(1200,1620,'residential',0.20))






# ---------------------------------------------------------------------------
# OPTIONAL self-check: while building, you may UNCOMMENT these lines to compare
# your results against the tables in the instructions above. Comment them out
# again (or delete them) before you submit.
# ---------------------------------------------------------------------------
# print(units_used(1200, 1620))                       # expect 420
# print(energy_charge(420))                           # expect 1540.0
# print(total_due(420, "residential", 0.20))          # expect 1759.08
# print(format_baht(1759.08))                         # expect ฿1,759.08
# print(months_until_over_budget(1000, 100, 1500))    # expect 6
# print(bill_receipt(1200, 1620, "residential", 0.20))





    





