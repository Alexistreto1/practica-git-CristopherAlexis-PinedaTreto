# Front Page
# Student: Cristopher Alexis Pineda Treto
# Student ID: 2630007
# Group: 3
# Teacher: M.C Carlos Antonio Tovar Garcia

# =============================================================================
# EXECUTIVE SUMMARY
# In Python, int is a data type for whole numbers  and float
# is a data type for numbers with decimals .
# The main difference is that a float can store decimals and an int cannot.
# A boolean has only two values: True or False. We get a boolean when we
# compare values with operators like >=, <, == and !=, and we can join
# booleans with and, or, not.
# It is important to validate the ranges of the data 
#  and to avoid dividing by zero, because the program can fail or
# give wrong results.
# This document has 6 problems. For each one, it explains the description, the
# inputs and outputs, the validations and 3 test cases 
# The code uses int, float and bool to make simple decisions.

# =============================================================================
# Problem 1: Temperature converter and range flag
# Description: Converts a temperature from Celsius to Fahrenheit and Kelvin.
#              The boolean is_high_temperature is true if the temperature is
#              30.0 or more, and false in any other case.
# Inputs: temp_c (float, temperature in Celsius)
# Outputs: Fahrenheit, Kelvin and High temperature (true or false)
# Validations: temp_c must be converted to float and Kelvin cannot be below 0.0
# Normal: Anahi Treto checks "35.5" -> Fahrenheit: 95.9, Kelvin: 308.65,
#         High temperature: true
# Border: "30.0" -> Fahrenheit: 86.0, Kelvin: 303.15, High temperature: true
# Error: "abc" or "-300" (Kelvin below 0) -> Error: invalid input

HIGH_TEMPERATURE = 30.0

temp_c_text = "35.5"
# temp_c_text = "30.0"   # border case
# temp_c_text = "-300"   # error case (Kelvin below 0)
# temp_c_text = "abc"    # error case (not a number)

valid_input = True
try:
    temp_c = float(temp_c_text)
except ValueError:
    valid_input = False

if valid_input:
    temp_f = temp_c * 9 / 5 + 32
    temp_k = temp_c + 273.15

    if temp_k < 0.0:
        print("Error: invalid input")
    else:
        is_high_temperature = temp_c >= HIGH_TEMPERATURE  # true if 30.0 or more
        print("Fahrenheit:", round(temp_f, 2))
        print("Kelvin:", round(temp_k, 2))
        print("High temperature:", str(is_high_temperature).lower())
else:
    print("Error: invalid input")

print()

# =============================================================================
# Problem 2: Work hours and overtime payment
# Description: Calculates the weekly pay of a worker. Up to 40 hours are paid
#              at the hourly rate. The extra hours are paid at 150%.
#              has_overtime is true if the worker did more than 40 hours.
# Inputs: hours_worked (float) and hourly_rate (float)
# Outputs: Regular pay, Overtime pay, Total pay and Has overtime (true or false)
# Validations: hours_worked >= 0 and hourly_rate > 0
# Normal: Anahi Treto works "45" hours at "100.0" -> Regular pay: 4000.0,
#         Overtime pay: 750.0, Total pay: 4750.0, Has overtime: true
# Border: "40" hours at "100.0" -> Regular pay: 4000.0, Overtime pay: 0.0,
#         Total pay: 4000.0, Has overtime: false
# Error: "-5" hours at "100.0" -> Error: invalid input

REGULAR_HOURS = 40.0
OVERTIME_RATE = 1.5

hours_worked_text = "45"
hourly_rate_text = "100.0"
# hours_worked_text = "40"   # border case
# hours_worked_text = "-5"   # error case

valid_input = True
try:
    hours_worked = float(hours_worked_text)
    hourly_rate = float(hourly_rate_text)
except ValueError:
    valid_input = False

if valid_input and hours_worked >= 0 and hourly_rate > 0:
    regular_hours = min(hours_worked, REGULAR_HOURS)
    overtime_hours = max(hours_worked - REGULAR_HOURS, 0.0)

    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * OVERTIME_RATE
    total_pay = regular_pay + overtime_pay
    has_overtime = hours_worked > REGULAR_HOURS  # true if more than 40 hours

    print("Regular pay:", round(regular_pay, 2))
    print("Overtime pay:", round(overtime_pay, 2))
    print("Total pay:", round(total_pay, 2))
    print("Has overtime:", str(has_overtime).lower())
else:
    print("Error: invalid input")

print()

# =============================================================================
# Problem 3: Discount eligibility with booleans
# Description: Checks if a customer gets a discount. There is a discount if the
#              customer is a student OR is a senior OR the purchase is 1000.0
#              or more. When there is a discount, the total is reduced by 10%.
# Inputs: purchase_total (float), is_student_text ("YES" or "NO") and
#         is_senior_text ("YES" or "NO")
# Outputs: Discount eligible (true or false) and Final total
# Validations: purchase_total >= 0.0 and the texts must be YES or NO
#              (the texts are cleaned with strip() and upper())
# Normal: Anahi Treto buys "500.0", student "yes", senior "no" ->
#         Discount eligible: true, Final total: 450.0
# Border: "1000.0", student "no", senior "no" ->
#         Discount eligible: true, Final total: 900.0
# Error: "500.0", student "maybe", senior "no" -> Error: invalid input
# Extra: "500.0", student "no", senior "no" ->
#        Discount eligible: false, Final total: 500.0

DISCOUNT_RATE = 0.10
MIN_DISCOUNT_TOTAL = 1000.0

purchase_total_text = "500.0"
is_student_text = "yes"
is_senior_text = "no"
# purchase_total_text = "1000.0"   # border case (change the texts to "no")
# is_student_text = "maybe"        # error case

is_student_text = is_student_text.strip().upper()
is_senior_text = is_senior_text.strip().upper()

valid_input = True
try:
    purchase_total = float(purchase_total_text)
except ValueError:
    valid_input = False

if (valid_input and purchase_total >= 0.0
        and is_student_text in ("YES", "NO")
        and is_senior_text in ("YES", "NO")):
    is_student = is_student_text == "YES"
    is_senior = is_senior_text == "YES"

    discount_eligible = is_student or is_senior or (purchase_total >= MIN_DISCOUNT_TOTAL)

    if discount_eligible:
        final_total = purchase_total * (1 - DISCOUNT_RATE)
    else:
        final_total = purchase_total

    print("Discount eligible:", str(discount_eligible).lower())
    print("Final total:", round(final_total, 2))
else:
    print("Error: invalid input")

print()

# =============================================================================
# Problem 4: Basic statistics of three integers
# Description: Reads three integers and calculates the sum, the average (float),
#              the maximum, the minimum and a boolean all_even that is true if
#              the three numbers are even.
# Inputs: n1, n2 and n3 (int)
# Outputs: Sum, Average, Max, Min and All even (true or false)
# Validations: the three values must be converted to int (negatives are allowed)
# Normal: "4", "6", "10" -> Sum: 20, Average: 6.67, Max: 10, Min: 4,
#         All even: true
# Border: "-4", "0", "7" -> Sum: 3, Average: 1.0, Max: 7, Min: -4,
#         All even: false (negative numbers and zero are valid)
# Error: "4", "x", "10" -> Error: invalid input

n1_text = "4"
n2_text = "6"
n3_text = "10"
# n1_text = "-4"   # border case
# n2_text = "0"    # border case
# n3_text = "7"    # border case
# n2_text = "x"    # error case

valid_input = True
try:
    n1 = int(n1_text)
    n2 = int(n2_text)
    n3 = int(n3_text)
except ValueError:
    valid_input = False

if valid_input:
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print("Sum:", sum_value)
    print("Average:", round(average_value, 2))
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", str(all_even).lower())
else:
    print("Error: invalid input")

print()

# =============================================================================
# Problem 5: Loan eligibility (income and debt ratio)
# Description: Checks if a person can get a loan. The debt ratio is
#              monthly_debt / monthly_income. The person is eligible if the
#              income is 8000.0 or more AND the debt ratio is 0.4 or less AND
#              the credit score is 650 or more.
# Inputs: monthly_income (float), monthly_debt (float) and credit_score (int)
# Outputs: Debt ratio and Eligible (true or false)
# Validations: monthly_income > 0.0 (to avoid dividing by zero),
#              monthly_debt >= 0.0 and credit_score >= 0
# Normal: Anahi Treto has income "12000.0", debt "3000.0", score "700" ->
#         Debt ratio: 0.25, Eligible: true
# Border: income "8000.0", debt "3200.0", score "650" ->
#         Debt ratio: 0.4, Eligible: true (all values are exactly on the limit)
# Error: income "0", debt "3000.0", score "700" -> Error: invalid input

MIN_INCOME = 8000.0
MAX_DEBT_RATIO = 0.4
MIN_CREDIT_SCORE = 650

monthly_income_text = "12000.0"
monthly_debt_text = "3000.0"
credit_score_text = "700"
# monthly_income_text = "8000.0"   # border case
# monthly_debt_text = "3200.0"     # border case
# credit_score_text = "650"        # border case
# monthly_income_text = "0"        # error case (division by zero)

valid_input = True
try:
    monthly_income = float(monthly_income_text)
    monthly_debt = float(monthly_debt_text)
    credit_score = int(credit_score_text)
except ValueError:
    valid_input = False

if valid_input and monthly_income > 0.0 and monthly_debt >= 0.0 and credit_score >= 0:
    debt_ratio = monthly_debt / monthly_income
    eligible = (monthly_income >= MIN_INCOME
                and debt_ratio <= MAX_DEBT_RATIO
                and credit_score >= MIN_CREDIT_SCORE)

    print("Debt ratio:", round(debt_ratio, 2))
    print("Eligible:", str(eligible).lower())
else:
    print("Error: invalid input")

print()

# =============================================================================
# Problem 6: Body Mass Index (BMI) and category flag
# Description: Calculates the BMI with bmi = weight_kg / (height_m * height_m)
#              and creates three booleans: is_underweight (bmi < 18.5),
#              is_normal (18.5 <= bmi < 25.0) and is_overweight (bmi >= 25.0).
# Inputs: weight_kg (float) and height_m (float)
# Outputs: BMI (rounded to 2 decimals), Underweight, Normal and Overweight
# Validations: weight_kg > 0.0 and height_m > 0.0
# Normal: Anahi Treto has "65.0" kg and "1.70" m -> BMI: 22.49,
#         Underweight: false, Normal: true, Overweight: false
# Border: "100.0" kg and "2.0" m -> BMI: 25.0, Underweight: false,
#         Normal: false, Overweight: true (exactly on the limit)
# Error: "0" kg and "1.70" m -> Error: invalid input

UNDERWEIGHT_LIMIT = 18.5
OVERWEIGHT_LIMIT = 25.0

weight_kg_text = "65.0"
height_m_text = "1.70"
# weight_kg_text = "100.0"   # border case
# height_m_text = "2.0"      # border case
# weight_kg_text = "0"       # error case

valid_input = True
try:
    weight_kg = float(weight_kg_text)
    height_m = float(height_m_text)
except ValueError:
    valid_input = False

if valid_input and weight_kg > 0.0 and height_m > 0.0:
    bmi = weight_kg / (height_m * height_m)

    is_underweight = bmi < UNDERWEIGHT_LIMIT
    is_normal = UNDERWEIGHT_LIMIT <= bmi < OVERWEIGHT_LIMIT
    is_overweight = bmi >= OVERWEIGHT_LIMIT

    print("BMI:", round(bmi, 2))
    print("Underweight:", str(is_underweight).lower())
    print("Normal:", str(is_normal).lower())
    print("Overweight:", str(is_overweight).lower())
else:
    print("Error: invalid input")

# =============================================================================
# CONCLUSIONS
# Integers and floats are used together in real calculations, like payroll or BMI .
# Comparisons create booleans, and these booleans let the program make
# decisions with if and else.
# It is important to validate ranges and to avoid dividing by zero, like in the
# loan problem, where the income must be greater than zero.
# Combined conditions with and, or, not are easy to read when each part has a
# clear name, like is_student or discount_eligible.
# I learned that the same patterns repeat in payroll, discounts and loans:
# convert the data, validate it, calculate and then decide.
# I also learned that border cases are important to test because the operators >= and > give different results.

# =============================================================================
# REFERENCES
# 1) Python documentation - Built-in Types: Numeric Types - int, float, complex
#    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
# 2) Python documentation - Boolean Type - bool
#    https://docs.python.org/3/library/stdtypes.html#boolean-type-bool
# 3) Python documentation - Tutorial: Using Python as a Calculator (Numbers)
#    https://docs.python.org/3/tutorial/introduction.html#numbers
# 4) Real Python - Numbers in Python
#    https://realpython.com/python-numbers/
# 5) W3Schools - Python Numbers
#    https://www.w3schools.com/python/python_numbers.asp

############################                           ##########################