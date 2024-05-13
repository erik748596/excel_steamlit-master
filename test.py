import streamlit as st

# Define input fields
hw_usd = st.number_input('HW (USD)', value=0.0, step=0.01)
subscription_usd = st.number_input('Subscription (USD)', value=0.0, step=0.01)
penetration_rate = st.number_input('Penetration rate(%)', value=0.0, step=0.01, format='%.2f')/100
us_type2_diabetes_population = st.number_input('US type2 diabetes population', value=0, step=1)

# Calculate potential annual revenue
#penetration_rate = penetration_rate_percent / 100  # Convert percentage to decimal
potential_annual_revenue = us_type2_diabetes_population * penetration_rate * (hw_usd / 5 + subscription_usd * 12)

# Display the result
st.write(f'Potential Annual Revenue: ${potential_annual_revenue:,.2f}')