import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# .env ファイルからAPIキーを読み込む
load_dotenv()

# APIキーを設定
GENAI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GENAI_API_KEY:
    raise ValueError("APIキーが設定されていません。.envファイルを確認してください。")

genai.configure(api_key=GENAI_API_KEY)

def check_politeness(text):
    """
    テキストが丁寧語かどうかを判定する関数
    戻り値: (bool, str) -> (判定結果, 理由)
    """
    
    # 無料枠で使える軽量モデルを指定
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    prompt = f"""
    あなたは掲示板の管理人AIです。
    以下の投稿テキストが「丁寧語（です・ます調）」として適切か判定してください。

    # 判定ルール
    1. 文末が「です」「ます」などで終わる丁寧な表現なら true
    2. タメ口、乱暴な言葉、煽り、攻撃的な内容なら false
    3. 出力は必ず以下のJSON形式のみで行ってください。余計な文章は不要です。
    {{
        "isPolite": true または false,
        "reason": "判定の理由（NGの場合はユーザーへの修正アドバイス）"
    }}

    # 投稿テキスト
    "{text}"
    """

    try:
        # AIに問い合わせ
        response = model.generate_content(prompt)
        
        # 結果のテキストを取得
        result_text = response.text
        
        # ググれ
        result_text = result_text.replace("```json", "").replace("```", "").strip()
        
        # ググれ
        data = json.loads(result_text)
        
        return data["isPolite"], data["reason"]

    except Exception as e:
        print(f"AI判定エラー: {e}")
        print("===エラー内容===")
        print(e)
        # エラー時は安全のためFalse（NG）扱いにするか、True（スルー）にするか選べます
        return False, "AIの判定に失敗しました。もう一度試してください。"

# --- 動作テスト用（このファイルを直接実行した時だけ動く） ---
if __name__ == "__main__":
    test_text = "こんにちは"
    is_ok, reason = check_politeness(test_text)
    print(f"テキスト: {test_text}")
    print(f"判定: {'OK' if is_ok else 'NG'}")
    print(f"理由: {reason}")
    
    print("-" * 20)

    test_text_2 = "Hello World"
    is_ok, reason = check_politeness(test_text_2)
    print(f"テキスト: {test_text_2}")
    print(f"判定: {'OK' if is_ok else 'NG'}")
    print(f"理由: {reason}")