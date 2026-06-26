import streamlit as st

# 網頁設定
st.set_page_config(page_title="陳教授的系統分析儀", layout="centered")

st.title("🧪 陳教授的系統分析儀：動態環境版")
st.markdown("結合物質平衡與動力學參數，精確模擬生物反應器運作狀態。")
st.sidebar.image("image.png", use_container_width=True)

# 1. 專業參數設定 (kg/kg)
# 落葉: C=0.45, N=0.006 | 廚餘: C=0.10, N=0.025
C_B, N_B = 0.45, 0.006
C_G, N_G = 0.10, 0.025

# 2. 輸入面板
st.header("⚙️ 模擬參數設置")
brown_w = st.slider("褐色資材 (落葉) [kg]", 0.0, 100.0, 30.0)
st.caption(f"💡 資訊：含碳 {brown_w * C_B:.2f}kg, 含氮 {brown_w * N_B:.3f}kg")

green_w = st.slider("綠色資材 (廚餘) [kg]", 0.0, 100.0, 10.0)
st.caption(f"💡 資訊：含碳 {green_w * C_G:.2f}kg, 含氮 {green_w * N_G:.3f}kg")

st.markdown("---")
moisture = st.slider("環境水分含量 (%)", 20, 90, 60, help="理想區間 55-65%")
temp = st.slider("環境溫度 (°C)", 10, 60, 30, help="理想區間 25-35°C")

# 3. 系統工程邏輯計算 (物質平衡 + 動力學修正)
total_C = (brown_w * C_B) + (green_w * C_G)
total_N = (brown_w * N_B) + (green_w * N_G)
cn_ratio = total_C / total_N if total_N > 0 else 100.0

# 動力學修正因子 (0.0 - 1.0)
f_water = 1.0 - abs(moisture - 60) / 40
f_temp = 1.0 - abs(temp - 30) / 30
efficiency = ((1.0 if 25 <= cn_ratio <= 35 else 0.5) * 0.5 + 
              max(0, f_water) * 0.3 + 
              max(0, f_temp) * 0.2) * 100

# 4. 分析結果輸出
if st.button("執行系統動力學分析"):
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    c1.metric("計算 C/N 比", f"{cn_ratio:.2f}")
    c2.metric("水分因子", f"{f_water*100:.0f}%")
    c3.metric("溫度因子", f"{f_temp*100:.0f}%")
    
    st.progress(efficiency / 100)
    st.metric("最終預估反應效率", f"{efficiency:.0f}%")
    
    st.subheader("👨‍🏫 陳教授系統診斷：")
    if efficiency >= 85:
        st.success("「極佳的物質平衡與環境控制！微生物正處於最佳代謝速率，資源循環效益最大化。」")
    elif efficiency >= 60:
        st.info("「運作正常。注意水分與溫度波動可能限制傳質效率，系統尚未發揮 100% 的轉化潛力。」")
    else:
        st.error("「系統警示！環境條件已偏離生物降解動力學安全區間。請重新校正配比或調控溫濕度以避免轉化停滯。」")

st.markdown("---")
st.caption("© 2026 陳教授 - 環境科學與資源循環研究室")
