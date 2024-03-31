import streamlit as st
import pandas as pd
import datetime

# openweathermapから取得
import weather 

# 気温による服装のURLを取得
import clothing_url
clothing_url_dict = clothing_url.clothing_url_dict

# 今日の日付を取得
dt = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
today_year = dt.year
today_month = dt.month
today_day = dt.day

# csv(.csv)の読み込み
df = pd.read_csv('m_d_data.csv')
df = df.set_index('日付')


# 天気および天気予報の取得

#（現在）気温、最高気温、最低気温、湿度、天気
now_weather = weather.get_now_weather()

#（予報）最高気温、最低気温、天気
for_weather = weather.get_for_weather()






# タイトル
st.title(f' {today_year} 年 {today_month} 月 {today_day} 日')

# 気温を変数に格納
today_temp = int(now_weather[0])
today_max_temp = max(int(now_weather[1]+0.99),int(for_weather[0]+0.99))
today_min_temp = min(int(now_weather[2]),int(for_weather[1]))

# 3カラムで表示
col1, col2, col3 = st.columns(3)

col1.metric("最高気温", f"{today_max_temp} ℃")
col2.metric("最低気温", f"{today_min_temp} ℃")
col3.metric("湿度", f"{now_weather[3]} %")

"""
#### 今日の気温に適した服装
"""
if 5 <= today_temp <= 30:
    st.page_link(page=clothing_url_dict[today_temp], label=f'現在の気温 **{today_temp}** ℃に適した服装（Oggi.jp）',icon='👔')
if 5 <= today_max_temp <= 30:
    st.page_link(page=clothing_url_dict[today_max_temp], label=f'最高気温 **{today_max_temp}** ℃に適した服装（Oggi.jp）',icon='👕')
if 5 <= today_min_temp <= 30:
    st.page_link(page=clothing_url_dict[today_min_temp], label=f'最低気温 **{today_min_temp}** ℃に適した服装（Oggi.jp）',icon='🧥')

# 2カラムで表示
left_col, right_col = st.columns(2)

with left_col:
    """
    #### 現在の東京
    """
    now_max_temp = f'<span style="color:red">{now_weather[1]}</span>'
    now_min_temp = f'<span style="color:blue">{now_weather[2]}</span>'

    st.write(f'気温は **{now_weather[0]}** ℃')
    st.write(f'最高気温は **{now_max_temp}** ℃',unsafe_allow_html=True)
    st.write(f'最低気温は **{now_min_temp}** ℃',unsafe_allow_html=True)
    st.write(f'湿度は **{now_weather[3]}** %')
    st.write(f'天気は **{now_weather[4]}**')

with right_col:
    """
    #### 現在から10時間後までの予報
    """
    for_max_temp = f'<span style="color:red">{for_weather[0]}</span>'
    for_min_temp = f'<span style="color:blue">{for_weather[1]}</span>'

    st.write(f'最高気温は **{for_max_temp}** ℃',unsafe_allow_html=True)
    st.write(f'最低気温は **{for_min_temp}** ℃',unsafe_allow_html=True)
    st.write(f'天気は **{for_weather[2]}**')




st.subheader(f'過去24年間の東京の {today_month} 月 {today_day} 日の平均気温')

#過去の今日の平均気温
df_today = df[f'{today_month}/{today_day}':f'{today_month}/{today_day}']

#表
st.dataframe(df_today)

#折れ線グラフ
st.line_chart(df_today.T)


st.subheader('東京の過去の平均気温')

option_year = st.selectbox(
    '年を選択してください',
    list(range(2000, 2024))
)
df_year = pd.DataFrame(df.iloc[:, option_year-2000])

# 表
'', option_year, '年の平均気温'
st.dataframe(df_year.T)

# 折れ線グラフ
# 日付を1/1 -> 01/01に直す（ソートのため）

df_tmp = pd.read_csv('temp_data.csv')
date_list = list(df_tmp['日付'])
df_tmp = df_tmp.drop(columns='日付',axis=1)

date_new = []
for i in range(len(df_tmp)):
    s = date_list[i]
    if s[1] == '月':
        s = '0' + s 
    if s[-3] == '月':
        s = s[:3] + '0' + s[3:]
    s = s.replace('月','/').replace('日','')
    date_new.append(s)
df_tmp['日付'] = date_new
df_0101 = df_tmp.set_index('日付')

df_0101_year = pd.DataFrame(df_0101.iloc[:, option_year-2000])

'', option_year, '年の平均気温'
st.line_chart(df_0101_year)

