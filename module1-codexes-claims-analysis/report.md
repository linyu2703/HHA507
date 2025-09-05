<h1>Documentation of Analysis.py</h1>
<p><strong>Step 1: </strong>Imported my 'inpatient.csv' file using pandas 'read_csv' with delimiter argument '|'.</p>
<p>Checked if data successfully loaded by displaying the first 5 rows of the dataset.</p>
<p><strong>Step 2: </strong>Assigned codex data columns needed &lpar; ICD, ICD E, ICD P, DRG, HCPCS, NPI, PRINCIPAL DGNS, Admit codes &rpar; to variables.</p>
<p><strong>Step 3: </strong>Calculated frequency of unique values in each codex columns.</p>
<p><strong>Step 4: </strong>Identifying and handling missing values in the columns.<p>
<p>Filled in missing and null values with "MISSING" for clarity purposes.</p>
<p><strong>Step 5: </strong>Summarizing findings and data analysis.</p>
    <ul style = "margin-left: 10px;">
    <li>Top 5 most common ICD codes: Z733 (13,031) - related to stress e.g. experiencing mental/physical strain that influences health status, Z608 (8,227) - problems related to social environment e.g. lack of emotion support, T7432X (3,727) - related to psychological abuse of a child, Z604 (3,537) - related to social exlcusion and rejection (sub-code of Z608) e.g. excluded due to physical appearance, ilnness, chracterisitics, etc, Z940 (2,858) - related to kidney transplant status.</li>
    <li>Top 5 most common ICD E codes: W86 (10,445) - related to exposure to electric currents, X58 (6,868) - related to exposures to external factors no covered in codes e.g. prolonged weightlessness, hunger, exhaustion, W19 (5,162) - related to unspecified fall, Y92 (3,432) - related to place of occurrence of external causes of injury or health event, Y83 (2,320) - related to surigical operations and procedures that cause abnormal reaction and future complications.</li>
    <li>Top 5 most common ICD P codes: GZ3 (16,142) - related to monitoring and adjusting use of treatment for mental health disorder, Z741 (12,421) - related to the need of assistance for personal care, BW03ZZZ (3,337) - related to radiography of chest, G4730 (2,134) - related to sleep apnea, F13 (2,054) - related to mental behavior disorders due to sedatives, hypnotics, anxiolytics.</li>
    </ul>