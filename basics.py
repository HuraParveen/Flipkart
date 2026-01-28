import streamlit as st 
from datetime import datetime, date , time
import pandas as pd
import numpy as np
st.title("Welcome to streamlit deploymenent")
st.header("Deployed by Shaik Hura Parveen")
st.subheader("Hi my name is Parveen . Welcome to streamlit")
st.text("This is my first streamlit deployment project")
st.markdown("This is my **linkedin account** : [www.linkedin.com/in/shaik-hura-parveen] .. here you can *connect* with me")
st.caption("Thank you for visiting my page")


st.header("The below code is a basic python code")
st.code("""
def hello_world():
        print("Hello World")
        return "Welcome to Streamlit"
""",language="python")


st.header("The below code is a SQL Code")
st.code("select * from users where age > 18",language="SQL")


st.header("The below code is a Json data")
st.code({"Name":"parveen","Occupation":"Data Scientist"})


data=pd.DataFrame({
    'Column_A':[1,2,3,4,5],
    'Column_B':['A','B','C','D','E'],
    'Column_C':['apple','banana','mango','grape','orange'],
    'Column_D':[True,False,True,False,True]

})

st.header("Basic Dataframe")
df=st.dataframe(data)
print(df)

st.header("edited Dataframe")

edited_df=st.data_editor(data)
print(edited_df)

st.header("Static Table")
static_table=st.table(data)
print(static_table)


st.header("Creating Visualizations")
data=pd.DataFrame(np.random.randn(20,3),columns=['A','B','C'])
df1=st.dataframe(data)
print(df1)


st.header("Area Chart")
st.area_chart(data)

st.header("Bar Chart")
st.bar_chart(data)

st.header("Line Chart")
st.line_chart(data)

df2=pd.DataFrame({"X":np.random.randn(100),
                     "Y":np.random.randn(100)})
df2=st.dataframe(data)
print(df2)

st.header("Scatter chart")

st.scatter_chart(data)

# Widgets => important for ML
st.header("Button")
if st.button("Click Me"):
    st.write("Thank you for clicking me")

st.header("Check box")
agree=st.checkbox("I agree to the terms and conditions")
if agree:
    st.write("Thank you for agreeing")
else:
    st.write("Click on agree to move forward")


st.header("Radio Button")
genre=st.radio("Select your favourite genre",('Comedy','Drama','Documentary'))

st.write(f"My favourite genre is {genre}")

st.header("Select Box")
language=st.selectbox("Select your favourite programming language",['Python','R','Java','C++','Javascript'])
st.write(f"My favourite programming language is {language}")


st.header("Multi Select Boxes")
language=st.multiselect("Select your favourite programming language",['Python','R','Java','C++','Javascript'])
st.write(f"My favourite programming languages are {language}")


st.header(" select Slider")
review=st.select_slider("Movie Rating",
                        ["worst","bad","average","good","excellent"])
st.write(f"Movie Ratings : {review}")


st.header("Slider")
height=st.slider("my height is cms ",min_value=0,max_value=500)
st.write(f"My height is {height} cms")


st.header("Text Input")
name= st.text_input("What is your name")
st.write(f"My name is {name}")


st.header("Text Area")
feedback=st.text_area("Provide your feedback")   
st.write(f"My feedback is {feedback}")     


st.header("Number Input")
age=st.number_input("What is your age",min_value=0,max_value=150,step=1)   
st.write(f"My age is {age}")


st.header("Date ")
dob=st.date_input("What is your date of birth",min_value=datetime(1990,1,1),max_value=datetime(2026,1,31))
st.write(f"My date of birth is : {dob}")

