#!/usr/bin/env python3
# -*- coding: utf-8 -*-


CSS = '''
html {
    line-height: 1.15;
    -webkit-text-size-adjust: 100%;
}

body {
    margin: 0;
    padding: 10px 50px;
}

main {
    display: block;
}

h1 {
    font-size: 30px;
    margin: 0.67em 0;
    padding: 10px 20px;
}

h3 {
    font-family: monospace;
    font-size: 20px;
}

a {
    background-color: transparent;
}

i {
    color: #ff0000;
}
'''

HTML = '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Test task</title>
    <link rel="stylesheet" href="static/css/style.css">
    <style type="text/css">
        %s
    </style>
</head>
<body>
    <header>
        <h1>Тестовое задание: Middle Python Developer в BlackHub Games</h1>
    </header>
    <main>
    
    </main>
</body>
</html>
''' % (CSS)
