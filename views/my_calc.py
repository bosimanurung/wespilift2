import streamlit as st
import pandas as pd
import pandasql as ps
import math

#@st.dialog("ID Calculation")
#def show_id_form():
#    st.text_input("ID Calculation")

st.title("My Calculations")

#open datas
mycalc = pd.read_csv('data/mycalc.csv')
muserlogin = pd.read_csv('data/MUserLogin.csv')
minstrument = pd.read_csv('data/MInstrument.csv')
mcalcmethod = pd.read_csv('data/MCalcMethod.csv')
mwelltype = pd.read_csv('data/MWellType.csv')
mmeasurement = pd.read_csv('data/MMeasurement.csv')
mcasingsize = pd.read_csv('data/MCasingSize.csv')
mcasingid = pd.read_csv('data/MCasingID.csv')
mtubingsize = pd.read_csv('data/MTubingSize.csv')
mtubingid = pd.read_csv('data/MTubingID.csv')
mtubingcoeff = pd.read_csv('data/MTubingCoeff.csv')
#ipr_data = pd.read_csv('data/ipr_data.csv')

mycalc3 = ps.sqldf("select m.user_id, u.username, m.well_name, m.field_name, m.company, m.engineer, \
        m.date_calc, m.id_instrument, i.instrument, m.id_calc_method, c.calc_method, m.id_welltype, \
        w.welltype, m.id_measurement, meas.measurement, m.comment_or_info, m.top_perfo_tvd, m.top_perfo_md, \
        m.bottom_perfo_tvd, m.bottom_perfo_md, m.qtest, m.sbhp, m.fbhp, m.producing_gor, m.wc, m.bht, \
        m.sgw, m.sgg, m.qdes, m.psd, m.whp, m.psd_md, m.p_casing, m.pb, m.api, m.sgo, \
        s.casing_size, casid.casing_id, tubsize.tubing_size, tubid.tubing_id, \
        tubcoef.type, tubcoef.coefficient, \
        m.liner_id, m.top_liner_at, m.bottom_liner_at \
        from mycalc m \
            left join muserlogin u on m.user_id = u.user_id \
            left join minstrument i on m.id_instrument = i.id_instrument \
            left join mcalcmethod c on m.id_calc_method = c.id_calc_method \
            left join mmeasurement meas on m.id_measurement = meas.id_measurement \
            left join mwelltype w on m.id_welltype = w.id_welltype \
            left join mcasingsize s on m.id_casing_size = s.id_casing_size \
            left join mcasingid casid on m.id_casing_id = casid.id_casing_id \
            left join mtubingsize tubsize on m.id_tubing_size = tubsize.id_tubing_size \
            left join mtubingid tubid on m.id_tubing_id = tubid.id_tubing_id \
            left join mtubingcoeff tubcoef on m.id_tubing_coeff = tubcoef.id_tubing_coeff") 

st.dataframe(mycalc3, hide_index=True)

wellname=id_calc_01=""
col1, col2 = st.columns(2, gap="medium", vertical_alignment="top")
with col1:
    st.markdown("<p style='text-align: justify;'>Masukkan Well Name untuk melihat detail informasi \
        perhitungan yang sudah dibuat. Diantaranya adalah Well Name, Field Name, Created by, Company, \
        dan lain-lain.</p>", unsafe_allow_html=True)
        #Engineer, Date Input, dan lain-lain.</p>", unsafe_allow_html=True)
#        Diantaranya adalah Well Name, Field Name, Created by, Company, Engineer, Date Input, Instrument, Calculation Method, \
#        Well Type, Unit Measurement, dan lain-lain.</p>", unsafe_allow_html=True)

with col2:
    wellname = st.text_input("Well Name To Explore:")
     
if wellname:
    mycalc4 = mycalc3.loc[mycalc3['well_name']==wellname].reset_index(drop=True)
    #mycalc4b = pd.DataFrame(mycalc4)]

    _username = mycalc4['username'].values[0]; _well_name = mycalc4['well_name'].values[0]
    _field_name=mycalc4['field_name'].values[0]; _company=mycalc['company'].values[0]; _engineer=mycalc4['engineer'].values[0]
    _date_calc=mycalc4['date_calc'].values[0]; _instrument=mycalc4['instrument'].values[0]
    _calc_method=mycalc4['calc_method'].values[0]; _welltype=mycalc4['welltype'].values[0]
    _measurement=mycalc4['measurement'].values[0]; _comment_or_info=mycalc4['comment_or_info'].values[0]
    st.title("General Information")
    col1, col2 = st.columns(2, gap="medium", vertical_alignment="top")
    with col1:
        st.subheader('Well Name:')
        st.write(_well_name)
        #st.write('\n')
        st.subheader('Field Name:')
        st.markdown(_field_name)
        #st.write('\n')
        st.subheader('Company:')
        st.markdown(_company)
        #st.write('\n')
        st.subheader('User Name:')
        st.markdown(_username)
        #st.write('\n')
        st.subheader('Engineer:')
        st.markdown(_engineer)
        #st.write('\n')
        st.subheader('Date Calculation:')
        st.markdown(_date_calc)
        #st.write('\n')
    with col2:
        st.subheader('Instrument:')
        st.markdown(_instrument)
        #st.write('\n')
        st.subheader('Calculation Method:')
        st.markdown(_calc_method)
        #st.write('\n')
        st.subheader('Well Type:')
        st.markdown(_welltype)
        #st.write('\n')
        st.subheader('Measurement:')
        st.markdown(_measurement)
        #st.write('\n')
        st.subheader('Comment or Info:')
        st.markdown(_comment_or_info)
        #st.write('\n')

    _top_perfo_tvd=mycalc4['top_perfo_tvd'].values[0]; _top_perfo_md=mycalc4['top_perfo_md'].values[0]
    _bottom_perfo_tvd=mycalc4['bottom_perfo_tvd'].values[0]; _bottom_perfo_md=mycalc4['bottom_perfo_md'].values[0]
    _qtest=mycalc4['qtest'].values[0]; _sbhp=mycalc4['sbhp'].values[0]; _fbhp=mycalc4['fbhp'].values[0]
    _producing_gor=mycalc4['producing_gor'].values[0]; _wc=mycalc4['wc'].values[0]; _bht=mycalc4['bht'].values[0]
    _sgw=mycalc4['sgw'].values[0]; _sgg=mycalc4['sgg'].values[0]; _qdes=mycalc4['qdes'].values[0]
    _psd=mycalc4['psd'].values[0]; _whp=mycalc4['whp'].values[0]; _psd_md=mycalc4['psd_md'].values[0]
    
    _p_casing=mycalc4['p_casing'].values[0]; _pb=mycalc4['pb'].values[0]    
    _api=mycalc4['api'].values[0]; _sgo=mycalc4['sgo'].values[0]

    _casing_size=mycalc4['casing_size'].values[0]; _casing_id=mycalc4['casing_id'].values[0]
    _tubing_size=mycalc4['tubing_size'].values[0]; _tubing_id=mycalc4['tubing_id'].values[0]
    _tubing_coeff_type=mycalc4['type'].values[0]
    _coefficient=mycalc4['coefficient'].values[0]

    _liner_id=mycalc4['liner_id'].values[0]; _top_liner_at=mycalc4['top_liner_at'].values[0]
    _bottom_liner_at=mycalc4['bottom_liner_at'].values[0]
    st.write('\n')
    st.title("Data Input")
    col1, col2 = st.columns(2, gap="medium", vertical_alignment="top")
    with col1:
        st.header("Basic Data (Required)", divider="gray")
        st.write('Top Perfo    : ', _top_perfo_tvd, _measurement, 'TVD')
        st.write('Top Perfo    : ', _top_perfo_md, _measurement, 'MD')
        st.write('Bottom Perfo : ', _bottom_perfo_tvd, _measurement, 'TVD')
        st.write('Bottom Perfo : ', _bottom_perfo_md, _measurement, 'MD')
        st.write('Qtest        : ', _qtest, 'BPD')
        st.write('SBHP         : ', _sbhp, 'psig')
        st.write('FBHP         : ', _fbhp, 'psig')
        st.write('Producing GOR: ', _producing_gor, 'scf/stb')
        st.write('WC           : ', _wc, '%')
        st.write('BHT          : ', _bht, '℉')
        st.write('SGw          : ', _sgw)
        st.write('SGg          : ', _sgg)
        st.write('Qdes         : ', _qdes, 'BPD')
        st.write('PSD          : ', _psd, _measurement, 'TVD')
        st.write('WHP          : ', _whp, 'psi')
        st.write('PSD (MD)     : ', _psd_md, _measurement, 'MD')
        st.header("Basic Data (Optional)", divider="gray")
        st.write('P. Casing    : ', _p_casing, 'psi')
        st.write('Pb           : ', _pb, 'psig')
    with col2:        
        st.header("API/Sgo", divider="gray")
        st.write('API          : ', _api)
        st.write('Sgo          : ', _sgo)
        st.write('\n')
        st.header("Casing & Tubing", divider="gray")
        st.write('Casing Size  : ', _casing_size)
        st.write('Casing ID    : ', _casing_id, 'inch')
        st.write('Tubing Size  : ', _tubing_size)
        st.write('Tubing ID     : ', _tubing_id, 'inch')
        st.write('Tubing Coeffisien: ', _tubing_coeff_type)
        st.write('\n')
        st.header("Liner", divider="gray")
        st.write('Liner ID     : ', _liner_id, 'inch')
        st.write('Top Liner at : ', _top_liner_at, _measurement, 'TVD')
        st.write('Bottom Liner at: ', _bottom_liner_at, _measurement, 'MD')

    #Hitung2an Calculation sblm IPR Curve
    _qmax = _qtest / (1 - 0.2 * (_fbhp/_sbhp) - 0.8 * (_fbhp/_sbhp) ** 2)
    _Pwf_at_Qdes = (5 * math.sqrt(3.24 - 3.2 * (_qdes/_qmax)) - 1) / 8 * _sbhp

    # Vt=Vo+Vg+Vw; Vo=(1-WC)*Qdes*Bo; Vg=Bg * Free Gas (FG); Vw=WC * Qdes
    # Bo=0.972+0.000147*((Rs*SQRT(SGg/Sgo)+1.25*BHT)^1.175); 
    # Rs=Sgg*(( (PIP/18) * (10^(0.0125*API – 0.00091*BHT)) ) ^1.2048)
    # PIP=Pwf@Qdes-(MidPerf-PSD)*SGFluid/2.31
    # MidPerf = 0.5(TopPerfoTVD+BottomPerfoTVD)
    # SGFluid = WC * SGw + (1 - WC) * Sgo
    
    # Bg=5.04*0.85*(BHT+460)/(PIP+14.7)   
    # Tg=(1-WC)*Qdes*ProducingGOR/1000;
    # Sg=(1-WC)*Qdes*Rs/1000
    # Free Gas (FG) = Tg - Sg; 

    # MidPerf = 0.5(TopPerfoTVD+BottomPerfoTVD)
    _MidPerf = 0.5 * (_top_perfo_tvd + _bottom_perfo_tvd)
    # SGFluid = WC * SGw + (1 - WC) * Sgo
    _sgfluid = (_wc/100) * _sgw + (1-(_wc/100) * _sgo)
    # PIP=Pwf@Qdes-(MidPerf-PSD)*SGFluid/2.31
    _pip = _Pwf_at_Qdes - (_MidPerf - _psd) * _sgfluid/2.32 
    # Rs=Sgg*(( (PIP/18) * (10^(0.0125*API – 0.00091*BHT)) ) ^1.2048)
    _Rs=_sgg*(( (_pip/18) * (10**(0.0125*_api - 0.00091*_bht)) ) **1.2048)

    # Bo=0.972+0.000147*((Rs*SQRT(SGg/Sgo)+1.25*BHT)^1.175); 
    _Bo = 0.972+0.000147*((_Rs*math.sqrt(_sgg/_sgo)+1.25*_bht)**1.175)
    # Vo=(1-WC)*Qdes*Bo;
    _Vo = (1-(_wc/100))*_qdes*_Bo;

    # Bg=5.04*0.85*(BHT+460)/(PIP+14.7) -> yg benar kurung nya sprti di bawah
    _Bg=5.04*0.85*((_bht+460)/(_pip+14.7))
    # Tg=(1-WC)*Qdes*ProducingGOR/1000;
    _Tg=(1-(_wc/100))*_qdes*_producing_gor/1000
    #Sg=(1-WC)*Qdes*Rs/1000
    _Sg=(1-(_wc/100))*_qdes*_Rs/1000
    # Free Gas (FG) = Tg - Sg;
    _free_gas = _Tg - _Sg
    # Vg=Bg * Free Gas (FG);
    _Vg = _Bg * _free_gas

    # Vw=WC * Qdes
    _Vw = (_wc/100) * _qdes

     # Vt=Vo+Vg+Vw;
    _Vt = _Vo + _Vg + _Vw

    # _composite_sg = ( ( (1-WC)*Qdes*Sgo + WC*Qdes*Sgw) * 62.4*5.6146 + Producing GOR*(1-WC)*Qdes*Sgg*0.0752) / (Vt*5.6146*62.4)
    _composite_sg = ( ( (1-(_wc/100))*_qdes*_sgo + (_wc/100)*_qdes*_sgw) * 62.4*5.6146 + _producing_gor*(1-(_wc/100))*_qdes*_sgg*0.0752) / (_Vt*5.6146*62.4)

    # WFL =PSD-(PIP*2.31/SGFluid)
    _wfl = _psd-(_pip*2.31/_sgfluid)

    # WHP = THP(WHP)*2.31/SGFluid
    _whp_hitung=_whp*2.31/_sgfluid

    if _p_casing == 0:
        _p_casing_hitung = 0
    else:
        _p_casing_hitung = (_p_casing * 2.31 / _sgfluid) / 3.28084 # -> utk jadi meter

    # Friction Loss = (2.083*(100/TubingCoeff)^1.85*(Qdes         /34.3)^1.85/TubingID^4.8655)  *PSDft/1000
    _friction_loss = (2.083*(100/_coefficient)**1.85*(_qdes/34.3)**1.85/_tubing_id**4.8655)*_psd/1000

    # % Free Gas = Vg / Vt
    _persen_free_gas = _Vg / _Vt

    # TDH = sum(WFL, WHP, CP, FrictionLoss)  --> CP (Optional, bila tdk dinput, defaultnya nol) 
    _cp = 0
    _tdh = _wfl + _whp_hitung + _cp + _friction_loss

    #Fluid Over Pump = (PIP-CP)*2.31/SGFluid
    _fluid_over_pump = (_pip - _cp)*2.31/_sgfluid

    # Fluid Gradient = SGFluid/2.31
    _fluid_gradient = _sgfluid/2.31

    st.write('\n')
    st.title("Calculation")
    col1, col2 = st.columns(2, gap="medium", vertical_alignment="top")
    with col1:
        st.write("Pwf@Qdes: ", _Pwf_at_Qdes, 'psi')
        st.write('Qdes         : ', _qdes, 'BPD')
        st.write('Composite SG : ', _composite_sg)
        st.write('PSD          : ', _psd, _measurement, 'TVD')
        st.write('WFL          : ', _wfl, _measurement, 'TVD')
        st.write('Di file xls: 4744.936, cek PIP')
        st.write('\n')
        st.write('Qmax         : ', _qmax, 'BPD')
        st.write('WHP          : ', _whp_hitung, _measurement, 'TVD')
        st.write('Di file xls: 345.0997')
        st.write('\n')
        st.write('SG Fluid     : ', _sgfluid)
        st.write('Di file xls: 1.004')
        st.write('\n')
        st.write('P. Casing    : ', _p_casing_hitung, _measurement, 'TVD')
        st.write('PIP          : ', _pip, 'psi')
        st.write('Di file xls: 523.7896')
    with col2:
        st.write('Friction Loss: ', _friction_loss, _measurement, 'TVD')
        st.write('% Free Gas     : ', _persen_free_gas, '%')
        st.write('\n')
        st.write('TDH            : ', _tdh, _measurement, 'TVD')
        st.write('Di file xls: 5376.58')
        st.write('\n')
        st.write('SBHP           : ', _sbhp, 'psig')
        st.write('Fluid Over Pump: ', _fluid_over_pump, _measurement, 'TVD')
        st.write('Di file xls: 1205.1334')
        st.write('\n')
        st.write('FBHP           : ', _fbhp, 'psig')
        st.write('Fluid Gradient : ', _fluid_gradient, 'psi/', _measurement, 'TVD')
        st.write('Di file xls: 0.43463')

    import matplotlib.pyplot as plt
    import numpy as np

    #->comment: Plotting
    #->comment: Create a selection that chooses the nearest point & selects based on x-value
    #chat_nearest = alt.selection(type='single', nearest=True, on='mouseover',
                                    #fields=['WEEK_START'], empty='none')
            
    #->comment: The basic line
    #chat_line = alt.Chart(df_weekly_chat_app).mark_line(interpolate='linear').encode(
                        #x=alt.X("WEEK_START:T", axis=alt.Axis(title="Week Start", titlePadding=15,  titleFontSize=20, titleFontWeight=900, labelAngle=-90), scale=alt.Scale(padding=32)),
                        #y=alt.Y("WEEKLY_APP_PCT:Q", axis=alt.Axis(title=y_title, titlePadding=15, titleFontSize=20, titleFontWeight=900, format=y_format)),
                                        #color=alt.Color('APP_TYPE:N',
                                        #scale=alt.Scale(domain=['single text input', 'chat']),
                                        #legend=alt.Legend(title=" ") ))
            
    #->comment: Transparent selectors across the ch-art. This is what tells us the x-value of the cursor
    #chat_selectors = alt.Chart(df_weekly_chat_app).mark_point().encode(x='WEEK_START:T', opacity=alt.value(0),).add_selection(chat_nearest)
            
    #->comment: Draw points on the line, and highlight based on selection
    #chat_points = chat_line.mark_point().encode(opacity=alt.condition(chat_nearest, alt.value(1), alt.value(0)))
            
    #->comment: Draw text labels near the points, and highlight based on selection
    #chat_text = chat_line.mark_text(align='left', dx=0, dy=-15, fontSize=16).encode(text=alt.condition(chat_nearest, alt_text, alt.value(' ')))
            
    #->comment: Draw a rule at the location of the selection
    #chat_rules = alt.Chart(df_weekly_chat_app).mark_rule(color='gray').encode(x='WEEK_START:T',).transform_filter(chat_nearest)
            
    #->comment: Put the five layers into a chart and bind the data
    #chat_count = alt.layer(chat_line, chat_selectors, chat_points, chat_rules, chat_text
            #).properties(width=800, height=500
            #).configure(padding=20, background="#111111"
            #).configure_legend(orient='bottom', titleFontSize=16, labelFontSize=14, titlePadding=0
            #).configure_axis(labelFontSize=14)        
    #st.altair_chart(chat_count, use_container_width=True)


    #plt.plot(ipr_data['Flow_rate'], ipr_data['Pressure'])
    #->comment: set title & label
    #plt.title('GMV Value in 2019',color='darkblue', fontsize=17)
    #plt.xlabel('Flow Rate, Q (BFPD)',fontsize=13,color='darkred')
    #plt.ylabel('Pressure, P (psi)',fontsize=13,color='darkred')
    #->comment: custom line
    #plot_line = plt.plot(ipr_data['Flow_rate'], ipr_data['Pressure'])
    #plt.setp(plot_line, color='blue', linestyle='-',  linewidth=2, marker='o')
    #->comment: set start 0 y axis
    #plt.ylim(ymin=0)
    #->comment: set grid
    #plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
    #plt.show()

    import altair as alt
    st.write('\n')
    st.title("Inflow Performance Relationships")    
    row5_1, row5_spacer2, row5_2= st.columns((11.1, .1, 4.5))
    with row5_1:
    #col1, col2 = st.columns(2, gap="large", vertical_alignment="center")
    #with col1:
        ipr_data = pd.read_csv('data/ipr_data.csv')
        #->comment: make the chart
        _ipr_curve = alt.Chart(ipr_data).mark_line().encode(
            x='Flow rate, Q (BFPD)',
            y='Pressure (psi)',
        ).mark_circle()  #.interactive()
        st.write('\n')
        st.write('\n')
        st.altair_chart(_ipr_curve, use_container_width=True)               
    with row5_2:
    #with col2:
        st.write('The Data:') 
        st.dataframe(ipr_data, hide_index=True)

    #->comment: import altair with an abbreviated alias
    #import altair as alt
    #->comment: load a sample dataset as a pandas DataFrame
    #from vega_datasets import data
    #cars = data.cars()
    #->comment: make the chart
    #chart01 = alt.Chart(cars).mark_line().encode(
    #    x='Horsepower',
    #    y='Miles_per_Gallon',
    #    color='Origin',
    #).interactive()
    #st.altair_chart(chart01, use_container_width=True)