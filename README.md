## Описание:
Проект YaMDb собирает отзывы пользователей на на различные музыкальные произведения, книги, фильмы
## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```sh
git clone https://github.com/seerez/api_yamdb.git
```
```sh
cd api_yamdb
```
Cоздать и активировать виртуальное окружение:
```sh
python -m venv venv
```
```sh
source venv/bin/activate
```
```sh
python -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```sh
pip install -r requirements.txt
```
Выполнить миграции:
```sh
python manage.py migrate
```
Запустить проект:
```sh
python manage.py runserver
```
#### Пример использования API
##### Регистрация нового пользователя
Получить код подтверждения на переданный email.
Права доступа: Доступно без токена.
```web
api/v1/auth/signup/
```
```json
{
  "email": "string",
  "username": "string"
}
```
##### Получение JWT-токена
Получение JWT-токена в обмен на username и confirmation code.
Права доступа: Доступно без токена.
```web
api/v1/auth/token/
```
```json
{
  "username": "string",
  "confirmation_code": "string"
}
```
##### Получение списка всех жанров
Получить список всех жанров.
Права доступа: Доступно без токена
```web
api/v1/genres/
```
##### Полная документация доступна:
```web
/redoc/
```