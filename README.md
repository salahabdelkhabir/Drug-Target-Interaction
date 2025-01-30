# 🔬 Drug-Target Interaction (DTI) Prediction

## 📑 Table of Contents
- [📌 Abstract](#abstract)
- [📂 Project Repository Structure](#project-repository-structure)
- [🛠️ Detailed Methodology](#detailed-methodology)
  - [1️⃣ Data Collection](#1-data-collection)
  - [2️⃣ Data Preprocessing](#2-data-preprocessing)
  - [3️⃣ Model Architecture](#3-model-architecture)
  - [4️⃣ Model Training](#4-model-training)
  - [5️⃣ Model Evaluation](#5-model-evaluation)
  - [6️⃣ Model Deployment](#6-model-deployment)
- [📈 Results & Performance](#results--performance)
- [🚀 Future Work](#future-work)
- [📬 Contact](#contact)

---

## 📌 Abstract

This project aims to **predict drug-target interactions (DTI)** using **deep learning models** to accelerate drug discovery. We implemented a **hybrid deep learning approach (CNN + Transformer)** for predicting **binding affinity** between drugs and target proteins.

Our model processes **SMILES (Simplified Molecular Input Line Entry System)** representations for drugs and **protein sequences** as inputs. After preprocessing, a **hybrid deep learning model** predicts the **binding affinity** between drug-target pairs.

The final model is deployed via a **Flask-based web application**, allowing users to input drug and target information and get predictions instantly.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-1.9%2B-red)](https://pytorch.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-lightgrey)](https://flask.palletsprojects.com/)

---

## 📂 Project Repository Structure
```
DTI_Prediction/
├── Datasets/
│   ├── BindingDB.csv            # Primary binding database
│   └── Data with additional Info.csv   # Supplementary data
│
├── Deployment/
│   ├── static/                  # Static assets for web app
│   ├── templates/               # HTML templates
│   └── app.py                   # Flask application
│
├── Documentation/
│   ├── DTI Conference Presentation.pptx    # Presentation slides
│   ├── DTI Paper.pdf           # Research paper
│   ├── DTI Rollup.pdf          # Project summary
│   └── Final book DTI.pdf      # Comprehensive documentation
│
├── Model Checkpoint/
│   ├── DTI_config.pkl          # Model configuration
│   └── DTI_model.pt            # Trained model weights
│
└── Notebook/
    └── DTI.ipynb               # Development notebook
```

---

## 🛠️ Detailed Methodology

### 1️⃣ Data Collection
We collected **binding affinity** data from multiple sources:
- **BindingDB** → Contains experimental **drug-target interaction** data
- **PubChem & ChemSpider** → Used for **retrieving molecular structures** (SMILES)
- **UniProt** → Provided **protein sequences**

🔹 **Dataset Statistics**:
- **Total Dataset**: 42,236 drug-target pairs
- **Unique Drugs**: 9,644
- **Unique Targets**: 1,082

### 2️⃣ Data Preprocessing
**Key preprocessing steps:**

- **Data Cleaning**:
  - Removed missing values and duplicated records
  - Normalized **binding affinity scores** (log-transformed)

- **Feature Encoding**:
  - **Drug Encoding**: Converted **SMILES** into **numerical feature vectors** using **RDKit**
  - **Target Encoding**: Transformed **protein sequences** into feature vectors using **CNN-based embedding**

- **Dataset Splitting**:
  - **80% Training**
  - **10% Validation**
  - **10% Testing**

### 3️⃣ Model Architecture
We implemented a **hybrid deep learning model** combining:
- **CNN (Convolutional Neural Networks)** → For extracting features from **drug molecules**
- **Transformer Encoders** → For understanding **protein sequence relationships**

📌 **Architecture Details:**
- **CNN layers** → Extract **drug features**
- **Transformer layers** → Extract **protein features**
- **Fully Connected Layers** → Combine representations and predict binding affinity

**Model Configuration:**
- **Loss Function**: Mean Squared Error (MSE)
- **Optimizer**: Adam (learning rate = **0.0001**)

### 4️⃣ Model Training
**Training Setup:**

- **Frameworks Used**:
  - **PyTorch** → For deep learning implementation
  - **DeepPurpose** → For pre-built encoders and regression models

- **Training Hyperparameters:**
  - **Epochs**: 30
  - **Batch Size**: 128
  - **Learning Rate**: 0.0001

### 5️⃣ Model Evaluation
📊 **Performance Metrics**:

| Metric | Validation Score | Test Score |
|--------|-----------------|------------|
| **MSE** | 0.02 | 0.03 |
| **Pearson Correlation** | 0.85 | 0.82 |
| **Concordance Index (CI)** | 0.92 | 0.89 |

🔹 **Key Findings:**
- **Low MSE** indicates better accuracy in predicting binding affinity
- **Pearson correlation** shows strong alignment between predictions & actual values
- **Concordance Index** confirms the **model's ranking ability**

### 6️⃣ Model Deployment
The model is deployed as a **Flask API** for real-time predictions.

#### How to Use:
1. **Run the Web App**:
```bash
python app.py
```
2. Open `http://127.0.0.1:5000/`
3. Select a Drug and Target Protein from the dropdown
4. Click Predict
5. View the Binding Affinity Score

**API Example:**
```json
// Request
{
    "drug": "CCO[C@H](C)Oc1ccc(CCNC(=O)c2ccccc2)cc1",
    "target": "MGKNQLLTKQFT..."
}

// Response
{
    "binding_affinity": 7.85
}
```

## 📈 Results & Performance

🔹 **Key Observations:**
- Stable training loss shows effective learning
- High correlation values validate the model's predictions
- Minimal overfitting, indicating proper generalization

## 🚀 Future Work
We aim to improve and expand the project by:

1. **Data Enhancement**:
   - Expanding the dataset with more real-world drug-target interactions
   - Integrating multi-omics data

2. **Model Improvements**:
   - Integrating graph-based models for molecular structures
   - Enhancing explainability using SHAP values
   - Implementing attention mechanisms

3. **Deployment Upgrades**:
   - Developing an interactive web interface
   - Deploying as a cloud-based service
   - Adding batch prediction capabilities

## 📬 Contact

For inquiries, feedback, or collaborations, reach out:

👨‍🔬 **Salah Gamal Abdelkhabir**
- ✉️ Email: salahabdelkhabir@gmail.com
- 🔗 LinkedIn: [Salah Gamal](https://linkedin.com/in/salah-gamal)
- 📌 GitHub Repository: [DTI_Prediction](https://github.com/yourusername/DTI_Prediction)

---

🔬 **"Accelerating Drug Discovery with AI & Deep Learning!"** 🚀
