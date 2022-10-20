from modules import bits, wttr, morse, qr, translator, tts, ocr

from io import BytesIO
from telegram     import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

def ocr_cmd(update: Update, context: CallbackContext):
    bot = context.bot
    chat_id = update.effective_chat.id

    buffer = BytesIO()
    update.message.photo[-1].get_file().download(out=buffer)

    text = ocr.image_to_string(buffer)
    bot.send_message(chat_id=chat_id, text=text)

def id_cmd(update: Update, context: CallbackContext):
    bot = context.bot
    chat_id = update.effective_chat.id
    bot.send_message(chat_id=chat_id, text=chat_id)

def tts_cmd(update: Update, context: CallbackContext):
    bot = context.bot
    chat_id = update.effective_chat.id
    text = update.message.text.partition(' ')[2].strip().partition(' ')

    mp3 = tts.create(text[2], text[0])
    bot.send_audio(chat_id=chat_id, audio=mp3)

def translate_cmd(update: Update, context: CallbackContext):
    bot = context.bot
    chat_id = update.effective_chat.id
    text = update.message.text.partition(' ')[2].strip().partition(' ')

    text = translator.translate(text[2], text[0])
    bot.send_message(chat_id=chat_id, text=text)
    

def qr_decode_cmd(update: Update, context: CallbackContext):
    bot = context.bot
    chat_id = update.effective_chat.id

    buffer = BytesIO()
    update.message.photo[-1].get_file().download(out=buffer)

    detected_codes = qr.decode(buffer.getvalue())
    for code in detected_codes:
        bot.send_message(chat_id=chat_id, text=code.data.decode("utf8"))

def qr_create_cmd(update: Update, context: CallbackContext):
    bot = context.bot
    chat_id = update.effective_chat.id
    text = update.message.text.partition(' ')[2].strip()

    png = qr.create(text)
    bot.send_photo(chat_id=chat_id, photo=png)

def wttr_cmd(update: Update, context: CallbackContext):
    bot = context.bot
    chat_id = update.effective_chat.id
    text = update.message.text.partition(' ')[2].strip()

    for png in wttr.forecast(text):
        bot.send_photo(chat_id=chat_id, photo=png)

def bits_cmd(update: Update, context: CallbackContext):
    bot = context.bot
    chat_id = update.effective_chat.id
    text = update.message.text.partition(' ')[2].strip()

    text = bits.translate(text)
    bot.send_message(chat_id=chat_id, text=text)

def morse_cmd(update: Update, context: CallbackContext):
    bot = context.bot
    chat_id = update.effective_chat.id
    text = update.message.text.partition(' ')[2].strip()

    text = morse.translate(text)
    bot.send_message(chat_id=chat_id, text=text)

def help_cmd(update: Update, context: CallbackContext):
    id_help     = '/id -> Eigene Chat ID'
    ocr_help    = '/ocr (als Bildbeschreibung) -> Extrahiert Text aus dem Bild'
    wiki_help   = '/wiki [Begriff] -> Englische Zusammenfassung des Artikels'
    tts_help    = '/tts [Sprache] [Text] -> mp3 in [Sprache](en, de, ru, etc) mit [Text]'
    trans_help  = '/t [Sprache] [Text] -> Übersetzt [Text] in [Sprache](en, de, ru, etc)'
    qr_help     = '/qr [Text] -> Text <-> QR Code \n(Dekodierung: /qr als Bildbeschreibung)'
    wttr_help   = '/wttr [Orte] -> Wetterbericht für alle Orte (default: Weilheim)'
    morse_help  = '/morse [Text] -> Morse <-> Text'
    binary_help = '/bits [Text] -> Bits  <-> Text (utf8)'
    text = id_help + '\n' + ocr_help + '\n' + tts_help + '\n' + trans_help + '\n' + qr_help + '\n' + wttr_help + '\n' + morse_help + '\n' + binary_help
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

# main
with open("token", "r") as f:
    token = f.read().strip()
updater = Updater(token)

updater.dispatcher.add_handler(CommandHandler("id", id_cmd))
updater.dispatcher.add_handler(CommandHandler("t", translate_cmd))
updater.dispatcher.add_handler(CommandHandler("tts", tts_cmd))
updater.dispatcher.add_handler(MessageHandler(Filters.caption(update=['/qr']), qr_decode_cmd))
updater.dispatcher.add_handler(MessageHandler(Filters.caption(update=['/ocr']), ocr_cmd))
updater.dispatcher.add_handler(CommandHandler("qr", qr_create_cmd))
updater.dispatcher.add_handler(CommandHandler("wttr", wttr_cmd))
updater.dispatcher.add_handler(CommandHandler("bits", bits_cmd))
updater.dispatcher.add_handler(CommandHandler("morse", morse_cmd))
updater.dispatcher.add_handler(CommandHandler("help", help_cmd))

updater.start_polling()