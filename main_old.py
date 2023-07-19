import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プレグレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar =st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}' )
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!'
#st.write('Interactive Widgets')
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
   right_column.write('ここは右カラム')

expander1= st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2= st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3= st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')

#st.write('Display Image')
#if st.checkbox('Show Image'):
#    img =Image.open('cat.jpg')
#    st.image(img, caption='Neko', use_column_width=True)

#option = st.selectbox(
#    'あなたが好きな数字を教えてください',
#    list(range(1,10))
#)
#'あなたが好きな数字は', option, 'です'

#st.write('DataFrame')
#df = pd.DataFrame(
#    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#    columns=['lat', 'lon']
#)
#st.dataframe(df.style.highlight_max(axis=0))
#st.map(df)
