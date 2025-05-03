from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import joblib

def homepage(request):
    return render(request,"homePage.html")

def getInfo(request):
    if request.method == "POST":
        return render(request,"info.html")
    
def healthCheck(request):
    if request.method == "POST":
        return render(request,"project.html")

def process_data_diabetes(request):
    if request.method == "POST":
        Age = float(request.POST.get('Age'))
        Gender = float(request.POST.get('Sex'))
        Hypertension = float(request.POST.get('Hypertension'))
        HeartDisease = float(request.POST.get('HeartDisease'))
        Smoking = str(request.POST.get('Smoking'))
        BMI = float(request.POST.get('BMI'))
        HbA1c = float(request.POST.get('HbA1c'))
        BloodGlucose = float(request.POST.get('BloodGlucose'))

        data={'gender':Gender,'age':Age,'hypertension':Hypertension,'heartdisease':HeartDisease,'smoking_history':Smoking,'bmi':BMI,'hbaic':HbA1c ,'bloodglucose':BloodGlucose}
        xd = pd.DataFrame(data, index=[0])
        print(xd)
        print('__________________________________________________________________________')
        xd = pd.get_dummies(xd, columns=['smoking_history'], dtype=int)
        print('++++++++++++++++++++++++++++')
        print(xd.columns[-1])

        def get(gender, age, hypertension, heart_disease, bmi, HbA1c_level, blood_glucose_level, 
                smoking_history_NoInfo=0, smoking_history_current=0, smoking_history_ever=0, 
                smoking_history_former=0, smoking_history_never=0, smoking_history_not_current=0):
            model = joblib.load(r"C:\B tech\internship ACITE\diabetes.pkl")
            input_data = [[gender, age, hypertension, heart_disease, bmi, HbA1c_level, blood_glucose_level, 
                        smoking_history_NoInfo, smoking_history_current, smoking_history_ever, 
                        smoking_history_former, smoking_history_never, smoking_history_not_current]]
            prediction = model.predict(input_data)
            print(f"Prediction: {prediction}")
            print(prediction[0])
            print(type(prediction[0]))
            return prediction

        p = get(
            xd['gender'].iloc[0], xd['age'].iloc[0], xd['hypertension'].iloc[0], xd['heartdisease'].iloc[0],
            xd['bmi'].iloc[0], xd['hbaic'].iloc[0], xd['bloodglucose'].iloc[0], 
            xd.get(xd.columns[-1], pd.Series([0])).iloc[0]
        )

        return render(request, "result.html", {'output':p[0]})
    return HttpResponse("Invalid Request")

def process_data_heart(request):
    if request.method == "POST":
        Age = float(request.POST.get('Age', 0))
        sex = float(request.POST.get('sex', 0))
        chest_pain_type = float(request.POST.get('chest_pain_type', 0))
        resting_bp = float(request.POST.get('resting_bp', 0))
        cholesterol = float(request.POST.get('cholesterol', 0))
        fasting_blood_sugar = float(request.POST.get('fasting_blood_sugar', 0))
        resting_ecg = float(request.POST.get('resting_ecg', 0))
        max_heart_rate = float(request.POST.get('max_heart_rate', 0))
        exercise_induced_angina = float(request.POST.get('exercise_induced_angina', 0))
        oldpeak = float(request.POST.get('oldpeak', 0))
        slope = float(request.POST.get('slope', 0))
        ca = float(request.POST.get('ca', 0))
        thal = float(request.POST.get('thal', 0))

        data = {
        'Age': Age, 'sex': sex, 'chest_pain_type': chest_pain_type,
        'resting_bp': resting_bp, 'cholesterol': cholesterol,
        'fasting_blood_sugar': fasting_blood_sugar, 'resting_ecg': resting_ecg,
        'max_heart_rate': max_heart_rate, 'exercise_induced_angina': exercise_induced_angina,
        'oldpeak': oldpeak, 'slope': slope, 'ca': ca, 'thal': thal
        }
        df = pd.DataFrame(data, index=[0])
        print(df)

        def get(Age, sex, chest_pain_type, resting_bp, cholesterol, fasting_blood_sugar, resting_ecg, 
                max_heart_rate, exercise_induced_angina, oldpeak, 
                slope, ca, thal):
            model = joblib.load(r"C:\B tech\internship ACITE\heart.pkl")
            input_data = [[Age, sex, chest_pain_type, resting_bp, cholesterol, fasting_blood_sugar, resting_ecg, 
                max_heart_rate, exercise_induced_angina, oldpeak, 
                slope, ca, thal]]
            prediction = model.predict(input_data)
            print(f"Prediction: {prediction}")
            return prediction

        p = get(
            df['Age'].iloc[0], df['sex'].iloc[0], df['chest_pain_type'].iloc[0], df['resting_bp'].iloc[0],
            df['cholesterol'].iloc[0], df['fasting_blood_sugar'].iloc[0], df['resting_ecg'].iloc[0], 
            df['max_heart_rate'].iloc[0], df['exercise_induced_angina'].iloc[0], df['oldpeak'].iloc[0], df['slope'].iloc[0],
            df['ca'].iloc[0],df['thal'].iloc[0]
        )


        return render(request, "result.html", {'output':p[0]})
    return HttpResponse("Invalid Request")

def process_data_hypothyroid(request):
    if request.method == "POST":
        Age = float(request.POST.get('Age', 0))
        sex = float(request.POST.get('sex', 0))
        on_thyroxine = float(request.POST.get('on_thyroxine', 0))
        T3 = float(request.POST.get('T3', 0))
        TT4 = float(request.POST.get('TT4', 0))
        T3_measured = float(request.POST.get('T3_measured', 0))
        tsh = float(request.POST.get('tsh', 0))

        data = {
        'Age': Age, 'sex': sex, 'on_thyroxine': on_thyroxine,
        'T3': T3, 'TT4': TT4,
        'T3_measured': T3_measured, 'tsh': tsh
        }
        df = pd.DataFrame(data, index=[0])
        print(df)

        def get(Age, sex, on_thyroxine,tsh,T3_measured, T3, TT4):
            model = joblib.load(r"C:\B tech\internship ACITE\hypothyroid.pkl")
            input_data = [[Age, sex, on_thyroxine,tsh,T3_measured, T3, TT4]]
            prediction = model.predict(input_data)
            print(f"Prediction: {prediction}")
            return prediction

        p = get(
            df['Age'].iloc[0], df['sex'].iloc[0], df['on_thyroxine'].iloc[0], df['tsh'].iloc[0], df['T3_measured'].iloc[0], df['T3'].iloc[0],
            df['TT4'].iloc[0]
        )

        return render(request, "result.html", {'output':p[0]})
    return HttpResponse("Invalid Request")

def process_data_parkinson(request):
    if request.method == "POST":
        mdvp_fo_hz = float(request.POST.get('mdvp_fo_hz'))
        mdvp_fhi_hz = float(request.POST.get('mdvp_fhi_hz'))
        mdvp_flo_hz = float(request.POST.get('mdvp_flo_hz'))
        mdvp_jitter_percent = float(request.POST.get('mdvp_jitter_percent'))
        mdvp_jitter_abs = float(request.POST.get('mdvp_jitter_abs'))
        mdvp_rap = float(request.POST.get('mdvp_rap'))
        mdvp_ppq = float(request.POST.get('mdvp_ppq'))
        jitter_ddp = float(request.POST.get('jitter_ddp'))
        mdvp_shimmer = float(request.POST.get('mdvp_shimmer'))
        mdvp_shimmer_db = float(request.POST.get('mdvp_shimmer_db'))
        Shimmer_APQ3 = float(request.POST.get('Shimmer_APQ3'))
        Shimmer_APQ5 = float(request.POST.get('Shimmer_APQ5'))
        MDVP_APQ = float(request.POST.get('MDVP_APQ'))
        Shimmer_DDA = float(request.POST.get('Shimmer_DDA'))
        nhr = float(request.POST.get('nhr'))
        hnr = float(request.POST.get('hnr'))
        rpde = float(request.POST.get('rpde'))
        dfa = float(request.POST.get('dfa'))
        spread1 = float(request.POST.get('spread1'))
        spread2 = float(request.POST.get('spread2'))
        D2 = float(request.POST.get('D2'))
        PPE = float(request.POST.get('PPE'))

        data = {
            'mdvp_fo_hz': mdvp_fo_hz, 'mdvp_fhi_hz': mdvp_fhi_hz, 'mdvp_flo_hz': mdvp_flo_hz,
            'mdvp_jitter_percent': mdvp_jitter_percent, 'mdvp_jitter_abs': mdvp_jitter_abs,
            'mdvp_rap': mdvp_rap, 'mdvp_ppq': mdvp_ppq, 'jitter_ddp': jitter_ddp,
            'mdvp_shimmer': mdvp_shimmer, 'mdvp_shimmer_db': mdvp_shimmer_db,
            'Shimmer_APQ3': Shimmer_APQ3, 'Shimmer_APQ5': Shimmer_APQ5, 'MDVP_APQ': MDVP_APQ ,'Shimmer_DDA':Shimmer_DDA,
            'nhr': nhr, 'hnr': hnr, 'rpde': rpde, 'dfa': dfa,
            'spread1': spread1, 'spread2': spread2, 'D2': D2, 'PPE': PPE
        }
        df = pd.DataFrame(data, index=[0])
        print(df)

        def get(
            mdvp_fo_hz, mdvp_fhi_hz, mdvp_flo_hz, mdvp_jitter_percent, mdvp_jitter_abs,
            mdvp_rap, mdvp_ppq, jitter_ddp, mdvp_shimmer, mdvp_shimmer_db, 
            Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA,
            nhr, hnr, rpde, dfa, spread1, spread2, D2, PPE
        ):
            model = joblib.load(r"C:\B tech\internship ACITE\parkinson.pkl")
            input_data = [[
                mdvp_fo_hz, mdvp_fhi_hz, mdvp_flo_hz, mdvp_jitter_percent, mdvp_jitter_abs,
                mdvp_rap, mdvp_ppq, jitter_ddp, mdvp_shimmer, mdvp_shimmer_db,
                Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA,
                nhr, hnr, rpde, dfa, spread1, spread2, D2, PPE
            ]]
            prediction = model.predict(input_data)
            print(f"Prediction: {prediction}")
            return prediction

        p = get(
            df['mdvp_fo_hz'].iloc[0], df['mdvp_fhi_hz'].iloc[0], df['mdvp_flo_hz'].iloc[0],
            df['mdvp_jitter_percent'].iloc[0], df['mdvp_jitter_abs'].iloc[0], df['mdvp_rap'].iloc[0],
            df['mdvp_ppq'].iloc[0], df['jitter_ddp'].iloc[0], df['mdvp_shimmer'].iloc[0], df['mdvp_shimmer_db'].iloc[0],
            df['Shimmer_APQ3'].iloc[0], df['Shimmer_APQ5'].iloc[0], df['MDVP_APQ'].iloc[0], df['Shimmer_DDA'].iloc[0],
            df['nhr'].iloc[0], df['hnr'].iloc[0], df['rpde'].iloc[0],
            df['dfa'].iloc[0], df['spread1'].iloc[0], df['spread2'].iloc[0], df['D2'].iloc[0], df['PPE'].iloc[0]
        )

        
        return render(request, "result.html", {'output':p[0]})
    return HttpResponse("Invalid Request")

def process_data_lungcancer(request):
    if request.method == "POST":
        Age = float(request.POST.get('Age'))
        Gender = float(request.POST.get('Sex'))
        Smoking = float(request.POST.get('Smoking'))
        yellow_fingers = float(request.POST.get('yellow_fingers'))
        anxiety = float(request.POST.get('anxiety'))
        peer_pressure = float(request.POST.get('peer_pressure'))
        chronic_disease = float(request.POST.get('chronic_disease'))
        fatigue = float(request.POST.get('fatigue'))
        allergy = float(request.POST.get('allergy'))
        wheezing = float(request.POST.get('wheezing'))
        alcohol_consuming = float(request.POST.get('alcohol_consuming'))
        coughing = float(request.POST.get('coughing'))
        shortness_of_breath = float(request.POST.get('shortness_of_breath'))
        swallowing_difficulty = float(request.POST.get('swallowing_difficulty'))
        chest_pain = float(request.POST.get('chest_pain'))

        data = {
            'Age': Age, 'Gender': Gender, 'Smoking': Smoking, 
            'Yellow_Fingers': yellow_fingers, 'Anxiety': anxiety, 'Peer_Pressure': peer_pressure, 
            'Chronic_Disease': chronic_disease, 'Fatigue': fatigue, 'Allergy': allergy, 'Wheezing': wheezing, 
            'Alcohol_Consuming': alcohol_consuming, 'Coughing': coughing, 'Shortness_of_Breath': shortness_of_breath, 
            'Swallowing_Difficulty': swallowing_difficulty, 'Chest_Pain': chest_pain
        }
        df = pd.DataFrame(data, index=[0])
        print(df)

        def get(
            Age, Gender, Smoking, Yellow_Fingers, Anxiety, Peer_Pressure, Chronic_Disease, 
            Fatigue, Allergy, Wheezing, Alcohol_Consuming, Coughing, Shortness_of_Breath, 
            Swallowing_Difficulty, Chest_Pain
        ):
            model = joblib.load(r"C:\B tech\internship ACITE\lungs.pkl")
            input_data = [[
                Age, Gender, Smoking, Yellow_Fingers, Anxiety, Peer_Pressure, Chronic_Disease,
                Fatigue, Allergy, Wheezing, Alcohol_Consuming, Coughing, Shortness_of_Breath,
                Swallowing_Difficulty, Chest_Pain
            ]]
            prediction = model.predict(input_data)
            print(f"Prediction: {prediction}")
            return prediction

        # Calling the function using values from a DataFrame
        p = get(
            df['Age'].iloc[0], df['Gender'].iloc[0], df['Smoking'].iloc[0], df['Yellow_Fingers'].iloc[0],
            df['Anxiety'].iloc[0], df['Peer_Pressure'].iloc[0], df['Chronic_Disease'].iloc[0],
            df['Fatigue'].iloc[0], df['Allergy'].iloc[0], df['Wheezing'].iloc[0],
            df['Alcohol_Consuming'].iloc[0], df['Coughing'].iloc[0], df['Shortness_of_Breath'].iloc[0],
            df['Swallowing_Difficulty'].iloc[0], df['Chest_Pain'].iloc[0]
        )


        return render(request, "result.html", {'output':p[0]})
    return HttpResponse("Invalid Request")
 