import streamlit as st
import pandas as pd

@st.cache_data      # decorator to specify special functions - whenever user loads the csv, it will store in the memory - whenever it is run again, it can access the data through the memory
def load_csv(file_obj):
    return pd.read_csv(file_obj)

st.title('CSV Quick Plotter')

uploaded_file = st.sidebar.file_uploader("Upload your CSV", type=['csv']) # can shift anything easily to the sidebar through .sidebar

# if user reuploads the file, just use the one saved in the session
if 'df' not in st.session_state:
    st.session_state.df = None
if 'data_source_name' not in st.session_state:
    st.session_state.data_source_name = None

# if the file was not previously uploaded (check from session), save the file
if uploaded_file is not None: 
    if st.session_state.data_source_name != uploaded_file.name:
        st.session_state.df = load_csv(uploaded_file)
        st.session_state.data_source_name = uploaded_file.name
    df = st.session_state.df
    st.sidebar.success(f"{uploaded_file.name} uploaded successfully")
else:
    df = st.session_state.df

# check whether any csv was uploaded, if uploaded, display a visualisation using only variables that are numeric
if df is not None:
    st.header("Data Preview")
    st.dataframe(df)
    st.header("Create a plot")
    columns = df.columns.tolist()
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist() # select data types that includes number

    if not numeric_columns:
        st.warning("No numeric columns in this data for plotting the y-axis")
    else:
        col1, col2 = st.columns(2)
    with col1:
        x_axis = st.selectbox("Select x-axis:", columns)
    with col2:
        y_axis = st.selectbox("Select y-axis:", numeric_columns)
    plot_type = st.radio("Select plot type:", ("Bar Chart", "Line Chart"), horizontal=True)


    if x_axis and y_axis:
        st.subheader(f"{plot_type} of {x_axis} and {y_axis}")
        if plot_type == "Bar Chart":
            st.bar_chart(df, x=x_axis, y=y_axis)
            # if df[x_axis].dtype == 'object' and df[x_axis].nunique() < 20:
            #     st.bar_chart(df.groupby(x_axis)[y_axis].mean())
        else:
            st.line_chart(df, x=x_axis, y=y_axis)

        with st.expander("view data summary"):
            st.write("**Shape:**", df.shape)
            st.write("**Columns:**", df.columns.tolist())
            st.write("**Data Types**")
            st.dataframe(df.describe(include='all'))

else:
    st.info("Upload a csv file to get started")

# if df:
#     st.scatter_chart(df[['Age', 'Salary']])