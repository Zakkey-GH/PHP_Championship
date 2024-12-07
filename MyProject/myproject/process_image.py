# import sys

# if len(sys.argv) < 2:
#     print("画像パスが指定されていません")
#     sys.exit(1)

# image_path = sys.argv[1] 
# print(image_path.strip()) 

# 
# 
import cv2
import numpy as np
import sys

# if len(sys.argv) < 2:
#     print("画像パスが指定されていません")
#     sys.exit(1)

# image_path = sys.argv[1] 
# print(image_path.strip()) 


# ベクトルデータベース (カラーコードをRGB形式に変換)
database = [
    {"color": np.array([200, 200, 175]), "value": 1},
    {"color": np.array([191, 190, 135]), "value": 2},
    {"color": np.array([198, 194, 116]), "value": 3},
    {"color": np.array([207, 201, 71]), "value": 4},
    {"color": np.array([184, 159, 55]), "value": 5},
    {"color": np.array([173, 133, 61]), "value": 6},
    {"color": np.array([125, 118, 58]), "value": 7},
]

def find_closest_color(color):
    """データベース内で最も近い色を見つける"""
    closest = None
    min_distance = float('inf')
    for entry in database:
        dist = np.linalg.norm(color - entry["color"])  # ユークリッド距離を計算
        if dist < min_distance:
            min_distance = dist
            closest = entry
    return closest, min_distance

# 画像ファイルのアップロード
file_path = "/Applications/XAMPP/xamppfiles/htdocs/php_Championship/MyProject/myproject/uploads/Ben_4.png" #input("画像ファイルのパスを入力してください: ")
#file_path = "/uploads/Ben_3.png"

# image_path = sys.argv[1] 
# print(image_path.strip()) 


image = cv2.imread(file_path)

if image is None:
    print("画像を読み込めませんでした。ファイルパスを確認してください。")
else:
    # フレームの中心部分を対象領域として抽出
    h, w, _ = image.shape
    frame_size = 100
    start_x, start_y = w // 2 - frame_size // 2, h // 2 - frame_size // 2
    end_x, end_y = w // 2 + frame_size // 2, h // 2 + frame_size // 2
    roi = image[start_y:end_y, start_x:end_x]

    # ROIの平均色を計算
    avg_color = cv2.mean(roi)[:3]
    avg_color = np.array(avg_color[::-1])  # OpenCVはBGRなのでRGBに変換

    # データベース内で最も近い色を計算
    closest_entry, distance = find_closest_color(avg_color)

    # 結果を判定
    threshold = 50  # 距離が大きい場合は対象範囲外。※cv2は日本語不可
    if distance > threshold:
        text = "out of range"
    else:
        text = f"Value: {closest_entry['value']} (distance: {distance:.2f})"
    print(text)

#     # # 結果を画像に描画（フレーム削除済み）
#     # cv2.putText(image, text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, lineType=cv2.LINE_AA)

#     # # 結果画像を表示（ウィンドウサイズ調整）
#     # cv2.namedWindow("Color Detection", cv2.WINDOW_NORMAL)  # ウィンドウサイズ変更可能に
#     # cv2.resizeWindow("Color Detection", 800, 600)  # ウィンドウサイズを設定
#     # cv2.imshow("Color Detection", image)
#     # cv2.waitKey(0)
#     # cv2.destroyAllWindows()
