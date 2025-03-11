

# cd "C:\Users\muhammad faiz\OneDrive\Desktop\work\python"
# New-Item Converter.py
# streamlit run Converter.py

# Streamlit is a Python library that helps make web apps easily 🚀.
# import streamlit as st means we are calling Streamlit with st for short.
import streamlit as st

# Meters → Feet
# Kilograms → Pounds
# Celsius → Fahrenheit

# (Title and layout)
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")
# ⚠️ This MUST be the first Streamlit command! If not, Streamlit gets angry 😡 and gives an error.
# # window+. for emojis

# Large heading using # at the start
st.markdown("# Welcome to the Unit Converter 🚀")  

# Normal text on the page.
st.write("This assignment was created by **Armish Ameen**")

# Markdown allows us to add headings, bold text, lists, and more without writing complex HTML or CSS.
st.markdown("**Effortlessly convert length, weight, and temperature in an instant! 😎👁️‍🗨️**")  
st.markdown("- Easy to use\n- Fast and accurate\n- Supports multiple units")  # Bullet points with \n for line breaks

# Custom styling using Markdown (CSS)
st.markdown("""
    <style>
        body {
            background-color: #f8f9fa;
        }
        .stSelectbox, .stNumberInput {
            border-radius: 10px;
            border: 1px solid #ddd;
            padding: 8px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 10px;
            border: none;
            transition: 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stSuccess {
            font-weight: bold;
            color: green;
        }
        .stWarning {
            font-weight: bold;
            color: red;
        }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.title("🔄 Amazing Unit Converter")

# Dropdown for selecting conversion type
conversion_type = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature","Time"])
# st.selectbox(...) creates a dropdown menu 📜.
# The user can choose between Length, Weight, or Temperature.

# Select specific conversion based on type
if conversion_type == "Length":
    unit_conversion = st.selectbox("Select Unit Conversion", [
        "Miles to Kilometers", "Kilometers to Miles", 
        "Meters to Feet", "Feet to Meters"
    ])
elif conversion_type == "Weight":
    unit_conversion = st.selectbox("Select Unit Conversion", [
        "Kilograms to Pounds", "Pounds to Kilograms"
    ])
elif conversion_type == "Temperature":
    unit_conversion = st.selectbox("Select Unit Conversion", [
        "Celsius to Fahrenheit", "Fahrenheit to Celsius"
    ])
elif conversion_type == "Time":  
    unit_conversion = st.selectbox("Select Unit Conversion", [
        "Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", 
        "Hours to Minutes", "Hours to Days", "Days to Hours"
    ])

# The Brain 🧠 of the code (Conversion Function)
# Conversion Logic
# `value` is the number the user enters to convert.
# `conversion_type` indicates the type of conversion (Length, Weight, or Temperature).
def convert_units(value, conversion_type, unit_conversion):
    # We write `f` before a string in Python to create an f-string (formatted string literal).
    # f-strings allow us to insert variables directly without using concatenation (+) or `format()`.

    if conversion_type == "Length":
        if unit_conversion == "Kilometers to Miles":
            return f"{value:.2f} km = {value * 0.621371:.2f} miles"
        elif unit_conversion == "Miles to Kilometers":
            return f"{value:.2f} miles = {value / 0.621371:.2f} km"
        elif unit_conversion == "Meters to Feet":
            return f"{value:.2f} meters = {value * 3.281:.2f} feet"
        elif unit_conversion == "Feet to Meters":
            return f"{value:.2f} feet = {value / 3.281:.2f} meters"

    elif conversion_type == "Weight":
        if unit_conversion == "Kilograms to Pounds":
            return f"{value:.2f} kg = {value * 2.205:.2f} pounds"
        elif unit_conversion == "Pounds to Kilograms":
            return f"{value:.2f} pounds = {value / 2.205:.2f} kg"

    elif conversion_type == "Temperature":
        if unit_conversion == "Celsius to Fahrenheit":
            fahrenheit = (value * 9/5) + 32
            return f"{value:.2f}°C = {fahrenheit:.2f}°F"
        elif unit_conversion == "Fahrenheit to Celsius":
            celsius = (value - 32) * 5/9
            return f"{value:.2f}°F = {celsius:.2f}°C"
        
    elif conversion_type == "Time":
        if unit_conversion == "Seconds to Minutes":
            return f"{value:.2f} sec = {value / 60:.2f} min"
        elif unit_conversion == "Minutes to Seconds":
            return f"{value:.2f} min = {value * 60:.2f} sec"
        elif unit_conversion == "Minutes to Hours":
            return f"{value:.2f} min = {value / 60:.2f} hours"
        elif unit_conversion == "Hours to Minutes":
            return f"{value:.2f} hours = {value * 60:.2f} min"
        elif unit_conversion == "Hours to Days":
            return f"{value:.2f} hours = {value / 24:.2f} days"
        elif unit_conversion == "Days to Hours":
            return f"{value:.2f} days = {value * 24:.2f} hours"


# Input box for value entry
# If the user enters 5, the input will be displayed as 5.00 because of the "%.2f" format.
value = st.number_input("Please enter the Value", min_value=0.0, format="%.2f")

# Convert Button
if st.button("Convert"):
    # When the user clicks this button, the code inside the if block will execute.
    if value == 0:
        st.warning("Please enter a value greater than zero.")
    else:
        result = convert_units(value, conversion_type, unit_conversion)
        # Calls the convert_units function, passing:
        # 1. value (the user-inputted number).
        # 2. conversion_type (the unit type selected by the user).
        # 3. unit_conversion (specific unit conversion selected by the user).
        # The function returns a formatted conversion result, which is stored in `result`.
        
        st.success(result)  # Displays the result inside a green success message box.
        # This makes it clear to the user that the conversion was successful.
