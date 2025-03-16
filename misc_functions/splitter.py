import pandas as pd

def split_dataset(input_excel_file):
    df = pd.read_csv(input_excel_file)
 
    # 1. Patient Table (Patient_ID, Age, Gender, Country, Ethnicity)
    patient_columns = ['Patient_ID', 'Age', 'Gender', 'Country', 'Ethnicity']
    patient_df = df[patient_columns]
    
    # 2. Medical History Table (Patient_ID, Family_History, Radiation_Exposure, Iodine_Deficiency, Smoking, Obesity, Diabetes)
    medical_history_columns = ['Patient_ID', 'Family_History', 'Radiation_Exposure', 'Iodine_Deficiency', 'Smoking', 'Obesity', 'Diabetes']
    medical_history_df = df[medical_history_columns]
    
    # 3. Thyroid Test Results Table (Patient_ID, TSH_Level, T3_Level, T4_Level)
    thyroid_test_columns = ['Patient_ID', 'TSH_Level', 'T3_Level', 'T4_Level']
    thyroid_test_df = df[thyroid_test_columns]
    
    # 4. Nodule Details Table (Patient_ID, Nodule_Size, Thyroid_Cancer_Risk)
    nodule_columns = ['Patient_ID', 'Nodule_Size', 'Thyroid_Cancer_Risk']
    nodule_df = df[nodule_columns]
    
    # 5. Diagnosis Table (Patient_ID, Diagnosis)
    diagnosis_columns = ['Patient_ID', 'Diagnosis']
    diagnosis_df = df[diagnosis_columns]
    
    patient_df.to_csv('patient_table.csv', index=False)
    medical_history_df.to_csv('medical_history_table.csv', index=False)
    thyroid_test_df.to_csv('thyroid_test_results_table.csv', index=False)
    nodule_df.to_csv('nodule_details_table.csv', index=False)
    diagnosis_df.to_csv('diagnosis_table.csv', index=False)
    
    print("Data has been split into multiple CSV files.")


input_excel_file = 'thyroid_cancer_risk_data.csv'  
split_dataset(input_excel_file)
