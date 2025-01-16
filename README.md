# DiabCompSepsAI: Predictive Model for Postoperative Complications in Diabetic Patients

[![Research - Medical AI](https://img.shields.io/badge/Research-Medical%20AI-blue)](https://github.com/your-repo)
[![Libraries Used](https://img.shields.io/badge/Libraries-NumPy%2C%20Pandas%2C%20Joblib-green)](https://github.com/your-repo)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://diabcompsepsai.streamlit.app/)

## Table of Contents
1. [Abstract](#abstract)
2. [Methods](#methods)
    - [Data Collection](#data-collection)
    - [Features](#features)
    - [Feature Selection](#feature-selection)
3. [Data Preprocessing](#data-preprocessing)
    - [Encoding Categorical Variables](#encoding-categorical-variables)
4. [Model Development](#model-development)
    - [Random Forest Classifier](#random-forest-classifier)
    - [Algorithm Selection](#algorithm-selection)
5. [Results](#results)
    - [Model Performance](#model-performance)
    - [Validation Results](#validation-results)
    - [Receiver Operating Characteristic (ROC) Curve](#receiver-operating-characteristic-roc-curve)
6. [Feature Importance Analysis](#feature-importance-analysis)
    - [Demographic Influence](#demographic-influence)
7. [Interface Implementation & Usage Guide](#interface-implementation--usage-guide)
    - [Technology Stack](#technology-stack)
    - [Model Integration](#model-integration)
    - [User Instructions](#user-instructions)
8. [Model Selection Rationale](#model-selection-rationale)
9. [Conclusion](#conclusion)

---

## Abstract
Objective: This study aims to develop and evaluate a predictive model for postoperative complications, specifically wound infection and sepsis, in diabetic patients using a Random Forest Classifier.

---

## Methods

### Data Collection
- **Source Description:** The data used for this study was collected from an electronic health record (EHR) database. The total dataset consists of 17,000 records of diabetic patients and includes information on 22 different features for each patient record used for predicting postoperative complications.
- **Population Criteria Variables:** The study population consists of adult patients aged 18 to 90 years (mean age approximately 59 years) who underwent surgical procedures across 10 different specialties. These 22 features encompass a wide range of patient characteristics and clinical factors, including demographics, surgical details, and preoperative laboratory values. The dataset includes both elective (84.8%) and emergency surgeries (15.2%).
- **Dataset Completeness:** There was no missing data in the provided dataset, allowing for a robust analysis of postoperative complications in this high-risk population.

### Features
The 22 features used for training the model were:
- Demographics: `sex`, `age`
- Clinical Markers: `inout`, `transt`, `anesthes`, `dischdest`, `height`, `weight`
- Surgical Details: `surgspec`, `electsurg`, `optime`, `wndclass`
- Patient History: `smoke`, `dyspnea`, `discancr`, `diabetes`
- Laboratory Values: `dprna`, `dpralbum`, `dprhct`
- Other Clinical Factors: `emergncy`, `drenainsf`, `steroid`

### Feature Selection
Features were selected based on clinical relevance and potential to predict postoperative complications. Categories include demographics, clinical markers, surgical details, patient history, laboratory values, and other clinical factors.

---

## Data Preprocessing

### Encoding Categorical Variables
Categorical variables were encoded to numerical representations:
1. Binary Variables (Yes/No): Encoded as `0` for No, `1` for Yes.
2. `sex`: Encoded as `0` for Male, `1` for Female.
3. `inout`: Encoded as `0` for Inpatient, `1` for Outpatient.
4. `transt`: Encoded into multiple categories such as `0` for Not Transferred, `1` for Acute Care, etc.
5. Other variables like `anesthes`, `dischdest`, and `wndclass` were similarly encoded to retain categorical distinctions.

---

## Model Development

### Random Forest Classifier
- **Mechanics:** Constructs multiple decision trees using bootstrap sampling and aggregates results via majority voting for classification tasks.
- **Advantages:** Handles high-dimensional data, provides feature importance metrics, and reduces overfitting through ensemble learning.
- **Algorithm Selection:** Random Forest was chosen over other algorithms due to its superior accuracy and ability to manage diverse data types effectively.

- **Random Forest Mechanics:**
  - Bootstrap Sampling: Random samples are drawn with replacement.
  - Feature Selection: Random subsets of features are chosen for splits.
  - Aggregation: Results are aggregated for final prediction.

---

## Results

### Model Performance
The predictive model achieved:
- **Accuracy:** 94% for wound infection, 94.8% for sepsis.
- **Precision:** 93.6% for wound infection, 94.3% for sepsis.
- **Recall:** 94% for wound infection, 94.8% for sepsis.
- **F1-Score:** 93.4% for wound infection, 94.3% for sepsis.

### Validation Results
Validation on a separate test dataset confirmed the model's robustness with high consistency across metrics.

### Receiver Operating Characteristic (ROC) Curve
- ROC-AUC for Wound Infection: 0.92
- ROC-AUC for Sepsis: 0.95

---

## Feature Importance Analysis

### Feature Importance
Key predictors include:
- `optime`: Most influential.
- `weight`: Significant for recovery outcomes.
- `wndclass`, `age`, `surgspec`, and others.

### Demographic Influence
Older age significantly influenced higher complication risks, with moderate sex-based differences.

---

## Interface Implementation & Usage Guide

### Technology Stack
- **Streamlit:** Interactive web application.
- **Python Libraries:** Pandas, NumPy, Joblib.

### Model Integration
- **Loading the Model:** Pre-trained model loaded as a Joblib file.
- **User Input:** Drop-down menus and input fields for categorical and numerical variables.

### User Instructions
1. **Access the Interface:** [DiabCompSepsAI Application](https://diabcompsepsai.streamlit.app/)
2. **Enter Data:** Input patient data using provided fields.
3. **Submit Data:** Click 'Predict' for real-time results.

---

## Model Selection Rationale
- **Robust Performance:** High accuracy and precision.
- **Handling of Complex Data:** Effective with diverse data types.
- **Feature Importance:** Provides insights for clinical decision-making.
- **Resistance to Overfitting:** Ensemble learning ensures generalization.

---

## Conclusion
The model evaluation results demonstrate robust performance in predicting postoperative complications in diabetic patients. High scores across all metrics for wound infection (wndinf) and sepsis (prsepis) were achieved, with accuracy, precision, recall, and F1-scores all approaching 94%. The high precision scores indicate the model's ability to minimize false positives, ensuring that positive predictions are highly accurate. The ROC curves, with AUC values of 0.92 for wound infection and 0.95 for sepsis, further validate the model's strong discriminative ability. These results highlight the model's potential utility in clinical settings for early risk stratification and targeted interventions, ultimately enhancing patient care and outcomes.
