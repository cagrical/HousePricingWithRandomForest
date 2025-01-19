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
![correleation](https://github.com/user-attachments/assets/36519364-1060-40ad-a65a-cd315bb224ea)
![furnished](https://github.com/user-attachments/assets/00824446-8340-4850-8f54-a0d56f376dca)

2. Model Training:
   - Open `RandomForest.ipynb` to see the model development process
   - Includes data preprocessing, model training, and evaluation 
![Price](https://github.com/user-attachments/assets/6cd92008-7e99-4aeb-9db8-358f184783b1)

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
![RandomForestPredictionPage](https://github.com/user-attachments/assets/04b37f65-3858-416a-8ce9-56b224f88c8b)
![PredictionPage](https://github.com/user-attachments/assets/73f4b0c6-14b4-4ef7-8435-91bcbe045597)

