import streamlit as st
import pandas as pd
import joblib
from data_preprocessing import data_preprocessing, encoder_Credit_Mix, encoder_Payment_Behaviour, encoder_Payment_of_Min_Amount
from prediction import prediction

# Judul Aplikasi
st.header('Credit Scoring App (Prototype)')

# DataFrame untuk menyimpan input
data = pd.DataFrame()

# Input Form
Credit_Mix = st.selectbox(label='Credit_Mix', options=encoder_Credit_Mix.classes_, index=1)
data["Credit_Mix"] = [Credit_Mix]

Payment_of_Min_Amount = st.selectbox(label='Payment_of_Min_Amount', options=encoder_Payment_of_Min_Amount.classes_, index=1)
data["Payment_of_Min_Amount"] = [Payment_of_Min_Amount]

Payment_Behaviour = st.selectbox(label='Payment_Behaviour', options=encoder_Payment_Behaviour.classes_, index=5)
data["Payment_Behaviour"] = Payment_Behaviour

# Input Fitur Lainnya
Age = int(st.number_input(label='Age', value=23))
data["Age"] = Age

Num_Bank_Accounts = int(st.number_input(label='Num_Bank_Accounts', value=3))
data["Num_Bank_Accounts"] = Num_Bank_Accounts

Num_Credit_Card = int(st.number_input(label='Num_Credit_Card', value=4))
data["Num_Credit_Card"] = Num_Credit_Card

Interest_Rate = float(st.number_input(label='Interest_Rate', value=3))
data["Interest_Rate"] = Interest_Rate

Num_of_Loan = int(st.number_input(label='Num_of_Loan', value=4))
data["Num_of_Loan"] = Num_of_Loan

Delay_from_due_date = int(st.number_input(label='Delay_from_due_date', value=3))
data["Delay_from_due_date"] = Delay_from_due_date

Num_of_Delayed_Payment = int(st.number_input(label='Num_of_Delayed_Payment', value=7))
data["Num_of_Delayed_Payment"] = Num_of_Delayed_Payment

Changed_Credit_Limit = float(st.number_input(label='Changed_Credit_Limit', value=11.27))
data["Changed_Credit_Limit"] = Changed_Credit_Limit

Num_Credit_Inquiries = float(st.number_input(label='Num_Credit_Inquiries', value=5))
data["Num_Credit_Inquiries"] = Num_Credit_Inquiries

Outstanding_Debt = float(st.number_input(label='Outstanding_Debt', value=809.98))
data["Outstanding_Debt"] = Outstanding_Debt

Monthly_Inhand_Salary = float(st.number_input(label='Monthly_Inhand_Salary', value=1824.8))
data["Monthly_Inhand_Salary"] = Monthly_Inhand_Salary

Monthly_Balance = float(st.number_input(label='Monthly_Balance', value=186.26))
data["Monthly_Balance"] = Monthly_Balance

Amount_invested_monthly = float(st.number_input(label='Amount_invested_monthly', value=236.64))
data["Amount_invested_monthly"] = Amount_invested_monthly

Total_EMI_per_month = float(st.number_input(label='Total_EMI_per_month', value=49.5))
data["Total_EMI_per_month"] = Total_EMI_per_month

Credit_History_Age = float(st.number_input(label='Credit_History_Age', value=216))
data["Credit_History_Age"] = Credit_History_Age

# Tombol prediksi
if st.button('Predict'):
    new_data = data_preprocessing(data=data)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
    st.write("Credit Scoring: {}".format(prediction(new_data)))
