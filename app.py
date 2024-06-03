import plotly.express as px
import streamlit as st 
import pandas as pd 
import numpy as np 
import datetime
from datetime import date
import io
import os
import sys
import matplotlib.pyplot as plt


st.set_page_config(layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""
<style>
.title {
    font-size:25px !important;
    color: #ff6347;
    font-weight: 300px;
}
</style>

""",  unsafe_allow_html=True)



st.image("headline.jpg")
#st.title("DILAGAIN TECHNOLOGIES")
#st.write("""<p class="title"> As from 3rd August 2023</p>""", unsafe_allow_html=True)
st.header("Packaging Materials Inventory")
#st.write(date.today())
st.write("##")




#display dataset
outbound = pd.read_csv('outbound.csv')
inbound = pd.read_csv('inbound.csv')


st.image("./Revenue_analysis/analysis.png")
# st.write("Recent Entries")
# st.write(outbound.tail(1))

#Sidebar

st.sidebar.header("Data Entries")
st.sidebar.write("""<p class='title'>Daily record of Inbound and Outbound</p>""", unsafe_allow_html=True)
#inbound
with st.sidebar.expander('INBOUND'):
    with st.form('entry form1', clear_on_submit=True):
        in_date = st.date_input("Inbounding Date", key='in_date')
        in_GP = st.number_input("G Printers", min_value=0,  step=1, key='in_GP')
        in_CT = st.number_input("Clear Tapes", min_value=0, step=1, key='in_CT')
        in_BT = st.number_input("Branded Tapes", min_value=0, step=1, key='in_BT')
        in_A5 = st.number_input("A5 Envelopes", min_value=0, step=1, key='in_A5')
        in_A4 = st.number_input("A4 Envelopes", min_value=0, step=1, key='in_A4')
        in_CTN_S = st.number_input("Carton Boxes (Small)", min_value=0, step=1, key='in_CTN_S')
        in_CTN_M = st.number_input("Carton Boxes (Medium)", min_value=0, step=1, key='in_CTN_M')
        in_CTN_L = st.number_input("Carton Boxes (Large)", min_value=0, step=1, key='in_CTN_L')
        in_PB_M = st.number_input("Plastic Bags (Medium)", min_value=0, step=1, key='in_PB_M')
        in_KG90 = st.number_input("90KGS Suck", min_value=0, step=1, key='in_KG90')
        in_KG50 = st.number_input("50KGS Suck", min_value=0, step=1, key='in_KG50')
        submitted1 = st.form_submit_button("Save Data")
        if submitted1:
          in_entry = {'Inbounding Date' : in_date, "G Printers" : in_GP, 'Clear Tapes' : in_CT, "Branded Tapes" : in_BT, "A5 Envelopes" : in_A5, "A4 Envelopes":in_A4, 
            "Carton Boxes (Small)":in_CTN_S, "Carton Boxes (Medium)":in_CTN_M, "Carton Boxes (Large)":in_CTN_L, "90KGS Suck":in_KG90,
             "Plastic Bags (Medium)":in_PB_M, "50KGS Suck":in_KG50}
          st.success("Data Saved")
          inbound = pd.concat([inbound, pd.DataFrame(in_entry, index=[0])], ignore_index=True)
          inbound.to_csv("inbound.csv", index=False)
        #outbound
with st.sidebar.expander('OUTBOUND'):
    with st.form('entry form2', clear_on_submit=True):        
        DT = st.date_input("DATE", key='DT')
        GP = st.number_input("G Printers", min_value=0, step=1, key='GP')
        CT = st.number_input("Clear Tapes", min_value=0, step=1, key='CT')
        BT = st.number_input("Branded Tapes", min_value=0, step=1, key='BT')
        A5 = st.number_input("A5 Envelopes", min_value=0, step=1, key='A5')
        A4 = st.number_input("A4 Envelopes", min_value=0, step=1, key='A4')
        CTN_S = st.number_input("Carton Boxes (Small)", min_value=0, step=1, key='CTN_S')
        CTN_M = st.number_input("Carton Boxes (Medium)", min_value=0, step=1, key='CTN_M')
        CTN_L = st.number_input("Carton Boxes (Large)", min_value=0, step=1,key='CTN_L')
        PB_M = st.number_input("Plastic Bags (Medium)", min_value=0, step=1, key='PB_M')
        PB_L = st.number_input("90KGS Suck", min_value=0, step=1, key='PB_L')
        KG50 = st.number_input("50KGS Suck", min_value=0, step=1, key='KG50')
        ODRS = st.number_input("Orders", min_value=0, step=1, key='odrs')
        submitted2 = st.form_submit_button("Save outbound")
        if submitted2:
           out_entry = {'Date' : DT, "G Printers" : GP, 'Clear Tapes' : CT, "Branded Tapes" : BT, "A5 Envelopes" : A5, "A4 Envelopes":A4, 
            "Carton Boxes (Small)":CTN_S, "Carton Boxes (Medium)":CTN_M, "Carton Boxes (Large)":CTN_L, "90KGS Suck":PB_L,
            "Plastic Bags (Medium)":PB_M, "50KGS Suck":KG50, "Orders":ODRS}
           outbound = pd.concat([outbound, pd.DataFrame(out_entry, index=[0])], ignore_index=True)
           outbound.to_csv("outbound.csv", index=False)
           st.success("Outbound Saved")
  

st.write('##') 

#outbound display
# st.write("outbound data")
# st.write(outbound.tail(6))  

st.write('##')


#inbound
check_inbound = st.checkbox("Check Inbound")
if check_inbound:
    st.write(inbound)

#statistical summary
tapes = ((inbound['Clear Tapes'].sum())-(outbound['Clear Tapes'].sum()))
btapes = ((inbound['Branded Tapes'].sum())-(outbound['Branded Tapes'].sum()))
a5 = ((inbound['A5 Envelopes'].sum())-(outbound['A5 Envelopes'].sum()))
a4 = ((inbound['A4 Envelopes'].sum())-(outbound['A4 Envelopes'].sum()))
ctns = ((inbound['Carton Boxes (Small)'].sum())-(outbound['Carton Boxes (Small)'].sum()))
ctnm = ((inbound['Carton Boxes (Medium)'].sum())-(outbound['Carton Boxes (Medium)'].sum()))
ctnl = ((inbound['Carton Boxes (Large)'].sum())-(outbound['Carton Boxes (Large)'].sum()))
pbm = ((inbound['Plastic Bags (Medium)'].sum())-(outbound['Plastic Bags (Medium)'].sum()))
pbl = ((inbound['90KGS Suck'].sum())-(outbound['90KGS Suck'].sum()))
gp = ((inbound['G Printers'].sum())-(outbound['G Printers'].sum()))
s50 = ((inbound['50KGS Suck'].sum())-(outbound['50KGS Suck'].sum()))


#import datasets
nov_out = pd.read_csv("November_outbound.csv")
col1, col2 = st.columns(2)
with col1:
    
    #highlights
    st.subheader("Available Materials:-")
    st.markdown(f"(i)  :blue[**G Printers**] :  {gp}")
    st.markdown(f"(i)  :blue[**Clear Tapes**] :  {tapes}")
    st.markdown(f"(ii)  :blue[**Branded Tapes**] :  {btapes}")
    st.markdown(f"(iii)  :green[**A5 Envelopes**] :  {a5}")
    st.markdown(f"(iv)  :green[**A4 Envelopes**] :  {a4}")
    st.markdown(f"(v)  :red[**Cartons Small-size**] :  {ctns}")
    st.markdown(f"(vi)  :red[**Cartons Medium-size**] :  {ctnm}")
    st.markdown(f"(vii)  :red[**Cartons Large-size**] :  {ctnl}")
    st.markdown(f"(viii) :violet[**Plastic Bags Medium-size**] :  {pbm}")
    st.markdown(f"(ix) :violet[**90KGS Sucks**] :  {pbl}")
    st.markdown(f"(i)  :violet[**50KGS Sucks**] :  {s50}")

with col2:

    pie_out = outbound.drop('Date', axis=1)
    pie_out1 = pie_out.sum().reset_index(name='total')
    #plotting the pie chart for materials used.
   

    fig = px.pie(pie_out1, values='total', names='index', title='Materials used')

    st.plotly_chart(fig)



st.subheader("Material consumption for previous months")
st.write('---')


col1, col2 = st.columns(2)
with col1:
    st.write("Last Month**2")
    oct_out = pd.read_csv("october_outbound.csv")
    plt.figure(figsize=(12,5))


    plt.plot(oct_out['Date'], oct_out['Clear Tapes'], color='red', linestyle='-', marker='o', label='Clear tapes')
    plt.plot(oct_out['Date'], oct_out['A5 Envelopes'], color='blue', linestyle='-.', marker='s', label='A5 Envelopes')
    plt.plot(oct_out['Date'], oct_out['A4 Envelopes'], color='green', linestyle='-', marker='o', label='A4 Envelopes')
    plt.plot(oct_out['Date'], oct_out['Plastic Bags (Large)'], color='violet', linestyle='-', marker='o', label='Plastic Bags (Large)')
    plt.plot(oct_out['Date'], oct_out['Carton Boxes (Small)'], color='maroon', linestyle='-', marker='o', label='Carton Boxes (Small)')
    plt.plot(oct_out['Date'], oct_out['Carton Boxes (Large)'], color='black', linestyle='-', marker='o', label='Carton Boxes (Large)')

    #plt.rcParams['figure.facecolor'] = 'lightblue'
    plt.grid()
    plt.xticks(rotation=90)
    plt.legend()

    st.pyplot(plt)


with col2:

    st.write("Last Month")
    nov_out = pd.read_csv("November_outbound.csv")
    plt.figure(figsize=(12,5))


    plt.plot(nov_out['Date'], nov_out['Clear Tapes'], color='red', linestyle='-', marker='o', label='Clear tapes')
    plt.plot(nov_out['Date'], nov_out['A5 Envelopes'], color='blue', linestyle='-.', marker='s', label='A5 Envelopes')
    plt.plot(nov_out['Date'], nov_out['A4 Envelopes'], color='green', linestyle='-', marker='o', label='A4 Envelopes')
    plt.plot(nov_out['Date'], nov_out['Plastic Bags (Large)'], color='violet', linestyle='-', marker='o', label='Plastic Bags (Large)')
    plt.plot(nov_out['Date'], nov_out['Carton Boxes (Small)'], color='maroon', linestyle='-', marker='o', label='Carton Boxes (Small)')
    plt.plot(nov_out['Date'], nov_out['Carton Boxes (Large)'], color='black', linestyle='-', marker='o', label='Carton Boxes (Large)')




    plt.grid()
    plt.xticks(rotation=90)
    plt.legend()

    st.pyplot(plt)

st.write('##')

st.subheader("Current Month Packaging material Usage")
st.write('##')
import matplotlib.pyplot as plt
import pandas as pd

cols_maps = {'Date':'date', 'G Printers':'g_printers', 'Clear Tapes':'clear_tapes', 'Branded Tapes':'branded_tapes', 'A5 Envelopes':'A5_envelopes',
       'A4 Envelopes':'A4_envelopes', 'Carton Boxes (Small)':'carton_boxes_(small)', 'Carton Boxes (Medium)':'carton_boxes_(medium)',
       'Carton Boxes (Large)':'carton_boxes_(large)', 'Plastic Bags (Medium)':'Plastic_Bags_Medium', '90KGS Suck':'Plastic_Bags_(large)',
       '50KGS Suck':'50KGS_Suck'}
voutbound = outbound.rename(columns=cols_maps)
# Assuming you have a DataFrame named 'outbound' with the desired columns

# Create a figure and axis
fig, ax = plt.subplots(figsize=(15, 7))

# Define the width of each bar
bar_width = 0.15  # Adjust the bar width as needed

# Create x-values for the bars for the first set of data
x1 = range(len(voutbound.date))

# Create x-values for each set of bars
x2_A5 = [x + bar_width for x in x1]
x2_A4 = [x + 2 * bar_width for x in x1]
x2_Clear_Tapes = [x + 3 * bar_width for x in x1]
x2_Plastic_Bags = [x + 4 * bar_width for x in x1]
x2_50KGS_Suck = [x + 5 * bar_width for x in x1]
x2_Carton_Boxes_Medium = [x + 6 * bar_width for x in x1]

# Plot the first set of bars
ax.bar(x1, voutbound.A5_envelopes, width=bar_width, label='A5 Envelopes')

# Plot the second set of bars
ax.bar(x2_A4, voutbound.A4_envelopes, width=bar_width, label='A4 Envelopes')

# Plot the third set of bars
ax.bar(x2_Clear_Tapes, voutbound.clear_tapes, width=bar_width, label='Clear Tapes')

# Plot the fourth set of bars
ax.bar(x2_Plastic_Bags, voutbound.Plastic_Bags_Medium, width=bar_width, label='Plastic Bags Medium')

# Plot the fifth set of bars
ax.bar(x2_50KGS_Suck, voutbound['50KGS_Suck'], width=bar_width, label='50KGS Suck')

# Plot the sixth set of bars
ax.bar(x2_Carton_Boxes_Medium, voutbound['carton_boxes_(medium)'], width=bar_width, label='Carton Boxes Medium')

# Set the x-axis labels to be the dates
ax.set_xticks([x + 3 * bar_width for x in x1])
ax.set_xticklabels(voutbound.date, rotation=45, ha='right')

# Add a legend
ax.legend()
ax.set_facecolor('black')
# Set labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Quantity')
ax.set_title('Multiple Products Over Time')
plt.grid()
# Show the plot
st.pyplot(fig)


#preparation for dataset download
#inbound
csv_buffer_in = io.StringIO()
inbound.to_csv(csv_buffer_in, index=False)
csv_data_in = csv_buffer_in.getvalue()
#outbound
csv_buffer_out = io.StringIO()
outbound.to_csv(csv_buffer_out, index=False)
csv_data_out = csv_buffer_out.getvalue()
last_month_orders = st.checkbox("Last Month Orders")
if last_month_orders:
    try:
        st.image("./Revenue_analysis/previous_month_orders.png")
    except:
        st.text("The Visualiation is unavailable at the moment")

    
review = st.checkbox("Order rate")
if review:

    try:

        st.subheader("Work done rate")
        fig1, ax = plt.subplots(figsize=(12,5))

        ax.plot(outbound.Date, outbound.Orders, c="Red")
        ax.set_facecolor('gray')
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
        ax.grid()
        st.pyplot(fig1)
    except:
        print("Working progress, review later")    

st.write("##")
# download option
# inbound dataset
st.text("To Download the Inbound Dataset")
download = st.checkbox("Download", key="download2")   
if download:
    st.text('key-in the passcode')
    passcode = st.text_input("Passcode1")
    if passcode == '114986bn':
        st.download_button(
             label="Download CSV",
           data=csv_data_in,
               file_name="inbound_data.csv",
                 mime="text/csv"
                )
    elif passcode != '114986bn':    
        st.markdown(":red[**Input Valid Passcode**]")    


# outbound dataset
st.text("To Download the Outbound Dataset")
download = st.checkbox("Download", key="download1")   
if download:
    st.text('key-in the passcode2')
    passcode2 = st.text_input("Passcode")
    if passcode2 == '114986bn':
        st.download_button(
             label="Download CSV",
           data=csv_data_out,
               file_name="outbound_data.csv",
                 mime="text/csv"
                )        
    elif passcode2 != '114986bn':
        st.markdown(":red[**Input Valid Passcode**]")    



# Monetary Calculation
m_tapes = ((outbound['Clear Tapes'].sum())*99)
m_btapes = ((outbound['Branded Tapes'].sum())*220)
m_a5 = ((outbound['A5 Envelopes'].sum())*3)
m_a4 = ((outbound['A4 Envelopes'].sum())*4)
m_ctns = ((outbound['Carton Boxes (Small)'].sum())*20)
m_ctnm = ((outbound['Carton Boxes (Medium)'].sum())*40)
m_ctnl = ((outbound['Carton Boxes (Large)'].sum())*72)
m_pbm = ((outbound['Plastic Bags (Medium)'].sum())*13)
m_pbl = ((outbound['90KGS Suck'].sum())*21)
m_s50 = ((outbound['50KGS Suck'].sum())*25)



#Total sales button
st.text('Total Sales')
total_sales = st.checkbox("Show", key="total_sales")   
if total_sales:
    passcode3 = st.text_input("Passcode3")
    if passcode3 == '114986bn':
       total_sales = (m_tapes+m_btapes+m_a4+m_a5+m_ctns+m_ctnm+m_ctnl+m_pbm+m_pbl+m_s50)
       st.write(total_sales)
    elif passcode3 != '114986bn':
        st.markdown(":red[**Input Valid Passcode**]")    
