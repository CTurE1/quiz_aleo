from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext
import logging

TOKEN = "token"
ADMINS = {316509758, 123456789, 987654321}  # добавьте нужные user_id админов

QUESTIONS = [
    {
        "text": "What is Aleo?",
        "options": ["1️⃣ A blockchain for creating public applications",
                    "2️⃣ A platform for creating private applications", "3️⃣ A cloud storage service"],
        "answer": 1
    },
    {
        "text": "What are zk-SNARKs?",
        "options": ["1️⃣ Data encryption technology",
                    "2️⃣ A protocol for fast verification of mathematical assertions without revealing information",
                    "3️⃣ A programming language"],
        "answer": 1
    },
    {
        "text": "What is Leo used for in the context of Aleo?",
        "options": ["1️⃣ A programming language for creating private applications on Aleo",
                    "2️⃣ A currency within the Aleo platform", "3️⃣ A tool for monitoring the Aleo network"],
        "answer": 0
    },
    {
        "text": "What is Aleo Studio?",
        "options": ["1️⃣ A graphic design editor", "2️⃣ An online editor for development in Leo",
                    "3️⃣ A sound recording studio"],
        "answer": 1
    },
    {
        "text": "What is the main principle of Aleo's operation?",
        "options": ["1️⃣ Publicity", "2️⃣ Privacy", "3️⃣ Decentralization"],
        "answer": 1
    },
    {
        "text": "What is the Setup Ceremony in the context of Aleo?",
        "options": ["1️⃣ A process for generating public parameters for zk-SNARKs", "2️⃣ Installing Aleo software",
                    "3️⃣ A developer award ceremony"],
        "answer": 0
    },
    {
        "text": "What type of accounts is used in Aleo?",
        "options": ["1️⃣ Public accounts", "2️⃣ Private accounts", "3️⃣ Anonymous accounts"],
        "answer": 1
    },
    {
        "text": "What is Aleo Testnet?",
        "options": ["1️⃣ A test network for Aleo developers and users", "2️⃣ The main Aleo network",
                    "3️⃣ A service for testing internet speed"],
        "answer": 0
    },
    {
        "text": "What main element is used to create private transactions in Aleo?",
        "options": ["1️⃣ Zero-knowledge proofs (zk-SNARKs)", "2️⃣ Multi-signature wallets", "3️⃣ Encrypted channels"],
        "answer": 0
    },
    {
        "text": "Which programming language is used to write smart contracts on Aleo?",
        "options": ["1️⃣ Solidity", "2️⃣ Leo", "3️⃣ Rust"],
        "answer": 1
    },
    {
        "text": "What is Aleo Package Manager (APM)?",
        "options": ["1️⃣ A tool for managing dependencies and packages in Aleo projects", "2️⃣ A task manager",
                    "3️⃣ A data storage service"],
        "answer": 0
    },
    {
        "text": "Which compiler is used for the Leo language?",
        "options": ["1️⃣ Solc", "2️⃣ LeoC", "3️⃣ Rustc"],
        "answer": 1
    },
    {
        "text": "What is Aleo Explorer?",
        "options": ["1️⃣ A tool for space exploration",
                    "2️⃣ A web interface for viewing transactions and blocks in the Aleo network",
                    "3️⃣ An internet search engine"],
        "answer": 1
    },
    {
        "text": "Which consensus algorithm does Aleo use?",
        "options": ["1️⃣ Proof of Work (PoW)", "2️⃣ Proof of Succinct Work (PoSW)", "3️⃣ Proof of Stake (PoS)"],
        "answer": 1
    },
    {
        "text": "What is Aleo Identity?",
        "options": ["1️⃣ A protocol for creating and managing private identifiers on Aleo",
                    "2️⃣ An identity verification service", "3️⃣ A system for creating avatars"],
        "answer": 0
    },
    {
        "text": "What is the maximum block size in the Aleo network?",
        "options": ["1️⃣ 1 MB", "2️⃣ 2 MB", "3️⃣ 4 MB"],
        "answer": 1
    },
    {
        "text": "Which hashing type is used in Aleo?",
        "options": ["1️⃣ SHA-256", "2️⃣ Poseidon", "3️⃣ Keccak"],
        "answer": 1
    },
    {
        "text": "What is Aleo Records?",
        "options": ["1️⃣ A music label", "2️⃣ A system for storing and processing private data on Aleo",
                    "3️⃣ A time-tracking service"],
        "answer": 1
    },
    {
        "text": "Which main wallet is used to work with Aleo?",
        "options": ["1️⃣ Metamask", "2️⃣ Leo Wallet", "3️⃣ Trust Wallet"],
        "answer": 1
    }

]

subscribers = set()

def start(update: Update, context: CallbackContext) -> None:
    subscribers.add(update.message.chat_id)
    update.message.reply_text('Hi! Shall we start the test?')
    start_test(update, context)

def start_test(update: Update, context: CallbackContext) -> None:
    context.user_data['question_index'] = 0
    context.user_data['correct_answers'] = 0  # счетчик правильных ответов
    ask_question(update, context)

def ask_question(update: Update, context: CallbackContext) -> None:
    question_index = context.user_data.get('question_index', 0)
    if question_index < len(QUESTIONS):
        question = QUESTIONS[question_index]
        keyboard = [[InlineKeyboardButton(option, callback_data=str(i))] for i, option in enumerate(question["options"])]
        reply_markup = InlineKeyboardMarkup(keyboard)

        if update.callback_query:
            update.callback_query.message.reply_text(question["text"], reply_markup=reply_markup)
        else:
            update.message.reply_text(question["text"], reply_markup=reply_markup)
    else:
        correct_answers = context.user_data.get('correct_answers', 0)
        wrong_answers = question_index - correct_answers
        update.callback_query.edit_message_text(
            f'The test is complete.\n✅ **Correct answers:** {correct_answers}.  \n❌ **Wrong answers:** {wrong_answers}. \n\nThank you for participating! You will now receive notifications about upcoming quizzes that will take place on the official Aleo server in Discord.',
            parse_mode=ParseMode.MARKDOWN



def handle_answer(update: Update, context: CallbackContext) -> None:
    answer = int(update.callback_query.data)
    question_index = context.user_data['question_index']

    if question_index >= len(QUESTIONS):
        return

    if answer == QUESTIONS[question_index]["answer"]:
        context.bot.edit_message_text(chat_id=update.effective_chat.id,
                                      message_id=update.callback_query.message.message_id, text="✅That's right!")
        context.user_data['correct_answers'] += 1
    else:
        context.bot.edit_message_text(chat_id=update.effective_chat.id,
                                      message_id=update.callback_query.message.message_id, text="❌Wrong ")
    context.user_data['question_index'] += 1
    ask_question(update, context)

def broadcast_message(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.id in ADMINS:
        message_text = ' '.join(context.args)
        if not message_text:
            update.message.reply_text("Вы не указали текст рассылки!")
            return
        for user_id in subscribers:
            try:
                context.bot.send_message(user_id, message_text)
            except Exception as e:
                pass
        update.message.reply_text("Сообщение успешно отправлено всем пользователям!")

def send_message_to_all(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.id in ADMINS:
        text_to_send = " ".join(context.args)
        for chat_id in subscribers:
            context.bot.send_message(chat_id=chat_id, text=text_to_send)

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(handle_answer))
    dp.add_handler(CommandHandler("sendall", send_message_to_all, pass_args=True))
    dp.add_handler(CommandHandler("broadcast", broadcast_message, pass_args=True))

    updater.start_polling()
    updater.idle()
