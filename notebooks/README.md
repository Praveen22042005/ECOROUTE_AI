# Overview

This directory contains the Jupyter Notebook used for building and evaluating the Route Optimization AI Model. The notebook provides a step-by-step guide for **data preprocessing, model training, predictions, and evaluation metrics.** It allows for easy interaction and testing of the entire pipeline using sample data.

## Notebook File
**route_optimization_pipeline.ipynb:** This notebook covers the complete workflow, from loading the datasets to training the AI model and evaluating the results. It is designed to guide users through the process of route optimization using machine learning.

## Model Details
- Algorithm Used: The model uses Ridge Regression, which is an extension of linear regression that addresses multicollinearity by adding a regularization term to the model.

- Objective: The AI model aims to minimize total delivery costs and reduce delivery times by optimizing vehicle routes based on traffic delays, delivery demands, vehicle capacities, and distances between warehouses and delivery locations.

## Model Performance
### Evaluation Metrics:

- **Mean Absolute Error (MAE):** This metric evaluates the average magnitude of errors in the predictions.
  - MAE Score: **7.0**

- **Mean Squared Error (MSE):** This metric measures the average of the squares of the errors, giving more weight to large errors.
  - MSE Score: **55.0**

- **R² Score:** This represents the proportion of variance in the dependent variable that is predictable from the independent variables.
  - R² Score: **0.989**
