import streamlit as st

# 網頁設定
st.set_page_config(page_title="陳教授的系統分析儀", layout="centered")

st.title("🧪 陳教授的系統分析儀：動態參數版")
st.markdown("將物料平衡、水力與溫度動力學整合的系統工程分析器。")
st.sidebar.image("image.png", use_container_width=True)

# 1. 專業參數設定 (kg/kg)
C_B, N_B = 0.45, 0.006  # 落葉
C_G, N_G = 0.10, 0.025  # 廚餘

# 2. 輸入面板
st.header("⚙️ 反應器操作參數設定")
brown_w = st.slider("褐色資材 (落葉) [kg]", 0.0, 100.0, 30.0)
green_w = st.slider("綠色資材 (廚餘) [kg]", 0.0, 100.0, 10.0)
moisture = st.slider("水分含量 (%)", 20, 90, 60, help="理想區間 55-65%")
temp = st.slider("反應溫度 (°C)", 10, 60, 30, help="理想區間 25-35°C")

# 3. 系統工程邏輯計算
total_C = (brown_w * C_B) + (green_w * C_G)
total_N = (brown_w * N_B) + (green_w * N_G)
cn_ratio = total_C / total_N if total_N > 0 else 100.0

# 計算環境修正因子 (歸一化至 0.0 - 1.0)
# 水分影響因子：過乾或過濕皆會限制擴散作用
f_water = 1.0 - abs(moisture - 60) / 40
f_water = max(0, min(f_water, 1.0))

# 溫度影響因子：阿瑞尼士效應之簡化模擬
f_temp = 1.0 - abs(temp - 30) / 30
f_temp = max(0, min(f_temp, 1.0))

# 系統綜合效率 (%)
cn_score = 1.0 if 25 <= cn_ratio <= 35 else 0.5
efficiency = (cn_score * 0.5 + f_water * 0.3 + f_temp * 0.2) * 100

# 4. 分析結果輸出
if st.button("執行系統動力學分析"):
    st.markdown("---")
    col1, col2 = st.columns(2)
    col1.metric("計算 C/N 比", f"{cn_ratio:.2f}")
    col2.metric("預估反應效率", f"{efficiency:.0f}%")
    
    st.progress(efficiency / 100)
    
    st.subheader("👨‍🏫 陳教授系統診斷：")
    if efficiency >= 85:
        st.success("「極佳的系統操作！物質平衡、水分含量與溫度皆控制在生物動力學的最佳區間，轉化速率達到峰值。」")
    elif efficiency >= 60:
        st.info("「運作正常，但系統受限於環境因子（如水分或溫度）。微生物代謝受限，建議檢查是否處於傳質受阻狀態。」")
    else:
        st.error("「系統應力警示！環境參數已遠離微生物適應區間。請檢視是否導致厭氧發酵或酵素失活。」")

st.markdown("---")
st.caption("© 2026 陳教授 - 環境科學與資源循環研究室")
