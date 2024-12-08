import sys
import numpy as np

try:
    if len(sys.argv) < 2:
        print("画像パスが指定されていません")
        sys.exit(1)

    image_path = sys.argv[1] 
    print(image_path.strip())
    print('Hello, world!'.strip())
    print(str(1 + 5).strip())

except Exception as e:
    print(f"エラーが発生しました: {str(e)}")
    sys.exit(1)