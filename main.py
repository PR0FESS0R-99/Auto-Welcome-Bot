import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

Pr0fess0r_99= Client(
    "Welcome-Bot",
     bot_token = os.environ["BOT_TOKEN"],
     api_id = int(os.environ["API_ID"]),
     api_hash = os.environ["API_HASH"]
)

@Pr0fess0r_99.on_message(filters.command("start"))
async def start(client: Pr0fess0r_99, update):
    start_msg = "👋Hy {}, Iam Simple Auto Welcome Bot\n\nMaintained By @Mo_Tech_YT"
    bot_username = await client.get_me()
    link = "PR0FESS0R-99/Auto-Welcome-Bot"
    reply_markup = InlineKeyboardMarkup(
        [             
            [
                InlineKeyboardButton
                    (
                         "🤖More Bots", url="t.me/MT_Botz"
                    ),
                InlineKeyboardButton
                    (
                         "💡Open Source", url="https://github.com/{link}" # PR0FESS0R-99/Auto-Welcome-Bot
                    )
            ],   
            [
                InlineKeyboardButton
                   (
                        "➕️ Add Me To Your Chats ➕️", url=f"http://t.me/{bot_username.username}?startgroup=botstart"
                   )
            ]
        ] 
    )                       
    await update.reply_text(
        text=start_msg.format(update.from_user.mention), reply_markup=reply_markup)

@Pr0fess0r_99.on_message(filters.new_chat_members)
async def auto_welcome(bot: Pr0fess0r_99, msg: Message):
    # from PR0FESS0R-99 import ID-Bot
    first = msg.from_user.first_name
    last = msg.from_user.last_name
    mention = msg.from_user.mention
    username = msg.from_user.username
    id = msg.from_user.id
    group_name = msg.chat.title
    group_username = msg.chat.username
    welcome_text = f"👋Hey {mention}, Welcome To {group_name}\n\n Developed By @Mo_Tech_YT"
    welcome_msg = os.environ.get(f"WELCOME_TEXT", welcome_text)
    print("Welcome Message Activate")
    await msg.reply_text(text=welcome_msg.format(
        first = msg.from_user.first_name,
        last = msg.from_user.last_name,
        username = None if not msg.from_user.username else '@' + msg.from_user.username,
        mention = msg.from_user.mention,
        id = msg.from_user.id,
        group_name = msg.chat.title,
        group_username = None if not msg.chat.username else '@' + msg.chat.username
   )

@Pr0fess0r_99.on_message(filters.private & filters.command("admin"))
async def admin(bot: Pr0fess0r_99, update):
    # Heroku Support
    user_admin = "Open Heroku => Application => Settings => Config Vars => Welcome_Text Edit"
    user = "👋Hey {}, \n You are not the deploy of this bot"
    run = "PR0FESS0R-99/Auto-Welcome-Bot" # https://github.com/PR0FESS0R-99/Auto-Welcome-Bot
    api_key = os.environ.get("APP_NAME", "")
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "").split()) 
    reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton
                    (
                        "⚙️HEROKU SETTINGS⚙️", url=f"https://dashboard.heroku.com/apps/{api_key}/settings"
                    )
            ]
        ]
    )
    deploy =InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton
                    (
                        "💫 DEPLOY NOW 💫", url=f"https://heroku.com/deploy?template=https://github.com/{run}/tree/main"
                    )
            ]
        ]
    )
    if update.from_user.id not in OWNER_ID:
        await update.reply_text(text=user.format(update.from_user.mention), reply_markup=deploy)
        return
    await update.reply_text(text=user_admin, reply_markup=reply_markup)
   
print("""Auto Welcome Bot Started

Maintained By @Mo_Tech_YT""")

Pr0fess0r_99.run()
