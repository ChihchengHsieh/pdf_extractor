rubric_prompt = """I am conducting a Methods Audit of Mendelian Randomization (MR) studies using a study characteristics form and a structured scoring rubric. I will upload the MR study as a PDF file.

Please do the following:

**1\. Use the attached study characteristics form to extract the relevant data from the MR study.**

**2\. Use the attached rubric (Parts A and B) to score the MR study.**

- Score each item as 0, 1, or N/A based on the rubric's detailed evaluation criteria.

**3\. Output Format (JSON)**

Return only a single structured JSON object with the following three components.
Do not include any explanations, notes, or additional text.

1. **characteristics  
    Contains extracted responses for each item in the Study Characteristics Form (Q1–Q20).**
2. **scoring  
    Includes scores for each rubric item in Part A (A1–A12) and Part B (B1–B12), using 0, 1, or "N/A".**
3. **evidence  
    For each item in A1–A12 and B1–B12, include:**
    - **score: the assigned value (0, 1, or "N/A")**
    - **quote: verbatim excerpt from the paper**
    - **section: the section where the quote was found (e.g., "Methods", "Results")**

**Use the PDF file name as the value for study_id.**

**Example Output Format**

```json
{
  "study_id": "Chen2022.pdf",
  "characteristics": {
    "Q1": "...",
    "Q2": "...",
    "Q3": "...",
    "...": "...",
    "Q20": "..."
  },
  "scoring": {
    "A": {
      "A1": 1,
      "A2": 0,
      "...": "N/A"
    },
    "B": {
      "B1": 1,
      "B2": 0,
      "...": "N/A"
    }
  },
  "evidence": {
    "A": {
      "A1": {
        "score": 1,
        "quote": "...verbatim text from paper...",
        "section": "Methods – Instrument Selection"
      },
      "A2": {
        "score": 0,
        "quote": "N/A",
        "section": "N/A"
      }
    },
    "B": {
      "B1": {
        "score": 1,
        "quote": "...",
        "section": "Results – Sample Characteristics"
      }
    }
  }
}
```

**Notes:**

- Follow the rubric’s critical item and quality threshold rules if applicable.
- If any item is unclear or cannot be determined from the study, mark it as N/A and briefly explain why.

# Study Characteristics Form

| **Label** | **Field** | **Question** |
| --- | --- | --- |
| Q1  | Study ID | What is the study’s citation shorthand (first author and publication year, e.g. Storm 2023)? |
| Q2  | Study Title | What is the full title of the article? |
| Q3  | Journal | What is the full name of the journal in which the article was published? |
| Q4  | Publication Year | In what year was the article published? |
| Q5  | Study Design / MR Type | What type(s) of MR design(s) were used? (e.g. One-sample MR, Two-sample MR, Multivariable MR, Bidirectional MR, or combinations) |
| Q6  | Instrumental Variable(s) | What types of genetic instruments were used (e.g. GWAS SNPs, cis-variants, PRS)? If SNPs were LD-clumped, what were the clumping parameters (e.g. r² threshold, physical distance window)? |
| Q7  | Number of SNPs per Exposure | How many SNPs were used for each exposure? Report counts separately for each exposure and ancestry group.<br><br>Example: BMI: 62 SNPs (EAS), 298 SNPs (EUR); CRP: 6 SNPs (EAS), 183 SNPs (EUR); HDL-C: 50 SNPs (EAS), 247 SNPs (EUR); BS: 15 SNPs (EAS), 93 SNPs (EUR); TGs: 36 SNPs (EAS), 204 SNPs (EUR); SBP: 22 SNPs (EAS), 158 SNPs (EUR) |
| Q8  | Exposure(s) | What traits, biomarkers, or risk factors were analyzed as exposures? |
| Q9  | Outcome(s) | What traits, diseases, or phenotypes were analyzed as outcomes? |
| Q10 | Number of Exposures Assessed | How many distinct exposures were included? |
| Q11 | Number of Outcomes Assessed | How many distinct outcomes were assessed? |
| Q12 | GWAS Source for Exposure(s) | What GWAS datasets or consortia provided SNP–exposure associations? List all.<br><br>Example: ALT/AST: UK Biobank (Neale Lab); NAFLD liability: Million Veteran Program; liver MRI: UK Biobank subset; East Asian: Biobank Japan |
| Q13 | GWAS Source for Outcome(s) | What GWAS datasets or consortia provided SNP–outcome associations? List all.<br><br>Example: CAD: CARDIoGRAM; stroke: MEGASTROKE; atrial fibrillation: published GWAS; heart failure: HERMES consortium; T2D: DIAMANTE consortium; glycaemic traits: MAGIC; East Asian: Biobank Japan, AGEN consortium |
| Q14 | Sample Size for Exposure(s) | What was the total sample size for each exposure dataset, including cases and controls if applicable? |
| Q15 | Sample Size for Outcome(s) | What was the total sample size for each outcome dataset, including cases and controls if applicable? |
| Q16 | Ancestries Represented in Exposure GWAS | What ancestry groups were included in the exposure GWAS (e.g. European, East Asian)? |
| Q17 | Ancestries Represented in Outcome GWAS | What ancestry groups were included in the outcome GWAS? |
| Q18 | Separate MR Analyses by Ancestry | Did the study conduct ancestry-stratified MR analyses? (Yes/No) |
| Q19 | Geographic Region(s) Represented | What geographic regions or countries were the study populations drawn from |
| Q20 | Software Used | What statistical software, packages, or MR tools were used (e.g. R, Stata, TwoSampleMR, MR-Base, GSMR, LDSC)? |

# Scoring Rubric

### Part A: Core MR Methodology

**Scoring Instructions**:

- **0 = Not Addressed**: Item missing or not discussed anywhere in paper
- **1 = Fully Addressed**: Item explicitly addressed with required elements present
- **N/A**: Item clearly not applicable to study design
- **Specific numeric thresholds and keywords are provided below to minimize reviewer interpretation**

<table><tbody><tr><th><p><strong>Item</strong></p></th><th><p><strong>Category</strong></p></th><th><p><strong>Question</strong></p></th><th><p><strong>Evaluation Criteria</strong></p></th></tr><tr><td><p><strong>A1</strong></p></td><td><p><strong>Data Sources</strong></p></td><td><p>Are Exposure and Outcome GWAS described with source, ancestry, and sample size?</p></td><td><p><strong>Score 1 if ALL of the following for BOTH exposure and outcome GWAS:</strong></p><ul><li>Source identification: Study name (e.g., “UK Biobank”), consortium (e.g., “GIANT”), or specific cohort clearly stated</li><li>Sample size: Total N provided as specific number (not ranges like “~500,000”)</li><li>Ancestry composition: Population ancestry explicitly stated using standard terms or percentages</li></ul><p><strong>Score 0 if ANY element missing or vague:</strong></p><ul><li>Source described only as “published GWAS” or “large-scale study”</li><li>Sample size missing, unclear, or given as approximation</li><li>Ancestry not specified or described only as “mixed” without detail</li></ul></td></tr><tr><td><p><strong>A2</strong></p></td><td><p><strong>Instrument Selection</strong></p></td><td><p>Are SNP instruments selected using genome-wide significance and LD pruning/clumping with parameters specified?</p></td><td><p><strong>Score 1 if ALL of the following criteria present:</strong></p><ul><li>Genome-wide significance: p &lt; 5×10⁻⁸ threshold explicitly stated</li><li>LD pruning/clumping: Method clearly specified (pruning OR clumping)</li><li>LD parameters: r² threshold stated (e.g., r² &lt; 0.001, r² &lt; 0.01)</li><li>Distance parameter: Window size specified (e.g., 1MB, 250kb, 10,000kb)</li><li>Reference panel: LD reference panel named (e.g., “1000 Genomes Phase 3”)</li></ul><p><strong>Score 0 if ANY of the following:</strong></p><ul><li>Different p-value threshold used (e.g., p &lt; 5×10⁻⁶) without justification</li><li>LD method not specified (“independent SNPs” without method)</li><li>Parameters missing (r² or distance threshold not provided)</li><li>Reference panel not identified</li></ul></td></tr><tr><td><p><strong>A3a</strong></p></td><td><p><strong>Instrument Strength - Reporting</strong></p></td><td><p>Is instrument strength reported using F-statistics or R²?</p></td><td><p><strong>Score 1 if ANY of the following:</strong></p><ul><li>F-statistics provided with values (per instrument OR mean F-statistic)</li><li>R² (variance explained) provided as percentage or proportion</li><li>Both F-statistics and R² reported</li></ul><p><strong>Score 0 if:</strong></p><ul><li>Strength mentioned but no values provided (e.g., “strong instruments”)</li><li>Only weak instrument bias mentioned without metrics</li><li>No mention of instrument strength</li></ul></td></tr><tr><td><p><strong>A3b</strong></p></td><td><p><strong>Instrument Strength - Adequacy</strong></p></td><td><p>If F-statistics reported, are they adequate (F ≥ 10)?</p></td><td><p><strong>Score 1 if:</strong></p><ul><li>F ≥ 10</li></ul><p><strong>Score 0 if:</strong></p><ul><li>F &lt; 10</li></ul><p><strong>Mark N/A if:</strong></p><ul><li>F-statistics not reported</li></ul></td></tr><tr><td><p><strong>A4</strong></p></td><td><p><strong>MR Assumptions</strong></p></td><td><p>Are the three core IV assumptions explicitly stated and at least one empirically evaluated?</p></td><td><p><strong>Score 1 if ALL of the following:</strong></p><ul><li><strong>All three assumptions named: </strong>Relevance (instrument-exposure association), Independence (no confounding), Exclusion restriction (no pleiotropy)</li><li><strong>At least one assumption empirically tested</strong> using ANY of:</li><li>Confounder association testing (PhenoScanner, manual curation)</li><li>Known confounder control testing</li><li>Pleiotropy detection methods (MR-Egger, MR-PRESSO)</li><li>Negative control analyses</li></ul><p><strong>Score 0 if:</strong></p><ul><li>Assumptions mentioned but not all three clearly identified</li><li>No empirical evaluation of any assumption</li><li>Only theoretical discussion without testing</li></ul></td></tr><tr><td><p><strong>A5</strong></p></td><td><p><strong>Harmonization</strong></p></td><td><p>Are effect alleles harmonized and strand alignment issues addressed between datasets?</p></td><td><p><strong>Score 1 if AT LEAST ONE of the following approaches clearly described:</strong></p><ul><li><strong>Automated harmonization: </strong>Use of harmonization functions/packages (e.g., TwoSampleMR harmonise_data(), MungeSumstats)</li><li><strong>Manual harmonization: </strong>Process for aligning effect alleles described with specific steps</li><li><strong>Strand flip handling:</strong> Explicit mention of identifying and correcting strand flips</li><li><strong>Ambiguous SNP removal: </strong>A/T and G/C SNPs excluded or handled with frequency-based inference</li></ul><p><strong>Score 0 if:</strong></p><ul><li>No mention of harmonization procedures</li><li>Only states “data were harmonized” without method description</li></ul><p><strong>Mark N/A if:</strong></p><ul><li>Single-sample MR study</li></ul></td></tr><tr><td><p><strong>A6</strong></p></td><td><p><strong>Palindromic SNPs</strong></p></td><td><p>Are palindromic (A/T, G/C) SNPs handled appropriately?</p></td><td><p><strong>Score 1 if ANY of the following:</strong></p><ul><li><strong>Exclusion approach:</strong> A/T and G/C SNPs explicitly excluded</li><li><strong>Frequency-based inference:</strong> Allele frequencies used to determine strand alignment with frequency threshold stated (e.g., MAF &lt; 0.42 or 0.45)</li><li><strong>Reference-based alignment: </strong>Use of reference panel allele frequencies for alignment</li></ul><p><strong>Score 0 if:</strong></p><ul><li>Palindromic SNPs not mentioned</li><li>Handled but method not specified</li></ul><p><strong>Mark N/A if:</strong></p><ul><li>Single-sample MR study</li></ul></td></tr><tr><td><p><strong>A7</strong></p></td><td><p><strong>Sample Overlap</strong></p></td><td><p>Is sample overlap between exposure and outcome GWAS appropriately addressed?</p></td><td><p><strong>For 2-sample MR - Score 1 if:</strong></p><ul><li>Sample overlap explicitly discussed (even if stated as “none” or “minimal”)</li><li>Overlap quantified when present (e.g., “15% overlap”)</li><li>Appropriate methods used when overlap exists (e.g., CAUSE, MR-RAPS adjustment)</li></ul><p><strong>For 1-sample MR - Score 1 if:</strong></p><ul><li>Two-stage least squares (2SLS) or equivalent method used</li><li>Appropriate software mentioned (e.g., ivreg, ivpack)</li><li>Method justification provided for using same sample</li></ul><p><strong>Score 0 if:</strong></p><ul><li>Sample overlap not mentioned in 2-sample MR</li><li>1-sample MR without appropriate statistical method</li></ul></td></tr><tr><td><p><strong>A8</strong></p></td><td><p><strong>Confounder Control</strong></p></td><td><p>Are limitations of confounder control acknowledged (2-sample) or covariates appropriately controlled (1-sample)?</p></td><td><p><strong>For 2-sample MR - Score 1 if:</strong></p><ul><li>Explicit acknowledgment that individual-level covariates cannot be controlled</li><li>Discussion of residual confounding as study limitation</li><li>Population stratification control mentioned (if applicable)</li></ul><p><strong>For 1-sample MR - Score 1 if:</strong></p><ul><li>Covariate adjustment clearly described</li><li>Standard covariates included: age, sex, principal components</li><li>Method for covariate selection described</li></ul><p><strong>Score 0 if:</strong></p><ul><li>No discussion of confounder control limitations (2-sample)</li><li>No covariate adjustment described (1-sample)</li></ul></td></tr><tr><td><p><strong>A9</strong></p></td><td><p><strong>Outlier Detection</strong></p></td><td><p>Are outlier instruments identified using systematic methods and sensitivity analysis performed?</p></td><td><p><strong>Score 1 if ALL of the following:</strong></p><ul><li>Outlier detection method applied: Any systematic approach (leave-one-out analysis, radial MR, Cook's distance, MVMR-cML)</li><li>Method clearly named: Specific technique identified, not just “outlier analysis”</li><li>Sensitivity analysis: Results presented both with and without identified outliers</li><li>Impact discussed: Effect of outlier removal on estimates reported</li></ul><p><strong>Score 0 if:</strong></p><ul><li>No systematic outlier detection</li><li>Method not specified</li><li>No sensitivity analysis performed</li></ul></td></tr><tr><td><p><strong>A10</strong></p></td><td><p><strong>Sensitivity Analyses</strong></p></td><td><p>Are pleiotropy or heterogeneity assessed using appropriate statistical tests?</p></td><td><p><strong>Score 1 if AT LEAST ONE of the following methods applied with results reported:&lt;br/&gt;•</strong></p><ul><li>MR-Egger regression: Intercept and slope reported with p-values</li><li>Weighted median: Estimates and confidence intervals provided</li><li>MR-PRESSO: Global test and outlier correction results</li><li>Heterogeneity tests: Cochran's Q test with p-value and I² statistic</li><li>Radial MR: Modified Q-statistic and outlier identification</li><li>Contamination mixture methods: MR-Mix, CAUSE, or similar</li></ul><p><strong>Score 0 if:</strong></p><ul><li>Methods mentioned but results not provided</li><li>Only theoretical discussion of pleiotropy</li><li>No statistical testing performed</li></ul></td></tr><tr><td><p><strong>A11a</strong></p></td><td><p><strong>Robust Estimators - Use</strong></p></td><td><p>Are alternative estimators beyond inverse-variance weighted (IVW) used?</p></td><td><p><strong>Score 1 if:</strong></p><ul><li>At least one additional estimator beyond IVW used from: Weighted median, Weighted mode, MR-Egger, MR-RAPS, GSMR, or other validated methods</li><li>Results for additional estimators reported with confidence intervals</li></ul><p><strong>Score 0 if:</strong></p><ul><li>Only IVW method used</li><li>Additional methods mentioned but results not reported</li></ul></td></tr><tr><td><p><strong>A11b</strong></p></td><td><p><strong>Robust Estimators - Results</strong></p></td><td><p>Are results consistent across multiple estimators?</p></td><td><p><strong>Score 1 if:</strong></p><ul><li>Multiple estimators used AND results consistent across methods with explicit comparison</li><li>Discordant results appropriately discussed with potential explanations</li></ul><p><strong>Score 0 if:</strong></p><ul><li>Results are inconsistent</li><li>Results are not compared</li></ul><p><strong>Mark N/A if:</strong></p><ul><li>Only one estimator used</li></ul></td></tr><tr><td><p><strong>A12</strong></p></td><td><p><strong>Statistical Power</strong></p><p><strong>[NEW ITEM]</strong></p></td><td><p>Is statistical power assessed or sample size adequately justified for detecting clinically relevant effects?</p></td><td><p><strong>Score 1 if ANY of the following:</strong></p><ul><li><strong>Formal power calculation: </strong>Statistical power calculated using R² and sample sizes</li><li><strong>Minimum detectable effect size:</strong> Calculated and reported (e.g., “80% power to detect OR &gt; 1.15”)</li><li><strong>Sample size justification:</strong> Discussion of adequacy relative to expected effect sizes</li><li><strong>Power calculation software/formula referenced: </strong>mRnd, Mendelian randomization power calculator, or formula citation</li></ul><p><strong>Score 0 if:</strong></p><ul><li>No power assessment</li><li>Only general statements about “large sample sizes”</li></ul></td></tr></tbody></table>

#### Additional Quality Indicators

**Critical Items for Study Validity** (Must score 1 for minimum quality):

- A1 (Data Sources)
- A2 (Instrument Selection)
- A3 (Instrument Strength - must not score -1)
- A9 (Outlier Detection)
- A10 (Sensitivity Analyses)

**Methodological Rigor Indicators** (Items that distinguish high-quality studies):

- A4 (MR Assumptions empirical testing)
- A11 (Multiple robust estimators)
- A12 (Statistical power assessment)

#### Overall Part A Quality Assessment

**High Quality Core Methods:** ≥85% of applicable items scored ≥1, with all critical items = 1

**Moderate Quality:** 70-84% of applicable items scored ≥1

**Low Quality:** <70% of applicable items scored ≥1 OR any critical item = 0

### Part B: Cross-Ancestry Extensions to MR Methodology

**Scoring Instructions**:

- **0 = Not Addressed**: Item missing or not discussed anywhere in paper
- **1 = Fully Addressed**: Item explicitly addressed with required elements present
- **N/A**: Item clearly not applicable to study design
- **Specific numeric thresholds and keywords are provided below to minimize reviewer interpretation**

<table><tbody><tr><th><p><strong>Item</strong></p></th><th><p><strong>Category</strong></p></th><th><p><strong>Question</strong></p></th><th><p><strong>Evaluation Criteria</strong></p></th></tr><tr><td><p><strong>B1</strong></p></td><td><p><strong>Ancestry Reporting</strong></p></td><td><p>Are ancestries of Exposure and Outcome GWAS explicitly reported with sample composition details?</p></td><td><p><strong>Score 1 if ALL of the following are present:</strong></p><ul><li>Ancestry of exposure GWAS explicitly stated using standard terms (European, East Asian, African, South Asian, Hispanic/Latino, Native American, Oceanian, or specific population names)</li><li>Ancestry of outcome GWAS explicitly stated using same terminology</li><li>For multi-ancestry GWAS: numerical breakdown provided (e.g., "80% European, 15% East Asian, 5% African" OR sample sizes per ancestry group)</li><li>For admixed populations: either ancestry proportions OR population-specific labels (e.g., "African American," "Hispanic/Latino")</li></ul><p><strong>Score 0 if ANY of the following:</strong></p><ul><li>Ancestry described only as "diverse," "mixed," or "multi-ethnic" without specifics</li><li>Missing ancestry information for either exposure or outcome GWAS</li><li>Multi-ancestry GWAS mentioned without numerical breakdown</li></ul></td></tr><tr><td><p><strong>B2</strong></p></td><td><p><strong>Cross-Ancestry Harmonization</strong></p></td><td><p>Are exposure and outcome GWAS ancestry-matched, or is ancestry mismatch explicitly tested?</p></td><td><p><strong>Score 1 if ANY of the following:</strong></p><ul><li>Both exposure and outcome GWAS use identical ancestry populations (e.g., both European-only)</li><li>Cross-ancestry analysis with explicit testing: stratified analysis by ancestry reported</li><li>Replication performed in matched ancestry groups</li><li>Formal heterogeneity testing across ancestry groups with results discussed</li></ul><p><strong>Score 0 if:</strong></p><ul><li>Exposure and outcome GWAS use different ancestries without any testing or justification</li><li>Authors acknowledge mismatch but provide no empirical evaluation</li></ul></td></tr><tr><td><p><strong>B3</strong></p></td><td><p><strong>LD Structure Compatibility</strong></p></td><td><p>Is ancestry-appropriate LD reference panel used for instrument selection and pruning?</p></td><td><p><strong>Score 1 if ALL of the following:</strong></p><ul><li>LD reference panel explicitly named (e.g., "1000 Genomes Phase 3 EUR," "gnomAD v3.1 EAS")</li><li>Reference panel ancestry matches GWAS ancestry for instrument selection</li><li>LD pruning parameters stated (r² threshold, window size)</li><li>For multi-ancestry: either ancestry-specific panels used OR justification for single panel provided</li></ul><p><strong>Score 0 if ANY missing:</strong></p><ul><li>LD reference panel not named</li><li>Clear ancestry mismatch between panel and GWAS</li><li>LD parameters not specified</li></ul></td></tr><tr><td><p><strong>B4</strong></p></td><td><p><strong>Ancestry-Specific Instrument Strength</strong></p></td><td><p>Is instrument strength evaluated separately for each ancestry group?</p></td><td><p><strong>Score 1 if:</strong></p><ul><li>F-statistics OR R² reported separately for each ancestry in exposure GWAS</li><li>For single-ancestry exposure with multi-ancestry outcome: strength metrics calculated using ancestry-matched exposure data</li><li>Weak instrument bias discussed in context of ancestry-specific effects</li></ul><p><strong>Score 0 if:</strong></p><ul><li>Only pooled/overall instrument strength reported</li><li>Ancestry-specific strength not evaluated despite multi-ancestry data</li></ul></td></tr><tr><td><p><strong>B5</strong></p></td><td><p><strong>Allele Frequency Validation</strong></p></td><td><p>Are minor allele frequencies (MAF) reported and appropriate thresholds applied per ancestry?</p></td><td><p><strong>Score 1 if ALL of the following:</strong></p><ul><li>MAF thresholds explicitly stated (e.g., "MAF &gt; 0.01," "MAF &gt; 0.05")</li><li>MAF filtering applied separately by ancestry OR ancestry-specific MAF values reported</li><li>Number of SNPs excluded due to low MAF reported by ancestry group (if applicable)</li></ul><p><strong>Score 0 if:</strong></p><ul><li>MAF thresholds not specified</li><li>Only pooled MAF filtering without ancestry consideration</li><li>MAF information completely absent</li></ul></td></tr><tr><td><p><strong>B6</strong></p></td><td><p><strong>Instrument Transferability</strong></p></td><td><p>Is the validity of applying genetic instruments across ancestries explicitly justified?</p></td><td><p><strong>Score 1 if AT LEAST ONE of the following:</strong></p><ul><li><strong>Empirical replication:</strong> MR analysis replicated in target ancestry with results compared</li><li><strong>LD/frequency comparison:</strong> Explicit comparison of instrument LD patterns or allele frequencies across ancestries with data shown</li><li><strong>Biological justification:</strong> Stated rationale for cross-ancestry generalizability referencing conserved biological pathways, gene function, or mechanistic studies</li><li><strong>Literature support: </strong>Citations to studies demonstrating cross-ancestry validity of specific instruments used</li></ul><p><strong>Score 0 if:</strong></p><ul><li>No justification provided for cross-ancestry instrument application</li><li>Only general statements about genetic similarity without specific evidence</li><li>Transferability assumed without discussion</li></ul></td></tr><tr><td><p><strong>B7</strong></p></td><td><p><strong>Phenotype Consistency</strong></p></td><td><p>Are exposure and outcome phenotypes defined consistently across ancestry groups?</p></td><td><p><strong>Score 1 if ALL applicable elements present:</strong></p><p><strong><em>For binary traits:</em></strong></p><ul><li>Identical diagnostic criteria across ancestries (e.g., same ICD codes, clinical thresholds)</li><li>Case/control definitions explicitly stated for each ancestry</li></ul><p><strong><em>For continuous traits:</em></strong></p><ul><li>Measurement units consistent across ancestries (e.g., all BMI in kg/m²)</li><li>Standardization methods described if units differ</li><li>Transformation procedures (log, inverse-normal) applied consistently</li></ul><p><strong>Score 0 if ANY of the following:</strong></p><ul><li>Different diagnostic criteria used across ancestries without harmonization</li><li>Measurement units inconsistent without conversion</li><li>Phenotype definitions not specified for one or more ancestry groups</li></ul></td></tr><tr><td><p><strong>B8</strong></p></td><td><p><strong>Ancestry-Stratified Analysis</strong></p></td><td><p>Are MR results reported by ancestry and/or tested for heterogeneity across ancestry groups?</p></td><td><p><strong>Score 1 if AT LEAST ONE of the following:</strong></p><ul><li>Stratified results: MR estimates reported separately for each ancestry with effect sizes and confidence intervals</li><li>Formal heterogeneity testing: Cochran's Q, I², or similar tests performed across ancestries with p-values and interpretation</li><li>Meta-analysis approach: Random/fixed effects meta-analysis across ancestry groups with heterogeneity assessment</li></ul><p><strong>Score 0 if:</strong></p><ul><li>Only pooled results reported without ancestry breakdown</li><li>Heterogeneity mentioned but not formally tested</li><li>Results combined across ancestries without consideration of differences</li></ul></td></tr><tr><td><p><strong>B9</strong></p></td><td><p><strong>Colocalization Analysis</strong></p></td><td><p>Is colocalization or fine-mapping used to assess whether instruments tag the same causal variants across ancestries?</p></td><td><p><strong>Score 1 if ANY of the following methods applied:</strong></p><ul><li><strong>Formal colocalization:</strong> COLOC, eCAVIAR, or similar methods with posterior probabilities reported</li><li><strong>Fine-mapping comparison:</strong> SuSiE, FINEMAP, or credible sets compared across ancestries</li><li><strong>Lead SNP analysis:</strong> Assessment of whether lead SNPs are identical or in high LD (r² &gt; 0.8) across ancestries</li><li><strong>Conditional analysis:</strong> Testing whether signals remain after conditioning on lead variants</li></ul><p><strong>Score 0 if:</strong></p><ul><li>No assessment of variant-level concordance across ancestries</li><li>Only mentions colocalization without formal analysis</li></ul></td></tr><tr><td><p><strong>B10</strong></p></td><td><p><strong>Ancestry-Specific Pleiotropy</strong></p></td><td><p>Does the study evaluate whether SNP-outcome associations differ across ancestries independently of the exposure?</p></td><td><p><strong>Score 1 if AT LEAST ONE of the following:</strong></p><ul><li>Ancestry-stratified pleiotropy tests: MR-Egger intercepts, MR-PRESSO, or radial MR performed separately by ancestry with results compared</li><li>Confounder testing by ancestry: Instruments tested for association with known confounders in each ancestry group separately</li><li>Pathway analysis: Discussion of ancestry-specific biological pathways or gene expression differences that could affect pleiotropy</li><li>Negative control analysis: Testing instruments against negative control outcomes in each ancestry</li></ul><p><strong>Score 0 if:</strong></p><ul><li>Only pooled pleiotropy testing without ancestry stratification</li><li>Pleiotropy discussed generally without ancestry-specific evaluation</li></ul></td></tr><tr><td><p><strong>B11</strong></p></td><td><p><strong>Population Stratification</strong></p><p><strong>[NEW ITEM]</strong></p></td><td><p>Are population stratification and cryptic relatedness adequately controlled within and across ancestry groups?</p></td><td><p><strong>Score 1 if ALL of the following:</strong></p><ul><li>Principal components (PCs) inclusion explicitly stated with number of PCs reported</li><li>Genomic control (λ) values reported and appropriate (λ &lt; 1.1 preferred, λ &lt; 1.2 acceptable)</li><li>For multi-ancestry analysis: either ancestry-specific PC calculation OR justified approach for combined analysis</li><li>Relatedness filtering described (e.g., IBD &lt; 0.05, kinship thresholds)</li></ul><p><strong>Score 0 if ANY missing:</strong></p><ul><li>PC adjustment not mentioned</li><li>Genomic control not reported or λ &gt; 1.2</li><li>No relatedness filtering described</li></ul></td></tr><tr><td><p><strong>B12</strong></p></td><td><p><strong>Effect Size Interpretation</strong></p><p><strong>[NEW ITEM]</strong></p></td><td><p>Are effect sizes interpreted appropriately considering ancestry-specific baseline risks and phenotype distributions?</p></td><td><p><strong>Score 1 if:</strong></p><ul><li>Authors acknowledge potential differences in baseline risk/phenotype distributions across ancestries</li><li>Effect sizes discussed in context of ancestry-specific clinical relevance</li><li>Absolute risk differences calculated or discussed where appropriate</li><li>Limitations regarding generalizability of effect sizes across populations mentioned</li></ul><p><strong>Score 0 if:</strong></p><ul><li>Effect sizes interpreted identically across ancestries without consideration of population differences</li><li>No discussion of clinical relevance by ancestry</li></ul></td></tr></tbody></table>

#### Additional Scoring Guidelines

**For Multi-Ancestry Studies:** All items in Part B are applicable

**For Cross-Ancestry Studies (exposure and outcome from different ancestries):** Items B2, B6, B7, B10, B12 are particularly critical

**For Single-Ancestry Studies with Multi-Ancestry GWAS:** Items B1, B3, B4, B5, B11 apply

#### Quality Thresholds for Overall Assessment

**High Quality Cross-Ancestry Methods:** ≥80% of applicable Part B items scored as 1

**Moderate Quality:** 60-79% of applicable Part B items scored as 1

**Low Quality:** <60% of applicable Part B items scored as 1"""


rubric_prompt_1 = """I am conducting a Methods Audit of Mendelian Randomization (MR) studies using a study characteristics form and a structured scoring rubric. I will upload the MR study as a PDF file.

Please use the attached study characteristics form to extract the relevant data from the MR study.

**Notes:**
- If any item is unclear or cannot be determined from the study, mark it as N/A and briefly explain why.

# Study Characteristics Form

| **Label** | **Field** | **Question** |
| --- | --- | --- |
| Q1  | Study ID | What is the study’s citation shorthand (first author and publication year, e.g. Storm 2023)? |
| Q2  | Study Title | What is the full title of the article? |
| Q3  | Journal | What is the full name of the journal in which the article was published? |
| Q4  | Publication Year | In what year was the article published? |
| Q5  | Study Design / MR Type | What type(s) of MR design(s) were used? (e.g. One-sample MR, Two-sample MR, Multivariable MR, Bidirectional MR, or combinations) |
| Q6  | Instrumental Variable(s) | What types of genetic instruments were used (e.g. GWAS SNPs, cis-variants, PRS)? If SNPs were LD-clumped, what were the clumping parameters (e.g. r² threshold, physical distance window)? |
| Q7  | Number of SNPs per Exposure | How many SNPs were used for each exposure? Report counts separately for each exposure and ancestry group.<br><br>Example: BMI: 62 SNPs (EAS), 298 SNPs (EUR); CRP: 6 SNPs (EAS), 183 SNPs (EUR); HDL-C: 50 SNPs (EAS), 247 SNPs (EUR); BS: 15 SNPs (EAS), 93 SNPs (EUR); TGs: 36 SNPs (EAS), 204 SNPs (EUR); SBP: 22 SNPs (EAS), 158 SNPs (EUR) |
| Q8  | Exposure(s) | What traits, biomarkers, or risk factors were analyzed as exposures? |
| Q9  | Outcome(s) | What traits, diseases, or phenotypes were analyzed as outcomes? |
| Q10 | Number of Exposures Assessed | How many distinct exposures were included? |
| Q11 | Number of Outcomes Assessed | How many distinct outcomes were assessed? |
| Q12 | GWAS Source for Exposure(s) | What GWAS datasets or consortia provided SNP–exposure associations? List all.<br><br>Example: ALT/AST: UK Biobank (Neale Lab); NAFLD liability: Million Veteran Program; liver MRI: UK Biobank subset; East Asian: Biobank Japan |
| Q13 | GWAS Source for Outcome(s) | What GWAS datasets or consortia provided SNP–outcome associations? List all.<br><br>Example: CAD: CARDIoGRAM; stroke: MEGASTROKE; atrial fibrillation: published GWAS; heart failure: HERMES consortium; T2D: DIAMANTE consortium; glycaemic traits: MAGIC; East Asian: Biobank Japan, AGEN consortium |
| Q14 | Sample Size for Exposure(s) | What was the total sample size for each exposure dataset, including cases and controls if applicable? |
| Q15 | Sample Size for Outcome(s) | What was the total sample size for each outcome dataset, including cases and controls if applicable? |
| Q16 | Ancestries Represented in Exposure GWAS | What ancestry groups were included in the exposure GWAS (e.g. European, East Asian)? |
| Q17 | Ancestries Represented in Outcome GWAS | What ancestry groups were included in the outcome GWAS? |
| Q18 | Separate MR Analyses by Ancestry | Did the study conduct ancestry-stratified MR analyses? (Yes/No) |
| Q19 | Geographic Region(s) Represented | What geographic regions or countries were the study populations drawn from |
| Q20 | Software Used | What statistical software, packages, or MR tools were used (e.g. R, Stata, TwoSampleMR, MR-Base, GSMR, LDSC)? |


**Example Output Format**
Return only a single structured JSON object with the following format. Do not include any explanations, notes, or additional text.

```json
{
    "Q1": "...",
    "Q2": "...",
    "Q3": "...",
    "...": "...",
    "Q20": "..."
}
```
"""



rubric_prompt_1 = """I am conducting a Methods Audit of Mendelian Randomization (MR) studies using a study characteristics form and a structured scoring rubric. I will upload the MR study as a PDF file.

Please use the attached study characteristics form to extract the relevant data from the MR study.

**Notes:**
- If any item is unclear or cannot be determined from the study, mark it as N/A and briefly explain why.

# Study Characteristics Form

| **Label** | **Field** | **Question** |
| --- | --- | --- |
| Q1  | Study ID | What is the study’s citation shorthand (first author and publication year, e.g. Storm 2023)? |
| Q2  | Study Title | What is the full title of the article? |
| Q3  | Journal | What is the full name of the journal in which the article was published? |
| Q4  | Publication Year | In what year was the article published? |
| Q5  | Study Design / MR Type | What type(s) of MR design(s) were used? (e.g. One-sample MR, Two-sample MR, Multivariable MR, Bidirectional MR, or combinations) |
| Q6  | Instrumental Variable(s) | What types of genetic instruments were used (e.g. GWAS SNPs, cis-variants, PRS)? If SNPs were LD-clumped, what were the clumping parameters (e.g. r² threshold, physical distance window)? |
| Q7  | Number of SNPs per Exposure | How many SNPs were used for each exposure? Report counts separately for each exposure and ancestry group.<br><br>Example: BMI: 62 SNPs (EAS), 298 SNPs (EUR); CRP: 6 SNPs (EAS), 183 SNPs (EUR); HDL-C: 50 SNPs (EAS), 247 SNPs (EUR); BS: 15 SNPs (EAS), 93 SNPs (EUR); TGs: 36 SNPs (EAS), 204 SNPs (EUR); SBP: 22 SNPs (EAS), 158 SNPs (EUR) |
| Q8  | Exposure(s) | What traits, biomarkers, or risk factors were analyzed as exposures? |
| Q9  | Outcome(s) | What traits, diseases, or phenotypes were analyzed as outcomes? |
| Q10 | Number of Exposures Assessed | How many distinct exposures were included? |
| Q11 | Number of Outcomes Assessed | How many distinct outcomes were assessed? |
| Q12 | GWAS Source for Exposure(s) | What GWAS datasets or consortia provided SNP–exposure associations? List all.<br><br>Example: ALT/AST: UK Biobank (Neale Lab); NAFLD liability: Million Veteran Program; liver MRI: UK Biobank subset; East Asian: Biobank Japan |
| Q13 | GWAS Source for Outcome(s) | What GWAS datasets or consortia provided SNP–outcome associations? List all.<br><br>Example: CAD: CARDIoGRAM; stroke: MEGASTROKE; atrial fibrillation: published GWAS; heart failure: HERMES consortium; T2D: DIAMANTE consortium; glycaemic traits: MAGIC; East Asian: Biobank Japan, AGEN consortium |
| Q14 | Sample Size for Exposure(s) | What was the total sample size for each exposure dataset, including cases and controls if applicable? |
| Q15 | Sample Size for Outcome(s) | What was the total sample size for each outcome dataset, including cases and controls if applicable? |
| Q16 | Ancestries Represented in Exposure GWAS | What ancestry groups were included in the exposure GWAS (e.g. European, East Asian)? |
| Q17 | Ancestries Represented in Outcome GWAS | What ancestry groups were included in the outcome GWAS? |
| Q18 | Separate MR Analyses by Ancestry | Did the study conduct ancestry-stratified MR analyses? (Yes/No) |
| Q19 | Geographic Region(s) Represented | What geographic regions or countries were the study populations drawn from |
| Q20 | Software Used | What statistical software, packages, or MR tools were used (e.g. R, Stata, TwoSampleMR, MR-Base, GSMR, LDSC)? |


**Example Output Format**
Return only a single structured JSON object with the following format. Do not include any explanations, notes, or additional text.

```json
{
    "Q1": "...",
    "Q2": "...",
    "Q3": "...",
    "...": "...",
    "Q20": "..."
}
```
"""


rubric_prompt_2 = """I am conducting a Methods Audit of Mendelian Randomization (MR) studies using a study characteristics form and a structured scoring rubric. I will upload the MR study as a PDF file.

Please use the attached rubric (Parts A and B) to score the MR study.

- Score each item as 0, 1, or N/A based on the rubric's detailed evaluation criteria.

**Output Format (JSON)**

Return only a single structured JSON object with the following three components. Do not include any explanations, notes, or additional text.

1. **scoring  
    Includes scores for each rubric item in Part A (A1–A12) and Part B (B1–B12), using 0, 1, or "N/A".**
2. **evidence  
    For each item in A1–A12 and B1–B12, include:**
    - **score: the assigned value (0, 1, or "N/A")**
    - **quote: verbatim excerpt from the paper**
    - **section: the section where the quote was found (e.g., "Methods", "Results")**

**Use the PDF file name as the value for study_id.**

**Example Output Format**
```json
{
  "scoring": {
    "A": {
      "A1": 1,
      "A2": 0,
      "...": "N/A"
        // Continue for all A items
    },
    "B": {
      "B1": 1,
      "B2": 0,
      "...": "N/A"
        // Continue for all B items
    }
  },
  "evidence": {
    "A": {
      "A1": {
        "score": 1,
        "quote": "...verbatim text from paper...",
        "section": "Methods – Instrument Selection"
      },
      "A2": {
        "score": 0,
        "quote": "N/A",
        "section": "N/A"
      }
        // Continue for all A items
    },
    "B": {
      "B1": {
        "score": 1,
        "quote": "...",
        "section": "Results – Sample Characteristics"
      }
        // Continue for all B items
    }
  }
}
```

**Notes:**

- Follow the rubric’s critical item and quality threshold rules if applicable.
- If any item is unclear or cannot be determined from the study, mark it as N/A and briefly explain why.

# Scoring Rubric

### Part A: Core MR Methodology

**Scoring Instructions**:

- **0 = Not Addressed**: Item missing or not discussed anywhere in paper
- **1 = Fully Addressed**: Item explicitly addressed with required elements present
- **N/A**: Item clearly not applicable to study design
- **Specific numeric thresholds and keywords are provided below to minimize reviewer interpretation**

<table><tbody><tr><th><p><strong>Item</strong></p></th><th><p><strong>Category</strong></p></th><th><p><strong>Question</strong></p></th><th><p><strong>Evaluation Criteria</strong></p></th></tr><tr><td><p><strong>A1</strong></p></td><td><p><strong>Data Sources</strong></p></td><td><p>Are Exposure and Outcome GWAS described with source, ancestry, and sample size?</p></td><td><p><strong>Score 1 if ALL of the following for BOTH exposure and outcome GWAS:</strong></p><ul><li>Source identification: Study name (e.g., “UK Biobank”), consortium (e.g., “GIANT”), or specific cohort clearly stated</li><li>Sample size: Total N provided as specific number (not ranges like “~500,000”)</li><li>Ancestry composition: Population ancestry explicitly stated using standard terms or percentages</li></ul><p><strong>Score 0 if ANY element missing or vague:</strong></p><ul><li>Source described only as “published GWAS” or “large-scale study”</li><li>Sample size missing, unclear, or given as approximation</li><li>Ancestry not specified or described only as “mixed” without detail</li></ul></td></tr><tr><td><p><strong>A2</strong></p></td><td><p><strong>Instrument Selection</strong></p></td><td><p>Are SNP instruments selected using genome-wide significance and LD pruning/clumping with parameters specified?</p></td><td><p><strong>Score 1 if ALL of the following criteria present:</strong></p><ul><li>Genome-wide significance: p &lt; 5×10⁻⁸ threshold explicitly stated</li><li>LD pruning/clumping: Method clearly specified (pruning OR clumping)</li><li>LD parameters: r² threshold stated (e.g., r² &lt; 0.001, r² &lt; 0.01)</li><li>Distance parameter: Window size specified (e.g., 1MB, 250kb, 10,000kb)</li><li>Reference panel: LD reference panel named (e.g., “1000 Genomes Phase 3”)</li></ul><p><strong>Score 0 if ANY of the following:</strong></p><ul><li>Different p-value threshold used (e.g., p &lt; 5×10⁻⁶) without justification</li><li>LD method not specified (“independent SNPs” without method)</li><li>Parameters missing (r² or distance threshold not provided)</li><li>Reference panel not identified</li></ul></td></tr><tr><td><p><strong>A3a</strong></p></td><td><p><strong>Instrument Strength - Reporting</strong></p></td><td><p>Is instrument strength reported using F-statistics or R²?</p></td><td><p><strong>Score 1 if ANY of the following:</strong></p><ul><li>F-statistics provided with values (per instrument OR mean F-statistic)</li><li>R² (variance explained) provided as percentage or proportion</li><li>Both F-statistics and R² reported</li></ul><p><strong>Score 0 if:</strong></p><ul><li>Strength mentioned but no values provided (e.g., “strong instruments”)</li><li>Only weak instrument bias mentioned without metrics</li><li>No mention of instrument strength</li></ul></td></tr><tr><td><p><strong>A3b</strong></p></td><td><p><strong>Instrument Strength - Adequacy</strong></p></td><td><p>If F-statistics reported, are they adequate (F ≥ 10)?</p></td><td><p><strong>Score 1 if:</strong></p><ul><li>F ≥ 10</li></ul><p><strong>Score 0 if:</strong></p><ul><li>F &lt; 10</li></ul><p><strong>Mark N/A if:</strong></p><ul><li>F-statistics not reported</li></ul></td></tr><tr><td><p><strong>A4</strong></p></td><td><p><strong>MR Assumptions</strong></p></td><td><p>Are the three core IV assumptions explicitly stated and at least one empirically evaluated?</p></td><td><p><strong>Score 1 if ALL of the following:</strong></p><ul><li><strong>All three assumptions named: </strong>Relevance (instrument-exposure association), Independence (no confounding), Exclusion restriction (no pleiotropy)</li><li><strong>At least one assumption empirically tested</strong> using ANY of:</li><li>Confounder association testing (PhenoScanner, manual curation)</li><li>Known confounder control testing</li><li>Pleiotropy detection methods (MR-Egger, MR-PRESSO)</li><li>Negative control analyses</li></ul><p><strong>Score 0 if:</strong></p><ul><li>Assumptions mentioned but not all three clearly identified</li><li>No empirical evaluation of any assumption</li><li>Only theoretical discussion without testing</li></ul></td></tr><tr><td><p><strong>A5</strong></p></td><td><p><strong>Harmonization</strong></p></td><td><p>Are effect alleles harmonized and strand alignment issues addressed between datasets?</p></td><td><p><strong>Score 1 if AT LEAST ONE of the following approaches clearly described:</strong></p><ul><li><strong>Automated harmonization: </strong>Use of harmonization functions/packages (e.g., TwoSampleMR harmonise_data(), MungeSumstats)</li><li><strong>Manual harmonization: </strong>Process for aligning effect alleles described with specific steps</li><li><strong>Strand flip handling:</strong> Explicit mention of identifying and correcting strand flips</li><li><strong>Ambiguous SNP removal: </strong>A/T and G/C SNPs excluded or handled with frequency-based inference</li></ul><p><strong>Score 0 if:</strong></p><ul><li>No mention of harmonization procedures</li><li>Only states “data were harmonized” without method description</li></ul><p><strong>Mark N/A if:</strong></p><ul><li>Single-sample MR study</li></ul></td></tr><tr><td><p><strong>A6</strong></p></td><td><p><strong>Palindromic SNPs</strong></p></td><td><p>Are palindromic (A/T, G/C) SNPs handled appropriately?</p></td><td><p><strong>Score 1 if ANY of the following:</strong></p><ul><li><strong>Exclusion approach:</strong> A/T and G/C SNPs explicitly excluded</li><li><strong>Frequency-based inference:</strong> Allele frequencies used to determine strand alignment with frequency threshold stated (e.g., MAF &lt; 0.42 or 0.45)</li><li><strong>Reference-based alignment: </strong>Use of reference panel allele frequencies for alignment</li></ul><p><strong>Score 0 if:</strong></p><ul><li>Palindromic SNPs not mentioned</li><li>Handled but method not specified</li></ul><p><strong>Mark N/A if:</strong></p><ul><li>Single-sample MR study</li></ul></td></tr><tr><td><p><strong>A7</strong></p></td><td><p><strong>Sample Overlap</strong></p></td><td><p>Is sample overlap between exposure and outcome GWAS appropriately addressed?</p></td><td><p><strong>For 2-sample MR - Score 1 if:</strong></p><ul><li>Sample overlap explicitly discussed (even if stated as “none” or “minimal”)</li><li>Overlap quantified when present (e.g., “15% overlap”)</li><li>Appropriate methods used when overlap exists (e.g., CAUSE, MR-RAPS adjustment)</li></ul><p><strong>For 1-sample MR - Score 1 if:</strong></p><ul><li>Two-stage least squares (2SLS) or equivalent method used</li><li>Appropriate software mentioned (e.g., ivreg, ivpack)</li><li>Method justification provided for using same sample</li></ul><p><strong>Score 0 if:</strong></p><ul><li>Sample overlap not mentioned in 2-sample MR</li><li>1-sample MR without appropriate statistical method</li></ul></td></tr><tr><td><p><strong>A8</strong></p></td><td><p><strong>Confounder Control</strong></p></td><td><p>Are limitations of confounder control acknowledged (2-sample) or covariates appropriately controlled (1-sample)?</p></td><td><p><strong>For 2-sample MR - Score 1 if:</strong></p><ul><li>Explicit acknowledgment that individual-level covariates cannot be controlled</li><li>Discussion of residual confounding as study limitation</li><li>Population stratification control mentioned (if applicable)</li></ul><p><strong>For 1-sample MR - Score 1 if:</strong></p><ul><li>Covariate adjustment clearly described</li><li>Standard covariates included: age, sex, principal components</li><li>Method for covariate selection described</li></ul><p><strong>Score 0 if:</strong></p><ul><li>No discussion of confounder control limitations (2-sample)</li><li>No covariate adjustment described (1-sample)</li></ul></td></tr><tr><td><p><strong>A9</strong></p></td><td><p><strong>Outlier Detection</strong></p></td><td><p>Are outlier instruments identified using systematic methods and sensitivity analysis performed?</p></td><td><p><strong>Score 1 if ALL of the following:</strong></p><ul><li>Outlier detection method applied: Any systematic approach (leave-one-out analysis, radial MR, Cook's distance, MVMR-cML)</li><li>Method clearly named: Specific technique identified, not just “outlier analysis”</li><li>Sensitivity analysis: Results presented both with and without identified outliers</li><li>Impact discussed: Effect of outlier removal on estimates reported</li></ul><p><strong>Score 0 if:</strong></p><ul><li>No systematic outlier detection</li><li>Method not specified</li><li>No sensitivity analysis performed</li></ul></td></tr><tr><td><p><strong>A10</strong></p></td><td><p><strong>Sensitivity Analyses</strong></p></td><td><p>Are pleiotropy or heterogeneity assessed using appropriate statistical tests?</p></td><td><p><strong>Score 1 if AT LEAST ONE of the following methods applied with results reported:&lt;br/&gt;•</strong></p><ul><li>MR-Egger regression: Intercept and slope reported with p-values</li><li>Weighted median: Estimates and confidence intervals provided</li><li>MR-PRESSO: Global test and outlier correction results</li><li>Heterogeneity tests: Cochran's Q test with p-value and I² statistic</li><li>Radial MR: Modified Q-statistic and outlier identification</li><li>Contamination mixture methods: MR-Mix, CAUSE, or similar</li></ul><p><strong>Score 0 if:</strong></p><ul><li>Methods mentioned but results not provided</li><li>Only theoretical discussion of pleiotropy</li><li>No statistical testing performed</li></ul></td></tr><tr><td><p><strong>A11a</strong></p></td><td><p><strong>Robust Estimators - Use</strong></p></td><td><p>Are alternative estimators beyond inverse-variance weighted (IVW) used?</p></td><td><p><strong>Score 1 if:</strong></p><ul><li>At least one additional estimator beyond IVW used from: Weighted median, Weighted mode, MR-Egger, MR-RAPS, GSMR, or other validated methods</li><li>Results for additional estimators reported with confidence intervals</li></ul><p><strong>Score 0 if:</strong></p><ul><li>Only IVW method used</li><li>Additional methods mentioned but results not reported</li></ul></td></tr><tr><td><p><strong>A11b</strong></p></td><td><p><strong>Robust Estimators - Results</strong></p></td><td><p>Are results consistent across multiple estimators?</p></td><td><p><strong>Score 1 if:</strong></p><ul><li>Multiple estimators used AND results consistent across methods with explicit comparison</li><li>Discordant results appropriately discussed with potential explanations</li></ul><p><strong>Score 0 if:</strong></p><ul><li>Results are inconsistent</li><li>Results are not compared</li></ul><p><strong>Mark N/A if:</strong></p><ul><li>Only one estimator used</li></ul></td></tr><tr><td><p><strong>A12</strong></p></td><td><p><strong>Statistical Power</strong></p><p><strong>[NEW ITEM]</strong></p></td><td><p>Is statistical power assessed or sample size adequately justified for detecting clinically relevant effects?</p></td><td><p><strong>Score 1 if ANY of the following:</strong></p><ul><li><strong>Formal power calculation: </strong>Statistical power calculated using R² and sample sizes</li><li><strong>Minimum detectable effect size:</strong> Calculated and reported (e.g., “80% power to detect OR &gt; 1.15”)</li><li><strong>Sample size justification:</strong> Discussion of adequacy relative to expected effect sizes</li><li><strong>Power calculation software/formula referenced: </strong>mRnd, Mendelian randomization power calculator, or formula citation</li></ul><p><strong>Score 0 if:</strong></p><ul><li>No power assessment</li><li>Only general statements about “large sample sizes”</li></ul></td></tr></tbody></table>

#### Additional Quality Indicators

**Critical Items for Study Validity** (Must score 1 for minimum quality):

- A1 (Data Sources)
- A2 (Instrument Selection)
- A3 (Instrument Strength - must not score -1)
- A9 (Outlier Detection)
- A10 (Sensitivity Analyses)

**Methodological Rigor Indicators** (Items that distinguish high-quality studies):

- A4 (MR Assumptions empirical testing)
- A11 (Multiple robust estimators)
- A12 (Statistical power assessment)

#### Overall Part A Quality Assessment

**High Quality Core Methods:** ≥85% of applicable items scored ≥1, with all critical items = 1

**Moderate Quality:** 70-84% of applicable items scored ≥1

**Low Quality:** <70% of applicable items scored ≥1 OR any critical item = 0

### Part B: Cross-Ancestry Extensions to MR Methodology

**Scoring Instructions**:

- **0 = Not Addressed**: Item missing or not discussed anywhere in paper
- **1 = Fully Addressed**: Item explicitly addressed with required elements present
- **N/A**: Item clearly not applicable to study design
- **Specific numeric thresholds and keywords are provided below to minimize reviewer interpretation**

<table><tbody><tr><th><p><strong>Item</strong></p></th><th><p><strong>Category</strong></p></th><th><p><strong>Question</strong></p></th><th><p><strong>Evaluation Criteria</strong></p></th></tr><tr><td><p><strong>B1</strong></p></td><td><p><strong>Ancestry Reporting</strong></p></td><td><p>Are ancestries of Exposure and Outcome GWAS explicitly reported with sample composition details?</p></td><td><p><strong>Score 1 if ALL of the following are present:</strong></p><ul><li>Ancestry of exposure GWAS explicitly stated using standard terms (European, East Asian, African, South Asian, Hispanic/Latino, Native American, Oceanian, or specific population names)</li><li>Ancestry of outcome GWAS explicitly stated using same terminology</li><li>For multi-ancestry GWAS: numerical breakdown provided (e.g., "80% European, 15% East Asian, 5% African" OR sample sizes per ancestry group)</li><li>For admixed populations: either ancestry proportions OR population-specific labels (e.g., "African American," "Hispanic/Latino")</li></ul><p><strong>Score 0 if ANY of the following:</strong></p><ul><li>Ancestry described only as "diverse," "mixed," or "multi-ethnic" without specifics</li><li>Missing ancestry information for either exposure or outcome GWAS</li><li>Multi-ancestry GWAS mentioned without numerical breakdown</li></ul></td></tr><tr><td><p><strong>B2</strong></p></td><td><p><strong>Cross-Ancestry Harmonization</strong></p></td><td><p>Are exposure and outcome GWAS ancestry-matched, or is ancestry mismatch explicitly tested?</p></td><td><p><strong>Score 1 if ANY of the following:</strong></p><ul><li>Both exposure and outcome GWAS use identical ancestry populations (e.g., both European-only)</li><li>Cross-ancestry analysis with explicit testing: stratified analysis by ancestry reported</li><li>Replication performed in matched ancestry groups</li><li>Formal heterogeneity testing across ancestry groups with results discussed</li></ul><p><strong>Score 0 if:</strong></p><ul><li>Exposure and outcome GWAS use different ancestries without any testing or justification</li><li>Authors acknowledge mismatch but provide no empirical evaluation</li></ul></td></tr><tr><td><p><strong>B3</strong></p></td><td><p><strong>LD Structure Compatibility</strong></p></td><td><p>Is ancestry-appropriate LD reference panel used for instrument selection and pruning?</p></td><td><p><strong>Score 1 if ALL of the following:</strong></p><ul><li>LD reference panel explicitly named (e.g., "1000 Genomes Phase 3 EUR," "gnomAD v3.1 EAS")</li><li>Reference panel ancestry matches GWAS ancestry for instrument selection</li><li>LD pruning parameters stated (r² threshold, window size)</li><li>For multi-ancestry: either ancestry-specific panels used OR justification for single panel provided</li></ul><p><strong>Score 0 if ANY missing:</strong></p><ul><li>LD reference panel not named</li><li>Clear ancestry mismatch between panel and GWAS</li><li>LD parameters not specified</li></ul></td></tr><tr><td><p><strong>B4</strong></p></td><td><p><strong>Ancestry-Specific Instrument Strength</strong></p></td><td><p>Is instrument strength evaluated separately for each ancestry group?</p></td><td><p><strong>Score 1 if:</strong></p><ul><li>F-statistics OR R² reported separately for each ancestry in exposure GWAS</li><li>For single-ancestry exposure with multi-ancestry outcome: strength metrics calculated using ancestry-matched exposure data</li><li>Weak instrument bias discussed in context of ancestry-specific effects</li></ul><p><strong>Score 0 if:</strong></p><ul><li>Only pooled/overall instrument strength reported</li><li>Ancestry-specific strength not evaluated despite multi-ancestry data</li></ul></td></tr><tr><td><p><strong>B5</strong></p></td><td><p><strong>Allele Frequency Validation</strong></p></td><td><p>Are minor allele frequencies (MAF) reported and appropriate thresholds applied per ancestry?</p></td><td><p><strong>Score 1 if ALL of the following:</strong></p><ul><li>MAF thresholds explicitly stated (e.g., "MAF &gt; 0.01," "MAF &gt; 0.05")</li><li>MAF filtering applied separately by ancestry OR ancestry-specific MAF values reported</li><li>Number of SNPs excluded due to low MAF reported by ancestry group (if applicable)</li></ul><p><strong>Score 0 if:</strong></p><ul><li>MAF thresholds not specified</li><li>Only pooled MAF filtering without ancestry consideration</li><li>MAF information completely absent</li></ul></td></tr><tr><td><p><strong>B6</strong></p></td><td><p><strong>Instrument Transferability</strong></p></td><td><p>Is the validity of applying genetic instruments across ancestries explicitly justified?</p></td><td><p><strong>Score 1 if AT LEAST ONE of the following:</strong></p><ul><li><strong>Empirical replication:</strong> MR analysis replicated in target ancestry with results compared</li><li><strong>LD/frequency comparison:</strong> Explicit comparison of instrument LD patterns or allele frequencies across ancestries with data shown</li><li><strong>Biological justification:</strong> Stated rationale for cross-ancestry generalizability referencing conserved biological pathways, gene function, or mechanistic studies</li><li><strong>Literature support: </strong>Citations to studies demonstrating cross-ancestry validity of specific instruments used</li></ul><p><strong>Score 0 if:</strong></p><ul><li>No justification provided for cross-ancestry instrument application</li><li>Only general statements about genetic similarity without specific evidence</li><li>Transferability assumed without discussion</li></ul></td></tr><tr><td><p><strong>B7</strong></p></td><td><p><strong>Phenotype Consistency</strong></p></td><td><p>Are exposure and outcome phenotypes defined consistently across ancestry groups?</p></td><td><p><strong>Score 1 if ALL applicable elements present:</strong></p><p><strong><em>For binary traits:</em></strong></p><ul><li>Identical diagnostic criteria across ancestries (e.g., same ICD codes, clinical thresholds)</li><li>Case/control definitions explicitly stated for each ancestry</li></ul><p><strong><em>For continuous traits:</em></strong></p><ul><li>Measurement units consistent across ancestries (e.g., all BMI in kg/m²)</li><li>Standardization methods described if units differ</li><li>Transformation procedures (log, inverse-normal) applied consistently</li></ul><p><strong>Score 0 if ANY of the following:</strong></p><ul><li>Different diagnostic criteria used across ancestries without harmonization</li><li>Measurement units inconsistent without conversion</li><li>Phenotype definitions not specified for one or more ancestry groups</li></ul></td></tr><tr><td><p><strong>B8</strong></p></td><td><p><strong>Ancestry-Stratified Analysis</strong></p></td><td><p>Are MR results reported by ancestry and/or tested for heterogeneity across ancestry groups?</p></td><td><p><strong>Score 1 if AT LEAST ONE of the following:</strong></p><ul><li>Stratified results: MR estimates reported separately for each ancestry with effect sizes and confidence intervals</li><li>Formal heterogeneity testing: Cochran's Q, I², or similar tests performed across ancestries with p-values and interpretation</li><li>Meta-analysis approach: Random/fixed effects meta-analysis across ancestry groups with heterogeneity assessment</li></ul><p><strong>Score 0 if:</strong></p><ul><li>Only pooled results reported without ancestry breakdown</li><li>Heterogeneity mentioned but not formally tested</li><li>Results combined across ancestries without consideration of differences</li></ul></td></tr><tr><td><p><strong>B9</strong></p></td><td><p><strong>Colocalization Analysis</strong></p></td><td><p>Is colocalization or fine-mapping used to assess whether instruments tag the same causal variants across ancestries?</p></td><td><p><strong>Score 1 if ANY of the following methods applied:</strong></p><ul><li><strong>Formal colocalization:</strong> COLOC, eCAVIAR, or similar methods with posterior probabilities reported</li><li><strong>Fine-mapping comparison:</strong> SuSiE, FINEMAP, or credible sets compared across ancestries</li><li><strong>Lead SNP analysis:</strong> Assessment of whether lead SNPs are identical or in high LD (r² &gt; 0.8) across ancestries</li><li><strong>Conditional analysis:</strong> Testing whether signals remain after conditioning on lead variants</li></ul><p><strong>Score 0 if:</strong></p><ul><li>No assessment of variant-level concordance across ancestries</li><li>Only mentions colocalization without formal analysis</li></ul></td></tr><tr><td><p><strong>B10</strong></p></td><td><p><strong>Ancestry-Specific Pleiotropy</strong></p></td><td><p>Does the study evaluate whether SNP-outcome associations differ across ancestries independently of the exposure?</p></td><td><p><strong>Score 1 if AT LEAST ONE of the following:</strong></p><ul><li>Ancestry-stratified pleiotropy tests: MR-Egger intercepts, MR-PRESSO, or radial MR performed separately by ancestry with results compared</li><li>Confounder testing by ancestry: Instruments tested for association with known confounders in each ancestry group separately</li><li>Pathway analysis: Discussion of ancestry-specific biological pathways or gene expression differences that could affect pleiotropy</li><li>Negative control analysis: Testing instruments against negative control outcomes in each ancestry</li></ul><p><strong>Score 0 if:</strong></p><ul><li>Only pooled pleiotropy testing without ancestry stratification</li><li>Pleiotropy discussed generally without ancestry-specific evaluation</li></ul></td></tr><tr><td><p><strong>B11</strong></p></td><td><p><strong>Population Stratification</strong></p><p><strong>[NEW ITEM]</strong></p></td><td><p>Are population stratification and cryptic relatedness adequately controlled within and across ancestry groups?</p></td><td><p><strong>Score 1 if ALL of the following:</strong></p><ul><li>Principal components (PCs) inclusion explicitly stated with number of PCs reported</li><li>Genomic control (λ) values reported and appropriate (λ &lt; 1.1 preferred, λ &lt; 1.2 acceptable)</li><li>For multi-ancestry analysis: either ancestry-specific PC calculation OR justified approach for combined analysis</li><li>Relatedness filtering described (e.g., IBD &lt; 0.05, kinship thresholds)</li></ul><p><strong>Score 0 if ANY missing:</strong></p><ul><li>PC adjustment not mentioned</li><li>Genomic control not reported or λ &gt; 1.2</li><li>No relatedness filtering described</li></ul></td></tr><tr><td><p><strong>B12</strong></p></td><td><p><strong>Effect Size Interpretation</strong></p><p><strong>[NEW ITEM]</strong></p></td><td><p>Are effect sizes interpreted appropriately considering ancestry-specific baseline risks and phenotype distributions?</p></td><td><p><strong>Score 1 if:</strong></p><ul><li>Authors acknowledge potential differences in baseline risk/phenotype distributions across ancestries</li><li>Effect sizes discussed in context of ancestry-specific clinical relevance</li><li>Absolute risk differences calculated or discussed where appropriate</li><li>Limitations regarding generalizability of effect sizes across populations mentioned</li></ul><p><strong>Score 0 if:</strong></p><ul><li>Effect sizes interpreted identically across ancestries without consideration of population differences</li><li>No discussion of clinical relevance by ancestry</li></ul></td></tr></tbody></table>

#### Additional Scoring Guidelines

**For Multi-Ancestry Studies:** All items in Part B are applicable

**For Cross-Ancestry Studies (exposure and outcome from different ancestries):** Items B2, B6, B7, B10, B12 are particularly critical

**For Single-Ancestry Studies with Multi-Ancestry GWAS:** Items B1, B3, B4, B5, B11 apply

#### Quality Thresholds for Overall Assessment

**High Quality Cross-Ancestry Methods:** ≥80% of applicable Part B items scored as 1

**Moderate Quality:** 60-79% of applicable Part B items scored as 1

**Low Quality:** <60% of applicable Part B items scored as 1"""