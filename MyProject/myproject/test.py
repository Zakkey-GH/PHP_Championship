import sys

if len(sys.argv) < 2:
    print("画像パスが指定されていません")
    sys.exit(1)

image_path = sys.argv[1] 
print(image_path.strip()) #Python出力値はデフォルトで改行コード（\n）が付与。PHPでの出力結果に影響を及ぼす場合があるので削除。
print('Hello, world!'.strip())
print(str(1 + 5).strip())


