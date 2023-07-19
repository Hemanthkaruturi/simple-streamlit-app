import streamlit as st
import pandas as pd
import numpy as np
import time

df = pd.DataFrame({'First column':[1,2,3,4,5], 'Second column':[10,23,23,56,23]})

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

# Below are the filters/Widgets
# x = st.slider('x')
x = st.sidebar.slider('This is a slider')
st.write(x,'Squared is',x*x)

# input text
# st.text_input("Enter your name", key="name")
st.sidebar.text_input("Enter your name",key="name")
if st.sidebar.checkbox('Show name'):
    st.write("Hello ",st.session_state.name,"!")

# check box
if st.sidebar.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

# select box
option = st.sidebar.selectbox("Select the below",['Apple','Banana','Orange'])
st.write("You have selected ", option)

# multi select box
multi_option = st.sidebar.multiselect("Select the below",['Apple','Banana','Orange'])
st.write("You have selected ", multi_option)

# Below are the chart visuals
st.write("Below is a DataFrame")
# st.write(df)

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

left_column, right_column = st.columns(2)

# one way
left_column.table(df)
right_column.line_chart(chart_data)

# second way
# with left_column:
#     st.table(df)

# with right_column:
#     st.line_chart(chart_data)

st.map(map_data)





# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# left_column.button('Press me!')

# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")

'Starting a long computation...'
