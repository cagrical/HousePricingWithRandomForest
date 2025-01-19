# House Price Prediction Project

This project implements a machine learning model to predict house prices based on various features such as area, number of bedrooms, bathrooms, and other amenities.

## Overview

The project consists of two main components:
1. Data Analysis (DataAnalysis.ipynb)
2. Random Forest Model Implementation (RandomForest.ipynb)
3. Web Interface for Price Prediction

## Features

- Predicts house prices based on the following features:
  - Area (in square meters)
  - Number of bedrooms
  - Number of bathrooms
  - Number of stories
  - Main road access
  - Guest room availability
  - Basement availability
  - Hot water heating
  - Air conditioning
  - Parking space
  - Preferred area
  - Furnishing status

## Technology Stack

- Python 3.12.7
- Libraries:
  - pandas
  - numpy
  - scikit-learn
  - matplotlib
  - seaborn
  - pickle (for model serialization)

## Project Structure

```
project/
│
├── DataAnalysis.ipynb      # Data exploration and visualization
├── RandomForest.ipynb      # Model development and training
├── rf_model.pkl           # Saved Random Forest model
├── Housing.csv            # Dataset
└── README.md
```

## Model Details

- Algorithm: Random Forest Regressor
- Parameters:
  - n_estimators: 400
  - max_depth: 13
  - min_samples_split: 7
  - min_samples_leaf: 2
  - random_state: 32
  - test_size: 0.13

## Installation

1. Clone the repository:
```bash
git clone https://github.com/cagrical/housePricingWithRandomForest.git
```

2. Install required packages:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

3. Run Jupyter notebooks:
```bash
jupyter notebook
```

## Usage

1. Data Analysis:
   - Open `DataAnalysis.ipynb` to explore the dataset and visualizations
   - Contains comprehensive data exploration and statistical analysis
     ![correleation](https://github.com/user-attachments/assets/ebc5c597-8d90-4ceb-81a7-aaec0e5f5540)
![furnished](https://github.com/user-attachments/assets/343901b9-1dd4-4877-88e8-1507a6b3287f)


2. Model Training:
   - Open `RandomForest.ipynb` to see the model development process
   - Includes data preprocessing, model training, and evaluation
     ![Price](https://github.com/user-attachments/assets/def6fa2f-e2cc-4b4a-8256-59290c461688)


3. Making Predictions:
   - Use the web interface to input house features
   - Get instant price predictions based on the trained model

## Model Performance

- R-squared (R²) Score: [Score from your model]
- Root Mean Square Error (RMSE): [RMSE value]
- Mean Squared Error (MSE): [MSE value]

## Web Interface

The project includes a user-friendly web interface that allows users to:
- Input house features through a form
- Get instant price predictions
- Make multiple predictions easily

![RandomForestPredictionPage](https://github.com/user-attachments/assets/f4ce04bf-967b-423c-8fa9-031787b4bb9a)
![PredictionPage](https://github.com/user-attachments/assets/20b92411-e21d-466b-8ad2-9cd71d2dc2b9)

