import pandas as pd

# Step 1:
data = pd.read_csv('inpatient.csv', sep='|')

# Display the first few rows of the dataset to understand its structure
print(data.head())

# Step 2: Explore the Dataset
# Identify the columns related to medical codexes (e.g., ICD codes, DRG codes)
# Assuming 'ICD_CODE', 'DRG_CODE', and 'HCPCS_CODE' are the columns containing codex data
icd_codes = data['ICD_DGNS_CD1']
drg_codes = data['CLM_DRG_CD']
hcpcs_codes = data['HCPCS_CD']
npi_codes = data['OP_PHYSN_NPI']


# Step 3: Analyze the Frequency of Each Unique Value
# Calculate the frequency of unique values in each codex column

# Frequency count for ICD codes
icd_frequency = icd_codes.value_counts()
print("ICD Codes Frequency:\n", icd_frequency)

# Frequency count for DRG codes
drg_frequency = drg_codes.value_counts()
print("DRG Codes Frequency:\n", drg_frequency)

# Frequency count for HCPCS codes
hcpcs_frequency = hcpcs_codes.value_counts()
print("HCPCS Codes Frequency:\n", hcpcs_frequency)

#Frequency count for NPI codes
npi_frequency = npi_codes.value_counts().unique()
print("NPI Codes Frequency:\n", len(npi_frequency))

# Step 4: Handle Missing Data (if any)
# Check for missing values in codex-related columns
missing_icd = icd_codes.isnull().sum()
missing_drg = drg_codes.isnull().sum()
missing_hcpcs = hcpcs_codes.isnull().sum()

print(f"Missing ICD Codes: {missing_icd}")
print(f"Missing DRG Codes: {missing_drg}")
print(f"Missing HCPCS Codes: {missing_hcpcs}")

# Example of handling missing data by filling with a placeholder
data['ICD_DGNS_CD1'].fillna('MISSING', inplace=True)
data['CLM_DRG_CD'].fillna('MISSING', inplace=True)
data['HCPCS_CD'].fillna('MISSING', inplace=True)

# Step 5: Summary of Findings
# Provide a summary of the most common codes
# Here we'll just print the top 5 most common codes for each category
print("Top 5 Most Common ICD Codes:\n", icd_frequency.head())
print("Top 5 Most Common DRG Codes:\n", drg_frequency.head())
print("Top 5 Most Common HCPCS Codes:\n", hcpcs_frequency.head())

# Additional Analysis Example
# Are there any patterns? For instance, let's see if certain DRG codes are more common
# when ICD codes are specific values (e.g., 'E11' for Type 2 Diabetes)
diabetes_related = data[data['ICD_DGNS_CD1'].str.contains('E11', na=False)]
common_drg_for_diabetes = diabetes_related['CLM_DRG_CD'].value_counts()
print("Most Common DRG Codes for Patients with ICD Code E11 (Type 2 Diabetes):\n", common_drg_for_diabetes)