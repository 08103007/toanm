import json, base64, urllib.parse, requests
from pathlib import Path

vi_bank = json.loads(Path(r"d:\Game\audio_vi\voice_bank.json").read_text(encoding="utf-8"))
en_bank = json.loads(Path(r"d:\Game\audio_en\en_voice_bank.json").read_text(encoding="utf-8"))

extra_clips = {
    "bi_count": ("vi", "Đếm bằng Tiếng Anh cùng Gấu Bơ và Vẹt Poly nhé!"),
    "bi_add": ("vi", "Gộp thêm và đếm bằng Tiếng Anh xem có tất cả bao nhiêu nhé!"),
    "bi_sub": ("vi", "Bớt đi rồi đếm bằng Tiếng Anh xem còn lại bao nhiêu nhé!"),
    "bi_more": ("vi", "Bên nào có nhiều hơn? Chạm vào để nghe Tiếng Anh nhé!"),
    "bi_less": ("vi", "Bên nào có ít hơn? Chạm vào để nghe Tiếng Anh nhé!"),
    "bi_garden": ("vi", "Chào mừng bé đến Khu Vườn Thú Cưng! Hãy chạm vào từng bạn thú để nghe Tiếng Anh và đếm số lượng nhé!"),
}

headers = {"User-Agent": "Mozilla/5.0"}
out_dir = Path(r"d:\Game\audio_en")

for key, (lang, text) in extra_clips.items():
    mp3_path = out_dir / f"{key}.mp3"
    if not mp3_path.exists():
        url = f"https://translate.googleapis.com/translate_tts?ie=UTF-8&q={urllib.parse.quote(text)}&tl={lang}&client=tw-ob"
        r = requests.get(url, headers=headers, timeout=15)
        if r.status_code == 200 and len(r.content) > 500:
            mp3_path.write_bytes(r.content)
    if mp3_path.exists():
        en_bank[key] = "data:audio/mp3;base64," + base64.b64encode(mp3_path.read_bytes()).decode("ascii")

unified = {**vi_bank, **en_bank}
out_json = out_dir / "unified_voice_bank.json"
out_json.write_text(json.dumps(unified, ensure_ascii=False), encoding="utf-8")
print("Total unified clips:", len(unified), "JSON size:", out_json.stat().st_size)
