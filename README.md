This README file is generated based on the uploaded files, which indicate a **Drug Classification** project using a **Decision Tree** model deployed via a **Flask** application.


# 💊 Drug Prescription Prediction System

This repository contains a machine learning project that predicts the most appropriate drug for a patient based on their demographic and medical attributes. The classification model is built using a Decision Tree and is deployed using a simple Flask web application.

## 🎯 Project Goal

The primary goal of this project is to classify a patient's prescription into one of five drug categories (`drugA`, `drugB`, `drugC`, `drugX`, `drugY`) based on the following features:

* **Age**
* **Sex**
* **Blood Pressure (BP)**: High, Low, Normal
* **Cholesterol**: High, Normal (Based on model implementation)
* **Sodium to Potassium Ratio (Na\_to\_K)**

## 📂 Repository Contents

| File | Description |
| :--- | :--- |
| `drug200 - drug200.csv` | The original dataset containing patient data and corresponding prescribed drugs. |
| `dtree.ipynb` | Jupyter Notebook detailing the **Data Analysis, Preprocessing, Model Training (Decision Tree), and Evaluation**. |
| `dtmodel.pkl` | The **trained Decision Tree model** saved as a pickle file for deployment. |
| `dtapp.py` | A **Flask application** script that loads the `dtmodel.pkl` and provides a web interface for real-time predictions. |
| `requirements.txt` | (Assumed) List of necessary Python libraries to run the project. |
| `README.md` | This file. |

## 🚀 Getting Started

### Prerequisites

You will need Python 3.x installed on your system.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-link>
    cd <repo-name>
    ```

2.  **Create a virtual environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/Mac
    venv\Scripts\activate     # On Windows
    ```

3.  **Install dependencies:**
    The application relies on `scikit-learn` (for the model), `pandas` (for data handling), and `Flask` (for deployment).
    *(You may need to create a `requirements.txt` file listing these libraries: `pandas`, `scikit-learn`, `flask`)*
    ```bash
    pip install -r requirements.txt
    ```

## 💻 How to Run the Web Application

1.  Make sure the `dtmodel.pkl` file is in the same directory as `dtapp.py`.
2.  Run the Flask application:
    ```bash
    python dtapp.py
    ```
3.  Open your web browser and navigate to the displayed local address (e.g., `http://127.0.0.1:5000/`).

You can now input the patient features and receive a real-time drug prediction!

## 🤖 Model Implementation Details

The model used is a **Decision Tree Classifier** trained on the `drug200 - drug200.csv` dataset.

* **Categorical Encoding:** The model uses Ordinal Encoding internally for categorical features, which are mapped as follows in the `dtapp.py`:
    * **Sex:** `{'F': 0, 'M': 1}`
    * **BP:** `{'NORMAL': 0, 'LOW': 1, 'HIGH': 2}`
    * **Cholesterol:** `{'LOW': 0, 'HIGH': 1}`
* **Prediction Output:** The model predicts a numerical class which is then mapped back to the drug name:
    * `{0: "drugA", 1: "drugB", 2: "drugC", 3: "drugX", 4: "drugY"}`

