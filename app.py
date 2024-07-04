import joblib
import streamlit as st

# Load the trained model and vectorizer
best_model = joblib.load('movie_genre_model.pkl')
tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Define the genre prediction function
def predict_genre(plot_summary):
    plot_summary_transformed = tfidf_vectorizer.transform([plot_summary])
    predicted_genre = best_model.predict(plot_summary_transformed)
    return predicted_genre[0]

# Set up the Streamlit app
st.title('Movie Genre Classification')
st.write('Enter a movie plot summary below to get the predicted genre.')

# Create a text input box for the plot summary
plot_summary = st.text_area('Plot Summary', '', height=150)

# Provide example plot summaries
st.subheader('Example Plot Summaries')
st.write('1. "A young wizard discovers his magical heritage."')
st.write('2. "A detective investigates a mysterious disappearance."')
st.write('3. "An astronaut explores new planets in the future."')

# Display the predicted genre when the plot summary is submitted
if st.button('Predict Genre'):
    if plot_summary.strip():  # Check if input is not empty
        predicted_genre = predict_genre(plot_summary)
        st.write(f'**Predicted Genre:** {predicted_genre}')
    else:
        st.write('Please enter a valid movie plot summary.')

# Add additional features or information
st.sidebar.header('About This App')
st.sidebar.write('This app uses a machine learning model to predict movie genres based on plot summaries.')
