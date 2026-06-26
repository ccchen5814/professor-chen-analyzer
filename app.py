import streamlit as st

# 網頁設定
st.set_page_config(page_title="陳教授的生物反應器模擬器", layout="centered")

st.title("🧪 陳教授的生物反應器模擬器")
st.markdown("將物料平衡、水力負荷與溫度動力學整合為一體的系統工程分析。")
st.sidebar.image("image.png", use_container_width=True)

# 1. 輸入面板
st.header("⚙️ 反應器操作參數設定")
brown_w = st.slider("褐色資材重量 (落葉) [kg]", 0.0, 100.0, 30.0)
green_w = st.slider("綠色資材重量 (廚餘) [kg]", 0.0, 100.0, 10.0)
moisture = st.slider("系統水分含量 (%)", 20, 90, 60, help="理想值 55-65%")
temp = st.slider("反應器溫度 (°C)", 10, 60, 30, help="理想值 25-35°C")

# 2. 專業計算邏輯
C_B, N_B = 45.0, 0.6
C_G, N_G = 10.0, 2.5
total_C = (brown_w * C_B) + (green_w * C_G)
total_N = (brown_w * N_B) + (green_w * N_G)
cn_ratio = total_C / total_N if total_N > 0 else 100.0

# 3. 系統效率評分 (結合多變數影響)
# 理想區間得分
cn_score = 1.0 if 25 <= cn_ratio <= 35 else 0.5
moisture_score = 1.0 if 55 <= moisture <= 65 else (0.7 if 40 <= moisture <= 80 else 0.3)
temp_score = 1.0 if 25 <= temp <= 35 else (0.8 if 20 <= temp <= 45 else 0.4)

efficiency = (cn_score * 0.5 + moisture_score * 0.3 + temp_score * 0.2) * 100

# 4. 分析結果
if st.button("啟動系統分析"):
    st.markdown("---")
    col1, col2 = st.columns(2)
    col1.metric("計算 C/N 比", f"{cn_ratio:.2f}")
    col2.metric("預估轉化效率", f"{efficiency:.0f}%")
    
    st.progress(efficiency / 100)
    
    # 陳教授專業診斷
    st.subheader("👨‍🏫 陳教授系統診斷：")
    if efficiency >= 90:
        st.success("「極佳的系統操作！物質平衡、含水率與溫度皆控制在微生物代謝動力學的最佳區間，轉化速率達到峰值。」")
    elif efficiency >= 70:
        st.info("「運作正常，但系統仍有優化空間。建議微調水分與通氣狀況，以提升對應基質的降解反應常數。」")
    else:
        st.error("「系統應力警示！目前的操作參數已進入微生物代謝受限區（動力學抑制）。請依據工程準則檢視水分是否導致空隙阻塞，或溫度是否導致酵素失活。」")

st.markdown("---")
st.caption("© 2026 陳教授 - 環境科學與資源循環研究室")
