import streamlit as st

# 網頁設定
st.set_page_config(page_title="陳教授的物質平衡模擬器", layout="centered")

st.title("🧪 陳教授的系統分析儀：成分透明化版")
st.markdown("透過物料平衡，解構廢棄物的化學成分，精確掌控系統反應。")
st.sidebar.image("image.png", use_container_width=True)

# 專業成分參數 (kg/kg)
# 落葉: C=0.45, N=0.006 (碳45%, 氮0.6%)
# 廚餘: C=0.10, N=0.025 (碳10%, 氮2.5%)
C_B, N_B = 0.45, 0.006
C_G, N_G = 0.025, 0.025  # 修正：廚餘碳量一般較低，氮量較高

# 1. 輸入面板
st.header("⚙️ 模擬參數設置 (公斤為單位)")

# 褐色資材顯示標註
brown_w = st.slider("褐色資材重量 (落葉) [kg]", 0.0, 100.0, 30.0)
st.caption(f"📍 資訊：每 1kg 落葉含 {C_B}kg 碳 與 {N_B}kg 氮")

# 綠色資材顯示標註
green_w = st.slider("綠色資材重量 (廚餘) [kg]", 0.0, 100.0, 10.0)
st.caption(f"📍 資訊：每 1kg 廚餘含 {C_G}kg 碳 與 {N_G}kg 氮")

# 2. 物質平衡計算
total_C = (brown_w * C_B) + (green_w * C_G)
total_N = (brown_w * N_B) + (green_w * N_G)
cn_ratio = total_C / total_N if total_N > 0 else 100.0

# 3. 系統效率得分 (簡化模型)
cn_score = 1.0 if 25 <= cn_ratio <= 35 else 0.5
efficiency = cn_score * 100

# 4. 分析結果
if st.button("執行物質平衡分析"):
    st.markdown("---")
    st.metric("計算 C/N 比", f"{cn_ratio:.2f}")
    
    # 顯示總量統計
    c1, c2 = st.columns(2)
    c1.metric("系統總碳量", f"{total_C:.2f} kg")
    c2.metric("系統總氮量", f"{total_N:.2f} kg")
    
    st.subheader("👨‍🏫 陳教授系統診斷：")
    if 25 <= cn_ratio <= 35:
        st.success("「完美的物質平衡！系統已達成高效降解的黃金比例，落葉的碳與廚餘的氮完美協同。」")
    elif cn_ratio < 25:
        st.warning("「氮素過剩！廚餘的高濃度氮素正在衝擊微生物系統，請增加落葉投入量以提高碳儲備。」")
    else:
        st.info("「碳庫過剩，系統進入維護模式。雖然穩定但效率偏低，微生物需要更多氮素來加速代謝。」")

st.markdown("---")
st.caption("© 2026 陳教授 - 環境科學與資源循環研究室")
