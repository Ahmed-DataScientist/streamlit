import streamlit as st
import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Usman', 'Ali', 'Sara', 'Zara'],
    'Age': [25, 30, 22, 28]
}

df = pd.DataFrame(data)

# Display the table
st.title('Simple Table and Line Chart')

st.write("### Table:")
st.write(df)

# Display the line chart
st.write("### Line Chart:")
st.line_chart(df.set_index('Name'))


# Set page configuration at the very top

# App Title

# Upload File
uploaded_file = st.file_uploader("Choose an image file", type=['jpg', 'jpeg', 'png'])
    # Open the image
st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    
    # Display the image

