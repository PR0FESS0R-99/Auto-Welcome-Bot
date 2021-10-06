from pyrogram import Client, filters
from pyrogram.types import Message, User

Pr0fess0r_99= Client(
    "Welcome-Bot",
     bot_token = os.environ["BOT_TOKEN"],
     api_id = int(os.environ["API_ID"]),
     api_hash = os.environ["API_HASH"]
)

@Pr0fess0r_99.on_message(filters.command("start"))
async def start(bot, clinet)
    start_msg = "👋Hy {}, Iam Simple Auto Welcome Bot\n\nMaintained By @Mo_Tech_YT"
    reply_markup = InlineKeyboardMarkup
    (
         [
              [
                   InlineKeyboardButton
                        (
                             "🤖More Bots", url="t.me/MT_Botz"
                         ),
                   InlineKeyboardButton
                        (
                             "💡Open Source", url="t.me/MT_Botz"
                         )
              ],
              [
                   InlineKeyboardButton
                        (
                             "➕️ Add Your Chats ➕️", url=""
                         )
              ]
         ]
    )                         
    await replay_text(start_msg.fromat(update.from_user.mention), reply_markup=reply_markup)

@Pr0fess0r_99.on_message(filter.new_chat_members)
asnyc def auto_welcome(bot, message)
    first = message.from_user.first
    last = message.from_user.last
    mention = message.from_user.mention
    username = message.from_user.username
    id = message.from_user.id
    group = message.chat.name
    welcome_text = f"👋Hey {mention}, Welcome To {group}\n\n Developed By @Mo_Tech_YT"
    welcome_msg = os.envrison["WELCOME_TEXT", "welcome_text")
    await replay_text(welcome_msg)

Pr0fess0r_99(run)
