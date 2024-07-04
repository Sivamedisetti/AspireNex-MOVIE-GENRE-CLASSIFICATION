"# AspireNex-MOVIE-GENRE-CLASSIFICATION" 
Overview
The Movie Genre Classification project classifies movie genres based on plot summaries using machine learning techniques. The main steps include data cleaning, model training, optimization, evaluation, and creating a user-friendly interface for predictions.

1. Data Cleaning and Preprocessing
1.1 Introduction
Data cleaning is a crucial first step in any data science project. It involves preparing the raw data for analysis by ensuring it is accurate, consistent, and ready for modeling.

1.2 Data Loading
The project starts by loading the training and test datasets from text files. Each dataset contains three columns:

Movie Name: The title of the movie.
Genre: The genre of the movie.
Description: A textual summary of the movie’s plot.
1.3 Text Cleaning
To prepare the text data for machine learning models, several text preprocessing steps are applied:

Conversion to Lowercase: Ensures uniformity by converting all text to lowercase.
Removal of Numbers: Strips out numeric characters from the text.
Punctuation Removal: Eliminates punctuation marks from the text.
Whitespace Trimming: Removes leading and trailing whitespace.
1.4 Data Transformation
Post-cleaning, the following transformations are applied:

Dropping Columns: The Movie Name column is removed as it is not needed for genre classification.
Removing Duplicates: Duplicate rows are eliminated to ensure each training example is unique.
1.5 Data Inspection
The cleaned datasets are inspected to confirm that the data is in the correct format, with no missing values or further duplicates.

2. Model Training and Optimization
2.1 Feature Extraction
Feature extraction is the process of converting text data into a format that machine learning algorithms can process:

TF-IDF Vectorization: This method transforms text into numerical features by capturing the importance of words in the documents relative to the entire corpus.
2.2 Train-Test Split
The dataset is divided into training and validation sets. This split is essential for training the model and evaluating its performance on unseen data.

2.3 Model Training
Various machine learning algorithms are employed to find the best model for classifying movie genres:

Multinomial Naive Bayes: A simple probabilistic model based on Bayes’ theorem.
Logistic Regression: A regression model for binary or multi-class classification.
Support Vector Machine (SVM): A powerful classifier that works well for text classification.
Random Forest: An ensemble method that uses multiple decision trees to improve performance.
2.4 Hyperparameter Tuning
Grid Search is used to find the optimal settings for the models. This involves testing different combinations of hyperparameters to improve model performance.

2.5 Model Evaluation
The models are evaluated using accuracy and detailed classification reports, which provide insights into the model’s performance across different genres.

3. Cross-Validation
3.1 Introduction
Cross-validation is a technique used to assess how the model performs on different subsets of the data to ensure that it generalizes well to unseen data.

3.2 Implementation
Cross-validation involves splitting the training data into several folds and training the model on each fold to evaluate its performance.

3.3 Benefits
This technique helps to ensure that the model’s performance metrics are reliable and not just due to random chance or overfitting.

4. User Interface for Predictions
4.1 Introduction
A user interface is created to allow users to input movie plot summaries and receive genre predictions.

4.2 Components
Text Box: Users can type in the plot summary of a movie.
Output Area: Displays the predicted genre based on the input plot summary.
4.3 Functionality
The interface uses the trained model and TF-IDF vectorizer to transform the input plot summary and make predictions. It then displays the predicted genre to the user.

![Screenshot 2024-07-04 171341](https://github.com/Sivamedisetti/AspireNex-MOVIE-GENRE-CLASSIFICATION/assets/96729473/4b5ae300-5e5d-4c77-a327-dea5d6e76273)


