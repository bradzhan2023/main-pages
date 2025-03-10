print("Hello, World!")

html_content = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML 首頁測試</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #fdffe6; /* 新增底色設定 */
            text-align: center;
            margin: 50px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>歡迎來到我的網站!</h1>
    <p>這是一個基本的 HTML 頁面測試。</p>
    <p>2025.03.02 15:28。</p>
    <button onclick="alert('你好！')">點擊我</button>
</body>
</html>
"""

# 寫入檔案
with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("index.html 已成功建立！")
