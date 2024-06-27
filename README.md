## IBM anti laundering Transaction Project
This repository contains a machine learning project aimed at tracking and predicting illegal funds. By analyzing past transactions data, we develop models that can track the illicit funds for IBM, helping IBM optimize and eradicate fraudulent transactions.

## Workflow to follow
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the config_entity.py
5. Update the configuration manager in src/config
6. Update the components
7. Update the pipeline
8. Update main.py


## Table of Contents
Project Overview
Dataset
Installation
Usage
Model Building
Evaluation
Contributing
License


## Project Overview
The detection and prevention of money laundering activities is a critical challenge for financial institutions. This IBM anti-laundering transaction project leverages machine learning techniques to predict the likelihood of suspicious transactions based on historical data.


## Data Source
The dataset can be downloaded from [This Link]https://www.kaggle.com/datasets/ealtman2019/ibm-transactions-for-anti-money-laundering-aml/data.




## Clone the Repository
```git clone https://github.com/Somtochukwu-Achikanu/IBM-anti-laundering-transaction.git```


## Run the following commands
```bash init_setup.sh```

## Run the following commands
python main.py

## Run the Dvc Command
```dvc.init```
```dvc.repro```



## Feature Engineering
We perform feature engineering to enhance the predictive power of our models:

* Encoding categorical variables
* Scaling Numerical features



## Model Building
The project uses several machine learning algorithms to build predictive models, including:
* Logistic Regression
* K Nearest neighbors
* Gradient Boosting
* Support Vector Machines (SVM)
* Decision Trees



## Evaluation
The performance of the models is evaluated using the following metrics:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC AUC


## Contributing
We welcome contributions to improve the project. Here are some ways you can contribute:

* Fix bugs and issues
* Add new features or models
* Improve documentation

To contribute, please fork the repository, create a new branch, and submit a pull request.


## License
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to customize this README.md file as per your specific project requirements. This template should give you a solid starting point for documenting your marketing campaign prediction use case using machine learning.