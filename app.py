import streamlit as st

# 網頁設定
st.set_page_config(page_title="循環魔法師：C/N 配對挑戰", layout="centered")

# 標題與形象
st.title("🧙‍♂️ 循環魔法師：C/N 配對挑戰")
st.markdown("---")

# 側邊欄：陳教授形象
st.sidebar.image("image.png", use_container_width=True)
st.sidebar.write("### 陳教授的系統小叮嚀")
st.sidebar.write("透過調整高碳與高氮資材，找到微生物最快樂的黃金比例！")

# 1. 互動組件 (Sliders)
st.header("⚙️ 調整你的資材比例")
col1, col2 = st.columns(2)
with col1:
    brown_material = st.slider("高碳 (落葉、碎紙)", 0, 100, 50, help="這是微生物的能量來源")
with col2:
    green_material = st.slider("高氮 (果皮、廚餘)", 0, 100, 50, help="這是微生物的蛋白質來源")

# 2. 運算邏輯
if brown_material + green_material == 0:
    cn_ratio = 0
else:
    # 假設褐色資材碳含量 50%，綠色資材氮含量 2% (簡化模擬)
    # 這裡的邏輯可以根據您的專業進行微調
    cn_ratio = (brown_material * 0.5) / (green_material * 0.02) if green_material > 0 else 99

# 計算按鈕
if st.button("計算預估 C/N 比"):
    st.write(f"### 目前預估 C/N 比：{cn_ratio:.1f}")
    
    # 微生物動態顯示與陳教授點評
    st.markdown("---")
    st.subheader("微生物狀態：")
    
    if cn_ratio < 20 and cn_ratio > 0:
        st.write("## 🤢 缺氧/過臭")
        st.warning("「唉呀，蛋白質太多了！微生物分解會產生氨氣與惡臭，且容易引發酸化，請增加高碳資材來稀釋。」")
    elif 20 <= cn_ratio <= 35:
        st.write("## 🥳 黃金比例 (高效)")
        st.success("「完美！這是微生物分解的最適環境。養分平衡，能加速腐植化，將落葉轉化為優質肥料，顯著減少碳排。」")
    elif cn_ratio > 35:
        st.write("## 😴 代謝緩慢")
        st.info("「能量太足但營養不足！微生物會因為缺乏蛋白質而處於停工狀態，分解速率會變得非常緩慢。」")
    else:
        st.write("請設定資材比例以開始挑戰！")

# 底部人文總結
st.markdown("---")
st.caption("循環的意義，不僅在於物質的轉化，更在於我們如何以系統工程的角度，與自然規律對話。 —— 陳教授")
