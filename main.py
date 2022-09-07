from pyrogram import Client, filters
from time import sleep
import os

try:

    ####################### СОЗДАНИЕ ЮЗЕР-БОТА ##################################################################
    app = Client("my_account", api_id=os.getenv('API_ID'), api_hash=os.getenv('API_HASH'))
    users = []


    ###################### ОБРАБОТЧИКИ КОМАНД ####################################################################

    # ВЫВОД ВСЕХ ДОСТУПНЫХ КОМАНД


    @app.on_message(filters.command("help", prefixes=".") & filters.me)
    async def help(_, msg):
        await app.send_message("me", """
        Все доступные команды:
        **.usersInfo** - список добавленных пользователей 
        **.add (@......)** - добавить пользователя в список
        **.del (id в списке)**- удалить пользователя из списка
        **.send (текст)** - отправить сообщение всем пользователям из списка
        **.addtxt** - считывание пользователей из txt файла
        """)


    # ОТПРАВКА СООБЩЕНИЯ ПОЛЬЗОВАТЕЛЯМ ИЗ СПИСКА


    @app.on_message(filters.command("send", prefixes=".") & filters.me)
    async def send(_, msg):
        userMessage = msg.text.split(".send ", maxsplit=1)[1]
        await app.send_message("me", "Начата рассылка сообщений.")
        for x in users:
            try:
                await app.send_message(x, userMessage)
                sleep(15)

            except:
                await app.send_message("me", f'Ошибка при отправке сообщения пользователю {x}')
        await app.send_message("me", "Рассылка завершена.")


    # ДОБАВЛЕНИЯ ПОЛЬЗОВАТЕЛЯ В СПИСОК


    @app.on_message(filters.command("add", prefixes=".") & filters.me)
    async def addUser(_, msg):
        newUser = msg.text.split(".add ", maxsplit=1)[1]
        for newUser in newUser.split(", "):
            users.append(newUser)
        await app.send_message(chat_id=msg.from_user.id, text="Пользователь добавлен в список!")

    # СЧИТЫВАНИЕ ПОЛЬЗОВАТЕЛЕЙ ИЗ TXT ДОКУМЕНТА

    @app.on_message(filters.command("addtxt", prefixes=".") & filters.me)
    async def addUserTxt(_, msg):
        with open("peoples.txt", "r") as file:
            for people in file:
                users.append(people)
            await app.send_message("me", "Пользователи добавлены в список.")


    # СПИСОК ПОЛЬЗОВАТЕЛЕЙ


    @app.on_message(filters.command("usersInfo", prefixes=".") & filters.me)
    async def usersInfo(_, msg):
        x = 0
        try:
            if not users:
                await app.send_message("me", "Список пуст.")
            else:
                for i in users:
                    await app.send_message("me", f'{x}. {i}')
                    x += 1
        except:
            await app.send_message("me", text="Возникла ошибка при отправке списка.")


    # УДАЛЕНИЕ ИЗ СПИСКА


    @app.on_message(filters.command("del", prefixes=".") & filters.me)
    async def removeUser(_, msg):
        try:
            removeUsr = int(msg.text.split(".del ", maxsplit=1)[1])
            users.pop(removeUsr)
            await app.send_message("me", "Пользователь удален из списка.")
        except:
            await app.send_message("me", "Ошибка при удалении.")


    ################################## ЗАПУСК ЮЗЕР-БОТА ###############################################
    print("Юзер-бот запущен")
    app.run()

except:
    print("Возникла ошибка.")
