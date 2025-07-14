# import streamlit as st
# import os
# import json
# from pathlib import Path

# st.set_page_config(page_title="Day 1-100", page_icon="📅")
# st.title("🌟 100件最重要的小事 · Day 1 - 100")

# # 定义感官标签和子类标签
# sense_tags = {
#     "👃 香味": ["🐶 动物", "🌿 自然", "🏠 家", "📚 书"],
#     "🤲 触感": ["人", "动物", "家"],
#     "👀 看到": ["🎨 颜色", "自然", "人", "动物"],
#     "👄 口感": ["食物", "饮品", "水果"],
#     "👂 听到": ["音乐", "人声", "自然"]
# }

# # 创建本地数据文件夹
# DATA_DIR = Path("data")
# DATA_DIR.mkdir(exist_ok=True)

# # 显示网格 4*25
# cols = st.columns(4)
# for i in range(100):
#     col = cols[i % 4]
#     with col:
#         if st.button(f"Day {i+1}", key=f"day{i+1}"):
#             st.session_state["selected_day"] = i + 1
#             st.rerun()  # ✅ 替换这里

# # 记录界面
# if "selected_day" in st.session_state:
#     st.markdown("---")
#     day = st.session_state["selected_day"]
#     st.subheader(f"📝 填写 Day {day} 的小事")

#     # 选择感官标签
#     main_tag = st.selectbox("选择一个感官分类", list(sense_tags.keys()))
#     sub_tag = st.selectbox("选择具体类型", sense_tags[main_tag])

#     # 输入内容
#     icon = st.text_input("选择一个小图标（可输入emoji）")
#     note = st.text_area("写下一句话或一段话记录这件小事")

#     # 文件上传
#     uploaded_file = st.file_uploader("可以上传一张图片 / 音频 / 视频", type=["png", "jpg", "jpeg", "mp3", "mp4"])

#     # 保存按钮
#     if st.button("💾 保存这件小事"):
#         record = {
#             "day": day,
#             "main_tag": main_tag,
#             "sub_tag": sub_tag,
#             "icon": icon,
#             "note": note,
#         }

#         # 保存记录
#         record_path = DATA_DIR / f"day_{day}.json"
#         with open(record_path, "w", encoding="utf-8") as f:
#             json.dump(record, f, ensure_ascii=False, indent=2)

#         # 保存媒体文件
#         if uploaded_file:
#             media_path = DATA_DIR / f"day_{day}_{uploaded_file.name}"
#             with open(media_path, "wb") as f:
#                 f.write(uploaded_file.getbuffer())

#         st.success("小事已保存！🥕")
#         del st.session_state["selected_day"]
#         st.rerun()  # ✅ 替换这里



import streamlit as st
import os
import json
from pathlib import Path

st.set_page_config(page_title="Little things 1-100", page_icon="📅")
st.title("🌟 100件最重要的小事")

sense_tags = {
    "👃 香味": ["🐶 动物", "🌿 自然", "🏠 家", "📚 书"],
    "🤲 触感": ["🧍 人", "🐱 动物", "🏠 家"],
    "👀 看到": ["🎨 颜色", "🌳 自然", "🧍 人", "🐶 动物"],
    "👄 口感": ["🍙 食物", "🍹 饮品", "🍓 水果"],
    "👂 听到": ["🎵 音乐", "🗣️ 人声", "🌧️ 自然"]
}

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

cols = st.columns(4)

# 每个按钮 + 展开输入界面
for i in range(100):
    col = cols[i % 4]
    with col:
        if st.button(f"Day {i + 1}", key=f"btn_{i + 1}"):
            st.session_state["selected_day"] = i + 1

# 显示展开输入框
if "selected_day" in st.session_state:
    day = st.session_state["selected_day"]
    data_path = DATA_DIR / f"thing_{day}.json"
    
    # 加载已保存数据
    saved_data = {}
    if data_path.exists():
        with open(data_path, "r", encoding="utf-8") as f:
            saved_data = json.load(f)

    with st.expander(f"📝 Day {day} 的小事", expanded=True):
        main_tag = st.selectbox("选择一个感官分类", list(sense_tags.keys()), 
                                index=list(sense_tags.keys()).index(saved_data.get("main_tag", "👃 香味")))
        sub_tag = st.selectbox("选择具体类型", sense_tags[main_tag], 
                               index=sense_tags[main_tag].index(saved_data.get("sub_tag", sense_tags[main_tag][0])))
        icon = st.text_input("选择一个小图标（可输入emoji）", value=saved_data.get("icon", ""))
        note = st.text_area("写下一句话或一段话记录这件小事", value=saved_data.get("note", ""))

        uploaded_file = st.file_uploader("上传图片 / 音频 / 视频", type=["png", "jpg", "jpeg", "mp3", "mp4", "mpeg4"])

        if st.button("💾 保存这件小事"):
            record = {
                "thing": day,
                "main_tag": main_tag,
                "sub_tag": sub_tag,
                "icon": icon,
                "note": note,
            }
            with open(data_path, "w", encoding="utf-8") as f:
                json.dump(record, f, ensure_ascii=False, indent=2)

            if uploaded_file:
                media_path = DATA_DIR / f"thing_{day}_{uploaded_file.name}"
                with open(media_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

            st.success("✅ 小事已保存！")
            del st.session_state["selected_day"]
            st.experimental_rerun()