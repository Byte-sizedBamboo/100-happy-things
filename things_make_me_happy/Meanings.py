# import streamlit as st

# st.set_page_config(page_title="最重要的小事", page_icon="🥕")

# # 设置背景颜色
# st.markdown("""
#     <style>
#     [data-testid="stAppViewContainer"] {
#         background-color: #FFF8F0;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # 正文内容
# st.markdown("""
# # 100件最重要的小事 🥕

# <div style='color:#666; line-height: 2; font-size: 17px;'>
# 耳朵是一种很奇怪的器官<br>
# ————当一个声音出现在耳边很久，<br>
# 它就会渐渐习惯、适应，<br>
# 直到再也听不见那个声音。<br><br>
# 眼睛也是这样的器官吗？<br>
# 我们会不会总是出现在对方眼前，<br>
# 就慢慢看不见对方了？
# </div>

# ---

# 这是一个记录小幸福的网页工具。每次你想起一件让你觉得幸福的小事，都可以点进来填写。
# """, unsafe_allow_html=True)

# # st.markdown("""
# # <!-- 引入 Google 中文字体 -->
# # <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC&display=swap" rel="stylesheet">

# # <style>
# # /* 设置左边栏样式 */
# # section[data-testid="stSidebar"] {
# #     background-color: #FFDAC1;
# #     padding: 1.5rem;
# # }

# # /* 左边栏内所有文字样式 */
# # section[data-testid="stSidebar"] * {
# #     font-family: 'Noto Sans SC', sans-serif !important;
# #     font-size: 16px;
# #     color: #333;
# # }

# # /* 左侧导航按钮 hover 效果 */
# # section[data-testid="stSidebar"] .css-1v0mbdj:hover {
# #     background-color: #FFDAC1;
# #     border-radius: 6px;
# # }
# # </style>
# # """, unsafe_allow_html=True)

# # 跳转按钮
# if st.button("开始填写小幸福"):
#     st.switch_page("pages/enterluck.py")



# import streamlit as st

# st.set_page_config(page_title="最重要的小事", page_icon="🥕")

# # 设置背景颜色 + 侧边栏背景颜色
# st.markdown("""
#     <style>
#     [data-testid="stAppViewContainer"] {
#         background-color: #FFF8F0;  /* 米白色背景 */
#     }
#     section[data-testid="stSidebar"] {
#         background-color: #F5E3DA;  /* 浅棕色侧边栏 */
#     }
#     /* 去除 sidebar 顶部 keyboard_control */
#     [data-testid="stSidebarNav"]::before {
#         content: "";
#         display: none;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # 正文内容
# st.markdown("""
# # 100件最重要的小事 🥕

# <div style='color:#666; line-height: 2; font-size: 17px;'>
# 耳朵是一种很奇怪的器官<br>
# ————当一个声音出现在耳边很久，<br>
# 它就会渐渐习惯、适应，<br>
# 直到再也听不见那个声音。<br><br>
# 眼睛也是这样的器官吗？<br>
# 我们会不会总是出现在对方眼前，<br>
# 就慢慢看不见对方了？
# </div>

# ---

# 这是一个记录小幸福的网页工具。每次你想起一件让你觉得幸福的小事，都可以点进来填写。
# """, unsafe_allow_html=True)

# # 跳转按钮
# if st.button("开始填写小幸福"):
#     st.switch_page("pages/enterluck.py")







import streamlit as st

st.set_page_config(page_title="最重要的小事", page_icon="🥕")

# 设置背景颜色、侧边栏颜色、文字颜色
st.markdown("""
    <style>
    /* 背景颜色 */
    [data-testid="stAppViewContainer"] {
        background-color: #FFF8F0;
        color: #5D4037;  /* 全站文字颜色 */
    }

    /* 侧边栏背景 */
    section[data-testid="stSidebar"] {
        background-color: #F5E3DA;
        color: #5D4037;
    }

    /* 所有文字颜色（增强兼容性） */
    html, body, [class*="css"] {
        color: #5D4037;
    }

    /* 去除 keyboard_double_arrow */
    [data-testid="stSidebarNav"]::before {
        content: "";
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# 正文内容
st.markdown("""
# 100件最重要的小事 🥕

<div style='line-height: 2; font-size: 17px; color: #5D4037;'>
耳朵是一种很奇怪的器官<br>
————当一个声音出现在耳边很久，<br>
它就会渐渐习惯、适应，<br>
直到再也听不见那个声音。<br><br>
眼睛也是这样的器官吗？<br>
我们会不会总是出现在对方眼前，<br>
就慢慢看不见对方了？
</div>

---

这是一个记录小幸福的网页工具。每次你想起一件让你觉得幸福的小事，都可以点进来填写。
""", unsafe_allow_html=True)

# 跳转按钮
if st.button("开始填写小幸福"):
    st.switch_page("pages/My little things.py")

