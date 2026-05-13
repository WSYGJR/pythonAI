import streamlit as st

import streamlit as st

st.set_page_config(
    page_title="入门",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")

#段落文字
st.write("This is ")
st.write(" ")

#图片
st.image("头像.jpg",width=500)

#视频
st.video("VID20251028201908(1).mp4")

#logo
st.logo("111.png")

#表格
student_data = {
    "姓名":["111","222","333"]
}
st.table(student_data)

#输入框
name = st.text_input("请输入姓名")
st.write(name)
#

gender = st.radio("请输入你的性别",["male","female"])
st.write(gender)
