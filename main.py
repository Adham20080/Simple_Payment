import asyncio
import logging
from aiogram import Bot
from aiogram import Dispatcher
from aiogram.filters.command import Command
from aiogram.types import Message, LabeledPrice, ShippingOption

BOT_TOKEN = ''
PAYMENTS_PROVIDER_TOKEN = ''

bot = Bot(BOT_TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

prices = [
    LabeledPrice(label='Ish vaqti mashinasi', amount=10000, currency='UZS'),
    LabeledPrice(label="Sovg'a o'rash", amount=15000, currency='UZS'),
]


@dp.message(Command('start'))
async def cmd_start(message: Message):
    await bot.send_message(message.chat.id,
                           """Salom, men demo savdogar botiman. Men sizga “Vaqt mashinasi”ni sotishim mumkin.
Buyurtma berish uchun /buy, Shartlar va shartlar uchun /terms foydalaning""")


@dp.message(Command('terms'))
async def cmd_terms(message: Message):
    await bot.send_message(message.chat.id,
                           """Demo botimiz bilan xarid qilganingiz uchun tashakkur. Yangi vaqt mashinasi sizga yoqadi degan umiddamiz!\n
1. Agar vaqt mashinangiz o'z vaqtida yetkazib berilmagan bo'lsa, iltimos, vaqt tushunchangizni qayta ko'rib chiqing.
 va qayta urinib ko'ring.\n
2. Vaqt mashinangiz ishlamayotganligini aniqlasangiz, bizning kelajakdagi xizmatimizga murojaat qiling.
 Trappist-1e bo'yicha seminarlar. Ularga istalgan joyda kirish mumkin bo'ladi
 2075 yil may va 4000 yil noyabr\n
3. Agar siz to'lovni qaytarib olishni istasangiz, iltimos, kecha ariza bering, biz uni yuboramiz
- darhol sizga.""")


@dp.message(Command('buy'))
async def cmd_buy(message: Message):
    await bot.send_message(message.chat.id,
                           "Haqiqiy kartalar men bilan ishlamaydi, sizning hisobingizdan pul yechib olinmaydi."
                           "Vaqt mashinasi uchun to'lovni amalga oshirish uchun ushbu test kartasi raqamidan foydalaning: `4231 2000 0932 2941`"
                           "\n\nBu sizning demo hisob-fakturangiz:",
                           parse_mode='Markdown')
    await bot.send_invoice(message.chat.id,
                           title="To'lo'v",
                           description='Katta buvijonlaringizni ziyorat qilishni xohlaysizmi?'
                                       ' Poygalarda boylik topasizmi?'
                                       " Hammurabi bilan qo'l berib ko'rishib, osilgan bog'larda sayr qilyapsizmi?"
                                       ' Ish vaqti mashinamizga bugun buyurtma bering!',
                           provider_token=PAYMENTS_PROVIDER_TOKEN,
                           currency='uzs',
                           photo_url='[6](https://telegra.ph/file/d08ff863531f10bf2ea4b.jpg)',
                           photo_height=512,
                           photo_width=512,
                           photo_size=512,
                           is_flexible=True,
                           prices=prices,
                           start_parameter='time-machine-example',
                           payload='JUMA KUPONI MUBORAK')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
