from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import Message

kb = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = "Archive"),
    KeyboardButton(text = "Popular")],
    [KeyboardButton(text = "Top_Stories"),
    KeyboardButton(text = "Newswire")],
    [KeyboardButton(text = "Search")]],
    resize_keyboard = True, input_field_placeholder = "Choose option",
    one_time_keyboard = True)

async def popular_news_period_kb():
    keyboard = ReplyKeyboardBuilder()
    keyboard.add(KeyboardButton(text = str(1)))
    keyboard.add(KeyboardButton(text = str(7)))
    keyboard.add(KeyboardButton(text = str(30)))
    return keyboard.adjust(2).as_markup()
    



