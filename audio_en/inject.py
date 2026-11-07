from pathlib import Path

# 1. Inject English voice bank into tieng-anh-cho-be.html
bank_json = Path(r"d:\Game\audio_en\en_voice_bank.json").read_text(encoding="utf-8")
en_html_path = Path(r"d:\Game\tieng-anh-cho-be.html")
en_html = en_html_path.read_text(encoding="utf-8")
if "__EN_VOICE_BANK_PLACEHOLDER__" in en_html:
    en_html = en_html.replace("__EN_VOICE_BANK_PLACEHOLDER__", bank_json)
    en_html_path.write_text(en_html, encoding="utf-8")
    print("Injected voice bank into tieng-anh-cho-be.html, size:", len(en_html))
else:
    print("tieng-anh-cho-be.html already has voice bank, size:", len(en_html))

# 2. Add link to English Garden in toan-cho-be.html and copy to index.html
math_path = Path(r"d:\Game\toan-cho-be.html")
math_html = math_path.read_text(encoding="utf-8")
link_html = '<a href="tieng-anh-cho-be.html" class="voice-btn" style="text-decoration:none; background:#f3e8ff; border-color:#7c3aed; color:#5b21b6;" title="Chuyển sang Khu Vườn Tiếng Anh">🦜 Vườn Tiếng Anh</a>\n        '
target_str = '<select class="range-select" id="select-range"'
if "tieng-anh-cho-be.html" not in math_html and target_str in math_html:
    math_html = math_html.replace(target_str, link_html + target_str, 1)
    math_path.write_text(math_html, encoding="utf-8")
    print("Added English Garden link to toan-cho-be.html")

Path(r"d:\Game\index.html").write_text(math_html, encoding="utf-8")
print("Synced index.html")
