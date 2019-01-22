# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
bank = pd.read_csv(path)

categorical_var = bank.select_dtypes(include='object')
print(categorical_var)

numerical_var = bank.select_dtypes(include='number')
print(numerical_var)
# code starts here






# code ends here


# --------------
# code starts here

banks = bank.drop('Loan_ID',axis=1)
print(banks.isnull().sum())
bank_mode = banks.mode()
for column in banks.columns:
    banks[column].fillna(banks[column].mode()[0], inplace=True)
print(banks.isna().sum())
#code ends here


# --------------
# Code starts here

avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed',],values='LoanAmount')


# code ends here



# --------------
# code starts here
loan_approved_se = banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')].shape[0]
loan_approved_nse = banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')].shape[0]
Loan_Status = 614
percentage_se = (loan_approved_se / Loan_Status) * 100
percentage_nse = (loan_approved_nse / Loan_Status) * 100    

# code ends here


# --------------
# code starts here

loan_term = banks["Loan_Amount_Term"]/12
big_loan_term = sum(loan_term >= 25 )



# code ends here


# --------------
# code starts here

loan_groupby = banks.groupby(['Loan_Status'])['ApplicantIncome', 'Credit_History']

mean_values = (banks.groupby(['Loan_Status'])['ApplicantIncome', 'Credit_History']).mean()

# code ends here


