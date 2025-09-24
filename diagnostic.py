import os
import sys
import importlib
from pathlib import Path

print("=== Diagnostic 開始 ===")

# 專案根目錄
BASE_DIR = Path(__file__).resolve().parent
print(f"專案根目錄 BASE_DIR = {BASE_DIR}")

# sys.path
print("\n=== sys.path ===")
for p in sys.path:
    print(" -", p)

# DJANGO_SETTINGS_MODULE
print("\n=== DJANGO_SETTINGS_MODULE ===")
print("DJANGO_SETTINGS_MODULE =", os.environ.get("DJANGO_SETTINGS_MODULE"))

# 測試 import eastusatours
print("\n=== 測試 import eastusatours ===")
try:
    import eastusatours
    print("✅ 成功 import eastusatours:", eastusatours.__file__)
except Exception as e:
    print("❌ 失敗:", e)

# 測試 import eastusatours.settings
print("\n=== 測試 import eastusatours.settings ===")
try:
    settings_module = importlib.import_module("eastusatours.settings")
    print("✅ 成功 import eastusatours.settings:", settings_module.__file__)
except Exception as e:
    print("❌ 失敗:", e)

print("\n=== Diagnostic 結束 ===")
