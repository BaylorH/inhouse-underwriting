# In-House Underwriting Model

This project is an in-house machine learning underwriting system designed to replicate and replace the functionality currently provided by third-party services like Underwrite.ai. It processes application data and returns a risk score and decision (`Accept` or `Deny`) in under 60 seconds.

## 🔍 Goal

- Predict risk scores (0–1) based on applicant data
- Return a decision (`Accept` or `Deny`) using a threshold
- Allow customizable weighting of criteria
- Ensure explainability (via SHAP or similar tools)
- Support future retraining and performance improvement
- Integrate with the current system (e.g. IntroXL, LoanTill)

---

## 🗂️ Dataset Columns & Definitions

### 🔹 Basic Application Fields
| Column | Description |
|--------|-------------|
| `uuid` | Unique identifier for the application (UUID) |
| `tracking_number` | Internal or external tracking ID for the loan |
| `requested_amount` | Amount of money the applicant is requesting |
| `lead_price` | Cost of acquiring this loan lead |
| `paycheck_amount` | Amount per paycheck for the applicant |
| `years_with_bank_account` | Number of years applicant has held a bank account |
| `net_monthly_income` | Applicant's income after taxes per month |
| `score` | Risk score from third-party model (target for replication) |
| `decision` | Final decision: `Accept` or `Deny` |

### 🔹 Consumer Account Activity (CAA_*)
| Column | Description |
|--------|-------------|
| `caa_c1_inq_3_yrs` | Credit inquiries by company type C1 (3 years) |
| `caa_c3_inq_3_yrs` | Credit inquiries by company type C3 (3 years) |
| `caa_ca_clu_24_hrs` | New account clusters created (last 24 hrs) |
| `caa_ca_clu_3_yrs` | Account clusters created in 3 years |
| `caa_ca_inq_2_yrs` | Total credit inquiries (2 years) |
| `caa_ca_inq_3_yrs` | Total credit inquiries (3 years) |
| `caa_debt_ratio` | Debt-to-income ratio |
| `caa_exp_all0100` | Experience with personal loans |
| `caa_exp_all0216` to `caa_exp_all8325` | Experience with specific loan types (internal codes) |
| `caa_exp_aua5820` | Auto loan activity |
| `caa_exp_brc3425` | Bank revolving credit |
| `caa_exp_col5060` | Collections experience |
| `caa_exp_iqt9420`, `caa_exp_iqt9426` | Inquiry types |
| `caa_exp_rev5320` | Revolving credit (credit cards) |
| `caa_exp_rtr1300` | Rent-to-own activity |
| `caa_exp_taua4710`, `tbca3255`, `tbcc4355`, `trtr3624` | Other coded account types |

### 🔹 Credit Consumer Report (CCR_*)
| Column | Description |
|--------|-------------|
| `ccr_all_ato_2_yrs` | Auto loans opened in last 2 years |
| `ccr_all_dd_3_yrs` | Defaults/delinquencies (3 years) |
| `ccr_all_dd_7_yrs` | Defaults/delinquencies (7 years) |
| `ccr_amt_of_loans_pd_off` | Total loans paid off |
| `ccr_c3_aco_7_yrs` | C3 account opened in last 7 years |
| `ccr_c3_dd_180_days` | C3 delinquencies (180 days) |
| `ccr_c3_dd_7_yrs` | C3 delinquencies (7 years) |
| `ccr_c3_inq_180_days` | Inquiries from C3 companies (180 days) |
| `ccr_c3_inq_24_hrs` | C3 inquiries in last 24 hours |
| `ccr_ca_inq_1_yr` | Total inquiries (1 year) |
| `ccr_dsince_1st_bankacct_1st_seen` | Days since first bank account seen |
| `ccr_dsince_1st_loan_opened` | Days since first loan opened |
| `ccr_dsince_1st_ontime_pmt` | Days since first on-time payment |
| `ccr_dsince_lst_loan_chrg_off` | Days since last charge-off |
| `ccr_dsince_lst_loan_opened` | Days since last loan opened |
| `ccr_dsince_lst_loan_pd_off` | Days since last loan paid off |
| `ccr_dsince_lst_loan_pmt` | Days since last loan payment |
| `ccr_dsince_lst_ontime_pmt` | Days since last on-time payment |
| `ccr_exp_all7360`, etc. | Experience with specific lender types |
| `ccr_score` | External/internal credit score |
| `ccr_worst_pmt_rating` | Worst recorded payment rating (0–9) |

### 🔹 Fraud Intelligence (FI_*)
| Column | Description |
|--------|-------------|
| `fi_ratio_15_days_365_days` | Recent activity ratio (15d vs. 365d) |
| `fi_ratio_15_days_90_days` | Recent activity ratio (15d vs. 90d) |
| `fi_ratio_90_days_365_days` | Medium-term activity ratio |
| `fi_xtab_hmphone_home_addr` | Cross-match home phone with address |
| `fi_xtab_multiple` | Count of repeated values across apps |
| `fi_xtab_pts_tot` | Total fraud points from cross-tab analysis |
| `fi_score` | Overall fraud score (0–100) |

### 🔹 Metadata
| Column | Description |
|--------|-------------|
| `created_at` | Timestamp when application was submitted |

---

## ⚙️ Usage (coming soon)

- `src/train.py`: Training script for initial model
- `src/predict.py`: Scoring function for new applications
- `src/explain.py`: SHAP-based model explanation

---

## 📌 Notes

- Fields like `score` and `decision` are used as targets for modeling.
- Features are subject to further cleaning and correlation analysis.
- Location-specific scoring may be introduced in a future version.

---

## 📫 Contact

For questions or collaboration, reach out to [Baylor Harrison](mailto:bp21harrison@gmail.com).
