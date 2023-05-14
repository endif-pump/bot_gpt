"""/start command."""

from telegram import Update
from telegram.ext import CallbackContext
from telegram.constants import ParseMode

from bot.config import config
from . import constants
from . import help


class StartCommand:
    """Answers the `start` command."""

    async def __call__(self, update: Update, context: CallbackContext) -> None:
        if update.effective_user.username not in config.telegram.usernames:
            text = (
                "Привет можешь задавать любые вопросы, мне доступна инфа до 2021 года. Если хочешь, чтобы я поддерживал контекст вопросов, то задавай связанные вопросы отвечая на мои ответы, это стандартная механика для телеграм."
            )
            await update.message.reply_text(text)
            return

        text = "Hi! I'm a humble AI-driven chat bot.\n\n"
        text += help.generate_message(update.effective_user.username)
        if not context.bot.can_read_all_group_messages:
            text += f"\n\n{constants.PRIVACY_MESSAGE}"
        await update.message.reply_text(
            text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
        )
