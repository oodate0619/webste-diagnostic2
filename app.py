import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ページ設定
st.set_page_config(page_title="個別専用設計図ロードマップ作成", layout="wide")

# カスタムCSSでフォントサイズなどを調整（X世代への配慮）
st.markdown("""
    <style>
    .main { font-size: 1.1rem; }
    .stButton>button { width: 100%; height: 3em; font-size: 1.2rem; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# タイトル
st.title("🛡️ 個別専用設計図ロードマップ作成")
st.write("あなたの人生経験を『稼げる型』へ変換し、最短ルートを確定させます。")

# セッション状態の初期化
if 'step' not in st.session_state:
    st.session_state.step = 1

# --- STEP 1: 人生棚卸し ---
st.header("STEP 1: 資産の言語化（人生棚卸し）")
job_options = {
    "選択してください": "",
    "看護師・医療従事者": "薬機法・景表法への高い意識、多忙な現場のタスク管理術、患者家族への高難度共感能力",
    "介護・福祉職": "現場の一次情報（レク・身体拘束等のリアル）、高齢者市場のインサイト",
    "一般事務・管理部門": "業務フローの標準化能力、正確なドキュメント作成能力（AIへの指示精度の高さ）",
    "営業・販売職": "『売れる構成』の勘所、顧客の反論処理（ベネフィット提示）のスキル",
    "工場・技術・夜勤": "納期への徹底した規律、現場の効率化マインド、実直なフィードバック能力",
    "その他": "独自の視点による課題発見能力、AIによる言語化で化ける『未言語化された経験資産』"
}

selected_job = st.selectbox("あなたの過去の主な職種・業界を選んでください", list(job_options.keys()))

if selected_job != "選択してください":
    st.info(f"✅ **企業があなたに発注する理由（資産価値）**: \n\n{job_options[selected_job]}")
    if st.button("STEP 1 を確定して次へ"):
        st.session_state.step = 2

# --- STEP 2: 収益シミュレーション ---
if st.session_state.step >= 2:
    st.divider()
    st.header("STEP 2: 市場選定と収益の逆転")
    st.write("「同じ3,000文字」でも、設計の有無でこれだけの価値（時給）の差が生まれます。")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("【作業】従来の労働型ライター")
        old_price = 3000 
        old_time = 3.0
        st.markdown(f"* 執筆：3,000文字 [cite: 5, 38]")
        st.markdown(f"* 作業時間：{old_time}時間 [cite: 4, 38]")
        st.markdown(f"* 報酬：**{old_price:,}円** [cite: 5, 38]")
        st.markdown(f"### 👉 時給：{old_price/old_time:,.0f}円 [cite: 2, 38]")

    with col2:
        st.subheader("【設計】ウェブステ流・次世代設計士")
        new_package_price = st.number_input("設計＋画像＋3,000文字執筆の総報酬（推奨：1.8万円以上）", value=18000)
        # 労働時間の選択式への変更
        time_options = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
        new_time = st.selectbox("実労働時間（AI執筆＋Canva図解＋設計の合計）を選択してください", time_options, index=2)
        
        hourly_rate_new = new_package_price / new_time
        st.markdown(f"* 執筆：3,000文字（AIフル活用） [cite: 4, 11]")
        st.markdown(f"* 図解：プロ級画像3枚セット（Canva活用） [cite: 4, 11]")
        st.markdown(f"### 👉 予測時給：{hourly_rate_new:,.0f}円 [cite: 4, 38]")

    # 時給比較グラフの視認性向上
    st.latex(r'''
    \text{時給逆転の法則} = \frac{\text{（文章報酬 + 画像報酬 + 設計報酬）}}{\text{AI活用による実作業時間}}
    ''')
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=['労働型（作業）', '設計士（価値）'], 
        y=[1000, hourly_rate_new], 
        marker_color=['#E9ECEF', '#007BFF'], 
        text=[f"1,000円", f"{hourly_rate_new:,.0f}円"], 
        textfont=dict(size=20),
        textposition='auto'
    ))
    fig.update_layout(
        height=500,
        yaxis=dict(title="時給（円）", titlefont=dict(size=18), tickfont=dict(size=16)),
        xaxis=dict(tickfont=dict(size=18)),
        margin=dict(l=20, r=20, t=20, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)
    
    if st.button("STEP 2 を確定して次へ"):
        st.session_state.step = 3

# --- STEP 3: ロードマップ ---
if st.session_state.step >= 3:
    st.divider()
    st.header("STEP 3: 3ヶ月間のロードマップ")
    st.write("意志力に頼らず「環境」で稼ぐ。最短距離の工程表です。 [cite: 8]")
    
    df_roadmap = pd.DataFrame([
        dict(Task="Phase 1: 企業案件潜入・型のコピー", Start='2026-04-01', Finish='2026-05-01', Resource='実績獲得'),
        dict(Task="Phase 2: 図解提案セット化（単価UP）", Start='2026-05-01', Finish='2026-06-01', Resource='価値向上'),
        dict(Task="Phase 3: 盗んだ型で自分の資産建築", Start='2026-06-01', Finish='2026-07-01', Resource='労働卒業')
    ])
    
    # ガントチャートの文字サイズ拡大
    fig_roadmap = px.timeline(df_roadmap, x_start="Start", x_end="Finish", y="Task", color="Resource", template="plotly_white")
    fig_roadmap.update_layout(
        height=400,
        font=dict(size=18), # 全体的なフォントサイズを大きく
        xaxis=dict(title="2026年 収益化スケジュール", titlefont=dict(size=20), tickfont=dict(size=16)),
        yaxis=dict(title="", tickfont=dict(size=18)), # フェーズの文字を大きく
        showlegend=False
    )
    st.plotly_chart(fig_roadmap, use_container_width=True)
    
    if st.button("STEP 3 を確定して最終確認へ"):
        st.session_state.step = 4

# --- STEP 4: 禁止事項 ---
if st.session_state.step >= 4:
    st.divider()
    st.header("STEP 4: やらないことリスト（迷いの排除）")
    st.write("成功を確実にするため、これまでの「稼げない習慣」をここで断ち切ります。 [cite: 2, 4]")
    
    st.warning("以下の項目をチェックし、プロとしての『設計図』を確定させてください。")
    st.checkbox("文字単価1円未満の『労働案件』を一切受けない [cite: 5, 11]", value=True)
    st.checkbox("AIを筆にせず、0から自分で文章をひねり出すのをやめる [cite: 13, 21]", value=True)
    st.checkbox("テンプレートを使わず、センスでデザインしようとするのを止める [cite: 13, 36]", value=True)
    st.checkbox("自分の判断で『ズレた努力』を続けるのを止める [cite: 4, 30]", value=True)
    st.checkbox("一人で30分以上悩むことを禁止する（即、プロに相談・フィードバックを得る） [cite: 4, 18]", value=True)

    st.success("🎉 おめでとうございます。あなた専用の設計図が完成しました。個別相談にて、この『ルート』の検収と詳細プランを確定させましょう。")
