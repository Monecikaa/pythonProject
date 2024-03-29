from aiogram import types

import keyboardButtons


async def welcome(message: types.Message):
    introduction = ("Hello! I'm your task manager bot. You can use the following commands:\n"
                    "/start - Start the bot and see this message\n"
                    "/quit - Quit the current operation\n"
                    "/add_task - Add a new task\n"
                    "/remove - Remove an existing task\n"
                    "/show - Show all your tasks\n\n"
                    "Get organized and stay on top of your tasks with TaskManagerBot!")

    await message.answer(introduction, reply_markup=keyboardButtons.user_kb)
