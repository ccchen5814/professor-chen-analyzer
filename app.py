import streamlit as st
import time

# 設定網頁標題與風格
st.set_page_config(page_title="陳教授的系統分析儀", layout="centered")
st.title("🌱 陳教授的系統分析儀")
st.subheader("循環經濟｜微型化生物處理系統模擬器")
st.markdown("---")

# 側邊欄：顯示您的卡通形象
st.sidebar.image("your_cartoon_image.png", caption="陳教授 (生物處理技術專家)")
st.sidebar.info("請調整參數，模擬反應器運作狀態。")

# 1. 輸入面板
st.header("⚙️ 模擬參數設置")
cn_ratio = st.slider("資材配比 (C/N Ratio)", 10, 50, 30, help="25-30為黃金比例")
moisture = st.slider("水分控制 (%)", 20, 90, 60, help="60%為最佳代謝環境")
temp = st.slider("環境溫度 (°C)", 10, 50, 30, help="25-35°C 為微生物適宜區")

# 選擇廢棄物類型
waste_type = st.selectbox("選擇處理目標", ["落葉 (高碳)", "廚餘 (高氮)"])

if st.button("執行系統分析"):
    with st.spinner('陳教授正在計算反應器數據中...'):
        time.sleep(1.5) # 模擬運算延遲
        
    # 2. 核心運算邏輯
    efficiency = 0
    feedback = ""
    
    # 簡單的系統工程判斷邏輯
    if 25 <= cn_ratio <= 35 and 55 <= moisture <= 65 and 25 <= temp <= 35:
        efficiency = 95
        state = "穩定運作 (🟢)"
        feedback = f"### 完美！\n這是微生物分解的最適環境。養分平衡，能加速腐植化，將{waste_type}轉化為優質肥料，顯著減少碳排。"
    elif moisture > 80:
        efficiency = 30
        state = "系統失控 (🔴)"
        feedback = "### 警告！\n水分過多導致孔隙被堵塞，氧氣無法傳遞，系統已轉為厭氧發酵，易產生甲烷（強效溫室氣體）。"
    elif cn_ratio < 20:
        efficiency = 50
        state = "酸化風險 (🟡)"
        feedback = "### 調整建議：\n氮源過高！微生物分解產生過多氨氣與惡臭，請增加褐色資材（高碳）來稀釋。"
    else:
        efficiency = 40
        state = "代謝遲緩 (🟠)"
        feedback = "### 代謝抑制：\n環境條件未達最佳化，微生物活性降低。建議根據碳氮比特性微調原料配比。"

    # 3. 視覺化分析區
    st.markdown("---")
    col1, col2 = st.columns(2)
    col1.metric("反應器狀態", state)
    col2.metric("降解效率", f"{efficiency}%")
    
    st.progress(efficiency / 100)
    
    # 4. 陳教授點評
    st.success(feedback)
    
    st.info("💡 **陳教授小學堂**：循環的意義，不僅在於物質的轉化，更在於我們如何以系統工程的視角，與生態規律對話。")

# 腳本結尾
st.markdown("---")
st.caption("© 2026 陳教授 - 環境科學與資源循環研究室")
