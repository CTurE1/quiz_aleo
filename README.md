# README for Telegram Quiz Bot

#DS - vadimwright

## Overview

I made this bot in the "era" of quizzes. So that every participant could get a notification about the upcoming quiz, and also to test his knowledge on a quiz that I invented. Read more about what the bot can do below.

## Features

- Quiz functionality with multiple-choice questions.
- Inline keyboard for answer selection.
- Score tracking for correct and incorrect answers.
- Admin capability to send broadcast messages to all subscribers.
- Persistent subscriber list across bot restarts.

## Requirements

- Python 3.6 or higher
- `python-telegram-bot` module

## Installation

1. Clone the repository to your local machine.
2. Install the required Python package by running `pip install python-telegram-bot`.
3. Create a bot in Telegram using BotFather and obtain the TOKEN.
4. Replace the `TOKEN` variable in the script with your actual bot token.
5. Add the user IDs of the admins in the `ADMINS` set.

## Usage

1. Run the bot script with `python bot_script.py`.
2. Use the `/start` command in Telegram to subscribe to the bot and start the quiz.
3. Answer the quiz questions using the inline buttons.
4. Admins can use `/sendall` followed by a message to send a broadcast to all subscribers.
5. Admins can use `/broadcast` followed by a message to send a broadcast to all subscribers.

## Bot Commands

- `/start` - Subscribe to the bot and start the quiz.
- `/sendall [message]` - (Admin only) Send a message to all subscribers.
- `/broadcast [message]` - (Admin only) Broadcast a message to all subscribers.

## Admins

To add or remove admins, update the `ADMINS` set in the script with the respective Telegram user IDs.

## Questions Configuration

The quiz questions are stored in the `QUESTIONS` list. Each question is a dictionary with the following keys:

- `text`: The question text.
- `options`: A list of answer options.
- `answer`: The index of the correct answer in the `options` list.

To add or modify questions, edit the `QUESTIONS` list accordingly.

## Subscribers

The bot maintains a set of subscribers who have interacted with the `/start` command. This list is used to send broadcast messages.

## Error Handling

The bot includes basic error handling for sending messages. If a message fails to send to a user (e.g., if the bot is blocked by the user), it will silently fail and continue.

## Logging

The bot uses Python's `logging` module to log messages and errors. The log level is set to `INFO` by default.

## License

This bot is released under the [MIT License](https://opensource.org/licenses/MIT).

## Contributions

Contributions are welcome. Please open an issue or pull request on the repository.

## Support

For support, please open an issue on the repository or contact the bot administrator.

------

Please ensure you have the correct permissions and have followed the Telegram Bot API's guidelines before deploying the bot.
