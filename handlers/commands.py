from aiogram import types
from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile, ReplyKeyboardRemove
import handlers.keyboard as KB 
from aiogram.enums import ParseMode
from parcing import * 

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Welcome to the News Bot!\nTo get information about bot use /help", reply_markup = KB.kb)

@router.message(Command(commands = ["help"]))
async def help(message: Message):
    await message.answer(
        "<b>This bot for recieve articles, descriptions and URLs from news by NYT</b>\n"
        "\n"
        "<b>Commands:</b>\n"
        "/start - for starting\n"
        "/help - to get information about bot\n"
        "----------------------------------------------\n"
        "<b>Buttons:</b>\n"
        "<b>Archive</b> - The Archive returns an array of NYT articles for a given month, going back to 1851. Its response fields are the same as the Article Search. The Archive is very useful if you want to build your own database of NYT article metadata. You simply pass the API the year and month and it returns a JSON object with all articles for that month. The Archive response size can be large (~20mb) and isn't meant to be called from the browser.\n"
        "<b>Popular</b> - Returns an array of the most viewed articles on NYTimes.com for specified period of time (1 day, 7 days, or 30 days).\n"
        "<b>Newswire</b> - With the Times Newswire, you can get links and metadata for Times' articles as soon as they are published on NYTimes.com. The Times Newswire provides an up-to-the-minute stream of published articles. You can filter results by source (all, nyt, inyt) and section (arts, business, ...).\n"
        "<b>Top_Stories</b> - The Top Stories returns an array of articles currently on the specified section.\n"
        "<b>Search</b> - Search for NYT articles by keywords, filters and facets.\n"
        "----------------------------------------------\n"
        "<b>Others:</b>\n"
        "<b>1</b> - you can write 1 to get interesting news for a day\n"
        "<b>7</b> - you can write 7 to get interesting news for a week\n"
        "<b>30</b> - you can write 30 to get interesting news for a month\n",
        parse_mode=ParseMode.HTML
    )

@router.message(F.text == "Archive")
async def archive(message: Message):
    await message.reply("<b>Enter the year and month begin from 1940</b> <u>(example of query: 2023 6):</u>", parse_mode=ParseMode.HTML)

@router.message(lambda message: message.text.startswith('19') or message.text.startswith('20'))
async def handle_archive_message(message: Message):
    try:
        year, month = message.text.split()
        year = int(year)
        month = int(month)
        archive_news = get_archive_news(year, month)
        if archive_news:
            for article in archive_news:
                await message.answer(f"<b>Title:</b> {article['title']}\n<b>Description:</b> {article['description']}\n<b>URL:</b> {article['url']}", reply_markup=KB.kb, parse_mode=ParseMode.HTML)
        else:
            await message.answer("Doesn't have any information")
    except ValueError:
        await message.answer("Invalid command format. Please use year month (for example, /archive 2023 6).")

    
@router.message(F.text == "Popular")
async def popular(message: Message):
    await message.answer("Choose period for popular news: ", reply_markup = await KB.popular_news_period_kb())

@router.message(F.text == "1")
async def popular_1(message: Message):
    popular_news = get_popular_news(1)
    for article in popular_news:
        await message.answer(f"<b>Title:</b> {article['title']}\n<b>Description:</b> {article['description']}\n<b>URL:</b> {article['url']}",  reply_markup=KB.kb, parse_mode=ParseMode.HTML)

    
@router.message(F.text == "7")
async def popular_1(message: Message):
    popular_news = get_popular_news(7)
    for article in popular_news:
        await message.answer(f"<b>Title:</b> {article['title']}\n<b>Description:</b> {article['description']}\n<b>URL:</b> {article['url']}", reply_markup= KB.kb, parse_mode=ParseMode.HTML)

@router.message(F.text == "30")
async def popular_1(message: Message):
    popular_news = get_popular_news(30)
    for article in popular_news:
        await message.answer(f"<b>Title:</b> {article['title']}\n<b>Description:</b> {article['description']}\n<b>URL:</b> {article['url']}", reply_markup= KB.kb, parse_mode=ParseMode.HTML)

@router.message(F.text == "Top_Stories")
async def top_stories(message: Message):
    await message.answer(
        "<b>Topic sections for Top Stories:</b>\n"
        "/arts - about arts\n"
        "/automobiles - about automobiles\n"
        "/business - about business\n"
        "/fasion - about fashion\n"
        "/food - about food\n"
        "/science - about science\n"
        "/politics - about politics\n"
        "/technology - about technology\n"
        "/theatre - about theatre\n",
        parse_mode=ParseMode.HTML
    )

@router.message(lambda message: message.text.startswith("/") and not (message.text.startswith("/start") and message.text.startswith("/help")))
async def section_top_stories(message: Message):
    section = message.text[1:]
    top_stories_news = get_top_stories(section)
    for article in top_stories_news:
        await message.answer(f"<b>Title: {article['title']}\n<b>Description:</b> {article['description']}\n<b>URL:</b> {article['url']}", reply_markup=KB.kb, parse_mode=ParseMode.HTML)

@router.message(F.text == "Newswire")
async def newswire(message: Message):
    await message.answer(
        "<b>Choose and Enter some options:</b>\n"
        "\n"
        "<b>Sources:</b>\n"
        "<b>all</b> - items from both The New York Times and The \n"
        "<b>nyt</b> - New York Times items only \n"
        "<b>inyt</b> = International New York Times items only (FKA The International Herald Tribune)\n"
        "\n"
        "<b>Sections:</b>\n"
        "<b>arts</b> - about arts\n"
        "<b>automobiles</b> - about automobiles\n"
        "<b>business</b> - about business\n"
        "<b>fasion</b> - about fashion\n"
        "<b>food</b> - about food\n"
        "<b>science</b> - about science\n"
        "<b>politics</b> - about politics\n"
        "<b>technology</b> - about technology\n"
        "<b>theatre</b> - about theatre\n"
        "\n"
        "<b>Example of query</b>: <u>newswire nyt all</u>", 
        parse_mode=ParseMode.HTML
    )

@router.message(lambda message: message.text.startswith('newswire'))
async def chosen_newswire(message: Message):
    command, source, section = message.text.split()
    news = get_times_newswire(source, section)
    for article in news:
            await message.answer(f"<b>Title:</b> {article['title']}\n<b>Description:</b> {article['description']}\n<b>URL:</b> {article['url']}", reply_markup=KB.kb, parse_mode=ParseMode.HTML)

@router.message(F.text == "Search")
async def select(message: Message):
    await message.answer("Enter interesting topic <b>(Example of query: search election)</b>: ", parse_mode=ParseMode.HTML)

@router.message(lambda message: message.text.startswith('search'))
async def query_of_interest(message: Message):
    command, topic = message.text.split()
    searching_news = get_search_news(topic)
    for article in searching_news:
            await message.answer(f"<b>Title:</b> {article['title']}\n<b>Description:</b> {article['description']}\n<b>URL:</b> {article['url']}", reply_markup=KB.kb, parse_mode=ParseMode.HTML)