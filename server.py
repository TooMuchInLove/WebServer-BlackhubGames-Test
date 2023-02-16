#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import socket, gethostbyname
from socket import AF_INET, SOCK_STREAM
from typing import List

from config import SERVER_ADDRESS, SERVER_START
from config import HOSTNAME, PROTOCOL
from parser import get_links_html


# socket (сервер/клиент)
ServerSocket = socket
ClientSocket = socket
# Список полученных данных
DataList = List[str]


def create_server() -> None:
    # Программный интерфейс для обеспечения инфо обмена между процессами
    server = socket(AF_INET, SOCK_STREAM)
    # Подключение к веб-серверу через порт
    server.bind(SERVER_ADDRESS)
    # Одновременное прослушивание сервером кол-ва человек
    server.listen(1)
    # Запуск сервера
    _start_server(server)


def _start_server(_server: ServerSocket) -> None:
    # Запуск сервера
    while SERVER_START:
        # Принимаем подключение от сервера (клиентский сокет и адрес)
        client, address = _server.accept()
        # Манипуляция с данными клиента/сервера
        _manipulation_data(client)
        # Закрытие соединения с сервером
        _close_server(client)


def _manipulation_data(_client: ClientSocket) -> None:
    # Чтение запрошенных данных
    request = _read_data(_client)
    # Ответ от сервера
    response = _response_server(request)
    # Отправка данных клиенту
    _send_data(_client, response)


def _read_data(_client: ClientSocket) -> DataList:
    # Чтение запрошенных данных от клиента
    request = _client.recv(1024).decode().split('\n')
    print(request, '\n')
    # Возвращаем результат :param List[str]: список строк
    return request


def _response_server(_request: DataList) -> str:
    # Список url-адресов
    urls = get_links_html(PROTOCOL+HOSTNAME)
    print(urls)
    # Формируем ответ от сервера
    response = '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
    <meta charset="UTF-8">
    <title>Home</title>
    <style type="text/css">
    body {padding: 10px 50px;}
    h1 {font-size: 30px; padding: 10px 20px;}
    h3 {font-size: 20px; font-family: monospace;}
    i {color: #ff0000;}
    </style>
    '''
    response += '</head>'
    response += '<body>'
    response += '<header>'
    response += '<h1>Тестовое задание: Middle Python Developer в BlackHub Games</h1>'
    response += '</header>'
    response += '<main>'
    if _request != ['']:
        # Метод, путь, протокол, localhost
        method, path, protocol = _request[0].split()
        _, localhost = _request[1].split()
        # Списко компонентов
        response += '<h3><i>Protocol:</i> '+protocol+'</h3>'
        response += '<h3><i>Method:</i> '+method+'</h3>'
        response += '<h3><i>Localhost:</i> '+localhost+'</h3>'
        response += '<h3><i>Hostname:</i> '+HOSTNAME+'</h3>'
        response += '<h3><i>Path:</i> '

        link = PROTOCOL+HOSTNAME+path
        if link in urls:
            response += '<a href="'+link+'">'+path+'</a>'
        else:
            response += '404 Page Not Found: ' + link

        response += '</h3>'
        response += '<h3><i>Host:</i> '+gethostbyname(HOSTNAME)+'</h3>'
    response += '</main>'
    response += '</body></html>'
    # Возвращаем результат :param str: html
    return response


def _send_data(_client: ClientSocket, _response: str) -> None:
    # Формируем отправку данных клиенту
    _client.send(_response.encode())


def _close_server(_client: ClientSocket) -> None:
    # Формируем закрытие соединения с сервером
    _client.close()


# Основная функция для вызова набора команд
def main() -> None:
    # Создание сервера
    create_server()


if __name__ == '__main__':
    main()
