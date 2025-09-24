import sys
from pathlib import Path

print("=== sys.path ===")
for p in sys.path:
    print(p)

print("\n=== BASE_DIR (當前資料夾) ===")
print(Path(__file__).resolve().parent)

print("\n=== 嘗試匯入 eastusatours ===")
try:
    import eastusatours
    print("✅ 成功匯入 eastusatours (package found)")
except ModuleNotFoundError as e:
    print("❌ 匯入失敗:", e)
