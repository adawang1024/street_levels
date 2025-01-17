# stress_levels

## About 

This project gives an analysis of 2000 college students lifestyle habits and their corresponding stress levels, using various models. 

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
