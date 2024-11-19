# 분류 모델 웹앱 만들기

import streamlit as st

# 1. 기계학습 모델 파일 로드
import joblib
model = joblib.load('logistic_regression_model.pkl') 

# 2. 모델 설명
st.title('비만 분류기')
col1, col2,col3 = st.columns( 3 )      # 몇 개의 컬럼으로 나눌까?
with col1:
      st.subheader('모델 설명 ')
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
