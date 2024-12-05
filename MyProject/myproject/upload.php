<?php
// PHPファイルの冒頭で画像データを受け取り、Pythonスクリプトを呼び出します
echo "3";


// POSTリクエストからBase64形式の画像データを取得
if (isset($_POST['image'])) {
    $imageData = $_POST['image'];

    // Base64ヘッダーを削除し、デコード
    $imageData = str_replace('data:image/png;base64,', '', $imageData);
    $imageData = base64_decode($imageData);
    

    // サーバーに一時的に画像を保存
    $filePath = 'uploads/captured_image.png';
    if (!file_exists('uploads')) {
        mkdir('uploads', 0777, true); // 保存ディレクトリがない場合は作成
    }
    file_put_contents($filePath, $imageData);

    // Pythonスクリプトを実行し、画像認識を行う
    $command = escapeshellcmd("python3 process_image.py $filePath");
    $output = shell_exec($command);

    // 結果をクライアントに返す
    echo json_encode(['status' => 'success', 'output' => $output]);
} else {
    echo json_encode(['status' => 'error', 'message' => 'No image data received.']);
}
