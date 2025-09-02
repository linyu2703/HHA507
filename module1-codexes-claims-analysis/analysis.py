import pandas as pd

# Step 1:
data = pd.read_csv('inpatient.csv', sep='|')

# Display the first few rows of the dataset to understand its structure
print(data.head())

# Step 2: Explore the Dataset
# Identify the columns related to medical codexes (e.g., ICD codes, DRG codes)
# Assuming 'ICD_CODE', 'DRG_CODE', and 'HCPCS_CODE' are the columns containing codex data
icd_codes = data['ICD_DGNS_CD1']
icd_e_codes = data['ICD_DGNS_E_CD1']
icd_p_codes = data['ICD_PRCDR_CD1']
drg_codes = data['CLM_DRG_CD']
hcpcs_codes = data['HCPCS_CD']
npi_codes = data['AT_PHYSN_NPI']
prncpal_dgns_codes = data['PRNCPAL_DGNS_CD']
admit_date_codes = data['CLM_ADMSN_DT']

# Step 3: Analyze the Frequency of Each Unique Value
# Calculate the frequency of unique values in each codex column

# Frequency count for ICD codes (Claim Diagnosis Code)
icd_frequency = icd_codes.value_counts()
print("ICD Codes Frequency:\n", icd_frequency)

#Frequency count for ICD E codes (Claim Diagnosis E Code) - for external causes
icd_e_frequency = icd_e_codes.value_counts()
print("ICD E Codes Frequency:\n", icd_e_frequency)

#Frequency count for ICD P codes (Claim Procedure Code) - for procedure performed
icd_p_frequency = icd_p_codes.value_counts() 
print("ICD P Codes Frequency:\n", icd_p_frequency)

# Frequency count for DRG codes
drg_frequency = drg_codes.value_counts()
print("DRG Codes Frequency:\n", drg_frequency)

# Frequency count for HCPCS codes
hcpcs_frequency = hcpcs_codes.value_counts()
print("HCPCS Codes Frequency:\n", hcpcs_frequency)

# Frequency count for NPI codes - for operating physician
npi_frequency = npi_codes.value_counts()
print("NPI Codes Frequency:\n", npi_frequency)

# Frequency count for PRINCIPAL Diagnosis codes
prncpal_dgns_frequency = prncpal_dgns_codes.value_counts()
print("Principal Diagnosis Codes Frequency:\n", prncpal_dgns_frequency)

# Frequency count for patient admit dates
admit_date_frequency = admit_date_codes.value_counts()
print("Patient Admit Date Frequency:\n", admit_date_frequency)

# Step 4: Handle Missing Data (if any)
# Check for missing values in codex-related columns
missing_icd = icd_codes.isnull().sum()
missing_icd_e = icd_e_codes.isnull().sum()
missing_icd_p = icd_p_codes.isnull().sum()
missing_drg = drg_codes.isnull().sum()
missing_hcpcs = hcpcs_codes.isnull().sum()
missing_npi = npi_codes.isnull().sum()
missing_prncpal_dgns = prncpal_dgns_codes.isnull().sum()
missing_admit_date = admit_date_codes.isnull().sum()

print(f"Missing ICD Codes: {missing_icd}")
print(f"Missing ICD E Codes: {missing_icd_e}")
print(f"Missing ICD P Codes: {missing_icd_p}")
print(f"Missing DRG Codes: {missing_drg}")
print(f"Missing HCPCS Codes: {missing_hcpcs}")
print(f"Missing NPI Codes: {missing_npi}")
print(f"Missing Principal Diagnosis Codes: {missing_prncpal_dgns}")
print(f"Missing Admit Dates: {missing_admit_date}")

# Example of handling missing data by filling with a placeholder
data['ICD_DGNS_CD1'].fillna('MISSING', inplace=True)
data['ICD_DGNS_E_CD1'].fillna('MISSING', inplace=True)
data['ICD_PRCDR_CD1'].fillna('MISSING', inplace=True)
data['CLM_DRG_CD'].fillna('MISSING', inplace=True)
data['HCPCS_CD'].fillna('MISSING', inplace=True)
data['AT_PHYSN_NPI'].fillna('MISSING', inplace=True)
data['PRNCPAL_DGNS_CD'].fillna('MISSING', inplace=True)
data['CLM_ADMSN_DT'].fillna('MISSING', inplace=True)

# Step 5: Summary of Findings
# Provide a summary of the most common codes
# Here we'll just print the top 5 most common codes for each category
print("Top 5 Most Common ICD Codes:\n", icd_frequency.head())
print("Top 5 Most Common ICD E Codes:\n", icd_e_frequency.head())
print("Top 5 Most Common ICD P Codes:\n", icd_p_frequency.head())
print("Top 5 Most Common DRG Codes:\n", drg_frequency.head())
print("Top 5 Most Common HCPCS Codes:\n", hcpcs_frequency.head())
print("Top 5 Most Common NPI Codes:\n", npi_frequency.head())
print("Top 5 Most Common Principal Diagnosis Codes:\n", prncpal_dgns_frequency.head())
print("Top 5 Most Common Admit Dates:\n", admit_date_frequency.head())

# Additional Analysis Example
# Are there any patterns? For instance, let's see if certain DRG codes are more common
# when ICD codes are specific values (e.g., 'E11' for Type 2 Diabetes)
diabetes_related = data[data['ICD_DGNS_CD1'].str.contains('E11', na=False)]
common_drg_for_diabetes = diabetes_related['CLM_DRG_CD'].value_counts()
print("Most Common DRG Codes for Patients with ICD Code E11 (Type 2 Diabetes):\n", common_drg_for_diabetes)

# What ICD procedures are commonly performed for the most common ICD code? "Z733" - which is related to stress?
stress_related = data[data['ICD_DGNS_CD1'].str.contains('Z733', na=False)]
common_procedures_for_stress = stress_related['ICD_PRCDR_CD1'].value_counts().head()
print("Top 5 most common ICD procedures for patients dealing with the Z733, stress, the most common ICD diagnosis code:\n", common_procedures_for_stress)
            
# What admit dates are most commonly associated with ICD ("F41") - anxiety disorders?
anxiety_related = data[data['ICD_DGNS_CD1'].str.contains('F41', na=False)]
common_dates_for_anxiety = anxiety_related['CLM_ADMSN_DT'].value_counts()
print("Most common dates for patients experiencing anxiety disorders:\n", common_dates_for_anxiety)
# Mostly around holidays towards the end of the year!

#What ICD procedures are commonly performed for the most common ICD E code, W86?
w86_related = data[data['ICD_DGNS_E_CD1'].str.contains('W86', na=False)]
common_procedures_for_w86 = w86_related['ICD_PRCDR_CD1'].value_counts().head()
print("Top 5 most common ICD procedures done for patients dealing with W86, the most common ICD E diagnosis code:\n", common_procedures_for_w86)
#Very similar procedures done for patients experiencing external cause of injury, poisoning, or other adverse effects compared to internal.

#What DRG codes are commonly associated with 99221 HCPCS code