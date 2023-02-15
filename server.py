#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import socket
from socket import AF_INET, SOCK_STREAM

from config import SERVER_IP, SERVER_PORT, SERVER_ADDRESS, SERVER_START


# typing для аннотации типов socket
ServerSocket = socket
ClientSocket = socket


def create_server() -> None:
    # Программный интерфейс для обеспечения инфо обмена между процессами
    server = socket() # socket(AF_INET, SOCK_STREAM)
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
    _read_data(_client)
    # Отправка данных клиенту
    _send_data(_client)


def _read_data(_client: ClientSocket) -> None:
    # Чтение запрошенных данных от клиента
    request = _client.recv(1024).decode().split('\n')
    # Метод, адрес, протокол, хост
    method, usl, protocol = request[0].split()
    host = request[1].split()[1]
    
    print('Метод: %s\nАдрес: %s\nПротокол: %s\nХост: %s\n' % (method, usl, protocol, host))


def _send_data(_client: ClientSocket) -> None:
    # Ответ от сервера
    response = _response_server()
    # Формируем отправку данных клиенту
    _client.send(response.encode())


def _response_server() -> str:
    # Формируем ответ от сервера
    response = '<h1>TEST DATA</h1>'
    # Возвращаем результат :param str: html
    return response


def _close_server(_client: ClientSocket) -> None:
    # Формируем закрытие соединения с сервером
    _client.close()
    print('Подключение завершено.\n')


# Основная функция для вызова набора команд
def main() -> None:
    # Создание сервера
    create_server()


if __name__ == '__main__':
    main()
