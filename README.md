# AspireNex-MOVIE-GENRE-CLASSIFICATION

## Project Overview

**MOVIE-GENRE-CLASSIFICATION** is a machine learning project aimed at classifying movie genres based on plot summaries. The objective is to develop a model that can accurately predict the genre of a movie from its description. The project encompasses several key phases, including data cleaning and preprocessing, model training and optimization, cross-validation, and the creation of a user-friendly interface for genre prediction.

## Key Components

### Data Cleaning and Preprocessing

The first phase of the project focuses on preparing the data for analysis. This involves:

- **Loading Data:** Importing datasets that contain movie names, genres, and plot summaries.
- **Text Cleaning:** Preprocessing the text data by converting it to lowercase, removing numbers and punctuation, and trimming whitespace to ensure consistency.
- **Data Transformation:** Dropping unnecessary columns and removing duplicate entries to create a clean and unique dataset.
- **Data Inspection:** Verifying that the data is correctly formatted and free from missing values or errors.

### Model Training and Optimization

After cleaning the data, the next phase involves building and refining machine learning models:

- **Feature Extraction:** Transforming the text data into numerical features using TF-IDF Vectorization to capture the importance of words in the plot summaries.
- **Model Selection:** Testing various algorithms for genre classification, such as Multinomial Naive Bayes, Logistic Regression, Support Vector Machine (SVM), and Random Forest.
- **Hyperparameter Tuning:** Optimizing model performance through techniques like Grid Search to find the best hyperparameters.
- **Model Evaluation:** Assessing model effectiveness and accuracy using detailed classification reports.

### Cross-Validation

To ensure that the model generalizes well to unseen data, cross-validation techniques are employed:

- **Process:** Splitting the data into multiple folds and evaluating model performance across these folds.
- **Benefits:** Ensures that the model’s performance metrics are reliable and not just due to overfitting or random chance.

### User Interface for Predictions

The final phase involves creating a user-friendly interface:

- **Design:** Developing a simple interface where users can input a movie’s plot summary.
- **Functionality:** The interface utilizes the trained model to predict the genre of the movie based on the provided plot summary and displays the result to the user.

## Technologies Used

- **Programming Language:** Python
- **Libraries:** scikit-learn for machine learning algorithms and model evaluation, pandas for data manipulation, and Flask for building the user interface.

## Conclusion

The **MOVIE-GENRE-CLASSIFICATION** project demonstrates the ability to develop a complete machine learning pipeline, from data preparation and model training to creating a practical user interface. It showcases skills in data cleaning, feature extraction, model optimization, and application development.

![Screenshot 2024-07-04 171341](https://github.com/Sivamedisetti/AspireNex-MOVIE-GENRE-CLASSIFICATION/assets/96729473/b2b80f8b-08aa-436e-a31b-2311ccf1d278)
