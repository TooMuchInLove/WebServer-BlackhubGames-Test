#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Аннотации типов
from typing import List
# Программный интерфейс для обеспечения обмена данными между процессами
from socket import socket, gethostbyname
from socket import AF_INET, SOCK_STREAM
# Конфигурация + локальные модули
from config import SERVER_ADDRESS, SERVER_START
from config import HOSTNAME, PROTOCOL
from parser import read_html_remote, read_html_local, get_links_html
# html-шаблон
from template import HTML


# socket (сервер/клиент)
SERVERObject = socket
CLIENTObject = socket
# Список полученных данных
DATAList = List[str]


def create_server() -> None:
    # Программный интерфейс для обеспечения инфо обмена между процессами
    server = socket(AF_INET, SOCK_STREAM)
    # Подключение к веб-серверу через порт
    server.bind(SERVER_ADDRESS)
    # Одновременное прослушивание сервером кол-ва человек
    server.listen(1)
    # Запуск сервера
    _start_server(server)


def _start_server(_server: SERVERObject) -> None:
    # Запуск сервера
    while SERVER_START:
        # Принимаем подключение от сервера (клиентский сокет и адрес)
        client, address = _server.accept()
        # Манипуляция с данными клиента/сервера
        _manipulation_data(client)
        # Закрытие соединения с сервером
        _close_server(client)


def _manipulation_data(_client: CLIENTObject) -> None:
    # Чтение запрошенных данных
    request = _read_data(_client)
    # Ответ от сервера
    response = _response_server(request)
    # Отправка данных клиенту
    _send_data(_client, response)


def _read_data(_client: CLIENTObject) -> DATAList:
    # Чтение запрошенных данных от клиента
    request = _client.recv(1024).decode().split('\n')
    print(request, '\n')
    # Возвращаем результат :param List[str]: список строк
    return request


def _response_server(_request: DATAList) -> str:
    # Список url-адресов
    #urls = get_links_html(PROTOCOL+HOSTNAME)
    urls = ''
    # Формируем ответ от сервера
    response = ''
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
    # ...
    # index = HTML.find('</main>')
    # HTML = HTML[:index] + response + HTML[index:]
    # print(HTML)
    # Возвращаем результат :param str: html
    return response


def _send_data(_client: CLIENTObject, _response: str) -> None:
    # Формируем отправку данных клиенту
    _client.send(_response.encode())


def _close_server(_client: CLIENTObject) -> None:
    # Формируем закрытие соединения с сервером
    _client.close()


# Основная функция для вызова набора команд
def main() -> None:
    # Создание сервера
    create_server()


if __name__ == '__main__':
    main()
