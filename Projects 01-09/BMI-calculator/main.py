import streamlit as st

def calculate_bmi(weight, height):
    """Calculate BMI given weight in kg and height in meters"""
    return weight / (height ** 2)

def bmi_category(bmi):
    """Return BMI category based on BMI value"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    st.title("BMI Calculator")
    st.write("Calculate your Body Mass Index (BMI)")

    # Measurement system selection
    measurement_system = st.radio("Select measurement system:", 
                                 ("Metric (kg & cm)", "Imperial (lbs & in)"))

    if measurement_system == "Metric (kg & cm)":
        # Metric inputs
        weight = st.number_input("Enter your weight (kg):", min_value=30.0, max_value=300.0, value=70.0)
        height = st.number_input("Enter your height (cm):", min_value=100.0, max_value=250.0, value=170.0)
        height_m = height / 100  # Convert cm to m
    else:
        # Imperial inputs
        weight_lbs = st.number_input("Enter your weight (lbs):", min_value=50.0, max_value=700.0, value=150.0)
        height_in = st.number_input("Enter your height (inches):", min_value=36.0, max_value=120.0, value=65.0)
        # Convert to metric for calculation
        weight = weight_lbs * 0.453592
        height_m = height_in * 0.0254

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height_m)
        category = bmi_category(bmi)
        
        st.success(f"Your BMI is: {bmi:.1f}")
        st.info(f"Category: {category}")
        
        # Display BMI chart for reference
        st.subheader("BMI Categories:")
        st.write("- Underweight: BMI < 18.5")
        st.write("- Normal weight: 18.5 ≤ BMI < 25")
        st.write("- Overweight: 25 ≤ BMI < 30")
        st.write("- Obese: BMI ≥ 30")

if __name__ == "__main__":
    main()
