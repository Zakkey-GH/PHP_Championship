<?php

        $command = escapeshellcmd("python3 test.py $image_path");
        $output = shell_exec($command);
    
        // 結果をクライアントに返す
        echo json_encode(['status' => 'success', 'output' => $output]);
    