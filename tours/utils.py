# tours/utils.py
from typing import Dict

LANG_MAP = {
    "zh-Hant": "zh_Hant",
    "zh-hant": "zh_Hant",
    "zh-TW": "zh_Hant",
    "zh-tw": "zh_Hant",
    "zh-Hans": "zh_Hans",
    "zh-hans": "zh_Hans",
    "zh-CN": "zh_Hans",
    "zh-cn": "zh_Hans",
    "en": "en",
    "en-us": "en",
}

def pick_lang(block: Dict, lang: str, default_key: str = "zh_Hant") -> str:
    """
    從 JSON 多語 block 取對應語言值，若無則回退 zh_Hant，再回退 en。
    block: {"zh_Hant": "...", "zh_Hans": "...", "en": "..."}
    """
    if not isinstance(block, dict):
        return ""
    key = LANG_MAP.get((lang or "").lower(), default_key)
    v = (block.get(key) or "").strip()
    if v:
        return v
    # fallback
    for k in (default_key, "en"):
        v = (block.get(k) or "").strip()
        if v:
            return v
    return ""
