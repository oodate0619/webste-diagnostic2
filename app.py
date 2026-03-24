import math
from typing import List, Tuple

import plotly.graph_objects as go
import streamlit as st


st.set_page_config(
    page_title="個別専用キャリア設計図ロードマップ作成",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    html, body, [class*="css"]  {
        font-family: 'Helvetica Neue', Helvetica, Arial, 'Hiragino Sans', sans-serif;
        color: #243447;
    }
    .stApp {
        background-color: #F7F8FA;
    }
    h1, h2, h3 {
        color: #17324D;
        letter-spacing: 0.2px;
    }
    .lead {
        font-size: 17px;
        line-height: 1.8;
        color: #425466;
    }
    .card {
        background: #FFFFFF;
        border: 1px solid #E6E8EC;
        border-radius: 16px;
        padding: 18px 20px;
        margin-bottom: 16px;
        box-shadow: 0 2px 10px rgba(16, 24, 40, 0.04);
    }
    .mini-card {
        background: #FFFFFF;
        border: 1px solid #E6E8EC;
        border-radius: 14px;
        padding: 12px 14px;
        margin-bottom: 10px;
    }
    .caption {
        font-size: 13px;
        color: #6B7280;
    }
    .em {
        color: #C77D1A;
        font-weight: 700;
    }
    .section-title {
        font-size: 24px;
        font-weight: 700;
        color: #17324D;
        margin-top: 10px;
        margin-bottom: 8px;
    }
    .timeline {
        position: relative;
        margin-top: 8px;
        padding-left: 18px;
    }
    .timeline:before {
        content: "";
        position: absolute;
        left: 8px;
        top: 8px;
        bottom: 8px;
        width: 2px;
        background: #D8DEE8;
    }
    .timeline-item {
        position: relative;
        background: #FFFFFF;
        border: 1px solid #E6E8EC;
        border-radius: 14px;
        padding: 12px 14px;
        margin-bottom: 12px;
    }
    .timeline-item:before {
        content: "";
        position: absolute;
        left: -16px;
        top: 16px;
        width: 12px;
        height: 12px;
        border-radius: 999px;
        background: #17324D;
        border: 2px solid #F7F8FA;
    }
    .timeline-label {
        display: inline-block;
        font-size: 13px;
        font-weight: 700;
        color: #17324D;
        background: #EEF4FB;
        padding: 4px 8px;
        border-radius: 999px;
        margin-bottom: 8px;
    }
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        background: #17324D;
        color: white;
        font-weight: 700;
        border: none;
        padding: 0.8rem 1rem;
        font-size: 18px;
    }
    .stButton > button:hover {
        background: #25496E;
        color: white;
    }
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

TARGET_INCOME_OPTIONS = {
    "月3万円": 30000,
    "月5万円": 50000,
    "月10万円": 100000,
    "月15万円": 150000,
    "月20万円": 200000,
}


if "generated" not in st.session_state:
    st.session_state.generated = False


def unique_keep_order(items: List[str]) -> List[str]:
    seen = set()
    result = []
    for item in items:
        if item and item not in seen:
            seen.add(item)
            result.append(item)
    return result


def experience_score(experiences: List[str], side_history: str, current_revenue: str, best_revenue: str) -> int:
    score = len(experiences)

    if side_history in ["3〜6ヶ月", "6ヶ月〜1年"]:
        score += 2
    elif side_history in ["1〜2年", "2年以上"]:
        score += 4

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
        return 0.90
    if score <= 7:
        return 1.00
    if score <= 12:
        return 1.10
    return 1.18


def get_target_uplift(score: int) -> float:
    if score <= 4:
        return 1.15
    if score <= 10:
        return 1.18
    return 1.20


def hours_to_ceiling(hours: float) -> int:
    base_map = {
        0.5: 18000,
        1.0: 30000,
        1.5: 42000,
        2.0: 55000,
        2.5: 70000,
        3.0: 85000,
        3.5: 100000,
        4.0: 120000,
        4.5: 135000,
        5.0: 150000,
    }
    return base_map.get(hours, 55000)


def build_simulation(target_income: int, work_hours: float, score: int) -> Tuple[List[str], List[int], int, bool]:
    months = ["1ヶ月目", "2ヶ月目", "3ヶ月目", "4ヶ月目", "5ヶ月目", "6ヶ月目"]
    base_ceiling = int(hours_to_ceiling(work_hours) * get_experience_multiplier(score))
    uplifted_target = int(round(target_income * get_target_uplift(score) / 1000) * 1000)
    ceiling = max(base_ceiling, uplifted_target)
    progress = [0.24, 0.46, 0.64, 0.81, 0.93, 1.00]
    forecast = [int(round(ceiling * p / 1000) * 1000) for p in progress]
    can_hit = ceiling >= target_income
    return months, forecast, ceiling, can_hit


def build_long_term_projection(monthly_end: int, score: int, work_hours: float) -> Tuple[List[str], List[int], List[int]]:
    years = ["1年目", "2年目", "3年目", "4年目", "5年目"]

    if work_hours <= 1.0:
        growth_curve = [0.95, 1.18, 1.35, 1.50, 1.62]
    elif work_hours <= 2.0:
        growth_curve = [1.00, 1.28, 1.52, 1.72, 1.90]
    else:
        growth_curve = [1.05, 1.35, 1.65, 1.92, 2.15]

    score_bonus = 0.00
    if score >= 8:
        score_bonus = 0.06
    if score >= 13:
        score_bonus = 0.10

    annuals: List[int] = []
    for idx, base in enumerate(growth_curve):
        factor = base + score_bonus
        annual = int(round((monthly_end * factor * 12) / 10000) * 10000)
        if idx > 0 and annual <= annuals[-1]:
            annual = annuals[-1] + 120000
        annuals.append(annual)

    cumulative: List[int] = []
    running = 0
    for annual in annuals:
        running += annual
        cumulative.append(running)

    return years, annuals, cumulative


def pick_entry_tasks(job: str, experiences: List[str]) -> List[Tuple[str, str]]:
    tasks: List[Tuple[str, str]] = []

    def add(title: str, desc: str) -> None:
        tasks.append((title, desc))

    job_map = {
        "会社員": [
            ("社内向けFAQ・説明資料の整理", "普段の業務でよく聞かれることを、1枚資料や簡易マニュアルに落とし込む仕事から入りやすいです。"),
            ("比較表・導線整理", "情報を並べて整理する力がそのまま企業の資料改善に転用しやすいです。"),
        ],
        "パート": [
            ("店舗・サービスの説明整理", "お客様目線で分かりやすく言い換える仕事に変えやすいです。"),
            ("口コミ・レビュー整理", "現場感のある言葉で、選ばれる理由を整える仕事につなげやすいです。"),
        ],
        "アルバイト": [
            ("接客導線の見直し資料", "現場で詰まりやすい箇所を見つけて、分かりやすく直す役割から入りやすいです。"),
            ("求人向けの現場説明コンテンツ", "仕事内容をやさしく伝える文章や図解に変えやすいです。"),
        ],
        "主婦": [
            ("生活者目線の比較記事・レビュー構成", "家事・子育て・買い物のリアルな視点が、そのまま信頼される一次情報になります。"),
            ("やさしい説明資料づくり", "難しい内容を日常の言葉で置き換える役割に向いています。"),
        ],
        "営業職": [
            ("提案資料・比較表の改善", "相手が判断しやすい並べ方や伝え方が、そのまま価値になります。"),
            ("商談後の要点整理", "会話を整理して、次の行動に落とす仕事に変えやすいです。"),
        ],
        "事務職": [
            ("業務フロー・マニュアル整備", "手順を抜け漏れなく整理する力が、そのまま高単価な裏方業務になります。"),
            ("議事録・情報整理の再構成", "バラバラな情報をまとめ直して、見やすい形にする仕事が狙いやすいです。"),
        ],
        "接客販売": [
            ("FAQ・接客トーク整理", "よく聞かれる質問や案内の型を整える仕事に転用しやすいです。"),
            ("商品比較・導線改善", "迷うポイントが分かる人ほど、選びやすい導線を作れます。"),
        ],
        "医療従事者": [
            ("健康系コラム・説明資料", "専門知識を難しくしすぎず伝え直す仕事に向いています。"),
            ("患者向けのやさしい図解", "専門用語をやさしい言葉に変えて整理する力が価値になります。"),
        ],
        "介護福祉職": [
            ("介護現場の説明コンテンツ", "現場のリアルがわかる人しか書けない内容を企業向けに変えられます。"),
            ("採用向けの現場紹介記事", "きつさだけでなくやりがいも伝えられる一次情報が強みになります。"),
        ],
        "工場勤務": [
            ("作業手順書の見やすい再設計", "古い手順書を、スマホで見やすい図解やチェック形式に変える仕事に入りやすいです。"),
            ("安全確認・求人向け現場説明", "現場の空気感を知っている人の言葉は採用広報で強いです。"),
        ],
        "教育": [
            ("教材・説明スライド整理", "伝える順番を整える力が、そのまま企業の教育資料改善に変わります。"),
            ("初心者向けの解説コンテンツ", "難しい内容を段階的に伝える仕事に向いています。"),
        ],
        "保育": [
            ("保護者向けの説明資料", "やさしい言い換えと安心感のある伝え方が強みになります。"),
            ("子ども・家庭向けコンテンツ", "生活に根ざした視点がそのまま価値になります。"),
        ],
        "美容": [
            ("メニュー説明・比較導線", "選ばれる理由を見える化する資料やSNS導線改善に入りやすいです。"),
            ("美容体験をもとにした発信設計", "体感のある言葉が、企業の販促コンテンツに転用しやすいです。"),
        ],
        "サロン": [
            ("来店前の不安を減らすFAQ", "初回のお客様が迷うポイントを整えるコンテンツに向いています。"),
            ("継続導線の見直し", "来店後の案内や提案内容を見直す仕事につなげやすいです。"),
        ],
        "ジム・フィットネス関連": [
            ("初心者向けの説明資料・比較表", "入会前に迷う点を整理する役割に向いています。"),
            ("健康・運動習慣の発信補助", "現場感のある文章や図解にしやすいです。"),
        ],
        "フリーランス": [
            ("提案資料の改善", "すでにお客様目線があるので、情報整理と提案設計に寄せやすいです。"),
            ("既存実績の再編集", "事例整理や見せ方改善で単価アップに接続しやすいです。"),
        ],
        "自営業": [
            ("自社の強み整理・比較表作成", "お客様が迷うポイントを潰す資料づくりに向いています。"),
            ("既存導線の言語化", "来店・問い合わせまでの流れを整える仕事に変えやすいです。"),
        ],
        "その他": [
            ("日常業務の見える化", "今まで当たり前にやってきたことを、企業向けのノウハウや説明資料に変える入口から始めやすいです。"),
            ("AIを使った情報整理", "ゼロから作るより、既存情報を整理し直す仕事から入る方が現実的です。"),
        ],
    }

    for item in job_map.get(job, job_map["その他"]):
        add(*item)

    if "Canva" in experiences or "デザイン" in experiences or "画像作成" in experiences:
        add("1枚図解・スライド化", "文章だけでなく、見るだけで伝わる形にする仕事まで広げやすいです。")
    if "AI使用経験" in experiences or "ChatGPT使用経験" in experiences or "要約" in experiences:
        add("AIを使った下書き整理", "ゼロから書くより、AIで叩き台を作り、整えて仕上げる流れが合っています。")
    if "ブログ執筆" in experiences or "記事作成" in experiences or "ライティング" in experiences:
        add("企業ブログ・コラム構成", "まずは構成と見出しづくりから入り、徐々に改善提案まで寄せる動きが取りやすいです。")
    if "情報整理" in experiences or "資料作成" in experiences or "Excel・スプレッドシート" in experiences:
        add("比較表・業務整理資料", "整理力そのものが価値になりやすく、初心者でも入り口を作りやすい分野です。")
    if "接客" in experiences or "販売" in experiences or "問い合わせ対応" in experiences or "営業" in experiences:
        add("お客様目線の導線改善", "何で迷うか、どこで離脱するかが分かる人は、導線の改善提案に強いです。")

    unique_titles = set()
    unique_tasks: List[Tuple[str, str]] = []
    for title, desc in tasks:
        if title not in unique_titles:
            unique_titles.add(title)
            unique_tasks.append((title, desc))
    return unique_tasks[:5]


def build_strength_summary(job: str, experiences: List[str], career_text: str) -> str:
    strengths = []

    if job in ["事務職", "会社員", "営業職", "フリーランス", "自営業"]:
        strengths.append("情報を整理して、相手が判断しやすい形に直す力")
    if job in ["接客販売", "パート", "アルバイト", "営業職", "サロン", "美容", "ジム・フィットネス関連"]:
        strengths.append("相手が迷うポイントや不安を先回りして言葉にする力")
    if job in ["医療従事者", "介護福祉職", "教育", "保育"]:
        strengths.append("難しいことを、わかりやすく伝え直す力")
    if job in ["工場勤務"]:
        strengths.append("現場の手順や安全確認を、抜け漏れなく扱う力")
    if job in ["主婦"]:
        strengths.append("生活者としてのリアルな視点で、選ぶ理由や続ける理由を言葉にする力")

    if "Canva" in experiences or "デザイン" in experiences:
        strengths.append("文章だけでなく、視覚的に伝える形まで整えられる力")
    if "AI使用経験" in experiences or "ChatGPT使用経験" in experiences:
        strengths.append("叩き台を早く作り、仕上げに集中できる力")
    if "ブログ執筆" in experiences or "SNS運用" in experiences:
        strengths.append("発信を継続しやすいテーマや切り口を見つける力")
    if "情報整理" in experiences or "資料作成" in experiences:
        strengths.append("散らかった情報を、見やすく整える力")

    strengths = unique_keep_order(strengths)
    if not strengths:
        strengths = ["今まで当たり前にやってきたことを、企業向けの形に置き換える力"]

    career_hint = career_text.strip()
    if career_hint:
        return f"{job}としての経験や『{career_hint[:40]}』の文脈を見ると、{'、'.join(strengths[:3])}が強みとして活かしやすい状態です。"
    return f"{job}としての経験を見ると、{'、'.join(strengths[:3])}が強みとして活かしやすい状態です。"


def pick_markets(job: str, hobbies: str, reasons: List[str]) -> List[str]:
    markets = []

    job_to_market = {
        "医療従事者": ["医療・健康", "クリニック", "採用広報"],
        "介護福祉職": ["介護", "福祉", "採用広報"],
        "教育": ["教育", "研修", "学習支援"],
        "保育": ["子育て", "保育", "家庭向けサービス"],
        "美容": ["美容", "サロン", "EC・レビュー"],
        "サロン": ["美容", "店舗集客", "リピート導線"],
        "ジム・フィットネス関連": ["フィットネス", "健康習慣", "入会導線"],
        "接客販売": ["店舗集客", "口コミ改善", "比較・導線"],
        "営業職": ["BtoBサービス", "比較表", "提案資料"],
        "事務職": ["バックオフィス", "業務改善", "マニュアル整備"],
        "工場勤務": ["製造業", "採用広報", "安全教育"],
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

    if "自分のブログやSNSも資産化したい" in reasons:
        markets.append("自分資産につながる発信テーマ")
    if "企業案件で型を学びながら自分の資産にもつなげたい" in reasons:
        markets.append("企業案件→自分資産へ移植しやすい分野")

    return unique_keep_order(markets)[:5]


def build_roadmap(work_hours: float, blog_have: str, side_history: str, exp_score_value: int) -> List[Tuple[str, str]]:
    phase1 = (
        "0〜30日",
        "まずは『何を売るか』ではなく、『何を整理できる人か』を固めます。AIで下書きを作り、Canvaや文章で見やすく整える型を1つ身につけ、最初の納品サンプルを1〜2個作る段階です。",
    )

    if side_history in ["まだ取り組んでいない", "1ヶ月未満"]:
        phase2_text = "小さな案件や模擬案件で、FAQ整理・比較表・記事構成・1枚図解のどれか1つに絞って納品経験を作ります。ここでは完璧さより、型に沿って最後まで出すことを優先します。"
    else:
        phase2_text = "すでにある経験を活かして、単発作業ではなく『継続しやすい整理・改善業務』へ寄せます。既存の発信や実績を、企業案件用の見せ方に直していく段階です。"

    if work_hours <= 1.0:
        phase3_text = "時間が限られる前提なので、毎日少しずつ進められる業務に寄せるのが重要です。6ヶ月でまずは月3万円前後の土台を安定させ、その後に単価より継続性を優先して積み上げます。"
    elif work_hours <= 2.0:
        phase3_text = "平日夜の積み上げで、3ヶ月時点で月3〜5万円の現実ラインを狙い、6ヶ月で継続案件を持つ形に寄せるのが現実的です。ここで『書くだけ』ではなく、整理・構成・図解まで触れると伸びやすいです。"
    else:
        phase3_text = "稼働時間を取りやすいので、記事・図解・導線改善のように複数の納品パターンを持ちやすい状態です。6ヶ月時点で継続案件を複数持ち、企業案件で学んだ型を自分資産へ移す動きを並行できます。"

    phase2 = ("31〜60日", phase2_text)
    phase3 = ("61〜90日", phase3_text)

    if blog_have == "持っている":
        phase4 = ("90日以降の伸ばし方", "企業案件で使った構成や導線の型を、自分のブログやSNSにも移植します。自分の発信を後回しにせず、型を学びながら並行で育てる設計が取りやすいです。")
    else:
        phase4 = ("90日以降の伸ばし方", "最初は企業案件で型を学び、その後で自分のブログやSNSを立ち上げる流れが現実的です。ゼロから自分発信だけで悩むより遠回りしにくいです。")

    return [phase1, phase2, phase3, phase4]


def build_lifestyle_image(work_hours: float, holiday_text: str, marital: str, child_status: str, child_count: str) -> str:
    if work_hours <= 1.0:
        base = "平日は30分〜1時間で下書きや整理を進め、休日にまとめて仕上げる形が現実的です。"
    elif work_hours <= 2.0:
        base = "平日は夜1〜2時間で進め、休日に構成や図解をまとめる流れが現実的です。"
    else:
        base = "平日にもまとまった時間を使えるので、納品・改善・自分の発信まで並行しやすい状態です。"

    family = ""
    if marital == "既婚" and child_status == "いる":
        family = f"家庭との両立前提で進める必要があるので、子ども{child_count}人の生活リズムを崩さない範囲で『毎日少しずつ進む仕事』を優先した方が続きやすいです。"
    elif marital == "既婚":
        family = "家庭との両立前提で、急に大きく変えるより生活に乗る形にした方が続きやすいです。"

    holiday = f"休日の過ごし方が『{holiday_text}』なら、それを崩しすぎない働き方に寄せる方が現実的です。" if holiday_text.strip() else "休日を全部作業に充てる前提ではなく、無理なく続く配分で考える方が現実的です。"

    return f"{base}{family}{holiday}"


def build_inaction_risk(current_job: str, work_hours: float, goals: List[str], reasons: List[str]) -> str:
    risk_lines = [
        f"今の『{current_job}』の延長だけで数年が過ぎると、経験は増えても、それが副収入や資産に変わらないまま終わりやすいです。",
        "特に、日々の忙しさに流されると『判断はしているのに積み上がっていない』状態が続きやすくなります。",
    ]

    if work_hours <= 1.0:
        risk_lines.append("時間が限られる人ほど、自己流で遠回りすると、1年後も『やろうと思っていたのに進んでいない』に戻りやすいです。")
    else:
        risk_lines.append("時間が取れるのに型なしで進めると、頑張っているのに単発作業ばかり増えて、継続収益に繋がりにくくなります。")

    if "将来の収入不安に備えたい" in reasons or "会社以外の収入源を持ちたい" in goals:
        risk_lines.append("収入源を増やす準備を後回しにすると、不安が消えるどころか、仕事や家庭の変化が来た時に選択肢が少ないままになります。")

    return "".join(risk_lines)


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


st.title("個別専用キャリア設計図ロードマップ作成")
st.markdown(
    "<p class='lead'>Zoomで画面共有しながら、その場のヒアリング内容をもとに『何をやると、どう価値になり、どの順番で進めるか』を整理するためのシミュレーターです。見た目よりも、会話が前に進むことと、自分の場合が具体化されることを優先しています。</p>",
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

score = experience_score(experiences, side_history, current_revenue, best_revenue)
months, forecast, ceiling, can_hit = build_simulation(target_income, work_hours, score)
long_years, annual_projection, cumulative_projection = build_long_term_projection(ceiling, score, work_hours)

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=months,
        y=forecast,
        name="6ヶ月までの見込み収益",
        marker_color="#17324D",
        hovertemplate="%{x}<br>見込み収益: <b>%{y:,.0f}円</b><extra></extra>",
    )
)
fig.add_trace(
    go.Scatter(
        x=months,
        y=[target_income] * len(months),
        mode="lines",
        name="目標金額",
        line=dict(color="#C77D1A", width=3, dash="dash"),
        hovertemplate="目標: <b>%{y:,.0f}円</b><extra></extra>",
    )
)
fig.update_layout(
    height=420,
    margin=dict(l=20, r=20, t=30, b=20),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    hovermode="x unified",
)
fig.update_yaxes(title_text="月間収益額（円）", tickformat=",d", gridcolor="rgba(0,0,0,0.08)")
fig.update_xaxes(showgrid=False)
st.plotly_chart(fig, use_container_width=True)

uplift_rate = round((ceiling / target_income - 1) * 100)
if can_hit:
    sim_comment = f"今の条件だと、6ヶ月時点で<span class='em'>{ceiling:,}円前後</span>が見込みラインです。目標の{target_label}を<span class='em'>約{uplift_rate}%上回る</span>水準で着地する設計にしています。"
else:
    sim_comment = f"今の条件だと、6ヶ月時点の見込みラインは<span class='em'>{ceiling:,}円前後</span>です。今回は目標の{target_label}を基準に、少し上振れしたラインまで見える形で設計しています。"

st.markdown(
    f"""
    <div class="card">
        <div class="lead">{sim_comment}<br><br>
        いきなり大きく狙うより、<span class="em">3ヶ月で土台を作り、6ヶ月で目標を少し上回るライン</span>を見ながら進める方が、面談でも未来を具体的に描きやすいです。</div>
    </div>
    """,
    unsafe_allow_html=True,
)

if st.button("個別専用キャリア設計図を作成する"):
    st.session_state.generated = True

if st.session_state.generated:
    display_name = name.strip() if name.strip() else "この方"
    strength_summary = build_strength_summary(current_job, experiences, career_text)
    entry_tasks = pick_entry_tasks(current_job, experiences)
    markets = pick_markets(current_job, hobbies, goals + reasons)
    roadmap = build_roadmap(work_hours, blog_have, side_history, score)
    lifestyle = build_lifestyle_image(work_hours, holiday_style, marital, child_status, child_count)
    inaction_risk = build_inaction_risk(current_job, work_hours, goals, reasons)

    st.divider()
    st.markdown("<div class='section-title'>作成結果</div>", unsafe_allow_html=True)

    summary_text = (
        f"{display_name}さんは、現在『{current_job}』の文脈が軸です。"
        f"経験としては『{'、'.join(experiences[:6]) if experiences else '未整理の経験も含めて棚卸し余地あり'}』があり、"
        f"現状の作業時間は1日あたり{work_hours}時間。"
        f"目標は{target_label}で、今の条件だと6ヶ月時点の見込みラインは{ceiling:,}円前後です。"
    )
    render_result_card("今の土台から見えること", summary_text + "<br><br>" + strength_summary)

    task_lines = []
    for title, desc in entry_tasks:
        task_lines.append(f"<div class='mini-card'><b>{title}</b><br><span class='lead'>{desc}</span></div>")
    render_result_card("あなたの経験が高単価な価値に変わる具体的な業務", "".join(task_lines))

    market_text = "、".join(markets) if markets else "業務整理・情報整理・説明コンテンツ"
    render_result_card(
        "最初に狙いやすい市場・テーマ",
        f"最初から何でも狙うより、<span class='em'>{market_text}</span>のように、今の経験や興味とつながる分野から入る方が遠回りしにくいです。企業案件で型を学び、その型をあとから自分のブログやSNSへ移す流れが作りやすいです。",
    )

    render_timeline_card("90日ロードマップ", roadmap)

    render_result_card("日々のライフスタイルイメージ", lifestyle)

    income_text = (
        f"今の条件なら、3ヶ月時点で{forecast[2]:,}円前後、6ヶ月で{forecast[-1]:,}円前後を目安に設計できます。"
        f" 今回は目標の{target_label}をそのままなぞるのではなく、6ヶ月時点で約{uplift_rate}%上回るラインまで見えるようにしてあります。"
        f" ここで大事なのは、時間を増やすことだけではなく、整理・構成・図解のような『単価が落ちにくい仕事』へ寄せることです。"
    )
    render_result_card("収益ラインの見通し", income_text)

    render_result_card(
        "このまま取り組まなかった場合に起こりやすいこと",
        inaction_risk,
    )

    future_text = (
        f"だからこそ、{display_name}さんは『思いつきで頑張る』のではなく、"
        f"今ある経験を企業ニーズに変換しながら、型を学んで積み上げる進み方が合っています。"
        f" この流れで進むと、<span class='em'>1年目は{annual_projection[0]:,}円前後、2年目は{annual_projection[1]:,}円前後</span>を目安に伸ばしやすく、"
        f" 5年累計では<span class='em'>{cumulative_projection[-1]:,}円前後</span>の積み上がりが見えてきます。"
    )
    render_result_card("だから、このような取り組み方で前へ進みましょう", future_text)

    long_fig = go.Figure()
    long_fig.add_trace(
        go.Bar(
            x=long_years,
            y=annual_projection,
            name="年間収益",
            marker_color="#17324D",
            hovertemplate="%{x}<br>年間収益: <b>%{y:,.0f}円</b><extra></extra>",
        )
    )
    long_fig.add_trace(
        go.Scatter(
            x=long_years,
            y=cumulative_projection,
            mode="lines+markers",
            name="累計収益",
            line=dict(color="#C77D1A", width=3),
            hovertemplate="%{x}<br>累計収益: <b>%{y:,.0f}円</b><extra></extra>",
        )
    )
    long_fig.update_layout(
        height=430,
        margin=dict(l=20, r=20, t=30, b=20),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
        hovermode="x unified",
    )
    long_fig.update_yaxes(title_text="収益額（円）", tickformat=",d", gridcolor="rgba(0,0,0,0.08)")
    long_fig.update_xaxes(showgrid=False)
    st.plotly_chart(long_fig, use_container_width=True)
