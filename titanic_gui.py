import streamlit as st
import pickle

with open('titanic_predictor.sav', 'rb') as file:
    model = pickle.load(file)

def predict_survival(model, features):
    prediction = model.predict([features])
    return "Survived" if prediction[0] == 1 else "Did not survive"
#Streamlit App
def main():

    '''
    # Would you survive the Titanic desaster?

    '''
    
    #Inputs
    st.write('---')

    pclass = st.selectbox("What passenger class are you?", ["First", "Second", "Third"])

    gender = st.radio('What gender are you?',['Male', 'Female'])

    age = st.slider("How old are you?", 0, 80)

    sibsp = st.slider("How many siblings and spouses were with you?", 0, 8)

    parch = st.slider("How many parents and children were aboard with you?", 0, 6)
    
    fare = st.slider("How much did you pay for your cruise ticket (in 1910 USD)?", 0, 512)

    #port = st.selectbox("Which port did you embark from?", ["Cherbourg", "Queenstown", "Southampton"])

    sex = 1 if gender == "female" else 0
    features = [pclass, sex, age, sibsp, parch, fare]

    st.write('\n')
    
    # Prediction

    if st.button('Predict'):
        result = predict_survival(model, features)
        st.write(f"Prediction: {result}")
    #st.write('\n')

    #if st.button('Reset'):


if __name__ == "__main__":
    main()
