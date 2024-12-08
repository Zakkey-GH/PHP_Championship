<?php
$image_path = "/test";

// poetryの仮想環境のPythonを使用
$python_path = '/Applications/XAMPP/xamppfiles/htdocs/php_Championship/MyProject/.venv/bin/python';
$script_path = __DIR__ . '/test.py';

$command = escapeshellcmd($python_path) . ' ' . escapeshellarg($script_path) . ' ' . escapeshellarg($image_path);

// コマンドの実行前に権限を確認
error_log("Python file permissions: " . substr(sprintf('%o', fileperms($python_path)), -4));
error_log("Script file permissions: " . substr(sprintf('%o', fileperms($script_path)), -4));


$output = shell_exec($command . ' 2>&1'); // エラー出力も取得

// デバッグ用にログを出力
error_log("Command: " . $command);
error_log("Output: " . $output);

echo json_encode(['status' => 'success', 'output' => $output]);
?>