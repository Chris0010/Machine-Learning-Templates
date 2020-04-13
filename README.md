# Machine Learning Templates

This repository will be used as container for base code that can be manipulated to accomplish data munging, data cleaning, and eventually ground level algorithms for machine learning techniques used to predict, classify, cluster, and other machine learning applications.

## This README file

I will make every effort to continue to update this readme file as I add new material to this repo. For now I will jump right into the templates assuming most on the program have been able to get basic Python experience recently through the Python development track. Eventually, there will be some beginner to intermediate level instruction added into this repo aswell.

Before that templates for R programming will be added to this repo for those that prefer both Python and R for their machine learning work.

## Overview

## Python Templates

### Data Munging

*  ["Importing, Cleaning, Exporting"](https://github.com/ctrCwill7/Machine-Learning-Templates/blob/master/Import_Export_Dataset.py)
    * Further explanation
    * ["Dataset"](https://github.com/ctrCwill7/Machine-Learning-Templates/blob/master/RandomMissingDataframe.csv)

* ["Transforming Categorical Data"](https://github.com/ctrCwill7/Machine-Learning-Templates/blob/master/Categorical_Data_Coding.py)
    * Further explanation
    * ["Dataset"](https://github.com/ctrCwill7/Machine-Learning-Templates/blob/master/RandomMixedDataframe.csv)

* Feature Scaling and Preparing Data for Training and Testing
    * Further explanation

* Basic Level Regression Template

* Basic Level Classification Template

### Regression

* Simple Linear Regression

* Multiple Linear Regression

* Polynomial Regression

* Decission Tree (Regression)

* Random Forest (Regression)

* Support Vector Regression (SVR)

### Classification

* Logistic Regression

* K-Nearest Neighbor (KNN)

* Support Vector Machine (SVM) & Kernel SVM

* Naive Bayes

* Decision Tree (Classification)

* Random Forest (Classification)

### Necessary libraries to import

The libraries that will be used extensively here will be:

```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

Pandas is a library used extensively in data science applications for data manipulation and analysis. It offers data structures such as sets and dataframes.

Numpy is a library used for support of large matrices and arrays that can be multidimensional. When the subject of dimensionality comes into play for data science and linear algebra is necessary, numpy can help handle this level of mathematical operation.

Matplotlib is a library is an object-oriented application programming interface (API) for visualizing plots and seeing how data appears through the numpy mathematical operations. See it as the plotting function on your scientific calculator.

An additional library that will be used extensively here is scikit-learn (sklearn). The library will be called upon when needed and individual modules will be used to manipulate the data.