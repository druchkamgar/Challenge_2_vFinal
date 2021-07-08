# Challenge_2 - Loan Qualifier Application
This is a command-line-interface application. It pulls bank loan qualification criteria from a CSV, takes user-inputed information, and filters the bank loans the user would qualify for. It takes as inputs: loan amount, home value, monthly income and customer debt, and returns bank loan information in a .csv file. 

---

## Technologies
This project leverages python 3.7 with the following packages:

> questionary - For interactive user prompts and dialogs

> fire - For the command line interface

---

## Installation Guide
Before running this application first install the following packages:

1. "pip install fire"

2. "pip install questionary"


---

## Usage
### To use the loan qualifier application clone the repository and run the app.py file:

>"python app.py"

Upon launching the loan qualifier app the user will be greeted with the following prompt:

!['Enter a file path to a rate-sheet (.csv):'](https://github.com/druchkamgar/Challenge_2_vFinal/blob/78411570c9c7558a68614be9995bda9da26490f6/Screen%20Shot%202021-07-08%20at%2012.58.55%20PM.png)py

Followed by the following questions:

    *What's your credit score?*

    *What's your current amount of monthly debt?*

    *What's your total monthly income?*

    *What's your desired loan amount?*

    *What's your home value?*

    *Would you like to save your qaulifying loans in a .csv? (Y/n)*
    
    *Please enter a file path name to save your file*

After accurately answering the prompts, the user will have a .csv containing information regarding bank loans they qualify for. They may not qualify for any, in which case the app will exit with the prompt: "You have no qualifying loans". The logic looks as follows:


'''

def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # If there are no qualifying loans inform the user and exit the app
    if len(qualifying_loans) == 0:
        sys.exit("You have no qualifying loans")
    # If there are qualifying loans, prompt user and ask if they would like to save the results as a CSV file
    else:
        save_file = questionary.confirm("Would you like to save your qualifying loans in a .csv?").ask()
    # If the user decides to save the file, prompt the user for a file path
        if save_file == True:
            csvpath = Path(questionary.text('Please enter a file path name to save your file').ask())
    # Save the results as a .csv file by importing and using save_csv() from fileio
            save_csv(csvpath, qualifying_loans)
    # If the user decides not to save the file, exit the app
        else:
            sys.exit("You chose not to save your qualifying loans.")
'''
---

## Contributors
Brought to you by Columbia Fintech Bootcamp and Dariush Ruch-Kamgar. 

Contact information: 
> druchkamgar@gmail.com

---

## License
Columbia University
