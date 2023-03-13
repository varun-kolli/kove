import pandas as pd
import streamlit as st


#input = ['2442501', "21-24", "Bipolar" , "12+", "Other Hispanic or Latino origin", "White","Male", "Never married", "Yes", "Part time", "Other", "2", "TN"]
def convertAge(age):
    # define subgroups with corresponding age ranges
    subgroups = {
        '0-11': range(0, 12),
        '12-14': range(12, 15),
        '15-17': range(15, 18),
        '18-20': range(18, 21),
        '21-24': range(21, 25),
        '25-29': range(25, 30),
        '30-34': range(30, 35),
        '35-39': range(35, 40),
        '40-44': range(40, 45),
        '45-49': range(45, 50),
        '50-54': range(50, 55),
        '55-59': range(55, 60),
        '60-64': range(60, 65),
        '65 up': range(65, 150)  # use a large upper bound to include all ages 65 and above
    }

    # classify the age variable
    for group, age_range in subgroups.items():
        if age in age_range:
            age_group = group
            break
    else:
        age_group = '-9'

    # store the age group as a string variable
    age_group_str = age_group.replace(' ', '')  # remove any spaces

    return age_group_str

def display_user_input(user_input):
        variable_names = ['Age', 'Education', 'Ethnicity', 'Race', 'Gender', 'Marital Status', 'Socioeconomic Status', 'Employment Status', 'Living Arrangement', 'Veteran Status', 'State']
        df = pd.DataFrame({'Variable': variable_names, 'Value': user_input})
        st.table(df)

        print(user_input)
        input = ['2442501', "21-24", "Bipolar" , "12+", "Other Hispanic or Latino origin", "White","Male", "Never married", "Yes", "Part time", "Other", "2", "TN"]
        print(input)

def prompt():
    if "user" not in st.session_state:
            st.session_state.user = []

    with st.form(key='my_form'):
        user = []
        age = st.number_input(label='Enter Age')
        ageInput = convertAge(age)
        education_levels = ["0 to 8", "9 to 11", "12 or GED", "12+"]
        educInput = st.selectbox("Select your education level", education_levels)
        employment_statuses = ["Full time", "Part time", "Employed non differentiated", "Unemployed", "Not in labor force"]
        employInput = st.selectbox("Select your employment status", employment_statuses)
        ethnicities = ["Mexican", "Puerto Rican", "Other Hispanic or Latino origin", "Not of Hispanic or Latino origin"]
        ethnicityInput = st.selectbox("Select your Ethnicity", ethnicities)
        genderInput = st.radio("Select your gender", options=["Male", "Female"])
        marital_status_options = ['Never married', 'Now married', 'Separated', 'Divorced', 'Widowed']
        marStatInput = st.selectbox('Select your marital status:', options=marital_status_options)
        housing_situations = ["Homeless", "Private residence", "Other"]
        livArangInput = st.selectbox("Select your living arrangement", housing_situations)
        racial_groups = ["Native", "Asian", "Black or African American", "Pacific Islander", "White", "Other/Multiple"]
        raceInput = st.selectbox("Select your racial group", racial_groups)
        sapInput = st.radio("SAP", options=["Yes", "No"])

        stateInput = st.selectbox("Select a state",
                                      ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
                                       "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                                       "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                                       "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
                                       "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"])
        veteranInput = st.radio("Veteran", options=["Yes", "No"])

        submit_button = st.form_submit_button(label='Run')
        user_input = []
        if submit_button:
            user_input = [ageInput, educInput, ethnicityInput, raceInput, genderInput, marStatInput, sapInput, employInput, livArangInput, veteranInput, stateInput]
            st.session_state.user.append(user_input)



    if st.session_state.user:
            st.write("User inputs:")
            display_user_input(user_input)

    st.session_state.user = []
    return st.session_state.user

def interface():
    st.title("Backend Interface")
    seshUser = prompt()




