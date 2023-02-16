#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.parse import urljoin
from bs4 import BeautifulSoup # позволяет работать с HTML/XML-кодом.
from typing import List


# url-адрес
URLAddress = str
# List (список url-адресов)
ListingUrls = List[str]
# Документ html
HTMLObject = BeautifulSoup
HTMLString = str


# Считываем удалённый файл html
def read_html_remote(_html_file) -> HTMLString:
    pass


# Считываем локальный файл html
def read_html_local(_html_file) -> HTMLObject:
    # Считываем файл html
    HTMLFile = open(_html_file, 'r', encoding='utf-8')
    HTMLFileText = HTMLFile.read()
    # Добавляем html-страницы
    html = BeautifulSoup(HTMLFileText, 'html.parser')
    # Возвращаем результат :param object: html
    return html


# Возвращаем все URL-адреса
def get_links_html(_url: URLAddress, _html: HTMLObject) -> ListingUrls:
    # Множество url адресов (уникальные)
    urls = set()
    # Считываем файл html
    HTMLFile = open('BLACKRUSSIA.html', 'r', encoding='utf-8')
    HTMLFileText = HTMLFile.read()
    # Добавляем html вэб-страницы
    soup = BeautifulSoup(HTMLFileText, 'html.parser')
    print(type(soup))
    # Поиск всех тегов-ссылок
    for link in soup.findAll('a'):
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

urls = get_links_html('https://blackrussia.online')

print(urls)
