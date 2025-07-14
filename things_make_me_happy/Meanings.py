import streamlit as st
from PIL import Image

# 插入顶部大图
from PIL import Image
top_image = Image.open("images/cover_page.jpg")
st.image(top_image, use_column_width=True)


st.set_page_config(page_title="最重要的小事", page_icon="🥕")

# 页面样式设置
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #FFF8F0;
        color: #5D4037;
    }

    section[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #FFF8E7, #FDE6C3);
    }

    html, body, [class*="css"] {
        color: #5D4037;
    }

    [data-testid="stSidebarNav"]::before {
        content: "";
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# 语言选择
lang = st.selectbox("语言 Language", ["中文", "English"])

# 中文页面
if lang == "中文":
    st.markdown("""
    # 100件最重要的小事 🥕

    <div style='line-height: 2; font-size: 17px;'>
    <em>"耳朵是一种很奇怪的器官<br>
    ————当一个声音出现在耳边很久，它就会渐渐习惯、适应，直到再也听不见那个声音。<br>
    眼睛也是这样的器官吗？<br>
    我们会不会总是出现在对方眼前，就慢慢看不见对方了？"</em>
    </div>

    ---
    心理学中有一个概念叫做“hedonic treadmill（享乐适应）”，意思是：人对幸福和快乐的感受会随着时间而回归常态。<br>
    也就是说，即使我们曾经感到无比幸福，一旦这种感觉变成习惯，我们也会慢慢失去对它的感知。<br>

    很多时候，幸福被我们藏在了熟悉的日常中。<br>
    当你习惯了温暖的被窝，或每天清晨的阳光，你就可能忽略了它们所带来的幸福感。<br>
    </div>

    ---


    真正的幸福感，不在“拥有更多”，而在“我曾更有意识地活着”。<br>
    幸福可大可小————<br>
    也许是刚晒过太阳的被子的味道，<br>
    也许是穿上新袜子的那一瞬间，<br>
    也许是乘坐了一圈旋转木马，<br>
    也许是看到了草地上升起的萤火虫……<br>
    快乐也许就藏在你不经意的生活瞬间。<br>
    你的幸福由你定义✨。<br><br>

    每一件平凡快乐的小事，<br>
    都是属于你最重要的事。<br><br>

    这是一个记录小幸福的网页工具。每次想起一件让你觉得幸福的小事，都可以点进来填写 ✏️。
    """, unsafe_allow_html=True)

    if st.button("记录我最重要的小事"):
        st.switch_page("pages/Daily.py")

# 英文页面
else:
    st.markdown("""
    # 100 Most Important Little Things 🥕

    <div style='line-height: 1.5; font-size: 17px;'>
    <em>"Ears are strange organs.<br>
    — When a sound lingers by its side for too long, it gradually gets used to it—adapts—until it can no longer hear it at all.<br><br>
    Are eyes like that too?<br>
    If we keep appearing before each other day after day, will we eventually stop seeing one another?"</em>
    </div>

    ---
     <div style='line-height: 1.5; font-size: 17px;'>
    In psychology, there’s a concept called the <em><strong>hedonic treadmill</strong></em> —<br>
    it refers to our natural tendency to return to a baseline level of happiness,<br>
    even after experiencing joy or comfort.<br>

    That means:<br>
    Happiness always hides in the routines we’ve grown used to.<br>
    Once we become familiar with the warmth of our bed,<br>
    we may forget how happy it once made us feel.<br>
    </div>

    ---
     <div style='line-height: 1.5; font-size: 20px;'>
    <strong>True happiness doesn’t lie in “having more,” but in “having lived more consciously.”</strong><br>
     <div style='line-height: 1.5; font-size: 17px;'>
    Happiness can be big or small —<br>
    It could be the smell of blankets warmed by the sun,<br>
    The moment you put on new socks,<br>
    A spin on the carousel,<br>
    Or catching a firefly rising from the grass...<br>
    Joy might hide in the unnoticed corners of your life.<br>
    Your happiness is yours to define ✨.<br><br>

    Every small and ordinary joy<br>
    Is one of your most important things.<br><br>

    This is a tool for recording little happy moments.  
    Whenever a moment of joy comes to mind, you can click and write it down ✏️.
    """, unsafe_allow_html=True)

    if st.button("Record my most important little thing"):
        st.switch_page("pages/Daily.py")
