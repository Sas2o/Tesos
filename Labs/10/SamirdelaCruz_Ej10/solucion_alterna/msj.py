import telegram
import sys

chat_id=854666549
bot = telegram.Bot(token='707039446:AAF3SjOcxUMklriKuiOpZCpwPMSgNtMnxgs')
bot.send_message(chat_id=chat_id, text="Se compleraron "+ str(int(sys.argv[1])+1) +"000 pruebas, hasta el momento se han obtenido estos resultados")
bot.send_document(chat_id=chat_id, document=open(str(sys.argv[2]), 'rb'))
bot.send_photo(chat_id=chat_id, photo=open(str(sys.argv[3]), 'rb'))


