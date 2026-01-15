# import libraries
import streamlit as st
import pickle

# Set title
st.title('Penguin Classifier')
st.write("This app uses 6 inputs to predict the species of penguin using "
         "a model built on the Palmer Penguins dataset. Use the form below to get started!")

# Load pickle files
with open('penguin_model.pkl', 'rb') as rf_pickle:
    rfc = pickle.load(rf_pickle)

with open('output_penguin.pkl', 'rb') as map_pickle:
    unique_penguin_mapping = pickle.load(map_pickle)

# Get user input
island = st.selectbox('Penguin Island', options=['Biscoe', 'Dream', 'Torgerson'])
sex = st.selectbox('Sex', options=['Female', 'Male'])
bill_length = st.number_input('Bill Length (mm)', min_value=0.0, format="%.2f")
bill_depth = st.number_input('Bill Depth (mm)', min_value=0.0, format="%.2f")
flipper_length = st.number_input('Flipper Length (mm)', min_value=0.0, format="%.2f")
body_mass = st.number_input('Body Mass (g)', min_value=0.0, format="%.2f")

# Map categorical inputs
island_biscoe, island_dream, island_torgerson = 0, 0, 0
if island == 'Biscoe':
    island_biscoe = 1
elif island == 'Dream':
    island_dream = 1
elif island == 'Torgerson':
    island_torgerson = 1

sex_female, sex_male = 0, 0
if sex == 'Female':
    sex_female = 1
elif sex == 'Male':
    sex_male = 1

# Button to make prediction
if st.button('Predict Penguin Species'):
    try:
        # Making predictions
        new_prediction = rfc.predict([[bill_length, bill_depth, flipper_length, 
                                       body_mass, island_biscoe, island_dream, 
                                       island_torgerson, sex_female, sex_male]])

        # Mapping numerical output of model to penguin class
        prediction_species = unique_penguin_mapping[new_prediction][0]

        # Display output species class
        st.write(f"We predict your penguin is of the {prediction_species} species.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
