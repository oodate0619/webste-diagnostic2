import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time

# --- ページ設定と白基調の洗練されたUI ---
st.set_page_config(page_title="個別専用設計図・ロードマップ作成", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: 'Helvetica Neue', Helvetica, Arial, 'Hiragino Sans', sans-serif;
        color: #333333;
    }
    .stApp {
        background-color: #FAFAFA;
    }
    h1, h2, h3 {
        color: #1A365D;
        font-weight: 700;
        letter-spacing: 1.0px;
    }
    .big-font {
        font-size: 18px !important;
        line-height: 1.7;
        color: #4A5568;
    }
    .highlight {
        color: #D69E2E;
        font-weight: bold;
    }
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
    label {
        font-size: 16px !important;
        color: #2D3748 !important;
        font-weight: bold;
    }
    .step-box {
        background-color: #FFFFFF;
        padding: 20px;
        border-left: 5px solid #1A365D;
        margin-bottom: 20px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# --- セッションステート ---
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
# STEP 1：資産の言語化（ハードルを下げ、具体性を上げる）
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
        - **患者さんに説明している感覚で書く「健康コラム」の執筆**（医療の知識が少しあるだけで、企業からはプロとして重宝されます）
        - **新人スタッフに教えていた内容をCanvaで「マニュアル図解」にするだけ**（現場の痛みがわかるあなたにしか作れない資産です）
        - **「専門用語」をAIに放り込み、素人でもわかる言葉に変換する作業**（ゼロから文章を考える必要はありません）
        """)
    elif selected_job == "工場勤務・技術職・夜勤":
        st.markdown("""
        - **普段やっている「安全確認」のポイントを、スマホで見やすい画像にまとめる作業**（製造業の企業が喉から手が出るほど欲しい資料です）
        - **「きつい・汚い」のイメージを払拭する、現場目線のリアルな求人記事の作成**（AIが綺麗な文章に整えてくれます）
        - **文字だらけの古い作業手順書を、Canvaのテンプレートに当てはめて見やすくするだけ**
        """)
    elif selected_job == "一般事務・管理部門":
        st.markdown("""
        - **社内でよく聞かれる「これどうやるの？」を、AIとCanvaで1枚の画像（FAQ）にするだけ**
        - **普段エクセルでまとめているデータを、直感的にわかる「業務フロー図」に変換**（DX化を進めたい企業が高値で買い取ります）
        - **AIを使って、バラバラな会議の議事録や社内ルールを綺麗に整理する作業**
        """)
    else:
        st.markdown("""
        - **あなたが「当たり前」にやってきた日常業務を、AIが「企業向けのノウハウ」に変換します**
        - **ゼロからスキルを学ぶのではなく、今ある知識をCanvaのテンプレートに流し込むだけで「売れる商品」になります**
        """)
    
    st.markdown("<p class='big-font' style='margin-top:15px;'>難しい専門知識や、ゼロからのクリエイティブな発想は不要です。<b>「あなたの当たり前」をAIと型で整えるだけ</b>で、高単価な案件へと変わります。</p>", unsafe_allow_html=True)
    st.divider()

# ==========================================
# STEP 2：収益シミュレーション（現実的な単価とわかりやすいグラフ）
# ==========================================
if st.session_state.step1_done:
    st.header("STEP 2: 収益シミュレーション")
    st.markdown("<p class='big-font'>次世代設計士の報酬は、労働時間ではなく「納品価値」で決まります。<br>1案件の報酬は、初心者でも現実的な <span class='highlight'>10,000円〜15,000円</span>（今回は平均12,000円で計算）をベースにします。<br>あなたの1日の確保可能時間を教えてください。</p>", unsafe_allow_html=True)
    
    work_hours = st.slider("1日に確保できる平均作業時間（時間）", min_value=1.0, max_value=4.0, value=2.0, step=0.5)
    
    if st.button("資産構築の軌道をシミュレーションする"):
        st.session_state.step2_done = True
        
        with st.spinner('現実的な収益軌道を計算中...'):
            time.sleep(1)
            
    if st.session_state.step2_done:
        monthly_hours = work_hours * 20
        months = ["1ヶ月目", "2ヶ月目", "3ヶ月目", "4ヶ月目", "5ヶ月目", "6ヶ月目"]
        
        # 初心者が6ヶ月以内で成長する現実的な時間短縮モデル（1案件15時間 → 4時間）
        time_per_project = [15.0, 11.0, 8.0, 6.0, 5.0, 4.0] 
        base_reward = 12000 # 1案件12,000円
        
        revenue_per_month = [(monthly_hours / t) * base_reward for t in time_per_project]
        hourly_rate = [base_reward / t for t in time_per_project]
        
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        
        # マウスオーバー時（ホバー）の数値を分かりやすく整形
        fig.add_trace(
            go.Bar(
                x=months, y=revenue_per_month, name="月間収益額 (円)", 
                marker_color='#1A365D', opacity=0.8,
                hovertemplate='%{x}<br>月間収益: <b>%{y:,.0f}円</b><extra></extra>'
            ),
            secondary_y=False,
        )
        
        fig.add_trace(
            go.Scatter(
                x=months, y=hourly_rate, name="実質的な時間単価 (円/時)", 
                mode='lines+markers', line=dict(color='#D69E2E', width=4), marker=dict(size=10),
                hovertemplate='%{x}<br>時間単価: <b>%{y:,.0f}円/時</b><extra></extra>'
            ),
            secondary_y=True,
        )
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            legend=dict(x=0.01, y=0.99, bgcolor='rgba(255,255,255,0.8)', font=dict(color='#333')),
            margin=dict(l=40, r=40, t=40, b=40),
            hovermode="x unified"
        )
        fig.update_xaxes(showgrid=False, color='#333')
        fig.update_yaxes(title_text="<b>月間収益額 (円)</b>", secondary_y=False, color='#1A365D', showgrid=True, gridcolor='rgba(0,0,0,0.1)', tickformat=",d")
        fig.update_yaxes(title_text="<b>実質的な時間単価 (円/時)</b>", secondary_y=True, color='#D69E2E', showgrid=False, tickformat=",d")
        
        st.plotly_chart(fig, use_container_width=True)
        
        final_revenue = int(revenue_per_month[-1])
        st.markdown(f"""
        <div style='background-color: #F7FAFC; padding: 15px; border-radius: 8px; border: 1px solid #E2E8F0;'>
            <p class='big-font' style='margin-bottom:0;'>【解説】<br>
            初心者の場合、最初はツールの操作や型に慣れるため、1日{work_hours}時間稼働しても1ヶ月目の収益は数万円程度です。<br><br>
            しかし、AIの活用とCanvaのテンプレート（型）に慣れるにつれ、作業スピードは劇的に上がります。<b>毎日同じ「1日{work_hours}時間」の稼働であっても、6ヶ月以内には月収 <span class='highlight'>{final_revenue:,}円</span> ベースに到達することが現実的に可能です。</b><br><br>
            「働く時間を増やす」のではなく、「同じ時間で生み出せる価値（収益額）を増やす」こと。これが労働の延長線上ではない、ウェブステが提唱する別レールの働き方です。</p>
        </div>
        """, unsafe_allow_html=True)
        st.divider()

# ==========================================
# STEP 3：別レールへの詳細ロードマップ
# ==========================================
if st.session_state.step2_done:
    st.header("STEP 3: 別レールへの確実なロードマップ")
    
    st.markdown("""
    <div class='step-box'>
        <h3 style='margin-top:0;'>Phase 1【準備・確信】（最初の7〜14日間）</h3>
        <p class='big-font'>まずはAIに対する「難しそう」というブロックを外します。Canvaの基本操作と、プロンプト（指示文）の型をなぞるだけで、「自分の手で質の高いものが作れた」という絶対的な確信を得る期間です。</p>
    </div>
    <div class='step-box'>
        <h3 style='margin-top:0;'>Phase 2【実践・報酬獲得】（1ヶ月〜3ヶ月目）</h3>
        <p class='big-font'>ハードルの低い現実的な案件（1万円〜1.5万円）を実際に受注し、プロのサポートを受けながら納品します。「自分の経験がお金に変わる」成功体験を積み、売れる構成（型）を脳にインストールします。</p>
    </div>
    <div class='step-box'>
        <h3 style='margin-top:0;'>Phase 3【ディレクターへの昇華】（3ヶ月〜6ヶ月目）</h3>
        <p class='big-font'>作業の8割をAIとテンプレートに任せます。あなたは「作業者」を卒業し、クライアントに「こういう画像もセットにしましょう」と提案する「設計・判断」の側に回ります。ここで、同じ稼働時間でも収益が数倍に跳ね上がります。</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.session_state.step3_done = True
    st.divider()

# ==========================================
# STEP 4：やらないことリストと行動喚起
# ==========================================
if st.session_state.step3_done:
    st.header("STEP 4: 『やらないことリスト』の宣誓")
    st.markdown("<p class='big-font'>成功を確実にするため、以下の「失敗する人の共通点」を今後一切やめると約束してください。すべてチェックを入れると次へ進めます。</p>", unsafe_allow_html=True)
    
    c1 = st.checkbox("独学で無料のYouTubeやブログを漁り、時間をドブに捨てるのをやめる")
    c2 = st.checkbox("「1文字1円」のような低単価な労働で、自らの命（時間）を安売りするのをやめる")
    c3 = st.checkbox("「自分にはセンスがないから」と、始める前から言い訳をするのをやめる")
    c4 = st.checkbox("完璧主義に陥り、100点になるまでいつまでも行動しないのをやめる")
    c5 = st.checkbox("孤独に一人で悩み、誰にも相談せずに立ち止まるのをやめる")
    c6 = st.checkbox("すぐに一攫千金が手に入るという、安っぽい魔法を信じるのをやめる")
    c7 = st.checkbox("「自分の今までの人生経験には価値がない」と思い込むのをやめる")
    
    if c1 and c2 and c3 and c4 and c5 and c6 and c7:
        st.markdown("<p class='big-font highlight' style='text-align:center; margin-top:30px;'>覚悟が決まりましたね。独学の自腹はもう終わりです。あなたに必要なのは、正しい方向へ導く『環境』です。</p>", unsafe_allow_html=True)
        
        # ウェブステの伴走環境へ導くCTA
        st.markdown("""
        <a href="#" style="text-decoration:none;">
            <div style="background-color:#1A365D; color:#FFFFFF; text-align:center; padding:20px; font-size:24px; font-weight:bold; border-radius:8px; margin-top:20px; box-shadow: 0 4px 10px rgba(0,0,0,0.15);">
                🤝 ウェブステの伴走環境で進む
            </div>
        </a>
        <p style="text-align:center; margin-top:10px; color:#718096; font-size:14px;">※ここから先は、本気で人生のレールを乗り換える方のみお進みください。</p>
        """, unsafe_allow_html=True)
