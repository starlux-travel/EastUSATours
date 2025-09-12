# scripts/update_notes.py
import os
import sys
from datetime import date

NOTES_FILE = "PROJECT_NOTES.md"

def update_notes(message):
    # 如果沒有 PROJECT_NOTES.md，就自動建立一份初始檔案
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w", encoding="utf-8") as f:
            f.write("# EastUSATours — POR V2 專案紀錄\n\n")
            f.write("## 📌 專案概述\n")
            f.write("這是 EastUSATours — POR V2 的開發專案，主要功能包含：\n")
            f.write("- 多語言功能 (i18n)\n")
            f.write("- Tours 模組 (Bus / Cruise / EU)\n")
            f.write("- 首頁 UI 與搜尋功能\n")
            f.write("- API 與資料串接\n\n")
            f.write("---\n\n")
            f.write("## 📅 更新紀錄\n")

    # 讀取 PROJECT_NOTES.md
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        content = f.readlines()

    # 找到「更新紀錄」區塊
    idx = None
    for i, line in enumerate(content):
        if line.strip().startswith("## 📅 更新紀錄"):
            idx = i
            break

    if idx is None:
        raise ValueError("⚠️ 找不到 '## 📅 更新紀錄' 區塊")

    # 插入新紀錄
    today = date.today().isoformat()
    content.insert(idx + 1, f"- {today}：{message}\n")

    # 覆寫檔案
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        f.writelines(content)

    print(f"✅ 已新增紀錄：{today} - {message}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ 請輸入更新訊息，例如：python scripts/update_notes.py '完成首頁 UI'")
    else:
        message = " ".join(sys.argv[1:])
        update_notes(message)
