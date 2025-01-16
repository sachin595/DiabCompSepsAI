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
**Postoperative complications**, particularly wound infections and sepsis, are major concerns in diabetic patients. This study developed a predictive model using a **Random Forest Classifier** to identify high-risk cases preoperatively. The model was trained on a dataset of 17,000 diabetic patients, encompassing diverse features like demographics, surgical details, and laboratory values. With an accuracy of 94% for **wound infections** and 94.8% for **sepsis**, the model demonstrated strong performance. Key predictors included patient weight, and wound classification. Integrated into a **Streamlit application**, this tool enables **real-time risk assessment**, supporting early intervention and improved patient outcomes.

---

## Methods

### Data Collection
- **Source Description:** The data used for this study was collected from an electronic health record (EHR) database. The total dataset consists of 17,000 records of diabetic patients and includes information on 22 different features for each patient record used for predicting postoperative complications.
- **Population Criteria Variables:** The study population consists of adult patients aged 18 to 90 years (mean age approximately 59 years) who underwent surgical procedures across 10 different specialties. These 22 features encompass a wide range of patient characteristics and clinical factors, including demographics, surgical details, and preoperative laboratory values. The dataset includes both elective (84.8%) and emergency surgeries (15.2%).
- **Dataset Completeness:** There was no missing data in the provided dataset, allowing for a robust analysis of postoperative complications in this high-risk population.

### Features
The 22 features used for training the model were:
-   **sex**: The gender of the patient, typically categorized as male or female.
-	**Age**: The age of the patient at the time of the medical event.
-	**inout**: Whether the patient was admitted as an inpatient or treated as an outpatient
-	**transt**: Transfer status
-	**anesthes**: Type of anesthesia used during the procedure
-	**dischdest**: discharge destination
-	**height**: The patient's height
-	**weight**: The patient's weight
-	**surgspec**: The medical specialty of the surgeon performing the procedure
-	**electsurg**: Whether the surgery was elective (planned) or not
-	**smoke**: Indicates whether the patient is a smoker
-	**dyspnea**: Difficulty in breathing, if present or not
-	**discancr**: Diagnosis of cancer.
-	**Diabetes**: Indicates whether the patient has diabetes.
-	**dprna, dpralbum, dprhct** (lab results)
-	**emergncy**: Indicates whether the procedure was performed as an emergency
-	**optime**: Duration of the operation (surgery time).
-	**drenainsf**: Deep renal insufficiency
-	**steroid**: Use of steroids as part of treatment.
-	**Wndclass**: Classification of wound type (e.g., clean, contaminated).


### Feature Selection
Features were selected based on clinical relevance and potential to predict postoperative complications. Categories include demographics, clinical markers, surgical details, patient history, laboratory values, and other clinical factors.The careful selection of these features ensured that the model was trained on the most pertinent and informative variables, thereby improving its accuracy and reliability in predicting postoperative outcomes.

image

<div align="center">
    <p>◆ Demographics: sex, age</p>
    <p>◆ Clinical markers: inout, transt, anesthes, dischdest, height, weight</p>
    <p>◆ Surgical details: surgspec, electsurg, optime, wndclass</p>
    <p>◆ Patient history: smoke, dyspnea, discancr, diabetes</p>
    <p>◆ Laboratory values: dprna, dpralbum, dprhct</p>
    <p>◆ Other clinical factors: emergncy, drenainsf, steroid</p>
</div>

### Target Variables:
The primary outcomes of interest in this study were the presence of wound infection (wndinf) and sepsis (prsepis). These target variables were chosen due to their clinical significance in assessing postoperative complications.

---
## Workflow

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
- In our study, we employed a random forest classifier to develop a robust predictive model. Random forest, an ensemble learning method for classification, regression, & other tasks, operating by constructing multiple decision trees at training time.

### What it Does:
- The random forest classifier is a powerful supervised machine learning algorithm commonly used for both classification & regression tasks. It constructs multiple decision trees on various samples & uses their average for classification and majority vote for regression. This ensemble learning technique enhances prediction accuracy & mitigates the risk of overfitting.

### How it Works: 
- The figure below illustrates the mechanics of the random forest algorithm. Starting with the dataset, multiple decision trees are constructed. Each tree is trained on a different subset of the data, obtained through bootstrap sampling. During the training process, a random subset of features is selected at each node, which introduces diversity among the trees. The final prediction is made by aggregating the results from all trees, either by taking the majority vote for classification tasks or the mean for regression tasks.

### Algorithm Selection:
- In our study, we selected the random forest classifier after conducting a comparative analysis with other algorithms such as logistic regression, support vector machines, and neural networks. Random forests were chosen due to their ability to handle complex interactions, provide feature importance metrics, and resist overfitting. They also performed best in terms of accuracy, precision, and recall for predicting postoperative complications like wound infection and sepsis.

### Random Forest Mechanics:
 A random forest classifier addresses the overfitting problem by constructing multiple decision trees during training and outputting the mode of the classes (classification). The key steps involved in building a random forest model are as follows:



 - **1.	Bootstrap Sampling:** For each tree in the forest, a random sample is drawn with replacement from the training dataset. This process, known as bootstrap sampling, ensures that each tree is trained on a different subset of data.
 - **2.	Feature Selection:** At each node of a tree, a random subset of features is selected, and the best split is chosen only from this subset. This random feature selection introduces additional diversity among the trees, further reducing the correlation between them and enhancing the model's generalization ability.
 - **3.	Tree Construction:** Each tree is grown to its maximum extent without pruning. The randomness introduced in the sampling and feature selection stages ensures that the trees are diverse and uncorrelated.
 - **4.	Aggregation:** For classification tasks, each tree in the forest casts a "vote" for the predicted class. The final prediction of the random forest is the class with the majority of votes.

---

## Results

### Model Performance
The predictive model achieved:
- **Accuracy:** 94% for wound infection, 94.8% for sepsis.
- **Precision:** 93.6% for wound infection, 94.3% for sepsis.
- **Recall:** 94% for wound infection, 94.8% for sepsis.
- **F1-Score:** 93.4% for wound infection, 94.3% for sepsis.


### Receiver Operating Characteristic (ROC) Curve
- ROC-AUC for Wound Infection: 0.92
- ROC-AUC for Sepsis: 0.95

---

## Feature Importance Analysis

### Feature Importance
The feature importance diagram provides insights into which variables most significantly influence the model's predictions for postoperative complications. Here's a detailed explanation of the top features:
- 	**Operation Time (optime):** This is the most influential feature, indicating that longer surgical durations may increase the risk of complications. It suggests that minimizing operation time could be crucial in reducing postoperative risks.
-	**Weight:** Patient weight is a critical factor, likely due to its association with various health conditions that can affect recovery and complication rates.
-	**Wound Classification (wndclas):** The type of wound (clean, contaminated, etc.) plays a significant role in predicting complications, as certain classifications are more prone to infection.
-	**Age:** Older age is associated with higher risk, reflecting the general trend that older patients may have more comorbidities and slower recovery rates.
-	**Surgical Specialty (surgspec):** Different specialties may have varying complication rates, highlighting the importance of tailoring risk assessments to specific surgical contexts.
-	**Height:** While less intuitive, height may correlate with other health metrics that affect surgical outcomes.
-	**Emergency Status (emergency):** Emergency surgeries often carry higher risks due to less preparation time and potentially more severe underlying conditions.
-	**Diabetes Status (diabetes):** Diabetes is a known risk factor for complications, affecting wound healing and infection rates.
  
These insights can guide clinicians in identifying high-risk patients and tailoring interventions to mitigate potential complications. Understanding feature importance helps refine predictive models and improve patient care strategies.


### Demographic Influence
Demographic factors such as age and sex were analyzed to understand their influence on model predictions. Age emerged as a significant predictor, with older patients showing higher risk levels for complications. Sex showed a moderate influence, with slight variations in prediction accuracy between male and female patients.

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
The model evaluation results demonstrate robust performance in predicting postoperative complications in diabetic patients. High scores across all metrics for wound infection (wndinf) and sepsis (prsepis) were achieved, with accuracy, precision, recall, and F1-scores all approaching 94%.These results highlight the model's potential utility in clinical settings for early risk stratification and targeted interventions, ultimately enhancing patient care and outcomes.The integration of the machine learning model into the Streamlit interface enables seamless interaction and real-time predictions. This setup not only enhances the accessibility of the model but also ensures that healthcare providers can efficiently assess patient risks, ultimately improving clinical outcomes.
