# Stress Level Prediction

## About 
Kaggle Dataset: https://www.kaggle.com/datasets/steve1215rogg/student-lifestyle-dataset
This project gives an analysis of 2000 college students lifestyle habits and their corresponding stress levels, using various models. By leveraging machine learning models, the project identifies patterns in the data and predicts individual stress levels as either high, moderate, or low based on lifestyle habits.

## Goals 

Our goals for this project are: 
* Gain insights into the dataset by identifying patterns, trends, and relationships among variables
* Being able to idenitfy relevant variables that affect the variable we are analyzing 
* Develop machine learning models to predict stress levels based on lifestyle habits
* Refining the model for accuracy (stretch)
* Build a user interface for interactive stress level predictions (stretch)

## Process

Our process began with an in-depth analysis of the dataset to familiarize ourselves with its structure and content. We started by writing code to check for null cells and duplicate rows, confirming that our chosen dataset contained no missing or duplicate values. Next, we utilized a correlation matrix to identify lifestyle variables most closely associated with stress levels. Our analysis revealed that the most relevant factors were study hours per day, sleep hours per day, physical activity per day, and GPA. These correlations were visually represented using a heatmap.

Building on this, we developed additional data visualizations to enhance understanding. We created a pie chart to depict the distribution of stress levels and used box plots, bar charts, violin plots, and stacked bar plots to explore the relationships between stress levels and other variables in the dataset.

Finally, we shifted our focus to model building. Using the dataset, we trained a model to predict stress levels based on students' lifestyle habits. The model categorizes individuals into one of three stress levels: high, moderate, or low, providing valuable insights into the impact of lifestyle factors on stress.

## Models

We implemented 4 models: 
- **Logistic Regression**: A simple and interpretable model that uses a linear decision boundary to classify stress levels. It achieves good performance with scaled features.
- **Decision Tree**: A non-parametric model that splits the dataset into branches based on feature values, achieving perfect accuracy on the given dataset but with a risk of overfitting.
- **Random Forest**: An ensemble learning method that combines multiple decision trees to improve accuracy and reduce overfitting. It also achieved perfect accuracy on this dataset, benefiting from its aggregation of trees.
- **Support Vector Machine (SVM)**: A robust model that finds the optimal hyperplane to separate classes, using scaled features for improved performance. 

Each model was evaluated on its precision, recall, F1-score, and overall accuracy using the test dataset. 

## Tool 

Python 3.x
Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn

## Interactive prediction

We made a Python script that predicts an individual's stress level based on daily activities and GPA using a pre-trained decision tree model. To use the script:
1. **Setup**: Ensure the `dt_model.joblib` file is in the same directory as the script. Install required libraries if needed: pip install joblib
2. **Running the Script**: Execute the script from the command line: python stress_predictor.py
3. **Input Data**: Enter the following information when prompted:
- Daily study hours
- Daily sleep hours
- Daily social hours
- Daily physical activity hours
- GPA
4. **View Prediction**: The script will output the predicted stress level based on the inputs provided.

