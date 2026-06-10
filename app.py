import streamlit as st
import pandas as pd
import joblib

model = joblib.load("ai_impact_on_mental_growth_model.pkl")

st.title("Impact of AI on Human Mental Growth")

st.write(
    "Predict whether AI usage leads to Positive Growth, Moderate Growth or Cognitive Decline Risk."
)


# Categorical Inputs
#--------------------

era = st.selectbox("Era",["AI-Augmented", "Symbiotic", "Post-Singularity"])

scenario = st.selectbox("Scenario",["Optimistic", "Neutral", "Pessimistic"])

demographic = st.selectbox("Demographic Group", ["Teenager", "Young Adult", "Adult", "Senior"])

education = st.selectbox("Education Level", ["High School", "Undergraduate", "Postgraduate", "Doctorate"])

profession = st.selectbox("Profession", ["Student", "Technology", "Research", "Healthcare", "Business", "Education"])


# Numerical Inputs
#-------------------

year = st.number_input("Year", 2025, 2100, 2050)

weekly_usage = st.slider("Weekly AI Usage Hours", 0.0, 100.0, 20.0)

dependency = st.slider( "AI Dependency Score", 0.0, 100.0, 50.0)

creativity = st.slider("Human Creativity Score", 0.0, 100.0, 50.0)

critical = st.slider("Critical Thinking Ability", 0.0, 100.0, 50.0)

problem_solving = st.slider("Problem Solving Skills",  0.0, 100.0, 50.0)

emotional = st.slider("Emotional Intelligence",  0.0, 100.0, 50.0)

innovation = st.slider("Innovation Rate",  0.0, 100.0, 50.0)

learning_speed = st.slider("Learning Speed",  0.0, 100.0, 50.0)

decision = st.slider("Human Decision Making Involvement",  0.0, 100.0, 50.0)

social = st.slider("Social Interaction Quality", 0.0, 100.0, 50.0)

cognitive = st.slider("Cognitive Load Index", 0.0, 100.0, 50.0)

mental = st.slider("Mental Wellbeing Score",  0.0, 100.0, 50.0)

proficiency = st.slider("AI Tool Proficiency",  0.0, 100.0, 50.0)

adaptability = st.slider("Adaptability Score", 0.0, 100.0, 50.0)

attention = st.slider("Attention Span Minutes", 0.0, 120.0, 30.0)


# Prediction


if st.button("Predict Outcome"):

    input_df = pd.DataFrame({

        'Year':[year],
        'Era':[era],
        'Scenario':[scenario],
        'Demographic_Group':[demographic],
        'Education_Level':[education],
        'Profession':[profession],
        'Weekly_AI_Usage_Hours':[weekly_usage],
        'AI_Dependency_Score':[dependency],
        'Human_Creativity_Score':[creativity],
        'Critical_Thinking_Ability':[critical],
        'Problem_Solving_Skills':[problem_solving],
        'Emotional_Intelligence':[emotional],
        'Innovation_Rate':[innovation],
        'Learning_Speed':[learning_speed],
        'Human_Decision_Making_Involvement':[decision],
        'Social_Interaction_Quality':[social],
        'Cognitive_Load_Index':[cognitive],
        'Mental_Wellbeing_Score':[mental],
        'AI_Tool_Proficiency':[proficiency],
        'Adaptability_Score':[adaptability],
        'Attention_Span_Minutes':[attention]

    })

    prediction = model.predict(input_df)[0]

    if prediction == "Positive Growth":
        st.success("Positive Growth")

    elif prediction == "Stagnant / Moderate":
        st.warning("Stagnant / Moderate")

    else:
        st.error("Cognitive Decline Risk")
