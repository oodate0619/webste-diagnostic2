import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# ページ設定
st.set_page_config(page_title="次世代Web設計士・個別逆転設計図", layout="wide")

st.title("🎨 次世代Web設計士・個別逆転設計図")
st.write("あなたの人生経験を『企業の資産』へ変換し、時給を10倍に跳ね上げる設計図を構築します。")

# --- ① 人生棚卸しシート ---
st.header("① 人生棚卸しシート")
col1, col2 = st.columns(2)
with col1:
    job_experience = st.text_input("過去の主な職歴（例：看護師、事務職、営業など）", "看護師")
    years = st.slider("業界経験年数", 0, 30, 10)
with col2:
    pain_points = st.text_area("現場の人間しか知らない『不満』や『非効率』", "夜勤の引き継ぎが紙ベースで時間がかかる...")

# 強み変換ロジック
st.info(f"💡 【企業への提案価値】: {job_experience}歴{years}年のあなたは、現場の『{pain_points[:10]}...』という深い悩みを知る唯一無二の専門家です。")

# --- ⑤ 収益シミュレーション (LaTeX数式とグラフ) ---
st.header("⑤ 収益シミュレーション")

# 数式の提示
st.latex(r'''
\text{次世代設計士の時給} = \frac{(\text{執筆単価} \times \text{文字数}) + \text{Canva図解・提案報酬}}{\text{実労働時間}}
''')

col3, col4 = st.columns(2)
with col3:
    base_price = st.number_input("記事単価（設計含む）", value=15000)
    working_hours = st.slider("実労働時間（設計＋AI活用）", 0.5, 5.0, 1.5)
    
hourly_rate_new = base_price / working_hours
st.metric("予測時給", f"{hourly_rate_new:,.0f}円", delta=f"従来比 {hourly_rate_new - 1000:,.0f}円 UP")

# 比較グラフ
fig_sim = go.Figure()
fig_sim.add_trace(go.Bar(x=['従来（文字のみ）', '設計士（ウェブステ流）'], y=[1000, hourly_rate_new], name='時給比較'))
fig_sim.update_layout(title='労働単価の劇的な変化')
st.plotly_chart(fig_sim)

# --- ④ 3ヶ月ロードマップ (ガントチャート) ---
st.header("④ 3ヶ月ロードマップ")

df_roadmap = pd.DataFrame([
    dict(Task="Phase 1: 企業案件潜入", Start='2026-04-01', Finish='2026-05-01', Resource='準備・受注'),
    dict(Task="Phase 2: 型のコピー＆単価UP", Start='2026-05-01', Finish='2026-06-01', Resource='スキル拡張'),
    dict(Task="Phase 3: 自社資産（ブログ）転用", Start='2026-06-01', Finish='2026-07-01', Resource='資産建築')
])
fig_roadmap = px.timeline(df_roadmap, x_start="Start", x_end="Finish", y="Task", color="Resource")
st.plotly_chart(fig_roadmap)

# --- ⑥ やらないことリスト ---
st.header("⑥ やらないことリスト")
st.checkbox("文字単価1円未満の『労働案件』を全て捨てる", value=True)
st.checkbox("センスに頼って0からデザインすることを止める", value=True)
st.checkbox("一人で30分以上悩むことを禁止（プロに即相談）", value=True)

st.success("個別相談にて、この設計図を確定させましょう。")
