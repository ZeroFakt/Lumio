from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message
from utils.local_gpt import ask_gpt

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Привет, я твой собеседник) Расскажи, как у тебя дела?"
        )
    
@router.message()
async def handle_message(message: types.Message):
    user_text = message.text
    if user_text is not None:
        reply = await ask_gpt(user_text)
    else:
        reply = "Похоже, ты ничего не написал 🤔"

    await message.answer(reply)