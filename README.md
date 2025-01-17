# stress_levels

## About 

This project gives an analysis of 2000 college students lifestyle habits and their corresponding stress levels, using various models. By leveraging machine learning models, the project identifies patterns in the data and predicts individual stress levels as either high, moderate, or low based on lifestyle habits.

## Goals 

Our goals for this project are: 
* exploring/analyzing the data set 
* recognizing/categorizing trends 
* implementing the model 
* refining the model for accuracy (stretch)
* implement a user interface (stretch)

## Process

Our process began with an in-depth analysis of the dataset to familiarize ourselves with its structure and content. We started by writing code to check for null cells and duplicate rows, confirming that our chosen dataset contained no missing or duplicate values. Next, we utilized a correlation matrix to identify lifestyle variables most closely associated with stress levels. Our analysis revealed that the most relevant factors were study hours per day, sleep hours per day, physical activity per day, and GPA. These correlations were visually represented using a heatmap.

Building on this, we developed additional data visualizations to enhance understanding. We created a pie chart to depict the distribution of stress levels and used box plots, bar charts, violin plots, and stacked bar plots to explore the relationships between stress levels and other variables in the dataset.

Finally, we shifted our focus to model building. Using the dataset, we trained a model to predict stress levels based on students' lifestyle habits. The model categorizes individuals into one of three stress levels: high, moderate, or low, providing valuable insights into the impact of lifestyle factors on stress.

## Models

We implemented both a decision tree and a support vector machine that allowed the model to categorize each individual. 

## Usage 

Python 3.x
Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn

## Interactive prediction tool
## Usage
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

