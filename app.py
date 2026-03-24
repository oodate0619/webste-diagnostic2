from typing import Dict, List, Tuple

import plotly.graph_objects as go
import streamlit as st


COLOR_BLUE = "#40C1E9"
COLOR_PINK = "#F17F9E"
COLOR_YELLOW = "#F9CE23"
COLOR_TEXT = "#243447"
COLOR_SUB = "#5B6675"
COLOR_BORDER = "#E6E8EC"
COLOR_BG = "#FFFFFF"
COLOR_SOFT = "#F8FAFC"


st.set_page_config(
    page_title="個別専用キャリア設計図ロードマップ作成",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    f"""
    <style>
    html, body, [class*="css"] {{
        font-family: 'Helvetica Neue', Helvetica, Arial, 'Hiragino Sans', sans-serif;
        color: {COLOR_TEXT};
    }}
    .stApp {{
        background-color: {COLOR_BG};
    }}
    h1, h2, h3 {{
        color: {COLOR_TEXT};
        letter-spacing: 0.2px;
    }}
    .lead {{
        font-size: 16px;
        line-height: 1.85;
        color: {COLOR_SUB};
    }}
    .card {{
        background: {COLOR_BG};
        border: 1px solid {COLOR_BORDER};
        border-radius: 16px;
        padding: 18px 20px;
        margin-bottom: 16px;
        box-shadow: 0 2px 10px rgba(16, 24, 40, 0.04);
    }}
    .mini-card {{
        background: {COLOR_SOFT};
        border: 1px solid {COLOR_BORDER};
        border-radius: 14px;
        padding: 12px 14px;
        margin-bottom: 10px;
    }}
    .compare-wrap {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 12px;
        margin-top: 10px;
    }}
    .compare-box {{
        background: {COLOR_SOFT};
        border: 1px solid {COLOR_BORDER};
        border-radius: 14px;
        padding: 14px;
    }}
    .compare-title {{
        font-size: 15px;
        font-weight: 700;
        margin-bottom: 8px;
        color: {COLOR_TEXT};
    }}
    .section-title {{
        font-size: 24px;
        font-weight: 700;
        color: {COLOR_TEXT};
        margin-top: 10px;
        margin-bottom: 8px;
    }}
    .timeline {{
        position: relative;
        margin-top: 8px;
        padding-left: 18px;
    }}
    .timeline:before {{
        content: "";
        position: absolute;
        left: 8px;
        top: 8px;
        bottom: 8px;
        width: 3px;
        background: {COLOR_BLUE};
        opacity: 0.35;
    }}
    .timeline-item {{
        position: relative;
        background: {COLOR_BG};
        border: 1px solid {COLOR_BORDER};
        border-radius: 14px;
        padding: 12px 14px;
        margin-bottom: 12px;
    }}
    .timeline-item:before {{
        content: "";
        position: absolute;
        left: -17px;
        top: 16px;
        width: 12px;
        height: 12px;
        border-radius: 999px;
        background: {COLOR_PINK};
        border: 2px solid {COLOR_BG};
    }}
    .timeline-label {{
        display: inline-block;
        font-size: 13px;
        font-weight: 700;
        color: {COLOR_TEXT};
        background: #EEF9FD;
        padding: 4px 8px;
        border-radius: 999px;
        margin-bottom: 8px;
    }}
    .accent {{
        color: {COLOR_PINK};
        font-weight: 700;
    }}
    .accent-blue {{
        color: {COLOR_BLUE};
        font-weight: 700;
    }}
    .accent-yellow {{
        color: #C99A00;
        font-weight: 700;
    }}
    .center-button button {{
        width: 100%;
        border-radius: 12px;
        background: {COLOR_BLUE};
        color: white;
        font-weight: 700;
        border: none;
        padding: 0.82rem 1rem;
        font-size: 18px;
    }}
    .center-button button:hover {{
        background: #2CB2DB;
        color: white;
    }}
    @media (max-width: 768px) {{
        .compare-wrap {{
            grid-template-columns: 1fr;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)


JOB_OPTIONS = [
    "会社員",
    "パート",
    "アルバイト",
    "主婦",
    "営業職",
    "事務職",
    "接客販売",
    "医療従事者",
    "介護福祉職",
    "工場勤務",
    "教育",
    "保育",
    "美容",
    "サロン",
    "ジム・フィットネス関連",
    "フリーランス",
    "自営業",
    "その他",
]

EXPERIENCE_OPTIONS = [
    "ブログ執筆",
    "記事作成",
    "SNS投稿",
    "SNS運用",
    "ライティング",
    "リライト",
    "要約",
    "情報整理",
    "リサーチ",
    "画像作成",
    "Canva",
    "デザイン",
    "チラシ作成",
    "資料作成",
    "マニュアル作成",
    "Excel・スプレッドシート",
    "データ入力",
    "会議メモ・議事録",
    "接客",
    "販売",
    "営業",
    "電話対応",
    "問い合わせ対応",
    "教える・指導する",
    "研修・教育",
    "医療知識の説明",
    "介護現場の説明",
    "子育て経験の発信",
    "美容・健康の情報発信",
    "写真撮影",
    "動画編集",
    "AI使用経験",
    "ChatGPT使用経験",
]

REASON_OPTIONS = [
    "独学の試行錯誤を終わらせたい",
    "自分に合うテーマや方向性を明確にしたい",
    "自分の経験がどんな仕事に変わるのか知りたい",
    "AI×Canva×ライティングを実務で使える形にしたい",
    "3ヶ月以内に収益の土台を作りたい",
    "企業案件で型を学びながら自分の資産にもつなげたい",
    "書くだけではなく設計・整理・改善側に回りたい",
    "体力勝負ではない働き方に切り替えたい",
    "将来の収入不安に備えたい",
    "家事・育児・仕事と両立できる別レールを作りたい",
    "自分一人で判断し続けるやり方を終わらせたい",
    "個別に設計されたロードマップで進みたい",
]

GOAL_OPTIONS = [
    "半年以内に月3〜5万円の副収入の土台を作りたい",
    "1年以内に月10万円以上を安定して目指したい",
    "会社以外の収入源を持ちたい",
    "在宅でも続けやすい働き方を作りたい",
    "自分のブログやSNSも資産化したい",
    "自分の経験を価値に変えられる働き方に移行したい",
    "将来的にフリーランスや独立も視野に入れたい",
    "子育てや家庭と両立しながら積み上げたい",
    "親の介護や将来の生活不安に備えたい",
    "今の仕事を続けながら次のレールを準備したい",
]

REGION_OPTIONS = [
    "北海道",
    "東北",
    "関東",
    "中部",
    "近畿",
    "中国",
    "四国",
    "九州",
    "沖縄",
    "海外",
    "その他",
]

AGE_OPTIONS = [
    "20代前半",
    "20代後半",
    "30代前半",
    "30代後半",
    "40代前半",
    "40代後半",
    "50代前半",
    "50代後半",
    "60代以上",
]

GENDER_OPTIONS = ["女性", "男性", "その他", "回答しない"]
MARITAL_OPTIONS = ["未婚", "既婚", "その他"]
CHILD_OPTIONS = ["いない", "いる"]
CHILD_COUNT_OPTIONS = ["0", "1", "2", "3", "4人以上"]

BLOG_HAVE_OPTIONS = ["持っている", "持っていない"]
BLOG_HISTORY_OPTIONS = [
    "まだ始めていない",
    "1ヶ月未満",
    "1〜3ヶ月",
    "3〜6ヶ月",
    "6ヶ月〜1年",
    "1〜2年",
    "2年以上",
]

SIDE_HISTORY_OPTIONS = [
    "まだ取り組んでいない",
    "1ヶ月未満",
    "1〜3ヶ月",
    "3〜6ヶ月",
    "6ヶ月〜1年",
    "1〜2年",
    "2年以上",
]

REVENUE_OPTIONS = [
    "0円",
    "1円〜5,000円",
    "5,001円〜1万円",
    "1万〜3万円",
    "3万〜5万円",
    "5万〜10万円",
    "10万〜30万円",
    "30万円以上",
]

ANNUAL_INCOME_OPTIONS = [
    "200万円未満",
    "200万〜300万円",
    "300万〜400万円",
    "400万〜500万円",
    "500万〜700万円",
    "700万〜1,000万円",
    "1,000万円以上",
    "回答しない",
]

HOUSEHOLD_INCOME_OPTIONS = [
    "300万円未満",
    "300万〜500万円",
    "500万〜700万円",
    "700万〜1,000万円",
    "1,000万円以上",
    "回答しない",
]

SAVINGS_OPTIONS = [
    "50万円未満",
    "50万〜100万円",
    "100万〜300万円",
    "300万〜500万円",
    "500万〜1,000万円",
    "1,000万円以上",
    "回答しない",
]

TARGET_INCOME_OPTIONS: Dict[str, int] = {
    "月3万円": 30000,
    "月5万円": 50000,
    "月10万円": 100000,
    "月15万円": 150000,
    "月20万円": 200000,
    "月25万円": 250000,
    "月30万円": 300000,
}

if "generated" not in st.session_state:
    st.session_state.generated = False


def unique_keep_order(items: List[str]) -> List[str]:
    seen = set()
    result: List[str] = []
    for item in items:
        if item and item not in seen:
            seen.add(item)
            result.append(item)
    return result


def round_thousand(value: float) -> int:
    return int(round(value / 1000) * 1000)


def experience_score(experiences: List[str], side_history: str, current_revenue: str, best_revenue: str, blog_history: str) -> int:
    score = len(experiences)

    if side_history in ["3〜6ヶ月", "6ヶ月〜1年"]:
        score += 2
    elif side_history in ["1〜2年", "2年以上"]:
        score += 4

    if blog_history in ["3〜6ヶ月", "6ヶ月〜1年"]:
        score += 1
    elif blog_history in ["1〜2年", "2年以上"]:
        score += 2

    if current_revenue in ["1万〜3万円", "3万〜5万円"]:
        score += 2
    elif current_revenue in ["5万〜10万円", "10万〜30万円", "30万円以上"]:
        score += 4

    if best_revenue in ["1万〜3万円", "3万〜5万円"]:
        score += 1
    elif best_revenue in ["5万〜10万円", "10万〜30万円", "30万円以上"]:
        score += 3

    return score


def get_experience_multiplier(score: int) -> float:
    if score <= 3:
        return 0.92
    if score <= 7:
        return 1.00
    if score <= 12:
        return 1.10
    return 1.20


def get_ideal_multiplier(score: int) -> float:
    if score <= 3:
        return 1.18
    if score <= 8:
        return 1.22
    if score <= 13:
        return 1.25
    return 1.28


def hours_to_base_monthly(hours: float) -> int:
    base_map = {
        0.5: 15000,
        1.0: 30000,
        1.5: 50000,
        2.0: 70000,
        2.5: 95000,
        3.0: 120000,
        3.5: 145000,
        4.0: 175000,
        4.5: 205000,
        5.0: 235000,
    }
    return base_map.get(hours, 70000)


def build_income_lines(score: int) -> Tuple[List[float], List[int], List[int]]:
    hours_points = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
    exp_multiplier = get_experience_multiplier(score)
    ideal_multiplier = get_ideal_multiplier(score)

    current_line: List[int] = []
    ideal_line: List[int] = []
    for hours in hours_points:
        current = round_thousand(hours_to_base_monthly(hours) * exp_multiplier)
        ideal = round_thousand(current * ideal_multiplier)
        if ideal <= current:
            ideal = current + 3000
        current_line.append(current)
        ideal_line.append(ideal)

    return hours_points, current_line, ideal_line


def selected_income_values(work_hours: float, hours_points: List[float], current_line: List[int], ideal_line: List[int]) -> Tuple[int, int]:
    idx = hours_points.index(work_hours)
    return current_line[idx], ideal_line[idx]


def build_long_term_projection(current_monthly: int, ideal_monthly: int, score: int, work_hours: float) -> Tuple[List[str], List[int], List[int]]:
    years = ["1年目", "2年目", "3年目", "4年目", "5年目"]

    base_monthly = round_thousand(current_monthly * 0.8 + ideal_monthly * 0.2)
    if work_hours <= 1.0:
        growth = [1.00, 1.14, 1.25, 1.34, 1.42]
    elif work_hours <= 2.0:
        growth = [1.00, 1.18, 1.34, 1.48, 1.60]
    else:
        growth = [1.00, 1.22, 1.42, 1.60, 1.76]

    score_bonus = 0.00
    if score >= 8:
        score_bonus = 0.04
    if score >= 13:
        score_bonus = 0.08

    annuals: List[int] = []
    for i, factor in enumerate(growth):
        monthly_run_rate = base_monthly * (factor + score_bonus)
        if i == 0:
            annual = round_thousand(monthly_run_rate * 10)
        else:
            annual = round_thousand(monthly_run_rate * 12)
        if annuals and annual <= annuals[-1]:
            annual = annuals[-1] + 120000
        annuals.append(annual)

    cumulative: List[int] = []
    running = 0
    for annual in annuals:
        running += annual
        cumulative.append(running)

    return years, annuals, cumulative


def profile_tags(age: str, region: str, marital: str, child_status: str, current_job: str) -> str:
    tags = [age, region, current_job]
    if marital == "既婚":
        if child_status == "いる":
            tags.append("家庭と両立前提")
        else:
            tags.append("家庭の固定費を見ながら判断する層")
    return " / ".join(tags)


def build_strength_summary(
    job: str,
    experiences: List[str],
    career_text: str,
    reasons: List[str],
    goals: List[str],
    why_now: str,
    hobbies: str,
) -> str:
    strengths = []

    if job in ["事務職", "会社員", "営業職", "フリーランス", "自営業"]:
        strengths.append("情報を整理して、相手が判断しやすい形に直す力")
    if job in ["接客販売", "パート", "アルバイト", "営業職", "サロン", "美容", "ジム・フィットネス関連"]:
        strengths.append("相手が迷うポイントや不安を先回りして言葉にする力")
    if job in ["医療従事者", "介護福祉職", "教育", "保育"]:
        strengths.append("難しいことを、やさしく伝え直す力")
    if job in ["工場勤務"]:
        strengths.append("現場の手順や抜け漏れを見つけ、流れに落とし込む力")
    if job in ["主婦"]:
        strengths.append("生活者としてのリアルな視点で、選ぶ理由や続ける理由を言葉にする力")

    if "Canva" in experiences or "デザイン" in experiences or "画像作成" in experiences:
        strengths.append("文章だけでなく、見た瞬間に伝わる形へ整える力")
    if "AI使用経験" in experiences or "ChatGPT使用経験" in experiences or "要約" in experiences:
        strengths.append("叩き台を早く作り、仕上げの精度に時間を使える力")
    if "ブログ執筆" in experiences or "SNS運用" in experiences or "記事作成" in experiences:
        strengths.append("発信テーマを切り出し、継続できる切り口へ落とす力")
    if "情報整理" in experiences or "資料作成" in experiences or "Excel・スプレッドシート" in experiences:
        strengths.append("散らかった情報を比較しやすい形へ整える力")

    strengths = unique_keep_order(strengths)
    if not strengths:
        strengths = ["今まで当たり前にやってきたことを、企業向けの作業に置き換える力"]

    goal_hint = ""
    if goals:
        goal_hint = f"今後の目標として『{goals[0]}』を置いているので、"
    reason_hint = ""
    if reasons:
        reason_hint = f"申し込み理由の『{reasons[0]}』にもつながる形で、"

    hobby_hint = ""
    if hobbies.strip():
        hobby_hint = f"また、興味領域の『{hobbies[:25]}』は、あとから自分の発信テーマにも転用しやすい素材です。"

    career_hint = career_text.strip()
    if career_hint:
        return (
            f"{goal_hint}{reason_hint}{job}として積み上げてきた『{career_hint[:45]}』の文脈を見ると、"
            f"{'、'.join(strengths[:3])}が土台になっています。{hobby_hint}"
        )
    return f"{goal_hint}{reason_hint}{job}としての経験を見ると、{'、'.join(strengths[:3])}が土台になっています。{hobby_hint}"


def pick_entry_tasks(job: str, experiences: List[str], goals: List[str], reasons: List[str]) -> List[Tuple[str, str]]:
    tasks: List[Tuple[str, str]] = []

    def add(title: str, desc: str) -> None:
        tasks.append((title, desc))

    job_map = {
        "会社員": [
            ("会議メモを1枚提案資料にまとめ直す作業", "打ち合わせ内容をそのまま文字にするのではなく、要点・比較・次アクションに整理し直す作業から入りやすいです。"),
            ("既存の営業資料を比較表つきで見やすく直す作業", "情報の並べ方を整えるだけで、企業側の判断コストを下げられるので入口として現実的です。"),
        ],
        "パート": [
            ("店舗やサービスの案内文をやさしく言い換える作業", "お客様目線で分かりにくい部分を見つけ、初回でも伝わる表現へ直す仕事に変えやすいです。"),
            ("口コミやレビューを拾って『選ばれる理由』に整理する作業", "現場で感じているリアルを、そのまま販促コンテンツの素材にしやすいです。"),
        ],
        "アルバイト": [
            ("求人ページ用に仕事内容をわかりやすく整理する作業", "現場の流れを知らない人向けに、仕事の順番や大変さを見える化する役割から入りやすいです。"),
            ("店舗案内・接客導線を1枚図解に直す作業", "来店前の不安や迷いを潰すコンテンツに変えやすいです。"),
        ],
        "主婦": [
            ("生活者目線で比較記事やレビュー構成を作る作業", "買う側・使う側の感覚がそのまま価値になるので、企業コンテンツでも自分発信でも活かしやすいです。"),
            ("家事・子育ての工夫を図解やチェックリストに直す作業", "実体験を『伝わる形』に変える入口として取り組みやすいです。"),
        ],
        "営業職": [
            ("提案トークを比較表と短い資料に落とす作業", "話せる人ほど、相手が理解しやすい資料へ変換する仕事に入りやすいです。"),
            ("商談後の要点整理と次アクション設計", "会話をそのまま終わらせず、次に進む形へまとめる作業が価値になります。"),
        ],
        "事務職": [
            ("業務手順をチェックリスト化・図解化する作業", "抜け漏れなく整理できる人ほど、企業の裏側で重宝されやすいです。"),
            ("散らかった資料を1枚に要約し直す作業", "情報の要点抽出そのものが収益に変わりやすいです。"),
        ],
        "接客販売": [
            ("商品比較表と接客トークの叩き台を作る作業", "お客様がどこで迷うかが分かる人ほど、売れる前の整理がしやすいです。"),
            ("初回客向けの来店前案内を見やすく整える作業", "不安を減らす一枚資料や導線づくりに向いています。"),
        ],
        "医療従事者": [
            ("専門用語をやさしい説明文に置き換える作業", "患者向け・家族向けの説明を短くわかりやすく整える作業から入りやすいです。"),
            ("健康テーマの記事構成や図解の下書きを作る作業", "専門性をそのまま書くのではなく、理解できる順番に直す役割が強みになります。"),
        ],
        "介護福祉職": [
            ("介護現場のリアルを採用向け文章に変える作業", "現場の実感がある人しか書けない内容を、企業の採用広報に変えやすいです。"),
            ("家族向け説明資料や流れ図を整える作業", "不安が強いテーマだからこそ、やさしく整理する力が価値になります。"),
        ],
        "工場勤務": [
            ("作業手順をスマホで見やすい形に直す作業", "文字ばかりの手順書を、図やチェック式に変える作業から入りやすいです。"),
            ("現場紹介や求人向けの流れ説明を作る作業", "働いたことがない人でも分かるように整理する仕事が向いています。"),
        ],
        "教育": [
            ("教材や説明スライドの順番を整え直す作業", "知っている人向けの資料を、初心者でも理解できる形に変える作業に向いています。"),
            ("長い解説を短い要点シートに直す作業", "要点抽出と順序設計がそのまま価値になります。"),
        ],
        "保育": [
            ("保護者向けの案内文や説明資料を整える作業", "安心感のある言い回しと、伝える順番の設計が価値になりやすいです。"),
            ("家庭向けコンテンツの構成を作る作業", "子ども・家庭のリアルな視点が、そのまま発信テーマにもつながります。"),
        ],
        "美容": [
            ("メニュー比較表や来店前案内を作る作業", "選び方が分かりにくいサービスほど、整理の価値が出やすいです。"),
            ("体験ベースのレビュー構成やSNS下書きを作る作業", "施術や商品選びの迷いを言語化できる人は強いです。"),
        ],
        "サロン": [
            ("初回来店前の不安を減らす案内文を作る作業", "予約前・来店前の離脱を減らすコンテンツづくりに向いています。"),
            ("ビフォーアフターや口コミを見やすく並べ直す作業", "実績の見せ方を整えるだけでも価値になります。"),
        ],
        "ジム・フィットネス関連": [
            ("初心者向けに入会前の流れを整理する作業", "最初の不安を減らす比較表や流れ説明に入りやすいです。"),
            ("運動・健康習慣の継続を支える発信下書き", "現場感のある言葉で、続ける理由を作るコンテンツに向いています。"),
        ],
        "フリーランス": [
            ("実績を比較表と事例シートに整理し直す作業", "いま持っている仕事を、単価が伝わる形へ見せ直す作業が先です。"),
            ("提案資料の構成と導線を整える作業", "提案の勝率を上げる裏方作業に寄せやすいです。"),
        ],
        "自営業": [
            ("自社の強みを比較表・説明図に落とす作業", "お客様が選びやすくなる見せ方を整えるところから始めやすいです。"),
            ("問い合わせ前の不安を潰すページ下書きを作る作業", "現場でよく聞かれることを、そのままコンテンツに変えやすいです。"),
        ],
        "その他": [
            ("日常業務を『見える化』して1枚にまとめる作業", "今まで当たり前にやってきたことを、企業が使える形へ変える入口として現実的です。"),
            ("既存情報をAIで整理し直して叩き台を作る作業", "ゼロから作るより、まずは整える作業の方が入りやすいです。"),
        ],
    }

    for item in job_map.get(job, job_map["その他"]):
        add(*item)

    if "Canva" in experiences or "デザイン" in experiences or "画像作成" in experiences:
        add("文章を1枚図解やスライドに変える作業", "説明だけでは伝わりにくい内容を、視覚的に理解しやすい形へ変える作業まで広げやすいです。")
    if "AI使用経験" in experiences or "ChatGPT使用経験" in experiences or "要約" in experiences:
        add("AIで叩き台を作り、人が仕上げる作業", "構成・下書き・要点整理をAIで早め、人が精度を上げる作業の相性が良いです。")
    if "ブログ執筆" in experiences or "記事作成" in experiences or "ライティング" in experiences:
        add("記事構成と見出し設計の作業", "いきなり長文を書くより、構成・見出し・比較軸を整える作業から入る方が再現しやすいです。")
    if "情報整理" in experiences or "資料作成" in experiences or "Excel・スプレッドシート" in experiences:
        add("比較表・一覧表・進行表を整える作業", "整理そのものが価値になりやすく、初心者でも入り口を作りやすいです。")
    if "接客" in experiences or "販売" in experiences or "問い合わせ対応" in experiences or "営業" in experiences:
        add("お客様が迷うポイントを先回りして潰す作業", "どこで止まるかが分かる人は、導線改善や説明整理で価値を出しやすいです。")

    if "自分のブログやSNSも資産化したい" in goals or "企業案件で型を学びながら自分の資産にもつなげたい" in reasons:
        add("企業案件で学んだ型を自分の発信へ移植する作業", "納品だけで終わらず、構成・導線・見せ方を自分のブログやSNSにも移せる流れを作りやすいです。")

    unique_titles = set()
    unique_tasks: List[Tuple[str, str]] = []
    for title, desc in tasks:
        if title not in unique_titles:
            unique_titles.add(title)
            unique_tasks.append((title, desc))
    return unique_tasks[:5]


def pick_markets(job: str, hobbies: str, reasons: List[str], goals: List[str]) -> List[str]:
    markets = []
    job_to_market = {
        "医療従事者": ["医療・健康", "クリニック", "患者向け説明コンテンツ"],
        "介護福祉職": ["介護", "福祉", "採用広報"],
        "教育": ["教育", "研修", "初心者向け解説"],
        "保育": ["子育て", "家庭向けサービス", "保護者向け説明"],
        "美容": ["美容", "サロン", "比較・レビュー"],
        "サロン": ["美容", "店舗集客", "継続導線"],
        "ジム・フィットネス関連": ["フィットネス", "健康習慣", "入会導線"],
        "接客販売": ["店舗集客", "比較・導線", "レビュー整理"],
        "営業職": ["BtoBサービス", "比較表", "提案資料"],
        "事務職": ["バックオフィス", "業務改善", "手順整理"],
        "工場勤務": ["製造業", "安全教育", "採用広報"],
        "主婦": ["生活情報", "子育て", "レビュー"],
    }
    markets.extend(job_to_market.get(job, ["業務整理", "情報発信", "比較・説明コンテンツ"]))

    hobby_lower = hobbies.lower()
    if any(word in hobby_lower for word in ["美容", "コスメ", "スキンケア"]):
        markets.append("美容・レビュー")
    if any(word in hobby_lower for word in ["旅行", "ホテル", "おでかけ"]):
        markets.append("旅行・比較")
    if any(word in hobby_lower for word in ["料理", "食", "レシピ"]):
        markets.append("食・暮らし")
    if any(word in hobby_lower for word in ["子育て", "育児"]):
        markets.append("子育て")
    if any(word in hobby_lower for word in ["健康", "運動", "ジム"]):
        markets.append("健康・運動")

    if "自分のブログやSNSも資産化したい" in goals:
        markets.append("自分資産につながる発信テーマ")
    if "企業案件で型を学びながら自分の資産にもつなげたい" in reasons:
        markets.append("企業案件→自分資産へ移植しやすい分野")

    return unique_keep_order(markets)[:5]


def build_roadmap(work_hours: float, blog_have: str, side_history: str) -> List[Tuple[str, str]]:
    phase1 = (
        "0〜30日",
        "まずは『何を売るか』ではなく、『何を整理できる人か』を固めます。AIで下書きを作り、Canvaや文章で見やすく整える型を1つ身につけ、最初のサンプルを1〜2個作る段階です。",
    )

    if side_history in ["まだ取り組んでいない", "1ヶ月未満"]:
        phase2_text = "小さな案件や模擬案件で、比較表・記事構成・1枚図解・手順整理のどれか1つに絞って納品経験を作ります。ここでは完璧さより、型に沿って最後まで出すことを優先します。"
    else:
        phase2_text = "すでにある経験を活かして、単発作業ではなく『継続しやすい整理・改善作業』へ寄せます。既存の発信や実績を、企業案件用の見せ方に直していく段階です。"

    if work_hours <= 1.0:
        phase3_text = "時間が限られる前提なので、毎日少しずつ進められる作業に寄せるのが重要です。まずは継続しやすい型を固定し、作業時間を増やさずに単価が落ちにくい内容へ寄せていきます。"
    elif work_hours <= 2.0:
        phase3_text = "平日夜の積み上げで、90日で土台を作り、その後に継続案件へ寄せるのが現実的です。『書くだけ』ではなく、整理・構成・図解まで触れると伸びやすいです。"
    else:
        phase3_text = "稼働時間を取りやすいので、記事・図解・導線改善のように複数の納品パターンを持ちやすい状態です。90日で型を固め、継続案件と自分発信を並行しやすくなります。"

    phase2 = ("31〜60日", phase2_text)
    phase3 = ("61〜90日", phase3_text)

    if blog_have == "持っている":
        phase4 = ("90日以降の伸ばし方", "企業案件で使った構成や導線の型を、自分のブログやSNSにも移植します。自分の発信を後回しにせず、型を学びながら並行で育てる設計が取りやすいです。")
    else:
        phase4 = ("90日以降の伸ばし方", "最初は企業案件で型を学び、その後で自分のブログやSNSを立ち上げる流れが現実的です。ゼロから自分発信だけで悩むより遠回りしにくいです。")

    return [phase1, phase2, phase3, phase4]


def build_lifestyle_image(work_hours: float, holiday_text: str, marital: str, child_status: str, child_count: str, holiday_hours: str) -> str:
    if work_hours <= 1.0:
        base = "平日は30分〜1時間で下書きや整理を進め、休日にまとめて仕上げる形が現実的です。"
    elif work_hours <= 2.0:
        base = "平日は夜1〜2時間で進め、休日に構成や図解をまとめる流れが現実的です。"
    else:
        base = "平日にもまとまった時間を使えるので、納品・改善・自分の発信まで並行しやすい状態です。"

    family = ""
    if marital == "既婚" and child_status == "いる":
        family = f"家庭との両立前提なので、子ども{child_count}人の生活リズムを崩さない範囲で『毎日少しずつ進む作業』を優先した方が続きやすいです。"
    elif marital == "既婚":
        family = "家庭との両立前提で、急に大きく変えるより生活に乗る形にした方が続きやすいです。"

    holiday = f"休日は『{holiday_hours}』ほど確保しやすく、過ごし方が『{holiday_text}』なら、それを崩しすぎない進め方に寄せる方が現実的です。" if holiday_text.strip() else f"休日は『{holiday_hours}』ほど確保しやすいので、全部を作業に使う前提ではなく、無理なく回せる配分で設計した方が現実的です。"

    return f"{base}{family}{holiday}"


def build_current_pattern(
    current_job: str,
    work_hours: float,
    reasons: List[str],
    goals: List[str],
    side_history: str,
    experiences: List[str],
) -> Tuple[str, str]:
    pattern1 = (
        f"いまの『{current_job}』の延長だけで日々が過ぎると、経験は増えても、それが副収入や資産に変わらないまま止まりやすいです。"
        f" とくに{work_hours}時間の作業時間を確保できるのに着手しない状態が続くと、1年後も『考えていたけど何も積み上がっていない』に戻りやすいです。"
    )

    reason_hint = ""
    if reasons:
        reason_hint = f"『{reasons[0]}』という悩みがあるのに、"
    goal_hint = ""
    if goals:
        goal_hint = f"『{goals[0]}』を目指していても、"

    if side_history in ["まだ取り組んでいない", "1ヶ月未満"]:
        pattern2 = (
            f"{reason_hint}{goal_hint}型や順番を持たずに始めると、頑張っているつもりでも、収益に繋がらない作業だけが増えやすいです。"
            " 調べる・投稿する・作るを繰り返しても、企業ニーズに合う形へ変換できないままだと、時間だけを消費して止まりやすくなります。"
        )
    else:
        exp_hint = "、".join(experiences[:3]) if experiences else "これまでの経験"
        pattern2 = (
            f"すでに『{exp_hint}』のような土台があっても、正しい順番や型を使わずに自己流で広げると、単発作業ばかり増えて継続収益に繋がりにくくなります。"
            " 少し頑張っているのに手応えが薄い人は、このズレで止まっているケースが多いです。"
        )

    return pattern1, pattern2


def build_success_route(
    display_name: str,
    current_job: str,
    work_hours: float,
    entry_tasks: List[Tuple[str, str]],
    annual_projection: List[int],
    reasons: List[str],
    goals: List[str],
) -> str:
    first_task = entry_tasks[0][0] if entry_tasks else "整理・構成・図解の作業"
    reason_hint = f"『{reasons[0]}』という悩みがあるなら、" if reasons else ""
    goal_hint = f"『{goals[0]}』を目指すなら、" if goals else ""

    return (
        f"{reason_hint}{goal_hint}{display_name}さんは、型や順番を意識して、{current_job}としての経験を企業ニーズに合わせて価値へ変換していく方向性が合っています。"
        f" 入口は『{first_task}』のような、整理して伝わる形に直す作業から入るのが現実的です。"
        f" 1日{work_hours}時間の作業なら、<span class='accent-blue'>1年目は{annual_projection[0]:,}円前後</span>、"
        f"<span class='accent'>{annual_projection[1]:,}円前後</span>が現実ラインとして見えやすく、"
        f"その後は単発ではなく継続しやすい作業へ寄せながら積み上げていけます。"
        " 実際の取り組み方について、ここから具体的に解説します。"
    )


def build_income_outlook_text(target_label: str, target_income: int, current_monthly: int, ideal_monthly: int, work_hours: float) -> str:
    gap_current = target_income - current_monthly
    gap_ideal = target_income - ideal_monthly

    if target_income <= current_monthly:
        relation = f"いまの条件でも、1日{work_hours}時間なら<span class='accent-blue'>現実ラインで月{current_monthly:,}円前後</span>が見えています。"
    elif target_income <= ideal_monthly:
        relation = (
            f"いまの条件なら、1日{work_hours}時間で<span class='accent-blue'>現実ラインは月{current_monthly:,}円前後</span>、"
            f"<span class='accent'>理想ラインは月{ideal_monthly:,}円前後</span>です。"
            f" 目標の{target_label}は、型と順番を揃えることで十分に射程に入る位置です。"
        )
    else:
        relation = (
            f"いまの条件だと、1日{work_hours}時間で<span class='accent-blue'>現実ラインは月{current_monthly:,}円前後</span>、"
            f"<span class='accent'>理想ラインは月{ideal_monthly:,}円前後</span>です。"
            f" 目標の{target_label}までは現実ラインとの差が{gap_current:,}円、理想ラインとの差が{max(gap_ideal, 0):,}円あるため、"
            "作業時間を増やすより、単価が落ちにくい作業へ寄せる設計が重要です。"
        )

    lift = ideal_monthly - current_monthly
    return relation + f" 現実ラインと理想ラインの差は<span class='accent-yellow'>{lift:,}円前後</span>で、少し頑張り方を変えるだけでも数か月後の見え方は変わります。"


def render_result_card(title: str, body: str) -> None:
    st.markdown(
        f"""
        <div class="card">
            <h3 style="margin-top:0;">{title}</h3>
            <div class="lead">{body}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_timeline_card(title: str, roadmap: List[Tuple[str, str]]) -> None:
    items_html = ""
    for phase_title, phase_desc in roadmap:
        items_html += f"""
        <div class="timeline-item">
            <div class="timeline-label">{phase_title}</div>
            <div class="lead">{phase_desc}</div>
        </div>
        """

    st.markdown(
        f"""
        <div class="card">
            <h3 style="margin-top:0;">{title}</h3>
            <div class="timeline">{items_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_compare_card(title: str, left_title: str, left_body: str, right_title: str, right_body: str) -> None:
    st.markdown(
        f"""
        <div class="card">
            <h3 style="margin-top:0;">{title}</h3>
            <div class="compare-wrap">
                <div class="compare-box">
                    <div class="compare-title">{left_title}</div>
                    <div class="lead">{left_body}</div>
                </div>
                <div class="compare-box">
                    <div class="compare-title">{right_title}</div>
                    <div class="lead">{right_body}</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.title("個別専用キャリア設計図ロードマップ作成")
st.markdown(
    "<p class='lead'>Zoomで画面共有しながら、その場のヒアリング内容をもとに『何をやると、どう価値になり、どの順番で進めるか』を整理するためのシミュレーターです。入力項目全体から現在地と伸ばし方を見立て、会話の中で未来を具体化するために使います。</p>",
    unsafe_allow_html=True,
)
st.divider()

st.markdown("<div class='section-title'>1. 基本プロフィール</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("お名前", placeholder="例：山田 花子")
    age = st.selectbox("年齢", AGE_OPTIONS, index=4)
    current_job = st.selectbox("現在の職業", JOB_OPTIONS, index=0)
    gender = st.selectbox("性別", GENDER_OPTIONS, index=0)
with col2:
    marital = st.selectbox("既婚・未婚", MARITAL_OPTIONS, index=0)
    child_status = st.selectbox("お子様の有無", CHILD_OPTIONS, index=0)
    child_count = st.selectbox("お子様の人数", CHILD_COUNT_OPTIONS, index=0)
    region = st.selectbox("お住まいの地域", REGION_OPTIONS, index=2)

career_text = st.text_area("これまでの経歴", height=100, placeholder="例：医療事務を7年、その後クリニック受付を3年。新人教育も担当。")

st.divider()
st.markdown("<div class='section-title'>2. 経験の棚卸し</div>", unsafe_allow_html=True)
experiences = st.multiselect(
    "経験のあること（仕事・副業・趣味で、少しでも触れたことがあれば選択してください）",
    EXPERIENCE_OPTIONS,
)

blog_col1, blog_col2 = st.columns(2)
with blog_col1:
    blog_have = st.selectbox("ブログはお持ちですか", BLOG_HAVE_OPTIONS, index=1)
with blog_col2:
    blog_history = st.selectbox("ブログ運用歴", BLOG_HISTORY_OPTIONS, index=0)

side_col1, side_col2 = st.columns(2)
with side_col1:
    side_history = st.selectbox("副業歴", SIDE_HISTORY_OPTIONS, index=0)
with side_col2:
    current_revenue = st.selectbox("現在の収益額", REVENUE_OPTIONS, index=0)

best_revenue = st.selectbox("これまでに副業へ取り組んだことがあれば、最高実績を教えてください", ["実績なし"] + REVENUE_OPTIONS, index=0)

st.divider()
st.markdown("<div class='section-title'>3. 現在地と作業条件</div>", unsafe_allow_html=True)
work_col1, work_col2 = st.columns(2)
with work_col1:
    work_hours = st.slider("1日に確保できる平均作業時間", min_value=0.5, max_value=5.0, value=2.0, step=0.5)
with work_col2:
    holiday_hours = st.selectbox("休日に確保しやすい時間", ["ほぼ取れない", "1〜2時間", "3〜4時間", "5時間以上"], index=1)

holiday_style = st.text_area("休日の主な過ごし方", height=90, placeholder="例：家族と過ごす、買い物、子どもの習い事、家事をまとめる など")

income_col1, income_col2 = st.columns(2)
with income_col1:
    annual_income = st.selectbox("現在の年収", ANNUAL_INCOME_OPTIONS, index=3)
with income_col2:
    household_income = st.selectbox("世帯年収", HOUSEHOLD_INCOME_OPTIONS, index=3)

savings = st.selectbox("現在の貯金額（今後どのぐらい増えるかのお話もするためです）", SAVINGS_OPTIONS, index=2)

st.divider()
st.markdown("<div class='section-title'>4. 申し込み理由・今後の目標</div>", unsafe_allow_html=True)
reasons = st.multiselect("個別相談に申し込んだ理由", REASON_OPTIONS)
goals = st.multiselect("今後の目標・将来設計", GOAL_OPTIONS)
why_now = st.text_area("なぜ、これから頑張ってみようと思いましたか？", height=90, placeholder="例：このまま今の働き方だけだと不安で、次の収入源を準備したい")
hobbies = st.text_area("趣味・特技・少しでも興味があること", height=90, placeholder="例：旅行、健康、美容、家計管理、子育て、料理、SNSを見ること など")

st.divider()
st.markdown("<div class='section-title'>5. 収益シミュレーター</div>", unsafe_allow_html=True)
target_label = st.select_slider("目標金額", options=list(TARGET_INCOME_OPTIONS.keys()), value="月5万円")
target_income = TARGET_INCOME_OPTIONS[target_label]

score = experience_score(experiences, side_history, current_revenue, best_revenue, blog_history)
hours_points, current_line, ideal_line = build_income_lines(score)
current_monthly, ideal_monthly = selected_income_values(work_hours, hours_points, current_line, ideal_line)
years, annual_projection, cumulative_projection = build_long_term_projection(current_monthly, ideal_monthly, score, work_hours)

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=hours_points,
        y=current_line,
        mode="lines+markers",
        name="現実ライン",
        line=dict(color=COLOR_BLUE, width=4),
        marker=dict(size=8, color=COLOR_BLUE),
        hovertemplate="1日%{x}時間<br>現実ライン: <b>%{y:,.0f}円</b><extra></extra>",
    )
)
fig.add_trace(
    go.Scatter(
        x=hours_points,
        y=ideal_line,
        mode="lines+markers",
        name="理想ライン",
        line=dict(color=COLOR_PINK, width=4),
        marker=dict(size=8, color=COLOR_PINK),
        hovertemplate="1日%{x}時間<br>理想ライン: <b>%{y:,.0f}円</b><extra></extra>",
    )
)
fig.add_trace(
    go.Scatter(
        x=hours_points,
        y=[target_income] * len(hours_points),
        mode="lines",
        name="目標金額",
        line=dict(color=COLOR_YELLOW, width=3, dash="dash"),
        hovertemplate="目標: <b>%{y:,.0f}円</b><extra></extra>",
    )
)
fig.add_trace(
    go.Scatter(
        x=[work_hours],
        y=[current_monthly],
        mode="markers",
        name="現在の作業時間での現実ライン",
        marker=dict(size=14, color=COLOR_BLUE, line=dict(color=COLOR_BG, width=2)),
        hovertemplate="選択中: 1日%{x}時間<br>現実ライン: <b>%{y:,.0f}円</b><extra></extra>",
        showlegend=False,
    )
)
fig.add_trace(
    go.Scatter(
        x=[work_hours],
        y=[ideal_monthly],
        mode="markers",
        name="現在の作業時間での理想ライン",
        marker=dict(size=14, color=COLOR_PINK, line=dict(color=COLOR_BG, width=2)),
        hovertemplate="選択中: 1日%{x}時間<br>理想ライン: <b>%{y:,.0f}円</b><extra></extra>",
        showlegend=False,
    )
)
fig.update_layout(
    height=430,
    margin=dict(l=20, r=20, t=30, b=20),
    plot_bgcolor=COLOR_BG,
    paper_bgcolor=COLOR_BG,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    hovermode="x unified",
)
fig.update_yaxes(title_text="月間収益額（円）", tickformat=",d", gridcolor="rgba(36,52,71,0.08)")
fig.update_xaxes(title_text="1日に確保できる平均作業時間", showgrid=False)
st.plotly_chart(fig, use_container_width=True)

income_comment = build_income_outlook_text(target_label, target_income, current_monthly, ideal_monthly, work_hours)
render_result_card("収益ラインの見通し", income_comment)

center_left, center_mid, center_right = st.columns([1, 1.6, 1])
with center_mid:
    st.markdown('<div class="center-button">', unsafe_allow_html=True)
    if st.button("個別専用キャリア設計図を作成する"):
        st.session_state.generated = True
    st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.generated:
    display_name = name.strip() if name.strip() else "この方"
    strength_summary = build_strength_summary(current_job, experiences, career_text, reasons, goals, why_now, hobbies)
    entry_tasks = pick_entry_tasks(current_job, experiences, goals, reasons)
    markets = pick_markets(current_job, hobbies, reasons, goals)
    roadmap = build_roadmap(work_hours, blog_have, side_history)
    lifestyle = build_lifestyle_image(work_hours, holiday_style, marital, child_status, child_count, holiday_hours)
    risk_pattern_1, risk_pattern_2 = build_current_pattern(current_job, work_hours, reasons, goals, side_history, experiences)
    success_route = build_success_route(display_name, current_job, work_hours, entry_tasks, annual_projection, reasons, goals)

    st.divider()
    st.markdown("<div class='section-title'>作成結果</div>", unsafe_allow_html=True)

    experience_text = "、".join(experiences[:6]) if experiences else "未整理の経験も含めて棚卸し余地あり"
    profile_line = profile_tags(age, region, marital, child_status, current_job)
    summary_text = (
        f"{display_name}さんは<span class='accent-blue'>{profile_line}</span>の条件で、経験としては『{experience_text}』が土台です。"
        f" 現状の作業時間は1日あたり{work_hours}時間。ブログは『{blog_have}』、副業歴は『{side_history}』で、"
        f"現収益は『{current_revenue}』、最高実績は『{best_revenue}』です。"
        f" 年収は『{annual_income}』、世帯年収は『{household_income}』、貯金額は『{savings}』という前提なので、"
        f"短期で無理に跳ねさせるより、生活に乗る形で積み上げる設計の方が合っています。"
        f" 『{why_now[:40] if why_now.strip() else 'いま動く理由を言語化できる状態'}』という動機も見えているため、"
        f"思いつきではなく、順番を決めて進める方が成果に変わりやすい状態です。"
    )
    render_result_card("今の土台から見えること", summary_text + "<br><br>" + strength_summary)

    task_lines = []
    for title, desc in entry_tasks:
        task_lines.append(f"<div class='mini-card'><b>{title}</b><br><span class='lead'>{desc}</span></div>")
    render_result_card("あなたの経験が高単価な価値に変わる具体的な作業内容", "".join(task_lines))

    market_text = "、".join(markets) if markets else "業務整理・情報整理・説明コンテンツ"
    render_result_card(
        "最初に狙いやすい市場・テーマ",
        f"最初から何でも狙うより、<span class='accent-blue'>{market_text}</span>のように、今の経験や興味とつながる分野から入る方が遠回りしにくいです。企業案件で型を学び、その型をあとから自分のブログやSNSへ移す流れが作りやすいです。",
    )

    render_timeline_card("90日ロードマップ", roadmap)
    render_result_card("日々のライフスタイルイメージ", lifestyle)

    render_compare_card(
        "現状維持で起こりやすいパターン",
        "実際に取り組まないまま時間が過ぎるパターン",
        risk_pattern_1,
        "少し頑張っているが、順番や型がズレるパターン",
        risk_pattern_2,
    )

    render_result_card("成功する人のルート", success_route)

    long_fig = go.Figure()
    long_fig.add_trace(
        go.Bar(
            x=years,
            y=annual_projection,
            name="年間収益",
            marker_color=COLOR_BLUE,
            hovertemplate="%{x}<br>年間収益: <b>%{y:,.0f}円</b><extra></extra>",
        )
    )
    long_fig.add_trace(
        go.Scatter(
            x=years,
            y=cumulative_projection,
            mode="lines+markers",
            name="累計収益",
            line=dict(color=COLOR_PINK, width=4),
            marker=dict(size=9, color=COLOR_YELLOW, line=dict(color=COLOR_PINK, width=1.5)),
            hovertemplate="%{x}<br>累計収益: <b>%{y:,.0f}円</b><extra></extra>",
        )
    )
    long_fig.update_layout(
        height=430,
        margin=dict(l=20, r=20, t=30, b=20),
        plot_bgcolor=COLOR_BG,
        paper_bgcolor=COLOR_BG,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
        hovermode="x unified",
    )
    long_fig.update_yaxes(title_text="収益額（円）", tickformat=",d", gridcolor="rgba(36,52,71,0.08)")
    long_fig.update_xaxes(showgrid=False)
    st.plotly_chart(long_fig, use_container_width=True)

    long_summary = (
        f"いまの条件なら、<span class='accent-blue'>1年目は{annual_projection[0]:,}円前後</span>を現実ラインとして見ながら、"
        f"<span class='accent'>2年目は{annual_projection[1]:,}円前後</span>、"
        f"5年累計では<span class='accent-yellow'>{cumulative_projection[-1]:,}円前後</span>まで積み上がる見立てです。"
        " ここで重要なのは、作業時間だけで伸ばすのではなく、整理・構成・図解のように単価が落ちにくい作業へ寄せることです。"
    )
    render_result_card("1〜5年の収益見通し", long_summary)
