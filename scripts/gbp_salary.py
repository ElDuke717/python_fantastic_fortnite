from forex_python.converter import CurrencyRates

def convert_gbp_to_usd(amount_in_gbp):
    cr = CurrencyRates()
    return cr.convert('GBP', 'USD', amount_in_gbp)

min_salary_gbp = 66861
max_salary_gbp = 74290

min_salary_usd = convert_gbp_to_usd(min_salary_gbp)
max_salary_usd = convert_gbp_to_usd(max_salary_gbp)

print(f"The salary range in USD is: ${min_salary_usd}-{max_salary_usd} per annum")
