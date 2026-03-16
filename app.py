import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time

# --- ページ設定と白基調の洗練されたUI ---
st.set_page_config(page_title="個別専用設計図・ロードマップ作成", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    /* 全体のフォントサイズとトーン（白基調・高視認性） */
    html, body, [class*="css"]  {
        font-family: 'Helvetica Neue', Helvetica, Arial, 'Hiragino Sans', sans-serif;
        color: #333333; /* 視認性の高いダークグレー */
    }
    .stApp {
        background-color: #FAFAFA; /* 清潔感のある白系背景 */
    }
    h1, h2, h3 {
        color: #1A365D; /* 信頼感と高級感のあるネイビー */
        font-weight: 700;
        letter-spacing: 1.0px;
    }
    .big-font {
        font-size: 18px !important;
        line-height: 1.7;
        color: #4A5568;
    }
    .highlight {
        color: #D69E2E; /* 落ち着いたゴールド */
        font-weight: bold;
    }
    /* ボタンの装飾 */
    .stButton>button {
        width: 100%;
        background-color: #1A365D;
        color: #FFFFFF;
        font-size: 20px;
        font-weight: bold;
        padding: 12px;
        border-radius: 6px;
        border: none;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #2B6CB0;
        color: #FFFFFF;
        transform: translateY(-2px);
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    /* セレクトボックスやスライダーのテキスト */
    label {
        font-size: 16px !important;
        color: #2D3748 !important;
        font-weight: bold;
    }
    /* STEP3のボックス装飾 */
    .step-box {
        background-color: #FFFFFF;
        padding: 20px;
        border-left: 5px solid #1A365D;
        margin-bottom: 20px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# --- セッションステートの初期化 ---
if 'step1_done' not in st.session_state:
    st.session_state.step1_done = False
if 'step2_done' not in st.session_state:
    st.session_state.step2_done = False
if 'step3_done' not in st.session_state:
    st.session_state.step3_done = False

# --- ヘッダー ---
st.title("🛡️ 個別専用設計図・ロードマップ作成")
st.markdown("<p class='big-font'>あなたの過去の経験は、企業が予算を投じてでも欲しがる「資産」です。<br>労働の延長線上ではなく、AIとデザインを駆使し、確実な収益を積み上げる『別レール』へのルートを証明します。</p>", unsafe_allow_html=True)
st.divider()

# ==========================================
# STEP 1：資産の言語化（解像度を極限まで引き上げた具体例）
# ==========================================
st.header("STEP 1: 隠された資産の言語化")
st.markdown("<p class='big-font'>現在の、または過去の職種を選択してください。</p>", unsafe_allow_html=True)

job_options = [
    "選択してください",
    "看護師・医療職・介護",
    "工場勤務・技術職・夜勤",
    "一般事務・管理部門",
    "その他（未言語化の経験）"
]

selected_job = st.selectbox("", job_options, key="job_select")

if selected_job != "選択してください":
    st.session_state.step1_done = True
    
    st.markdown("### 💎 あなたの経験が『高単価な価値』に変わる具体的な業務")
    if selected_job == "看護師・医療職・介護":
        st.markdown("""
        - **未経験ライターには書けない「健康食品LP」の構成案作成**（薬機法や医療法を考慮した安心感のある訴求）
        - **介護施設の離職防止を目的とした、社内向け「図解マニュアル」のディレクション**（現場の痛みがわかるからこそ作れるマニュアル）
        - **クリニックのLINE公式アカウント用「リッチメニュー作成」**（患者の不安を先回りして消す導線設計）
        """)
    elif selected_job == "工場勤務・技術職・夜勤":
        st.markdown("""
        - **専門用語だらけの「機械の取扱説明書」を、新人でも即日理解できるCanva図解へ翻訳**
        - **「きつい・汚い」のイメージを払拭する、製造業特化の求人ページのライティングとアイキャッチ制作**（現場のリアルな良さを抽出）
        - **BtoB向け展示会で配る、「自社技術の強み」を1枚で直感的に伝える営業用チラシの設計**
        """)
    elif selected_job == "一般事務・管理部門":
        st.markdown("""
        - **煩雑な経費精算フローを、全社員が迷わず使えるようにする「業務効率化フローチャート」の作成**
        - **クラウドツール導入企業向けの、初期設定・活用ガイドラインの図解化**（ITリテラシーが低い人向けの翻訳）
        - **属人化している社内ルールをAIで整理し、視覚的にわかりやすい社内ポータル用バナーへ変換**
        """)
    else:
        st.markdown("""
        - **あなたの「当たり前の日常業務」の中に潜む、他社が喉から手が出るほど欲しいノウハウの抽出**
        - **属人化しているスキルをAIで言語化し、Canvaでパッケージ化（図解・マニュアル化）した法人向け提案書の作成**
        """)
    
    st.markdown("<p class='big-font' style='margin-top:15px;'>これらは単なる『作業』ではなく、企業の課題を解決する『設計』です。だからこそ高単価が成立します。</p>", unsafe_allow_html=True)
    st.divider()

# ==========================================
# STEP 2：収益シミュレーション（現実的な数値とポジティブな視覚化）
# ==========================================
if st.session_state.step1_done:
    st.header("STEP 2: 収益シミュレーション")
    st.markdown("<p class='big-font'>次世代設計士の報酬は、労働時間ではなく「納品価値」で決まります。<br>1案件の報酬は現実的な <span class='highlight'>20,000円</span> をベースに計算します。あなたの1日の確保可能時間を教えてください。</p>", unsafe_allow_html=True)
    
    work_hours = st.slider("1日に確保できる平均作業時間（時間）", min_value=1.0, max_value=4.0, value=2.0, step=0.5)
    
    if st.button("資産構築の軌道をシミュレーションする"):
        st.session_state.step2_done = True
        
        with st.spinner('現実的な収益軌道を計算中...'):
            time.sleep(1)
            
    if st.session_state.step2_done:
        # 月間稼働20日とする
        monthly_hours = work_hours * 20
        months = ["1ヶ月目", "2ヶ月目", "3ヶ月目", "4ヶ月目", "5ヶ月目", "6ヶ月目"]
        
        # 現実的なスキルアップ推移：最初は1案件に15時間かかるが、AIと型に慣れると半年後には5時間に短縮される
        time_per_project = [15.0, 12.0, 9.0, 7.0, 6.0, 5.0] 
        
        # 毎月の理論上のこなせる案件数と報酬額（地に足のついた数字）
        revenue_per_month = [(monthly_hours / t) * 20000 for t in time_per_project]
        
        # 実質的な時間単価（時給換算）の推移。右肩上がりのポジティブなグラフにする。
        hourly_rate = [20000 / t for t in time_per_project]
        
        # Plotlyによるコンボチャート作成
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        
        # 棒グラフ（月間報酬額）
        fig.add_trace(
            go.Bar(x=months, y=revenue_per_month, name="月間報酬額 (円)", marker_color='#1A365D', opacity=0.8),
            secondary_y=False,
        )
        
        # 線グラフ（実質的な時間単価：右肩上がりで成長を視覚化）
        fig.add_trace(
            go.Scatter(x=months, y=hourly_rate, name="実質的な時間単価 (円/時)", mode='lines+markers', line=dict(color='#D69E2E', width=4), marker=dict(size=10)),
            secondary_y=True,
        )
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            legend=dict(x=0.01, y=0.99, bgcolor='rgba(255,255,255,0.8)', font=dict(color='#333')),
            margin=dict(l=40, r=40, t=40, b=40)
        )
        fig.update_xaxes(showgrid=False, color='#333')
        fig.update_yaxes(title_text="<b>月間報酬額 (円)</b>", secondary_y=False, color='#1A365D', showgrid=True, gridcolor='rgba(0,0,0,0.1)')
        fig.update_yaxes(title_text="<b>実質的な時間単価 (円/時)</b>", secondary_y=True, color='#D69E2E', showgrid=False)
        
        st.plotly_chart(fig, use_container_width=True)
        
        final_revenue = int(revenue_per_month[-1])
        st.markdown(f"<p class='big-font'>【解説】<br>1日{work_hours}時間（月{int(monthly_hours)}時間）の稼働でも、最初は慣れずに月収{int(revenue_per_month[0]):,}円程度からのスタートです。しかし、AIと『売れる型』の活用で作業スピードが向上するため、<b>労働時間は変わらなくても半年後には月収 <span class='highlight'>{final_revenue:,}円</span> ベースが現実的に見込めます。</b><br>これが、単なる時間の切り売りではない『資産構築』の威力です。</p>", unsafe_allow_html=True)
        st.divider()

# ==========================================
# STEP 3：ロードマップと確信へのステップ
# ==========================================
if st.session_state.step2_done:
    st.header("STEP 3: 確実なる別レールへのロードマップ")
    
    st.markdown("""
    <div class='step-box'>
        <h3 style='margin-top:0;'>Phase 1【準備と確信】</h3>
        <p class='big-font'>AIとCanvaの環境を整え、最短7日で「自分にもできる」という絶対的な確信を得る。</p>
    </div>
    <div class='step-box'>
        <h3 style='margin-top:0;'>Phase 2【企業案件への潜入】</h3>
        <p class='big-font'>実際の企業案件に入り込み、報酬をもらいながらプロの「売れる構成（型）」を脳に直接インストールする。</p>
    </div>
    <div class='step-box'>
        <h3 style='margin-top:0;'>Phase 3【ディレクション権の掌握】</h3>
        <p class='big-font'>作業の8割をAIに任せ、自分は「設計・判断・提案」に回る。クライアントが手放せない存在となり、時給単価を極大化させる。</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.session_state.step3_done = True
    st.divider()

# ==========================================
# STEP 4：禁止事項（やらないことリスト）と行動喚起
# ==========================================
if st.session_state.step3_done:
    st.header("STEP 4: 『やらないこと』の誓い")
    st.markdown("<p class='big-font'>成功を確実にするため、以下の「貧者の行動」を今後一切やめると約束してください。</p>", unsafe_allow_html=True)
    
    c1 = st.checkbox("独学で無料のYouTubeやブログを漁り、時間をドブに捨てるのをやめる")
    c2 = st.checkbox("1文字1円の低単価ライターとして、自らの命（時間）を安売りするのをやめる")
    c3 = st.checkbox("「Photoshopが使えないから…」と、高度なデザインスキルを言い訳にするのをやめる")
    
    if c1 and c2 and c3:
        st.markdown("<p class='big-font highlight' style='text-align:center; margin-top:30px;'>覚悟が決まりましたね。今のあなたに必要なのは、独学ではなく『プロによる全体設計』です。</p>", unsafe_allow_html=True)
        
        # 最終の行動喚起ボタン
        st.markdown("""
        <a href="#" style="text-decoration:none;">
            <div style="background-color:#1A365D; color:#FFFFFF; text-align:center; padding:20px; font-size:24px; font-weight:bold; border-radius:8px; margin-top:20px; box-shadow: 0 4px 10px rgba(0,0,0,0.15);">
                個別相談（プロの設計）を申し込む
            </div>
        </a>
        <p style="text-align:center; margin-top:10px; color:#718096; font-size:14px;">※ここから先は、本気で人生のレールを乗り換える方のみお進みください。</p>
        """, unsafe_allow_html=True)
