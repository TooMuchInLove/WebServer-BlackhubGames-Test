# -*- coding: utf-8 -*-

# Аннотации типов
from typing import List
# Составления HTTP-запросов
import requests
# Разбор URL-адресов на компоненты
from urllib.parse import urljoin
# Позволяет работать с HTML/XML-кодом
from bs4 import BeautifulSoup


# url-адрес
URLString = str
# Список url-адресов
URLListing = List[str]
# Документ html
HTMLObject = BeautifulSoup
HTMLString = str


# Считываем удалённый файл html
def read_html_remote(_url: str) -> HTMLObject:
    headers = {
        'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/108.0.0.0 YaBrowser/23.1.2.987 Yowser/2.5 Safari/537.36'
    }
    # Чтении удалённой html-страницы
    response = requests.get(_url, headers=headers)
    # Добавляем html-страницу
    html = BeautifulSoup(response.text, 'html.parser')
    # Возвращаем результат :param str|object: url|html
    return html


# Считываем локальный файл html
def read_html_local(_html_file) -> HTMLObject:
    # Считываем файл html
    HTMLFile = open(_html_file, 'r', encoding='utf-8')
    HTMLFileText = HTMLFile.read()
    # Добавляем html-страницу
    html = BeautifulSoup(HTMLFileText, 'html.parser')
    # Возвращаем результат :param str|object: url|html
    return html


# Возвращаем все URL-адреса
def get_links_html(_url: URLString, _html: HTMLObject) -> URLListing:
    # Множество url адресов (уникальные)
    urls = set()
    # Поиск всех тегов-ссылок
    for link in _html.findAll('a'):
        href = link.attrs.get('href')
        if href == '' or href is None: # Если тег href пустой
            continue
        # Присоединить url, если он относительный (не абсолютная ссылка)
        href = urljoin(_url, href)
        # Всё что похоже на https://blackrussia.online
        if href.startswith(_url) and \
                not (href.endswith('.jpg') or href.endswith('.jpeg')):
            urls.add(href)
    # Преобразование множества в список url-адресов
    urls = list(urls)
    # Возвращаем результат :param List[str]: список url-адресов
    return urls
