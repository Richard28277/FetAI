import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter import * 
import pickle
import pandas as pd
from joblib import load
import sklearn.ensemble._voting
from sklearn import *
import sklearn
import sklearn.calibration
import sklearn.cross_decomposition
import sklearn.experimental
import sklearn.feature_extraction
import sklearn.feature_selection
import xgboost
import sklearn.calibration
import sklearn.cluster
import sklearn.covariance
import sklearn.cross_decomposition
import sklearn.datasets
import sklearn.decomposition
import sklearn.dummy
import sklearn.ensemble
import sklearn.exceptions
import sklearn.experimental
import sklearn.externals
import sklearn.feature_extraction
import sklearn.feature_selection
import sklearn.gaussian_process
import sklearn.inspection
import sklearn.isotonic
import sklearn.kernel_approximation
import sklearn.kernel_ridge
import sklearn.linear_model
import sklearn.manifold
import sklearn.metrics
import sklearn.mixture
import sklearn.model_selection
import sklearn.multiclass
import sklearn.multioutput
import sklearn.naive_bayes
import sklearn.neighbors
import sklearn.neural_network
import sklearn.pipeline
import sklearn.preprocessing
import sklearn.random_projection
import sklearn.semi_supervised
import sklearn.svm
import sklearn.tree
import sklearn.discriminant_analysis
import sklearn.impute
import sklearn.compose
import Main

class FetalForm(tk.Frame):
    global model
    model = None
    def set_ml_model(name):
        global model
        model = load(name)
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label = tk.Label(self, text="CTG Form")
        # label.pack(padx=10, pady=10)
        global model
        def pred(BV, AC, FM, UC, ASTV, MSTV, ALTV, MLTV, LD, SD, PD, HW, Hmin, HMax, NP, NZ, HMo, HMe, HMed, HV, HT, st, et):
            global model
            try:
                BV = float(BV.get())
                AC = float(AC.get()) / (float(et.get()) - float(st.get()))
                FM = float(FM.get()) / (float(et.get()) - float(st.get()))
                UC = float(UC.get()) / (float(et.get()) - float(st.get()))
                LD = float(LD.get()) / (float(et.get()) - float(st.get()))
                SD = float(SD.get()) / (float(et.get()) - float(st.get()))
                PD = float(PD.get()) / (float(et.get()) - float(st.get()))
                ASTV = float(ASTV.get())
                MSTV = float(MSTV.get())
                ALTV = float(ALTV.get())
                MLTV = float(MLTV.get())
                HW = float(HW.get())
                HMax = float(HMax.get())
                Hmin = float(Hmin.get())
                NP = float(NP.get())
                NZ = float(NZ.get())
                HMo = float(HMo.get())
                HMe = float(HMe.get())
                HMed = float(HMed.get())
                HV = float(HV.get())
                HT = float(HT.get())
                # print(float(et.get()) - float(st.get()))
                # print([BV, AC, FM, UC, ASTV, MSTV, ALTV, MLTV, LD, SD, PD, HW, Hmin, HMax, NP, NZ, HMo, HMe, HMed, HV, HT])
                result = model.predict(pd.DataFrame([[BV, AC, FM, UC, ASTV, MSTV, ALTV, MLTV, LD, SD, PD, HW, Hmin, HMax, NP, NZ, HMo, HMe, HMed, HV, HT]], columns=['LB', 'AC', 'FM', 'UC', 'ASTV', 'MSTV', 'ALTV', 'MLTV', 'DL', 'DS', 'DP', 'Width', 'Min', 'Max', 'Nmax', 'Nzeros', 'Mode', 'Mean', 'Median', 'Variance', 'Tendency']))
            except:
                if (model == None):
                    return "Error: Please upload a classifier (Upload > ML Model)"
                return "Error: make sure all values are correct"
            if result == 1:
                result = "calm sleep (class=1) \n \n Likely cause: non-REM sleep; quiet sleep [normal]"
            elif result == 2:
                result = "REM sleep (class=2) \n \n Likely cause: rapid eye movement; active sleep [normal]"
            elif result == 3:
                result = "calm vigilance (class=3) \n \n Likely cause: quiet awake [normal]"
            elif result == 4:
                result = "active vigilance (class=4) \n \n Likely cause: active awake [normal]"
            elif result == 5:
                result = "shift pattern (class=5) \n \n Likely cause: shifting pattern [normal/suspect]"
            elif result == 6:
                result = "accelerative/decelerative pattern (class=6) \n \n Likely cause: stress situation/voluntary movements [normal]"
            elif result == 7:
                result = "decelerative pattern (class=7) \n \n Likely cause: vagal stimulation [normal]"
            elif result == 8:
                result = "largely decelerative pattern (class=8) \n \n Likely cause: fetal hypoxia [pathological]"
            elif result == 9:
                result = "flat-sinusoidal pattern (class=9) \n \n Likely cause: fetal anemia [pathological]"
            elif result == 10:
                result = "suspect pattern (class=10) \n \n Likely cause: fetal hypoxia [suspect]"
            return "Morphologic state: " + result

        stepOne = tkinter.LabelFrame(self, text=" 1. Enter General Details: ")
        stepOne.grid(row=0, columnspan=7, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)

        helpLf = tkinter.LabelFrame(self, text=" Quick Help ")
        helpLf.grid(row=0, column=9, columnspan=2, rowspan=8, \
                    sticky='NS', padx=5, pady=5)
        helpLbl = tkinter.Label(helpLf, text="(1) FHR (Fetal Heart Rate) \n (2) bpm (beats per minute) \n (3) Histogram details refer to FHR histogram \n (4) Histogram tendency: \n  -1=left assymetric \n 0=symmetric \n 1=right assymetric  \n (5) Diagnosis based on 10-class system \n \n Authors: Richard Xu, Yifu Zuo")
        helpLbl.grid(row=0)

        stepTwo = tkinter.LabelFrame(self, text=" 2. Enter Variability Details: ")
        stepTwo.grid(row=2, columnspan=7, sticky='W', \
                    padx=5, pady=5, ipadx=5, ipady=5)

        stepThree = tkinter.LabelFrame(self, text=" 3. Enter Histogram Details: ")
        stepThree.grid(row=3, columnspan=7, sticky='W', \
                    padx=5, pady=5, ipadx=5, ipady=5)
        stepFour = tkinter.LabelFrame(self, text=" Actions: ")
        stepFour.grid(row=4, columnspan=7, sticky='W', \
                    padx=5, pady=5, ipadx=5, ipady=5)

        BV1 = tkinter.Label(stepOne, text="Baseline Value (mean FHR in bpm):")
        BV1.grid(row=0, column=0, sticky='E', padx=5, pady=2)

        BV = tkinter.Entry(stepOne)
        BV.grid(row=0, column=1, columnspan=7, sticky="WE", pady=3)

        AC1 = tkinter.Label(stepOne, text="Accelerations (total):")
        AC1.grid(row=1, column=0, sticky='E', padx=5, pady=2)

        AC = tkinter.Entry(stepOne)
        AC.grid(row=1, column=1, columnspan=7, sticky="WE", pady=2)

        FM1 = tkinter.Label(stepOne, text="Fetal Movement (#):")
        FM1.grid(row=2, column=0, sticky='E', padx=5, pady=2)

        FM = tkinter.Entry(stepOne)
        FM.grid(row=2, column=1, columnspan=7, sticky="WE", pady=2)

        UC1 = tkinter.Label(stepOne, text="Uterine Contractions (total):")
        UC1.grid(row=3, column=0, sticky='E', padx=5, pady=2)

        UC = tkinter.Entry(stepOne)
        UC.grid(row=3, column=1, sticky='E', pady=2)

        LD1 = tkinter.Label(stepOne, text="Light Decelerations (total):")
        LD1.grid(row=3, column=5, padx=5, pady=2)

        LD = tkinter.Entry(stepOne)
        LD.grid(row=3, column=7, pady=2)

        SD1 = tkinter.Label(stepOne, text="Severe Decelerations (total):")
        SD1.grid(row=4, column=0, sticky='E', padx=5, pady=2)

        SD = tkinter.Entry(stepOne)
        SD.grid(row=4, column=1, sticky='E', pady=2)

        PD1 = tkinter.Label(stepOne, text="Prolonged Decelerations (total):")
        PD1.grid(row=4, column=5, padx=5, pady=2)

        PD = tkinter.Entry(stepOne)
        PD.grid(row=4, column=7, pady=2)

        st1 = tkinter.Label(stepOne, text="Start Time (in seconds):")
        st1.grid(row=5, column=0, sticky='E', padx=5, pady=2)

        st = tkinter.Entry(stepOne)
        st.grid(row=5, column=1, sticky='E', pady=2)

        et1 = tkinter.Label(stepOne, text="End Time (in seconds):")
        et1.grid(row=5, column=5, padx=5, pady=2)

        et = tkinter.Entry(stepOne)
        et.grid(row=5, column=7, pady=2)
    #second section
        astv1 = tkinter.Label(stepTwo, text="Abnormal Short-Term Variability (%):")
        astv1.grid(row=3, column=0, sticky='E', padx=5, pady=2)

        ASTV = tkinter.Entry(stepTwo)
        ASTV.grid(row=3, column=1, sticky='E', pady=2)

        MSTV1 = tkinter.Label(stepTwo, text="Mean Value of Short-Term Variability:")
        MSTV1.grid(row=3, column=5, padx=5, pady=2)

        MSTV = tkinter.Entry(stepTwo)
        MSTV.grid(row=3, column=7, pady=2)

        ALTV1 = tkinter.Label(stepTwo, text="Abnormal Long-Term Variability (%):")
        ALTV1.grid(row=4, column=0, sticky='E', padx=5, pady=2)

        ALTV = tkinter.Entry(stepTwo)
        ALTV.grid(row=4, column=1, sticky='E', pady=2)

        MLTV1 = tkinter.Label(stepTwo, text="Mean Value of Long-Term Variability:")
        MLTV1.grid(row=4, column=5, padx=5, pady=2)

        MLTV = tkinter.Entry(stepTwo)
        MLTV.grid(row=4, column=7, pady=2)
    # section 3
        HW1 = tkinter.Label(stepThree, text="Histogram Width:")
        HW1.grid(row=0, column=0, sticky='E', padx=5, pady=2)

        HW = tkinter.Entry(stepThree)
        HW.grid(row=0, column=1, sticky='E', pady=2)

        HMax1 = tkinter.Label(stepThree, text="Histogram Max:")
        HMax1.grid(row=0, column=5, padx=5, pady=2)

        HMax = tkinter.Entry(stepThree)
        HMax.grid(row=0, column=7, pady=2)

        NP1 = tkinter.Label(stepThree, text="Number of Historgram Peaks:")
        NP1.grid(row=1, column=0, sticky='E', padx=5, pady=2)

        NP = tkinter.Entry(stepThree)
        NP.grid(row=1, column=1, sticky='E', pady=2)

        NZ1 = tkinter.Label(stepThree, text="Number of Histogram Zeroes:")
        NZ1.grid(row=1, column=5, padx=5, pady=2)

        NZ = tkinter.Entry(stepThree)
        NZ.grid(row=1, column=7, pady=2)

        Hmin1 = tkinter.Label(stepThree, text="Histogram Min:")
        Hmin1.grid(row=2, column=0, sticky='E', padx=5, pady=2)

        Hmin = tkinter.Entry(stepThree)
        Hmin.grid(row=2, column=1, sticky='E', pady=2)

        HMo1 = tkinter.Label(stepThree, text="Histogram Mode:")
        HMo1.grid(row=2, column=5, padx=5, pady=2)

        HMo = tkinter.Entry(stepThree)
        HMo.grid(row=2, column=7, pady=2)

        HMe1 = tkinter.Label(stepThree, text="Histogram Mean:")
        HMe1.grid(row=3, column=0, sticky='E', padx=5, pady=2)

        HMe = tkinter.Entry(stepThree)
        HMe.grid(row=3, column=1, sticky='E', pady=2)

        HMed1 = tkinter.Label(stepThree, text="Histogram Median:")
        HMed1.grid(row=3, column=5, padx=5, pady=2)

        HMed = tkinter.Entry(stepThree)
        HMed.grid(row=3, column=7, pady=2)

        HV1 = tkinter.Label(stepThree, text="Histogram Variance:")
        HV1.grid(row=4, column=0, sticky='E', padx=5, pady=2)

        HV = tkinter.Entry(stepThree)
        HV.grid(row=4, column=1, sticky='E', pady=2)

        HT1 = tkinter.Label(stepThree, text="Histogram Tendency:")
        HT1.grid(row=4, column=5, padx=5, pady=2)

        HT = tkinter.Scale(stepThree, from_ = -1, to = 1, orient = HORIZONTAL)
        HT.grid(row=4, column=7, pady=2)
        def showres():
            root = tkinter.Tk()
            root.geometry('400x200+150+150')
            root.iconbitmap("blueLogo.ico")
            root.wm_title('CTG Diagnosis Results')
            tenClass = tkinter.Label(root, text=pred(BV, AC, FM, UC, ASTV, MSTV, ALTV, MLTV, LD, SD, PD, HW, Hmin, HMax, NP, NZ, HMo, HMe, HMed, HV, HT, st, et), padx=5, pady=2)
            tenClass.pack(side = 'top', pady=20)
                                    
            btn = Button(root, text = "Back", bd = '5', command = root.destroy)
            btn.pack(side = 'bottom', pady=20)   
            
            root.mainloop()
        def clearAll():
            BV.delete(0, END)
            AC.delete(0, END)
            FM.delete(0, END)
            UC.delete(0, END)
            LD.delete(0, END)
            SD.delete(0, END)
            PD.delete(0, END)
            ASTV.delete(0, END)
            MSTV.delete(0, END)
            ALTV.delete(0, END)
            MLTV.delete(0, END)
            HW.delete(0, END)
            HMax.delete(0, END)
            Hmin.delete(0, END)
            NP.delete(0, END)
            NZ.delete(0, END)
            HMo.delete(0, END)
            HMe.delete(0, END)
            HMed.delete(0, END)
            HV.delete(0, END)
            st.delete(0, END)
            et.delete(0, END)
            HT.set(0)

        submit = Button(stepFour, text = 'Submit', bd = '5', command = showres)
        submit.grid(row=0, column=1, padx=100, pady=10)
        restart = Button(stepFour, text = 'Clear values', bd = '5', command = clearAll)
        restart.grid(row=0, column=5, padx=100, pady=10)

