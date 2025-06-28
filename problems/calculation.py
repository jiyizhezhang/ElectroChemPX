#
#
import numpy as np
#
#
# # Exp varying conditions
# no = 1
# current = 0.40
# conc_CoOAC2 = 0.05
# conc_Bu4NBF4 = 0.08
# ratio = 1.63
# time = 3.45 * 3600
# electrolyte = "LiBF4"
# # Bu4NBF4
# # Et4NBF4
# # LiBF4
# # LiClO4
#
#
#
#
class ChemicalRecord:

    def __init__(self, name, mw, role):
        self.name = name
        self.mw = mw
        self.role = role

CO_OAC2 = ChemicalRecord("CO(OAc)2", 177.02, "electrolyte")
Co_BF42 = ChemicalRecord("CO(BF4)2", 340.63, "electrolyte")
acetic_anhydride = ChemicalRecord("Acetic anhydride", 102.09, "electrolyte")

ss = ChemicalRecord("Terephthalic acid",166.13, "product") # ss
qs = ChemicalRecord("4-Carboxybenzaldehyde", 150.13, "product") # qs
js = ChemicalRecord("p-Toluic acid", 136.15, "product") # js
qq = ChemicalRecord("Terephthalaldehyde", 134.13, "product") # qq
jq = ChemicalRecord("p-Tolualdehyde", 120.15, "product") # jq
jj = ChemicalRecord("p-Xylene", 106.17, "reactant") # jj

#
#
#
#
# class ExpRecord:
#
#     def __init__(self, no, current, conc_CoOAC2, conc_Bu4NBF4, ratio, time, electrolyte):
#         self.no = no
#         self.current = current
#         self.conc_CoOAC2 = conc_CoOAC2
#         self.conc_Bu4NBF4 = conc_Bu4NBF4
#         self.ratio = ratio
#         self.time = time
#         self.electrolyte = electrolyte
#
#         self.temperature = 85
#         self.init_conc = 0.05
#         self.water = 0
#         self.v_anode = 9
#         self.v_cathode = 8
#         self.dilute_anode = 50
#         self.dilute_cathode = 50
#
#
#     def add_electrolyte_info(self):
#
#         if self.electrolyte == "LiBF4":
#             electrolyte = ChemicalRecord("LiBF4", 93.74, "electrolyte")
#             OAc_salt = ChemicalRecord("LiOAc", 65.99, "electrolyte")
#
#         if self.electrolyte == "Bu4NBF4":
#             electrolyte = ChemicalRecord("Bu4NBF4", 329.27, "electrolyte")
#             OAc_salt = ChemicalRecord("Bu4NOAc", 301.51, "electrolyte")
#
#         if self.electrolyte == "Et4NBF4":
#             electrolyte = ChemicalRecord("Et4NBF4", 217.06, "electrolyte")
#             OAc_salt = ChemicalRecord("Et4NOAc", 189.30, "electrolyte")
#
#         if self.electrolyte == "LiClO4":
#             electrolyte = ChemicalRecord("LiClO4", 106.39, "electrolyte")
#             OAc_salt = ChemicalRecord("LiOAc", 65.99, "electrolyte")
#
#         return electrolyte, OAc_salt
#
#
#     def get_electrolyte_recipe(self):
#
#         electrolyte, OAc_salt = self.add_electrolyte_info()
#
#         if ratio < 2:
#             mole_CO_OAC2 = self.ratio * self.conc_CoOAC2 / 2
#         else:
#             mole_CO_OAC2 = self.conc_CoOAC2
#
#         mole_Co_BF42 = conc_CoOAC2 - mole_CO_OAC2
#
#         m_CO_OAC2 = mole_CO_OAC2 * 25 / 1000 * CO_OAC2.mw
#         m_Co_BF42 = mole_Co_BF42 * 25 / 1000 * Co_BF42.mw
#
#
#         mole_OAc_salt = self.conc_CoOAC2 * self.ratio - mole_CO_OAC2 * 2
#         m_OAC_salt = mole_OAc_salt * OAc_salt.mw * 25 / 1000
#
#
#         v_OAC = ((mole_Co_BF42 * 6 * acetic_anhydride.mw * 25 / 1000) / 1.08) * 1000 / 0.98
#
#         mole_electrolyte = conc_Bu4NBF4 - mole_OAc_salt
#         m_electrolyte = mole_electrolyte * electrolyte.mw * 25 / 1000
#
#         recipe = {"m_CO_OAC2/(g)": m_CO_OAC2,
#                   "m_Co_BF42/(g)": m_Co_BF42,
#                   "m_OAC_salt/(g)": m_OAC_salt,
#                   "v_OAC/(uL)": v_OAC}
#
#         return recipe
#
#
#     def add_HPLC_data_anode(self, ss, qs, js, qq, jq, jj):
#         self.anode_peak_ss = ss
#         self.anode_peak_qs = qs
#         self.anode_peak_js = js
#         self.anode_peak_qq = qq
#         self.anode_peak_jq = jq
#         self.anode_peak_jj = jj
#
#     def add_HPLC_data_cathode(self, ss, qs, js, qq, jq, jj):
#         self.cathode_peak_ss = ss
#         self.cathode_peak_qs = qs
#         self.cathode_peak_js = js
#         self.cathode_peak_qq = qq
#         self.cathode_peak_jq = jq
#         self.cathode_peak_jj = jj
#
#     def _correct_conc(self, conc_anode, conc_cathode):
#         return conc_anode + conc_cathode * self.v_cathode / self.v_anode
#
#     def _calculate_yield(self, conc_anode, conc_cathode):
#         return (conc_anode * self.v_anode + conc_cathode * self.v_cathode) / (self.init_conc * self.v_anode) / 10
#
#
#     def calculate_objs(self):
#         peak_xylene = self.init_conc * 1000 * 106.17 * 9522.3 / self.dilute_anode
#
#         conc_anode_ss = self.dilute_anode * (self.anode_peak_ss /118492)/ss.mw
#         conc_anode_qs = self.dilute_anode * (self.anode_peak_qs /46768)/qs.mw
#         conc_anode_js = self.dilute_anode * (self.anode_peak_js /15629)/js.mw
#         conc_anode_qq = self.dilute_anode * (self.anode_peak_qq /39848)/qq.mw
#         conc_anode_jq = self.dilute_anode * (self.anode_peak_jq /20202)/jq.mw
#         conc_anode_jj = self.dilute_anode * (self.anode_peak_jj /9522.3)/jj.mw
#         # print(conc_anode_ss, conc_anode_qs, conc_anode_js, conc_anode_qq, conc_anode_jq, conc_anode_jj)
#
#         conc_cathode_ss = self.dilute_cathode * (self.cathode_peak_ss /118492)/ss.mw
#         conc_cathode_qs = self.dilute_cathode * (self.cathode_peak_qs /46768)/qs.mw
#         conc_cathode_js = self.dilute_cathode * (self.cathode_peak_js /15629)/js.mw
#         conc_cathode_qq = self.dilute_cathode * (self.cathode_peak_qq /39848)/qq.mw
#         conc_cathode_jq = self.dilute_cathode * (self.cathode_peak_jq /20202)/jq.mw
#         conc_cathode_jj = self.dilute_cathode * (self.cathode_peak_jj /9522.3)/jj.mw
#
#
#         corr_conc_ss = self._correct_conc(conc_anode_ss, conc_cathode_ss)
#         corr_conc_qs = self._correct_conc(conc_anode_qs, conc_cathode_qs)
#         corr_conc_js = self._correct_conc(conc_anode_js, conc_cathode_js)
#         corr_conc_qq = self._correct_conc(conc_anode_qq, conc_cathode_qq)
#         corr_conc_jq = self._correct_conc(conc_anode_jq, conc_cathode_jq)
#         corr_conc_jj = self._correct_conc(conc_anode_jj, conc_cathode_jj)
#         # print(corr_conc_ss, corr_conc_qs, corr_conc_js, corr_conc_qq, corr_conc_jq, corr_conc_jj)
#
#
#         Fe_conc_ss = corr_conc_ss / (0.001*current * time/96485/12/self.v_anode*1000000) * 100
#         Fe_conc_qs = corr_conc_qs / (0.001*current * time/96485/10/self.v_anode*1000000) * 100
#         Fe_conc_js = corr_conc_js / (0.001*current * time/96485/6/self.v_anode*1000000) * 100
#         Fe_conc_qq = corr_conc_qq / (0.001*current * time/96485/8/self.v_anode*1000000) * 100
#         Fe_conc_jq = corr_conc_jq / (0.001*current * time/96485/4/self.v_anode*1000000) * 100
#         Fe_conc_jj = 0.0
#
#
#         yield_ss = self._calculate_yield(conc_anode_ss, conc_cathode_ss)
#         yield_qs = self._calculate_yield(conc_anode_qs, conc_cathode_qs)
#         yield_js = self._calculate_yield(conc_anode_js, conc_cathode_js)
#         yield_qq = self._calculate_yield(conc_anode_qs, conc_cathode_qs)
#         yield_jq = self._calculate_yield(conc_anode_jq, conc_cathode_jq)
#
#         total_yield = yield_ss + yield_qs + yield_js + yield_qq + yield_jq
#         conversion = (peak_xylene - self.anode_peak_jj - self.cathode_peak_jj* 8/9) / peak_xylene * 100
#
#         fc = 10000/(Fe_conc_ss+Fe_conc_qs+Fe_conc_js+Fe_conc_qq+Fe_conc_jq+Fe_conc_jj)
#
#         return yield_js, fc
#
#
# exp1 = ExpRecord(no, current, conc_CoOAC2, conc_Bu4NBF4, ratio, time, electrolyte)
# recipe = exp1.get_electrolyte_recipe()
# exp1.add_HPLC_data_anode(0, 4793, 8772, 0, 101835, 5371090)
# exp1.add_HPLC_data_cathode(0, 0, 0, 0, 5473, 975880)
# yield_js, fc = exp1.calculate_objs()
# print(yield_js, fc)
#
#
#
# Placeholder for the recipe calculation function



import streamlit as st
import pandas as pd

st.title("Exp database")

uploaded_file = st.file_uploader("Choose an Excel file", type=['csv'])

data_placeholder = st.empty()
recipe_placeholder = st.empty()
input_placeholder = st.empty()
input_results_placeholder = st.empty()

def calculate_recipe(data):

    no = data["No"]
    current = data["Current(mA)"]
    conc_CoOAC2 = data["Co(OAc)2(M)"]
    conc_Bu4NBF4 = data["Bu4NBF4(M)"]
    ratio = data["Ratio"]
    time = data["Time(h)"]
    electrolyte = data["Electrolyte"]

    def add_electrolyte_info(electrolyte):

        if electrolyte == "LiBF4":
            electrolyte = ChemicalRecord("LiBF4", 93.74, "electrolyte")
            OAc_salt = ChemicalRecord("LiOAc", 65.99, "electrolyte")

        if electrolyte == "Bu4NBF4":
            electrolyte = ChemicalRecord("Bu4NBF4", 329.27, "electrolyte")
            OAc_salt = ChemicalRecord("Bu4NOAc", 301.51, "electrolyte")

        if electrolyte == "Et4NBF4":
            electrolyte = ChemicalRecord("Et4NBF4", 217.06, "electrolyte")
            OAc_salt = ChemicalRecord("Et4NOAc", 189.30, "electrolyte")

        if electrolyte == "LiClO4":
            electrolyte = ChemicalRecord("LiClO4", 106.39, "electrolyte")
            OAc_salt = ChemicalRecord("LiOAc", 65.99, "electrolyte")

        return electrolyte, OAc_salt

    electrolyte, OAc_salt = add_electrolyte_info(electrolyte)

    if ratio < 2:
        mole_CO_OAC2 = ratio * conc_CoOAC2 / 2
    else:
        mole_CO_OAC2 = conc_CoOAC2

    mole_Co_BF42 = conc_CoOAC2 - mole_CO_OAC2

    m_CO_OAC2 = mole_CO_OAC2 * 25 / 1000 * CO_OAC2.mw
    m_Co_BF42 = mole_Co_BF42 * 25 / 1000 * Co_BF42.mw


    mole_OAc_salt = conc_CoOAC2 * ratio - mole_CO_OAC2 * 2
    m_OAC_salt = mole_OAc_salt * OAc_salt.mw * 25 / 1000

    v_OAC = ((mole_Co_BF42 * 6 * acetic_anhydride.mw * 25 / 1000) / 1.08) * 1000 / 0.98

    mole_electrolyte = conc_Bu4NBF4 - mole_OAc_salt
    m_electrolyte = mole_electrolyte * electrolyte.mw * 25 / 1000

    recipe = {"m_CO_OAC2(g)": m_CO_OAC2,
              "m_Co_BF42(g)": m_Co_BF42,
              "m_OAC_salt(g)": m_OAC_salt,
              "v_OAC(uL)": v_OAC}

    return recipe



def calculate_from_input_data(anode_hplc, cathode_hplc, exp_cond):

    cathode_peak_ss = cathode_hplc[0]
    cathode_peak_qs = cathode_hplc[1]
    cathode_peak_js = cathode_hplc[2]
    cathode_peak_qq = cathode_hplc[3]
    cathode_peak_jq = cathode_hplc[4]
    cathode_peak_jj = cathode_hplc[5]

    anode_peak_ss = anode_hplc[0]
    anode_peak_qs = anode_hplc[1]
    anode_peak_js = anode_hplc[2]
    anode_peak_qq = anode_hplc[3]
    anode_peak_jq = anode_hplc[4]
    anode_peak_jj = anode_hplc[5]

    temperature = 85
    init_conc = 0.05
    water = 0
    v_anode = 9
    v_cathode = 8
    dilute_anode = 50
    dilute_cathode = 50


    def _correct_conc(conc_anode, conc_cathode):
        return conc_anode + conc_cathode * v_cathode / v_anode

    def _calculate_yield(conc_anode, conc_cathode):
        return (conc_anode * v_anode + conc_cathode * v_cathode) / (init_conc * v_anode) / 10

    def calculate_objs(exp_cond):

        peak_xylene = init_conc * 1000 * 106.17 * 9522.3 / dilute_anode

        conc_anode_ss = dilute_anode * (anode_peak_ss /118492)/ss.mw
        conc_anode_qs = dilute_anode * (anode_peak_qs /46768)/qs.mw
        conc_anode_js = dilute_anode * (anode_peak_js /15629)/js.mw
        conc_anode_qq = dilute_anode * (anode_peak_qq /39848)/qq.mw
        conc_anode_jq = dilute_anode * (anode_peak_jq /20202)/jq.mw
        conc_anode_jj = dilute_anode * (anode_peak_jj /9522.3)/jj.mw

        conc_cathode_ss = dilute_cathode * (cathode_peak_ss /118492)/ss.mw
        conc_cathode_qs = dilute_cathode * (cathode_peak_qs /46768)/qs.mw
        conc_cathode_js = dilute_cathode * (cathode_peak_js /15629)/js.mw
        conc_cathode_qq = dilute_cathode * (cathode_peak_qq /39848)/qq.mw
        conc_cathode_jq = dilute_cathode * (cathode_peak_jq /20202)/jq.mw
        conc_cathode_jj = dilute_cathode * (cathode_peak_jj /9522.3)/jj.mw


        corr_conc_ss = _correct_conc(conc_anode_ss, conc_cathode_ss)
        corr_conc_qs = _correct_conc(conc_anode_qs, conc_cathode_qs)
        corr_conc_js = _correct_conc(conc_anode_js, conc_cathode_js)
        corr_conc_qq = _correct_conc(conc_anode_qq, conc_cathode_qq)
        corr_conc_jq = _correct_conc(conc_anode_jq, conc_cathode_jq)
        corr_conc_jj = _correct_conc(conc_anode_jj, conc_cathode_jj)

        Fe_conc_ss = corr_conc_ss / (0.001*exp_cond["Current(mA)"] * exp_cond["Time(h)"]/96485/12/v_anode*1000000) * 100
        Fe_conc_qs = corr_conc_qs / (0.001*exp_cond["Current(mA)"] * exp_cond["Time(h)"]/96485/10/v_anode*1000000) * 100
        Fe_conc_js = corr_conc_js / (0.001*exp_cond["Current(mA)"] * exp_cond["Time(h)"]/96485/6/v_anode*1000000) * 100
        Fe_conc_qq = corr_conc_qq / (0.001*exp_cond["Current(mA)"] * exp_cond["Time(h)"]/96485/8/v_anode*1000000) * 100
        Fe_conc_jq = corr_conc_jq / (0.001*exp_cond["Current(mA)"] * exp_cond["Time(h)"]/96485/4/v_anode*1000000) * 100
        Fe_conc_jj = 0.0


        yield_ss = _calculate_yield(conc_anode_ss, conc_cathode_ss)
        yield_qs = _calculate_yield(conc_anode_qs, conc_cathode_qs)
        yield_js = _calculate_yield(conc_anode_js, conc_cathode_js)
        yield_qq = _calculate_yield(conc_anode_qs, conc_cathode_qs)
        yield_jq = _calculate_yield(conc_anode_jq, conc_cathode_jq)

        total_yield = yield_ss + yield_qs + yield_js + yield_qq + yield_jq
        conversion = (peak_xylene - anode_peak_jj - cathode_peak_jj* 8/9) / peak_xylene * 100

        fc = 10000/(Fe_conc_ss+Fe_conc_qs+Fe_conc_js+Fe_conc_qq+Fe_conc_jq+Fe_conc_jj)

        return conversion, fc

    conversion, fc = calculate_objs(exp_cond.iloc[-1,:])
    return conversion, fc


if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        # Display the data frame in the placeholder
        data_placeholder.write("Data from the uploaded file:")

        exp_cond = df[["No", "Current(mA)", "Co(OAc)2(M)", "Bu4NBF4(M)",
                       "Ratio", "Time(h)", "Electrolyte",
                       "obj1_yield_js", "obj2_fc"]]
        data_placeholder.dataframe(exp_cond)
        data_placeholder.dataframe(exp_cond.set_index(df.columns[0]))

    except pd.errors.EmptyDataError:
        st.error("The uploaded file is empty. Please upload a valid CSV file.")
    except pd.errors.ParserError:
        st.error("Parsing error: Unable to parse the CSV file. Check if the file is correctly formatted.")
    except Exception as e:
        st.error(f"An error occurred while reading the file: {e}")




if st.button("Calculate Recipe"):
    if uploaded_file is not None:
        try:
            # Ensure the DataFrame is loaded and valid
            if 'df' in locals() and isinstance(df, pd.DataFrame):
                # Calculate the recipe using the DataFrame
                recipe_result = calculate_recipe(exp_cond.iloc[-1,0:7])

                # Display the recipe results in the recipe placeholder
                recipe_placeholder.write("Recipe Calculation Results:")
                recipe_placeholder.dataframe(recipe_result)
            else:
                st.error("No valid data available for recipe calculation. Please upload a valid CSV file.")

        except Exception as e:
            st.error(f"An error occurred during recipe calculation: {e}")
    else:
        st.warning("Please upload a CSV file first to calculate the recipe.")

# Initial instructions
if not uploaded_file:
    st.info("Upload a CSV file to get started and then click 'Calculate Recipe'.")



# Define form for HPLC data input
with st.form(key='table_form'):

    st.write("Please enter HPLC results:")

    col1, col2 = st.columns(2)

    anode_ss = col1.number_input("anode_ss", min_value=0, step=1)
    cathode_ss = col2.number_input("cathode_ss", min_value=0, step=1)

    anode_qs = col1.number_input("anode_qs", min_value=0, step=1)
    cathode_qs = col2.number_input("cathode_qs", min_value=0, step=1)

    anode_js = col1.number_input("anode_js", min_value=0, step=1)
    cathode_js = col2.number_input("cathode_js", min_value=0, step=1)

    anode_qq = col1.number_input("anode_qq", min_value=0, step=1)
    cathode_qq = col2.number_input("cathode_qq", min_value=0, step=1)

    anode_jq = col1.number_input("anode_jq", min_value=0, step=1)
    cathode_jq = col2.number_input("cathode_jq", min_value=0, step=1)

    anode_jj = col1.number_input("anode_jj", min_value=0, step=1)
    cathode_jj = col2.number_input("cathode_jj", min_value=0, step=1)

    anode_hplc = [anode_ss, anode_qs, anode_js, anode_qq, anode_jq, anode_jj]
    cathode_hplc = [cathode_ss, cathode_qs, cathode_js, cathode_qq, cathode_jq, cathode_jj]

    # Submit button
    submit_button = st.form_submit_button(label='Submit')

# Handle form submission
if submit_button:

    # calculate objectives
    obj1, obj2 = calculate_from_input_data(anode_hplc, cathode_hplc, exp_cond)

    obj = {"obj1": obj1,
           "obj2": obj2}

    # Display the entered table
    st.write("Objectives:")
    st.dataframe(obj)


# Adding results and update csv
if st.button("Update database"):

    df.iloc[-1, 7:13] = anode_hplc
    df.iloc[-1, 13:19] = cathode_hplc

    obj1, obj2 = calculate_from_input_data(anode_hplc, cathode_hplc, exp_cond)
    df.iloc[-1, 19] = obj1
    df.iloc[-1, 20] = obj2

    # st.dataframe(df)
    df.to_csv("/Users/zhang/PycharmProjects/PDBO/database/try.csv", index=False)
    st.success("Results added!")


# Adding new experiment design
# input current X, current Y,
# output next X, hypervolume



# df = pd.read_csv("/Users/zhang/PycharmProjects/PDBO/database/try.csv")
# st.write(df)

# options = st.sidebar.header("Options")
# options_form = st.sidebar.form("options_form")
#
# current = options_form.text_input("Current")
# CoOAc2 = options_form.text_input("Concentration-Co(OAc)2")
# Bu4NBF4 = options_form.text_input("Concentration-Bu4NBF4")
# ratio = options_form.text_input("Ratio")
# time = options_form.text_input("Time")
# electrolyte = options_form.text_input("Electrolyte")
#
# add_data = options_form.form_submit_button()
#
# if add_data:
#     st.write(current, CoOAc2, Bu4NBF4, ratio, time, electrolyte)
#
#     # same format as csv
#     new_data = {"Current(mA)": current,
#                 "Co(OAc)2(M)": CoOAc2,
#                 "Bu4NBF4(M)": Bu4NBF4,
#                 "ratio": ratio,
#                 "Time (h)": time,
#                 "Electrolyte": electrolyte}
#
#     df = df.append(new_data, ignore_index=True)
#     df.to_csv("/Users/zhang/PycharmProjects/PDBO/database/try.csv", index=False)
#     st.write(df)


