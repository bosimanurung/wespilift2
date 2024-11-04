import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

muserlogin = pd.read_csv('MUserLogin.csv')

st.title("Sign In")
_user_id = 0
_username = _password1 = _password = _aktif = ''
while _user_id==0:
    _username = st.text_input("Login Username:", key=None, placeholder=None)
    _password = st.text_input("Password:")
    
    if st.button("Next"): 
        mycalc_temp = muserlogin.loc[muserlogin['username']==_username].reset_index(drop=True)
        #st.dataframe(mycalc_temp, hide_index=True)
        if mycalc_temp is not [[]]:
            #st.dataframe(mycalc_temp, hide_index=True)
            _user_id = mycalc_temp['user_id'].values[0]
            _password1 = mycalc_temp['password'].values[0]
            _aktif = mycalc_temp['aktif_or_not'].values[0]
            if _password==_password1:
                if _aktif=='aktif':
                    break
                else:
                    st.write('User tidak aktif!')
                    _user_id = 0
            else:    
                st.write('Password salah!')
                _user_id = 0                
        else:
            st.write('Username tersebut tidak ada!')
            _user_id = 0
            
    else:
        st.write('')

#while _password == '':
#    _password = st.text_input("Password:")

#    if st.button("Next"): 
#        if _passwrod==_password1 and _aktif=='aktif':
#            break
#        else:
#            st.write('Password salah!')
#            _password = ''

if _user_id>0 and _aktif=='aktif':
    st.sidebar.text('Powered by: ')
    #image = Image.open('logo_wespi.png')
    #st.sidebar.image(image)
    st.sidebar.image('logo_wespi.png')
    
    # -- page setup --
    my_calculations = st.Page(
        #page = "views/my_calc.py",
        page = "my_calc.py",
        title = "My Calculations",
        icon = ":material/account_circle:",
        default = True,
    )
    new_calculations = st.Page(
        #page = "views/data_input.py",
        page = "new_calc.py",
        title = "Add New Calculation",
        icon = ":material/bar_chart:",
    )
    #ipr_curve = st.Page(
    #    #page = "views/ipr_curve.py",
    #    page = "ipr_curve.py",
    #    title = "Calculation & IPR Curve",
    #    icon = ":material/bar_chart:",
    #)
    
    # --- navigation setup (without sections) ---
    #pg = st.navigation(pages=[my_calculations, new_calculations, ipr_curve])
    pg = st.navigation(pages=[my_calculations, new_calculations])
    
    # --- run navigation ---
    pg.run()
