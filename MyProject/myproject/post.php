<?php
session_start();

//１．関数群の読み込み
include("funcs.php");

//LOGINチェック
//sschk();

//２．データ登録SQL作成
$pdo = db_conn();
echo "2";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $caption = $_POST["caption"];
    $name = $_SESSION["name"];
    $image_path = "uploads/" . basename($_FILES["image"]["name"]); //ファイル名を取得

    if (move_uploaded_file($_FILES["image"]["tmp_name"], $image_path)) { //uploadsに移動したらインサート実行
        echo $image_path;
        $sql = "INSERT INTO posts (image_path ,caption,name) VALUES(:image_path,:caption,:name)";
        $stmt = $pdo->prepare($sql); //接続したDBにSQLをセットする関数
        $stmt->bindValue(':image_path', $image_path, PDO::PARAM_STR);
        $stmt->bindValue(':caption', $caption, PDO::PARAM_STR);
        $stmt->bindValue(':name', $name, PDO::PARAM_STR);
        $status = $stmt->execute();

        //４．データ登録処理後
        if ($status == false) {
            //SQL実行時にエラーがある場合（エラーオブジェクト取得して表示）
            $error = $stmt->errorInfo(); //errorInfoがエラー情報を取得する関数。
            exit("SQLInsertError:" . $error[2]);
        } else {
            //５．main.phpへリダイレクト
            redirect(index.html);
        }
    }
};