import streamlit as st

st.set_page_config(page_title='视频播放', page_icon='📺')

st.header("🎬视频播放器")

# 在内存中初始化一个ind,当内存中没有'ind'的时候，才初始化
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

#视频数组
video_obj=[{"url":"https://www.w3school.com.cn/example/html5/mov_bbb.mp4"
            },
           {"url":"https://www.w3schools.com/html/movie.mp4"
               },
           {"url":"https://media.w3.org/2010/05/sintel/trailer.mp4"
               }
           ]

image_obj = [{
        'url': 'https://file1.shop265.com/tk/20200711/702f97fdf525bced71fc66cb6b12dc19.jpg',
        'title': '夕阳'
    },{
        'url': 'https://cbu01.alicdn.com/img/ibank/O1CN016CtFOz1IMcvdJr84O_!!2214758190879-0-cib.jpg',
        'title': '鸡仔'
    }, {
        'url': 'https://n.sinaimg.cn/sinacn10109/300/w1620h1080/20190813/a52b-icapxph8830658.jpg',
        'title': '大海'
    }]

st.subheader("视频播放")
st.video(video_obj[st.session_state['ind']]["url"])

st.subheader("自然风光")
st.write('''描述：美丽的景观，夕阳，公仔\n
时长：2:15|分类：自然''')
st.subheader("视频库")
st.write('点击图片选择视频')
city = st.selectbox('全部',["一","二","三"])

# 根据返回值不同，选择不同的特色回答

if city=='一':
    st.session_state['ind'] =0
elif city=='二':
    st.session_state['ind'] =1
elif city=='三':
    st.session_state['ind'] =2

# 创建三列布局显示图片

for i, img in enumerate(image_obj):        
    # 添加透明按钮捕获点击
    if st.button("", key=f"img_btn_{i}"):
        st.session_state['ind'] = i
    # 显示图片
    st.image(img['url'],caption=img['title'])




    

