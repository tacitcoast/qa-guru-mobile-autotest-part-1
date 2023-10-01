# 📁 Урок "Мобильная автоматизация #1. Разрабатываем автотесты с Browserstack"

1. Учимся пользоваться инспектором в Browserstack, разрабатываем первые автотесты на Android / iOS с Selene
2. Browserstack-API. Забираем логи, видео
3. Теория. Основы тестирования мобильных приложений

[Конспект лекции](https://github.com/qa-guru/knowledge-base/wiki/19.-%D0%9C%D0%BE%D0%B1%D0%B8%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F-%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F-%231.-%D0%A0%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%B0%D1%82%D1%8B%D0%B2%D0%B0%D0%B5%D0%BC-%D0%B0%D0%B2%D1%82%D0%BE%D1%82%D0%B5%D1%81%D1%82%D1%8B-%D1%81-Browserstack)

## Задание

1. Зарегистрировать аккаунт в https://browserstack.com
2. Запустить автотест из занятия локально
3. Разработать еще один автотест на открытие любой статьи
4. Разработать еще один автотест на iOS
5. Aдаптировать conftest.py для работы с двумя типами платформ - Android, iOS
6. Вынести данные (логин, пароль, урл браузерстека и т.д.) в .env с pydantic
7. Сделать сборку в дженкинсе

## Решение

- [Проект в этой ветке](https://github.com/tacitcoast/qa-guru-mobile-autotest-part-1)
- [Сборка в Jenkins](https://jenkins.autotests.cloud/job/student-malinovskaia-anna-qa-guru-6-23-mobile/6/allure/)

___
## Дополнительные материалы

- [Страничка «Get Started» на браузерстек (выбирать язык Python)](https://app-automate.browserstack.com/dashboard/v2/quick-start/get-started)
- [Дешбоард на браузерстек](https://app-automate.browserstack.com/dashboard/v2)
- [Инспектор на браузерстек](https://app-live.browserstack.com)
- [Как загрузить свою версию апки в браузерстек](https://github.com/qa-guru/mobile-tests-13-py/tree/demo-selene-appium-with-browserstack-android#how-to-upload-your-own-version-of-application-to-browserstack)
