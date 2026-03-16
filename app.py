import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time

# --- ページ設定と高級感のあるUI ---
st.set_page_config(page_title="個別専用設計図・ロードマップ作成", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    /* 全体のフォントサイズとトーン */
    html, body, [class*="css"]  {
        font-family: 'Helvetica Neue', Helvetica, Arial, 'Hiragino Sans', sans-serif;
        color: #E0E0E0;
    }
    .stApp {
        background-color: #121212;
    }
    h1, h2, h3 {
        color: #D4AF37; /* 高級感のあるゴールド */
        font-weight: 700;
        letter-spacing: 1.5px;
    }
    .big-font {
        font-size: 20px !important;
        line-height: 1.6;
    }
    .highlight {
        color: #D4AF37;
        font-weight: bold;
    }
    /* ボタンの装飾 */
    .stButton>button {
        width: 100%;
        background-color: #D4AF37;
        color: #121212;
        font-size: 22px;
        font-weight: bold;
        padding: 15px;
        border-radius: 8px;
        border: none;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #F3E5AB;
        color: #000000;
        transform: scale(1.02);
    }
    /* セレクトボックスやスライダーのテキスト */
    label {
        font-size: 18px !important;
        color: #FFFFFF !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- セッションステートの初期化（段階的公開用） ---
if 'step1_done' not in st.session_state:
    st.session_state.step1_done = False
if 'step2_done' not in st.session_state:
    st.session_state.step2_done = False
if 'step3_done' not in st.session_state:
    st.session_state.step3_done = False

# --- ヘッダー ---
st.title("🛡️ 個別専用設計図・ロードマップ作成")
st.markdown("<p class='big-font'>あなたの過去の経験は、企業が喉から手が出るほど欲しい「資産」です。<br>労働の延長線上ではなく、AIとデザインを駆使する『別レール』への乗り換えルートを証明します。</p>", unsafe_allow_html=True)
st.divider()

# ==========================================
# STEP 1：資産の言語化
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
    
    st.markdown("### 💎 あなたの経験が『高単価な価値』に変わる市場")
    if selected_job == "看護師・医療職・介護":
        st.markdown("""
        - **ターゲット市場**: 健康食品、終活・介護メディア、医療DXツール
        - **具体的な提供価値**: AIを使って「難解な専門用語」を読者に伝わる言葉へ変換。さらにCanvaで「患者の悩み解決図解」を作成し、企業の信頼性を圧倒的に高める**『医療・ヘルスケア特化のWeb設計士』**としてポジションを確立します。
        """)
    elif selected_job == "工場勤務・技術職・夜勤":
        st.markdown("""
        - **ターゲット市場**: 製造業向けB2Bサイト、採用メディア、安全管理マニュアル
        - **具体的な提供価値**: 現場の「安全基準」や「効率化のコツ」をAIでマニュアル化。Canvaで「誰でも直感でわかる工程図」をデザインし、人材不足と技術継承に悩む企業を救う**『現場改善・採用特化のWeb設計士』**となります。
        """)
    elif selected_job == "一般事務・管理部門":
        st.markdown("""
        - **ターゲット市場**: SaaS導入支援、業務効率化メディア、バックオフィス代行
        - **具体的な提供価値**: 社内に散らばる「バラバラな情報」をAIで瞬時に整理。Canvaで「業務フロー図」を作成し、企業のDX化（効率化）を根底から加速させる**『バックオフィスDX設計士』**として重宝されます。
        """)
    else:
        st.markdown("""
        - **ターゲット市場**: あなたの経験を深掘りし、競合不在のブルーオーシャンを選定。
        - **具体的な提供価値**: あなたの未言語化された人生経験を、AIが「企業が予算を投じてでも欲しがる資産」へと翻訳します。作業者ではなく**『提案者』**としての独自ポジションを構築します。
        """)
    st.divider()

# ==========================================
# STEP 2：収益シミュレーション（AIによる時間圧縮）
# ==========================================
if st.session_state.step1_done:
    st.header("STEP 2: 収益の極大化シミュレーション")
    st.markdown("<p class='big-font'>次世代設計士の報酬は、労働時間ではなく「納品価値」で決まります。<br>1案件の報酬は <span class='highlight'>20,000円（執筆＋画像＋設計）</span> で固定。あなたの1日の確保可能時間を教えてください。</p>", unsafe_allow_html=True)
    
    work_hours = st.slider("1日に確保できる平均作業時間（時間）", min_value=0.5, max_value=4.0, value=2.0, step=0.5)
    
    if st.button("資産構築の軌道をシミュレーションする"):
        st.session_state.step2_done = True
        
        with st.spinner('あなたの未来の収益構造を計算中...'):
            time.sleep(1)
            
    if st.session_state.step2_done:
        # ロジック計算：月間稼働20日とする
        monthly_hours = work_hours * 20
        months = ["1ヶ月目", "2ヶ月目", "3ヶ月目", "4ヶ月目", "5ヶ月目", "6ヶ月目"]
        
        # AIと型の活用により、1案件あたりの所要時間が劇的に減少していく
        time_per_project = [10.0, 7.0, 4.5, 3.0, 2.0, 1.5] 
        
        # 毎月のこなせる案件数と報酬額
        projects_per_month = [int(monthly_hours / t) for t in time_per_project]
        revenue_per_month = [p * 20000 for p in projects_per_month]
        
        # Plotlyによる圧倒的な視覚化（コンボチャート）
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        
        # 棒グラフ（月間報酬額）
        fig.add_trace(
            go.Bar(x=months, y=revenue_per_month, name="月間報酬額 (円)", marker_color='#D4AF37', opacity=0.85),
            secondary_y=False,
        )
        
        # 線グラフ（1案件あたりの所要時間：短縮＝生産性向上）
        fig.add_trace(
            go.Scatter(x=months, y=time_per_project, name="1案件の所要時間 (時間)", mode='lines+markers', line=dict(color='#00E5FF', width=3), marker=dict(size=10)),
            secondary_y=True,
        )
        
        fig.update_layout(
            title_text="<b>AI×Canvaによる「労働時間からの解放」と「収益の極大化」</b>",
            title_font=dict(size=22, color='#FFFFFF'),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            legend=dict(x=0.01, y=0.99, bgcolor='rgba(255,255,255,0.1)', font=dict(color='#FFF')),
            margin=dict(l=40, r=40, t=60, b=40)
        )
        fig.update_xaxes(showgrid=False, color='#FFF')
        fig.update_yaxes(title_text="<b>月間報酬額 (円)</b>", secondary_y=False, color='#D4AF37', showgrid=True, gridcolor='rgba(255,255,255,0.1)')
        fig.update_yaxes(title_text="<b>1案件の所要時間 (時間)</b>", secondary_y=True, color='#00E5FF', showgrid=False)
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown(f"<p class='big-font'>【解説】<br>1日たった{work_hours}時間の作業でも、AIと『売れる型』を脳にインストールすることで、処理スピードが劇的に向上します。<b>労働時間は変わらないのに、半年後には月収 <span class='highlight'>{revenue_per_month[-1]:,}円</span> が見込めます。</b>これが『時給思考』から抜け出すということです。</p>", unsafe_allow_html=True)
        st.divider()

# ==========================================
# STEP 3：ロードマップと確信へのステップ
# ==========================================
if st.session_state.step2_done:
    st.header("STEP 3: 確実なる別レールへのロードマップ")
    
    st.markdown("""
    <div style='background-color: #1E1E1E; padding: 20px; border-left: 5px solid #D4AF37; margin-bottom: 20px;'>
        <h3 style='margin-top:0;'>Phase 1【準備と確信】</h3>
        <p class='big-font'>AIとCanvaの環境を整え、最短7日で「自分にもできる」という絶対的な確信を得る。</p>
    </div>
    <div style='background-color: #1E1E1E; padding: 20px; border-left: 5px solid #D4AF37; margin-bottom: 20px;'>
        <h3 style='margin-top:0;'>Phase 2【企業案件への潜入】</h3>
        <p class='big-font'>実際の企業案件に入り込み、報酬をもらいながらプロの「売れる構成（型）」を脳に直接インストールする。</p>
    </div>
    <div style='background-color: #1E1E1E; padding: 20px; border-left: 5px solid #D4AF37; margin-bottom: 20px;'>
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
            <div style="background-color:#D4AF37; color:#121212; text-align:center; padding:20px; font-size:26px; font-weight:bold; border-radius:10px; margin-top:20px; box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4);">
                🔥 個別相談（プロの設計）を申し込む
            </div>
        </a>
        <p style="text-align:center; margin-top:10px; color:#888;">※ここから先は、本気で人生のレールを乗り換える方のみお進みください。</p>
        """, unsafe_allow_html=True)
