<?php
$email = $_POST["email"];
$password = $_POST["password"];

// Запишите данные в текстовый файл
$file = fopen("login_data.txt", "a");
if ($file) {
    $data = "Email: $email, Password: $password\n";
    fwrite($file, $data);
    fclose($file);
}

// Выведите данные в консоль (лог)
error_log("Email: $email, Password: $password");

echo "Данные успешно записаны и выведены в консоль.";
?>
