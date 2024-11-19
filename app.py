# 분류 모델 웹앱 만들기

import streamlit as st

# 1. 기계학습 모델 파일 로드
import joblib
model = joblib.load('logistic_regression_model.pkl') 

# 2. 모델 설명
st.title('비만 분류기')
col1, col2,col3 = st.columns( 3 )      # 몇 개의 컬럼으로 나눌까?
with col1:
      st.subheader('식습관으로 나의 비만 예측하고 건강 관리 시작하기')
      st.write(' - 기계학습 알고리즘 : 로지스틱 회귀 ')
      st.write(' - 학습 데이터 출처 : https://www.kaggle.com/datasets/muhramasaputra/obesity-based-on-eating-habits-and-physical-cond')
      st.write(' - 훈련    데이터 : 2111건')
      st.write(' - 테스트 데이터 : 634건')
      st.write(' - 모델 정확도 : 0.74')

# 3. 데이터시각화
with col2:
      st.subheader('데이터시각화1')
      st.image('__2.png' )   # 이미지 불러오기
with col3:
      st.subheader('데이터시각화2')
      st.image('__3.png')
st.subheader('모델 활용')
st.write('**** 밑의 내용을 입력해주세요. 인공지능이 당신의 비만도를 알려드립니다!')

a = st.number_input(' 나이 입력 ', value=0)
b = st.number_input(' 성별 입력(남자면1 여자면0) ', value=0)
c = st.number_input(' 가족중 비만인 사람이 있나요?(예면1 아니면2) ', value=0)
d = st.number_input(' 고칼로리 음식을 자주 섭취하시나요?(예면1 아니면2)', value=0)
e = st.number_input(' 야채를 어느정도 먹는지 1부터3 척도로 알려주십시오 , value=0)
f = st.number_input(' 식사를 하루 몇 끼 하시나요? ', value=0)
g = st.number_input(' 간식을 얼마나 드시는지 0에서3 척도로 알려주십시오.', value=0)
h = st.number_input(' 신체활동을 얼마나 하시는지 0에서3 척도로 알려주십시오. ', value=0)

if st.button('합불분류'):              # 사용자가 '합불분류' 버튼을 누르면
        input_data = [[ a,b,c,d,e,f,g,h ]]          # 사용자가 입력한 a,b,c 를 input_data에 저장하고
        p = model.predict(input_data)      # model이 분류한 값을 p에 저장한다
        if p[0] == 1 :
              st.success('비만으로 예측됩니다.')
        else:
              st.success('비만이 아닌 것으로 예측됩니다.')
