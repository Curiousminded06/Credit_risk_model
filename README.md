# Credit_risk_model
This credit risk modeling ML project for a modest-scale finance company encompasses the entire process, from data collection and exploratory data analysis (EDA) to deployment.


This repository contains a machine learning project for predicting loan default risk using customer, loan, and bureau data.
Datasets used: Three CSV files (customers.csv, loans.csv, bureau_data.csv) placed in the data/ folder; merged on cust_id and loan_id for analysis.
Libraries installed via pip install -r requirements.txt: pandas for data manipulation, numpy for numerical operations, matplotlib and seaborn for visualizations, scikit-learn for preprocessing and models, xgboost for gradient boosting, imbalanced-learn for handling class imbalance, optuna for hyperparameter tuning, statsmodels for VIF calculation, joblib for model saving.
Data preprocessing: Merge datasets, handle missing values by filling with mode (e.g., residence_type), remove duplicates, filter outliers (e.g., processing_fee/loan_amount < 0.03), apply business rules (e.g., GST <= 20%), correct typos, split data into train/test (75-25%) with stratification.
Exploratory Data Analysis (EDA): Use box plots and histograms to visualize continuous features like age, income, loan_tenure_months; KDE plots to compare distributions by default status, revealing insights like younger applicants having higher default risk.
Feature engineering: Create loan_to_income ratio (loan_amount / income), delinquency_ratio ((delinquent_months * 100) / total_loan_months), avg_dpd_per_delinquency (total_dpd / delinquent_months if delinquent_months > 0); drop irrelevant columns like cust_id, loan_id, disbursal_date.
Feature selection: Calculate VIF to remove multicollinear features (e.g., sanction_amount, processing_fee); compute WOE/IV to select features with IV > 0.02 (e.g., age, loan_to_income); one-hot encode categoricals (e.g., residence_type_Owned); scale numerics with MinMaxScaler.
Model training: Train Logistic Regression, Random Forest, XGBoost; handle imbalance with RandomUnderSampler or SMOTE Tomek; tune hyperparameters using RandomizedSearchCV or Optuna; final model is tuned Logistic Regression.
Model evaluation: Use classification_report for precision/recall/F1; plot ROC curve for AUC (~0.98); calculate KS statistic (~85.98%) and Gini coefficient (~0.96) via decile analysis for rank ordering.
Results: Model achieves ~85-90% accuracy, F1 ~0.80-0.85; top features include avg_dpd_per_delinquency; save model, scaler, features, cols_to_scale in artifacts/model_data.joblib.
Usage: Run notebooks/credit_risk_full_pipeline.ipynb for full workflow; use src/train_model.py to train and save; src/predict.py for inference on new data.
Contributing: Fork repo, make changes, submit pull request; open issues for major updates.
