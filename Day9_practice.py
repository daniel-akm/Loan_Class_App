import joblib
import streamlit as st
import pandas as pd
import numpy as np

st.title('Loan Application')
st.header('User Input Parameter')

def user_input_parameter():
    gender = st.selectbox("Gender",["Male","Female"])
    married = st.selectbox("Married",["Yes","No"])
    dependents = st.selectbox("Dependents",["0","1","2","3+"])
    education = st.selectbox("Education",["Graduate","Not Graduate"])
    self_employed = st.selectbox("Self_Employed",["Yes","No"])
    application_income = st.number_input("ApplicantIncome", min_value=0)
    co_applicant_income = st.number_input("CoapplicantIncome", min_value=0)
    loan_amount = st.number_input("LoanAmount", min_value=0)
    loan_amount_term = st.number_input("Loan_Amount_Term", min_value=0)
    credit_history = st.selectbox("Credit_History",["0.0","1.0"])
    property_area = st.selectbox("Property_Area",["Urban","Rural", "Semiurban"])

    data = {
        "Gender" : gender,
        "Married" : married,
        "Dependents" : dependents,
        "Education" : education,
        "Self_Employed" : self_employed,
        "ApplicantIncome" : application_income,
        "CoapplicantIncome" : co_applicant_income,
        "LoanAmount" : loan_amount,
        "Loan_Amount_Term" : loan_amount_term,
        "Credit_History" : credit_history,
        "Property_Area" : property_area
    }
    feature = pd.DataFrame(data, index=[0])
    return feature

def change_data_type(df):
    df['Gender'] = df['Gender'].map({"Male":0,"Female":1})
    df['Married'] = df['Married'].map({"Yes":0,"No":1})
    df['Dependents'] = df['Dependents'].map({"0":0,"1":1,"2":2,"3+":3})
    df['Education'] = df['Education'].map({"Graduate":0,"Not Graduate":1})
    df['Self_Employed'] = df['Self_Employed'].map({"Yes":0,"No":1})
    df['Property_Area'] = df['Property_Area'].map({"Rural":0,"Urban":1,"Semiurban":2})
    df['Credit_History'] = df['Credit_History'].map({"0.0":0.0,"1.0":1.0})
    return df

df = user_input_parameter()
df = change_data_type(df)

def main():
    model = joblib.load('testing_day_9.pkl')
    
    if st.button('Predict'):
        pred_value = np.round(model.predict(df))
        st.write("Loan Status: ", "Approved" if pred_value[0]==0 else "Denied")

if __name__ == "__main__":
    main()