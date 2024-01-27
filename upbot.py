
import os
from telegram import update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import gspread
from google.oauth2 import service_account
from oauth2client.service_account import ServiceAccountCredentials


tele_tocken="6556831140:AAEwsGuiuywLcKpP21LMCujzJs5pqR9EzWk"
cred= r"E:\Download\new-upmarket-448072232ab9.json"
sheet_key="168AnrMIFFTUb0qvphMZY_lSMQ9yvbOpIa_CCc5U5rIQ"
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']


credentials=ServiceAccountCredentials.from_json_keyfile_name(cred,scope)
client=gspread.authorize(credentials)
sheet=client.open_by_key(sheet_key).sheet1


def start(update:update,context:CallbackContext)->None:
    update.message.reply_text('Welcome To UpMarket! Make your journey Profitable.')


def about(update:update,context:CallbackContext)->None:
    user_question=" ".join(context.args)
    answer=search_question_in_sheet(user_question)
    update.message.reply_text(answer)


def help_command(update:update,context:CallbackContext)->None:
    user_question=" ".join(context.args)
    answer=search_question_in_sheet(user_question)
    update.message.reply_text(answer)


def search_question_in_sheet(user_question):
    records=sheet.get_all_records()

    for record in records:
        if record['Questions'].lower()==user_question.lower():
            return record['Answer']
        
    return "Sorry, the answer to your question is not available."
    
def main():
    updater=Updater(token=tele_tocken)
    dispatcher=updater.dispatcher

    dispatcher.add_handler(CommandHandler('Start',start))
    dispatcher.add_handler(CommandHandler("about",about))
    dispatcher.add_handler(CommandHandler("help",help_command))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()