from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler,MessageHandler, filters,ContextTypes

TOKEN: Final = "7371880397:AAHRXkaLH4ehkQ1_YgnmB3BzfoRiRdqzJvA"
BOT_USERNAME: Final = '@yyorichiiibot'

#Commands 
async def start_commmand(update:  Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Helllo thanks for comming! I am Yorichii! ')

async def help_commmand(update:  Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hi I am Yorichii! Made by Ayush Please type something so that i can respond... Do your experiments!!!!!  ')

async def custom_commmand(update:  Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is an custom command!! ')


# Response 

def handle_response(text:str) -> str:
    processed : str = text.lower()
    if 'hello' in processed:
        return 'Hey there!'
    
    if 'how Are you' in processed:
        return 'Hope you are good'
    
    return 'I do not understand what you wrote.....'
    
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    
    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME,'').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    
    print('Bot:',response)    
    await update.message.reply_text(response)
    
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
    
if __name__ == '__main__':
    print('Starting Bot....')
    app = Application.builder().token(TOKEN).build()
    
    # commmands 
    app.add_handler(CommandHandler('start',start_commmand))
    app.add_handler(CommandHandler('help',help_commmand))
    app.add_handler(CommandHandler('custom',custom_commmand))


    #  Message 
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    # Errors
    
    app.add_error_handler(error)
    
    # Poll the bot
    print('Polling....')
    app.run_polling(poll_interval = 3)
    