from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class MainPageView(TemplateView):
    template_name = 'myapp/index.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['name'] = 'Евдокимов Алексей'
        contex['email'] = 'poligraphich@gmail.ru'
        contex['phone'] = '+9283593110'
        logger.info(f'посещение страницы index в: {datetime.now()}')
        return contex


class AboutView(TemplateView):
    template_name = 'myapp/about.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['name'] = 'Евдокимов Алексей'
        contex['email'] = 'poligraphich@gmail.ru'
        contex['phone'] = '+9283593110'
        logger.info(f'посещение страницы about в: {datetime.now()}')
        return contex


def index(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Мой первый Django-сайт</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 20px;
            }

            h1 {
                color: #333;
            }

            p {
                color: #777;
            }
        </style>
    </head>
    <body>
        <h1>Добро пожаловать на мой первый Django-ПРОЕКТ!</h1>

        <h2>О сайте</h2>
        <p>Этот сайт разработан с использованием Django, мощного фреймворка для создания веб-приложений на языке Python. </p>

        <h2>Обо мне</h2>
        <p>Привет, меня зовут Евдокимов Алексей. 
        <footer>
            <p>Свяжитесь со мной: poligraphich@gmail.ru | +79283593110</p>
        </footer>
    </body>
    </html>
    """
    logger.info(f'посещение страницы index в: {datetime.now()}')
    return HttpResponse(html)


def about(request):
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Обо мне</title>
</head>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 20px;
            }

            h1 {
                color: #333;
            }

            p {
                color: #777;
            }
        </style>
<body>
    <header>
        <h1>Привет! Я Евдокимов Алексей</h1>
    </header>

    <main>
        <section>
            <h2>Опыт работы</h2>
            <ul>
                <li>Место работы 1</li>
               
            </ul>
        </section>

        <section>
            <h2>Образование</h2>
            <ul>
                <li>Университет 1</li>
               
        </section>

        <section>
            <h2>Навыки</h2>
            <ul>
                <li>Навык 1</li>
                
            </ul>
        </section>
    </main>

    <footer>
        <p>Свяжитесь со мной: poligraphich@gmail.ru | +79283593110</p>
    </footer>
</body>
</html>
"""
    logger.info(f'посещение страницы about в: {datetime.now()}')
    return HttpResponse(html)