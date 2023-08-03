# QRKot
## Автор
- [Дятликович Денис](https://github.com/DenisVladimir)
## Технологии
- Python 3.10.6
- FastAPI 0.78
- FastAPI-Users 10.0.4
- SQLAlchemy 1.4.36
- aioSQLite 0.17.0
- Pydantic 1.9.1
- Alembic 1.7.7

## Команды развёртывания и запуска проекта
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/DenisVladimir/cat_charity_fund.git
cd cat_charity_fund
```
Cоздать и активировать виртуальное окружение:
Для Linux/macOS
```
python3 -m venv venv
```
Для Windows
```
source venv/bin/activate
```
Активация виртуального окружения:
```
source venv/scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Создать в корневой директории файл .env и заполнить его:
```
nano .env
APP_TITLE=Кошачий благотворительный фонд
APP_DESCRIPTION=Сервис для поддержки котиков!
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=<YOUR_SECRET_WORD>
```
Выполнить миграции:
```
alembic upgrade head
```
Запустить приложение:
```
uvicorn app.main:app
```
## Полная документация API со всеми возможными запросами доступна на развёрнутом проекте по адресам
- [Документация в формате docs](http://127.0.0.1:8001/docs)
- [Документация в формате redoc](http://127.0.0.1:8001/redoc)
