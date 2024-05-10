Increasing range to 18 should be considered because we will miss following service categories if we use .{0,15} :

| New categories with .{0,16}  | False Result?    | Matches
|----------------|-------------------------------|----|
| Discovery and Preclinical| No |discovery, optimization, and preclinical
| Cyclodextrin Complexes | No | cyclodextrin drug-inclusion complexes
| Metabolite Analysis| No|metabolite, and biomarker analysis
| Global Logistics| No|global product supply logistics
| NJ License|Yes |Kanji The number of licensed
| PA License|Yes|companies need to be licensed
| NGS Test development| Yes | meetings to share the latest developments
| TEM Services| Yes|system administration services
| GI Permeability (In Vitro)| Yes | strategies include poor permeability

Here categories start witn 'NJ', 'PA', 'NGS', 'TEM', 'GI' are falsy results. If we check space before and after them those categories won't be matched because the pattern finds them in a whole word. 

| New categories with .{0,17}  | False Result?    | Matches 
|----------------|-------------------------------|---|
|Variable Data| No|variable pharmacokinetic data
|Transporter Interactions| No|transporter-based drug-drug interactions
|Protein Analysis|No|protein and polypeptide analysis
|Heart disease| No|heart failure, kidney disease
|Candidate Evaluation|Yes|candidate. Loading... The evaluation
|CA License| Yes| applications for import licenses

We can exclude 'CA License' in the same way above.

|New categories with .{0,18}   | False Result?    | Matches
|----------------|-------------------------------|-----|
|505(b)(2) filing|No|505(b)(2) and CBE-30 filings|
|Downstream Process Development| No|downstream roles, including process research and development
|Verification and Validation| No | verification, quality control and validation
|High Pressure Chemistry (>100 psi)|No|high-pressure/high-temperature chemistry
|In Vivo Toxicity|No|in-vivo acute or chronic toxicity
|IND Submissions| Yes|industry and related submissions

Likewise can exclude 'IND Submissions' in the same way above and add 5 new categories.
