import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download NLTK data if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Load models and vectorizer
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# Function to preprocess text
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    ps = PorterStemmer()
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Define emoji and icons
emoji_spam = "🚫"
emoji_not_spam = "✅"
icon_email = "📧"
icon_model = "🤖"
icon_contact = "📞"

# Page configuration
st.set_page_config(page_title=" 🚫 Email Spam Classifier-Sahil Tiwari", page_icon=":email:")

# Navigation
pages = ["Problem Statement", "Model", "Contact Information"]
page_selection = st.sidebar.radio("Navigate", pages)

# Page 1: Problem Statement and Images
if page_selection == "Problem Statement":
    st.title(" 📧 Email Spam Classifier")
    st.header("Problem Statement")
    st.markdown(
        """
        Spam emails are a common nuisance and can potentially contain harmful content. 
        Detecting spam emails automatically can save time and prevent users from falling 
        prey to phishing attacks.

        This application uses machine learning to classify whether an email or SMS message 
        is spam or not. It leverages Natural Language Processing (Nlp) techniques to analyze text 
        and make predictions based on a trained model.

        **Objective:** Develop a model that accurately identifies spam messages with high 
        precision and recall.
        """
    )
    st.image("images/spam.jpg", caption="Example of Spam Detection", use_column_width=True)

# Page 2: Model Prediction
elif page_selection == "Model":
    st.title("Spam Classifier")
    st.header("Model Prediction")
    st.sidebar.title("Email Spam Classifier")
    st.sidebar.image("images/icon.png", use_column_width=True)
    input_sms = st.text_area("Enter the message", height=150)

    if st.button('Predict'):
        # Preprocess
        transformed_sms = transform_text(input_sms)
        # Vectorize
        vector_input = tfidf.transform([transformed_sms])
        # Predict
        result = model.predict(vector_input)[0]
        # Display result
        if result == 1:
            st.error(f"{emoji_spam} Spam Detected")
        else:
            st.success(f"{emoji_not_spam} Not Spam")

# Page 3: Contact Information
elif page_selection == "Contact Information":
    st.title("Contact Information")
    st.header("Get in Touch")
    st.info(
        """
        If you have any questions or feedback, feel free to reach out:
        
        - **Email:** sahiltiwari1222@gmail.com
        - **Phone:** 8670558757,8959688436
        - **LinkedIn** https://www.linkedin.com/in/sahil-tiwari-b2269b27a/
        - **Github** https://github.com/sahilTiwariiii
        - **Twitter** https://x.com/sahil_tiwa96610
        """
    )
    st.image("images/conn.jpg", caption="Example of Spam Detection", use_column_width=True)

