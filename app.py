
import scikit-learn
import pickle
import streamlit as st




st.header('Выявление сердечно-сосудистых заболеваний')
st.write('На этом сайте представлен предсказатель сердечно-сосудистых заболеваний. Он поможет Вам определить стоит ли посетить врача или нет, надеюсь кому-то он будет полезен.')
age = st.slider('Ваш возраст', 20, 70) * 365
height = st.slider('Ваш рост', 100, 250)
weight = st.slider('Ваш вес', 30, 183)
ap_hi = st.slider('Систолическое (верхнее) давление', 70, 210)
ap_lo = st.slider('Диастолическое (нижнее) давление', 30, 160)
male = st.selectbox('Ваш пол', ['мужской', 'женский'])
gluc = st.selectbox('Уровень глюкозы', ['низкий', 'средний', 'высокий'])
chol = st.selectbox('Уровень холестерина', ['низкий', 'средний', 'высокий'])
smoke = st.checkbox('Отметьте, если курите', key='курит')
alco = st.checkbox('Отметьте, если употребляете алкоголь', key='выпивает')
active = st.checkbox('Отметьте, если ведете активный образ жизни', key='физкультурник')

st.write(height, weight, ap_lo,ap_hi, male, gluc, chol, smoke, alco, active)

if male == 'мужской':
    gender = 2
else:
    gender = 1

if chol == 'низкий':
    ch = 2
elif chol == 'средний':
    ch = 1
else:
    ch = 3

if gluc == 'низкий':
    gl = 2
elif gluc == 'средний':
    gl = 1
else:
    gl = 3

if smoke == True:
    sm = 1
else:
    sm = 0

if alco == True:
    al = 1
else:
    al = 0

if active == True:
    act = 1
else:
    act = 0



a = []
a.append(age)
a.append(gender)
a.append(height)
a.append(weight)
a.append(ap_hi)
a.append(ap_lo)
a.append(ch)
a.append(gl)
a.append(sm)
a.append(al)
a.append(act)



def load():
    with open('heart_desease_model.pcl', 'rb') as fid:
        return pickle.load(fid)


model = load()
y_pr = model.predict_proba([[age, gender, height, weight, ap_hi, ap_lo, ch, gl, sm, al, act]])[:, 1]
st.write(f'Вероятность сердечно-сосудистого заболевания составляет: {round(float(y_pr), 3)}')

