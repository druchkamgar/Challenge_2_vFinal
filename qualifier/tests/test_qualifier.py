# Import pathlib
from pathlib import Path

#Import fileio
from qualifier.utils.fileio import load_csv, save_csv

# Import Calculators
from qualifier.utils.calculators import calculate_loan_to_value_ratio, calculate_monthly_debt_ratio

# Import Filters
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value
from qualifier.filters.max_loan_size import filter_max_loan_size


# Import Filter Test
from app import find_qualifying_loans


    # @TODO: Your code here!
    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv

csvpath = Path('./tests/data/output/qualifying_loans.csv')
save_csv(csvpath,'test')



def test_calculate_monthly_debt_ratio():
    assert calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    bank_data = load_csv(Path('./data/daily_rate_sheet.csv'))
    credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000
    assert len(find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value)) == 6

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84

    

    # @TODO: Test the new save_csv code!
    # YOUR CODE HERE!
def test_save_csv():
    assert Path('./tests/data/output/qualifying_loans.csv').exists()
