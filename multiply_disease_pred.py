# -*- coding: utf-8 -*-
"""
Creer le Samedi 25 Juin 2022

@author: ADOU Kouame Mathurin
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models
filename1='./diabetes_model.sav'
filename2='./heart_disease_model.sav'
filename3='./parkinsons_model.sav'

diabetes_model = pickle.load(open(filename1, 'rb'))

heart_disease_model = pickle.load(open(filename2, 'rb'))

parkinsons_model = pickle.load(open(filename3, 'rb'))



# sidebar for navigation
with st.sidebar: 
    selected = option_menu('Système de prédiction de maladies multiples',
                          ['Prédiction du diabète',
                           'Prédiction des maladies cardiaques',
                           'Prédiction de la maladie de Parkinson'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Prédiction du diabète'):
    
    # page title
    st.title('Prédiction du diabète à l\'aide du Machine Learning')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Résultat du test de diabète'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'La personne est diabétique'
            # Afficher le diagnostic pour une personne diabétique
          st.warning(diab_diagnosis)
            
            # Afficher les conseils pour gérer le diabète
          st.write("Conseils pour gérer le diabète :")
          st.write("1. Suivez les recommandations médicales : Écoutez votre professionnel de la santé et suivez votre plan de traitement.")
          st.write("2. Contrôlez régulièrement votre taux de glucose sanguin : Mesurez votre glycémie comme recommandé.")
          st.write("3. Adoptez un régime alimentaire équilibré : Consultez un diététicien pour un plan alimentaire adapté.")
          st.write("4. Gérez les glucides : Apprenez à compter les glucides pour ajuster votre médication.")
          st.write("5. Faites de l'exercice régulièrement : Suivez un programme d'exercice approuvé par votre médecin.")
          st.write("6. Surveillez votre poids : Maintenez un poids sain.")
          st.write("7. Évitez le tabac : Arrêtez de fumer si vous fumez.")
          st.write("8. Limitez la consommation d'alcool : Buvez de l'alcool avec modération.")
          st.write("9. Prenez soin de vos pieds et de votre peau : Inspectez régulièrement vos pieds et hydratez votre peau.")
          st.write("10. Restez informé : Apprenez constamment sur le diabète et ses traitements.")
          st.write("11. Gérez le stress : Utilisez des techniques de gestion du stress.")
          st.write("12. Consultez régulièrement votre médecin : Faites des bilans de santé réguliers.")

        else:
          diab_diagnosis = 'La personne n\'est pas diabétique'
            # Afficher le diagnostic pour une personne diabétique
          st.warning(diab_diagnosis)
            # Ajoutez les conseils si la personne n'est pas diabétique
          st.write("Conseils pour maintenir une bonne santé :")
          st.write("1. Adoptez une alimentation équilibrée : Consommez des fruits et des légumes frais, Choisissez des protéines maigres comme le poulet, le poisson et les légumineuses.")
          st.write("2. Contrôlez les portions : Évitez les portions excessives et surveillez votre apport calorique total.")
          st.write("3. Faites de l'exercice régulièrement : Essayez de faire au moins 30 minutes d'exercice modéré la plupart des jours de la semaine.")
          st.write("4. Surveillez votre poids : Maintenez un poids corporel sain en équilibrant votre apport calorique et votre dépense énergétique.")
          st.write("5. Évitez le tabac : Si vous fumez, envisagez d'arrêter. Le tabagisme est un facteur de risque pour de nombreuses maladies, dont le diabète de type 2.")
          st.write("6. Limitez la consommation d'alcool : Si vous buvez de l'alcool, faites-le avec modération.")
          st.write("7. Consultez régulièrement un professionnel de la santé : Effectuez des bilans de santé réguliers pour surveiller votre taux de glucose sanguin, votre pression artérielle, votre cholestérol, etc.")
          st.write("8. Gérez le stress : Le stress excessif peut avoir un impact négatif sur la santé. Apprenez des techniques de gestion du stress, comme la méditation, le yoga ou la relaxation.")
          st.write("9. Dormez suffisamment : Assurez-vous de dormir suffisamment chaque nuit pour favoriser la récupération et la régulation des hormones.")
          st.write("10. Soyez conscient des facteurs de risque : Si vous avez des antécédents familiaux de diabète ou d'autres facteurs de risque, discutez-en avec un professionnel de la santé.")
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Prédiction des maladies cardiaques'):
    
    # page title
    st.title('Prédiction des maladies cardiaques à l\'aide du Machine Learning')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Résultat du test de maladie cardiaque'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'La personne a une maladie cardiaque'
        else:
          heart_diagnosis = 'La personne n\'a pas de maladie cardiaque'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Prédiction des maladies cardiaques"):
    
    # page title
    st.title("Prédiction de la maladie de Parkinson à l\'aide du Machine Learning")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Résultat du test de la maladie de Parkinson"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "La personne a la maladie de Parkinson"
        else:
          parkinsons_diagnosis = "La personne n\'a pas la maladie de Parkinson"
        
    st.success(parkinsons_diagnosis)
