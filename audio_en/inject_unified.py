from pathlib import Path

bank = Path(r"d:\Game\audio_en\unified_voice_bank.json").read_text(encoding="utf-8")
idx_path = Path(r"d:\Game\index.html")
html = idx_path.read_text(encoding="utf-8")
if "__UNIFIED_VOICE_BANK_PLACEHOLDER__" in html:
    html = html.replace("__UNIFIED_VOICE_BANK_PLACEHOLDER__", bank)
    idx_path.write_text(html, encoding="utf-8")
    print("Injected 107 unified voice clips into index.html, size:", len(html))
else:
    print("Already injected, size:", len(html))
