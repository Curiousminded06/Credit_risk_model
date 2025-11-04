import streamlit as st
from prediction_helper import predict  # Ensure this is correctly linked to your prediction_helper.py

st.set_page_config(page_title="Lauki Finance: Credit Risk Modelling", page_icon="📊", layout="wide")
st.title("📊 Lauki Finance: Credit Risk Modelling")
st.markdown("Enter applicant details below to assess loan default risk.")

# Input Section
st.header("Applicant Information")
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input('Age', min_value=18, step=1, max_value=100, value=28, help="Applicant's age in years.")
    residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'], help="Type of residence owned by the applicant.")

with col2:
    income = st.number_input('Annual Income', min_value=0, value=1200000, help="Applicant's annual income.")
    loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'], help="Purpose of the loan.")

with col3:
    loan_amount = st.number_input('Loan Amount', min_value=0, value=2560000, help="Requested loan amount.")
    loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'], help="Type of loan security.")

# Calculated Ratio
loan_to_income_ratio = loan_amount / income if income > 0 else 0
st.metric("Loan to Income Ratio", f"{loan_to_income_ratio:.2f}", help="Ratio of loan amount to income.")

# Credit History Section
st.header("Credit History")
col4, col5, col6 = st.columns(3)

with col4:
    loan_tenure_months = st.number_input('Loan Tenure (Months)', min_value=1, step=1, value=36, help="Loan repayment period in months.")
    delinquency_ratio = st.slider('Delinquency Ratio (%)', min_value=0, max_value=100, step=1, value=30, help="Percentage of delinquent months.")

with col5:
    avg_dpd_per_delinquency = st.number_input('Avg DPD per Delinquency', min_value=0, value=20, help="Average days past due per delinquency event.")
    credit_utilization_ratio = st.slider('Credit Utilization Ratio (%)', min_value=0, max_value=100, step=1, value=30, help="Percentage of credit used.")

with col6:
    num_open_accounts = st.slider('Number of Open Accounts', min_value=1, max_value=10, step=1, value=2, help="Number of open loan accounts.")

# Prediction Button
if st.button('Calculate Risk', type='primary'):
    if income <= 0:
        st.error("Income must be greater than 0.")
    else:
        with st.spinner('Calculating...'):
            try:
                probability, credit_score, rating = predict(age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
                                                            delinquency_ratio, credit_utilization_ratio, num_open_accounts,
                                                            residence_type, loan_purpose, loan_type)
                
                # Results Section
                st.success("Risk Assessment Complete!")
                col7, col8, col9 = st.columns(3)
                
                with col7:
                    st.metric("Default Probability", f"{probability:.2%}", delta="High Risk" if probability > 0.5 else "Low Risk")
                
                with col8:
                    st.metric("Credit Score", credit_score)
                
                with col9:
                    color = "🟢" if rating == "Excellent" else "🟡" if rating == "Good" else "🟠" if rating == "Average" else "🔴"
                    st.metric("Rating", f"{color} {rating}")
                
                # Gauge for Probability
                st.subheader("Risk Visualization")
                st.progress(probability, text=f"Default Probability: {probability:.2%}")
                
                # Additional Insights
                if probability > 0.7:
                    st.warning("High risk of default. Consider stricter approval criteria.")
                elif probability < 0.3:
                    st.info("Low risk of default. Good candidate for approval.")
                else:
                    st.info("Moderate risk. Review additional factors.")
                    
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

st.markdown("---")

