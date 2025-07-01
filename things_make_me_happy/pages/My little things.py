import streamlit as st
import json
import os

st.set_page_config(page_title="填写小幸福", page_icon="🌱")

# 背景音乐
st.markdown("""
<audio autoplay loop>
  <source src="https://www.bensound.com/bensound-music/bensound-sunny.mp3" type="audio/mpeg">
</audio>
""", unsafe_allow_html=True)

# 美化输入框样式
st.markdown("""
<style>
    input {
        background-color: #fffafc;
        border-radius: 10px;
        padding: 8px;
        border: 1px solid #eee;
    }
    h1, h2 {
        font-family: "Comic Sans MS", cursive, sans-serif;
        color: #ff69b4;
    }
</style>
""", unsafe_allow_html=True)

# 数据保存路径
DATA_FILE = "data.json"

# 加载已有数据
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return [""] * 100

# 保存数据
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

st.markdown("# 🌱 填写你的100件小幸福")
st.markdown("> 随时可以回来继续填写，不必一次写完哦。")

# 加载现有数据
happiness_list = load_data()

# 显示输入框
for i in range(100):
    if i % 10 == 0:
        st.markdown(f"### 🌸 第 {i+1} ~ {i+10} 件小幸福")
    happiness_list[i] = st.text_input(f"**{i+1}.**", value=happiness_list[i], key=i)

# 保存按钮
if st.button("💾 保存"):
    save_data(happiness_list)
    st.success("已保存～期待你记录更多小幸福 💖")