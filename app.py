import streamlit as st

# 網頁設定
st.set_page_config(page_title="陳教授的系統分析儀", layout="centered")

st.title("🧪 陳教授的系統分析儀：物質平衡模擬")
st.markdown("以系統工程視角，精確調控有機資材轉化效率。")
st.sidebar.image("image.png", use_container_width=True)

# 1. 輸入面板
st.header("⚙️ 模擬參數設置")
brown_weight = st.slider("褐色資材重量 (落葉/碎紙) [kg]", 0, 100, 50)
green_weight = st.slider("綠色資材重量 (廚餘/剪草) [kg]", 0, 100, 50)

# 2. 專業計算邏輯 (基於碳氮含量係數)
# 落葉: C=45%, N=0.6% | 廚餘: C=10%, N=2.5%
C_B, N_B = 45.0, 0.6
C_G, N_G = 10.0, 2.5

total_carbon = (brown_weight * C_B) + (green_weight * C_G)
total_nitrogen = (brown_weight * N_B) + (green_weight * N_G)

if total_nitrogen > 0:
    cn_ratio = total_carbon / total_nitrogen
else:
    cn_ratio = 100.0

# 3. 分析結果與陳教授點評
if st.button("執行物質平衡分析"):
    st.markdown("---")
    st.metric("預估 C/N 比", f"{cn_ratio:.2f}")
    
    st.subheader("分析結果：")
    
    if cn_ratio < 20:
        st.write("## 🤢 系統狀態：氮過剩 (易產臭)")
        st.warning("「蛋白質含量過高！微生物代謝釋出氨氣，且易導致系統酸化。請增加褐色資材比例以提升系統的碳庫儲備。」")
    elif 25 <= cn_ratio <= 35:
        st.write("## 🥳 系統狀態：黃金比例 (高效)")
        st.success("「完美的物質平衡！這是微生物分解的最適環境。養分供應與能量轉換達到平衡，能將廢棄物高效轉化為腐植質肥料。」")
    else:
        st.write("## 😴 系統狀態：碳過剩 (降解緩慢)")
        st.info("「能量來源充足但氮素限制了微生物的成長速率。系統目前處理效率偏低，建議適度添加綠色資材以補充代謝所需之營養。」")

st.markdown("---")
st.caption("© 2026 陳教授 - 環境科學與資源循環研究室")
