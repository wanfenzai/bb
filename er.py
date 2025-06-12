import streamlit as st
import pandas as pd
import time
import random

# 假设数据字典，包含各餐厅在不同月份的人均消费
data = {
    "餐厅": ["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "西冷牛排店"],
    "类型": ["中餐", "中餐", "快餐", "自助餐", "西餐"],
    "评分": [4.2, 4.5, 4.0, 4.7, 4.3],
    "latitude": [22.853838, 22.965046, 22.812200, 22.809105, 22.839699],
    "longitude": [108.222177, 108.353921, 108.266629, 108.378664, 108.245804],
    "流量": [0,25,50,75,100],
    "一月": [10, 15, 20, 25, 30],
    "二月": [12, 18, 22, 27, 32],
    "三月": [14, 20, 24, 29, 34],
    "四月": [16, 22, 26, 31, 36],
    "五月": [18, 24, 28, 33, 38],
    "六月": [20, 26, 30, 35, 40],
    "七月": [22, 28, 32, 37, 42],
    "八月": [24, 30, 34, 39, 44],
    "九月": [26, 32, 36, 41, 46],
    "十月": [28, 34, 38, 43, 48],
    "十一月": [30, 36, 40, 45, 50],
    "十二月": [32, 38, 42, 47, 52],
    "月份": ["一月", "四月","七月", "十月", "十二月"],
    "星艺会尝不忘":[10, 15, 27, 18, 8], 
    "高峰柠檬鸭":[3, 7, 41, 21, 10],
    "复记老友粉":[5, 14, 19, 25, 7],
    "好友缘":[13, 19, 51, 66, 12],
    "西冷牛排店":[3, 8, 13, 18, 23],
    "时段":["10:00", "12:00", "14:00", "16:00", "18:00"]
}

# 构建 DataFrame
df = pd.DataFrame(data)

st.header('🍔美食探索')
st.text("探索广西南宁最受欢迎的美食地点！选择你感兴趣的餐厅类型，查看评分和位置。")

st.header('📍南宁特色美食地图')

# 在地图上展示餐厅的位置
st.map(df[["latitude", "longitude"]])

st.header('⭐餐厅评分')

# 绘制餐厅评分的柱状图
st.bar_chart(df, x="餐厅", y="评分")

st.header('💰餐厅月流水')

# 使用 st.line_chart 绘制折线图
st.line_chart(df,x="月份",y=["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "西冷牛排店"])

st.header('⏱用餐高峰时段')

# 绘制餐厅流量的面积图
st.area_chart(df,x="时段",y=["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "西冷牛排店"])

st.header('🍽餐厅详细')

city = st.selectbox(
    '选择餐厅：',
    ["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "西冷牛排店"],
    index=2
)

col1, col2 = st.columns(2)
with col1:
    df_info = df[df['餐厅'] == city].iloc[0]
    st.subheader(city)
    st.markdown(f"**评分：** {df_info['评分']}/5.0")
    st.markdown(f"**人均消费:** {df_info['十二月']}元")

with col2:
    st.subheader("详细信息")
    st.markdown(f"**评分:** {df_info['评分']}/5.0")
    st.markdown(f"**坐标:** {df_info['latitude']}, {df_info['longitude']}")


st.header("当前拥挤程度") # 创建章节
progress_text_1='84%拥挤'
# 创建进度条
my_bar=st.progress(85,text=progress_text_1)

st.subheader("🎲今日午餐")
if st.button('帮我推荐午餐'):
    num=random.randint(1,10)%5

    if(num==0):
        st.text("今日推荐：星艺会尝不忘")
        st.image("https://cp1.douguo.com/upload/caiku/2/6/6/960_26286938fcda84f4b9638202951297b6.jpeg", caption='美食午餐等你')
    if(num==1):
        st.text("今日推荐：高峰柠檬鸭")
        st.image("https://cp1.douguo.com/upload/caiku/2/6/6/960_26286938fcda84f4b9638202951297b6.jpeg", caption='美食午餐等你')
    if(num==2):
        st.text("今日推荐：复记老友粉")
        st.image("https://cp1.douguo.com/upload/caiku/2/6/6/960_26286938fcda84f4b9638202951297b6.jpeg", caption='美食午餐等你')        
    if(num==3):
        st.text( "今日推荐：好友缘")
        st.image("https://cp1.douguo.com/upload/caiku/2/6/6/960_26286938fcda84f4b9638202951297b6.jpeg", caption='美食午餐等你')
    if(num==4):
        st.text("今日推荐：西冷牛排店")
        st.image("https://cp1.douguo.com/upload/caiku/2/6/6/960_26286938fcda84f4b9638202951297b6.jpeg", caption='美食午餐等你')


