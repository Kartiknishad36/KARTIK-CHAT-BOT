from pyrogram.types import InlineKeyboardButton
from config import SUPPORT_GRP, UPDATE_CHNL
from DNSCHAT import OWNER, DNSCHAT

# Centralized constants
SUPPORT_URL = f"https://t.me/{SUPPORT_GRP}"
UPDATE_URL = f"https://t.me/{UPDATE_CHNL}"
ADD_BOT_URL = f"https://t.me/{DNSCHAT.username}?startgroup=true"
HELP_URL = f"https://t.me/{DNSCHAT.username}?start=help"

# Utility function for styled buttons
def btn(text: str, **kwargs):
    return InlineKeyboardButton(text=text, **kwargs)

# Button layouts
BUTTON_SETS = {
    "start": [
        [btn("❖ ᴧᴅᴅ мᴇ ʙᴧʙʏ ❖", url=ADD_BOT_URL)],
        [btn("• ❍ᴡɴᴇꝛ •", user_id=OWNER), btn("• sᴜᴘᴘᴏꝛᴛ •", url=SUPPORT_URL)],
        [btn("⌯ ғᴇᴧᴛᴜʀᴇs ⌯", callback_data="HELP")],
    ],

    "developer": [
        [btn("• ❍ᴡɴᴇꝛ •", user_id=OWNER), btn("• sᴜᴘᴘᴏꝛᴛ •", url=SUPPORT_URL)],
        [btn("✦ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✦", url=ADD_BOT_URL)],
        [btn("« ʜᴇʟᴘ »", callback_data="HELP")],
        [btn("☁️ ᴀʙᴏᴜᴛ ☁️", callback_data="ABOUT")],
    ],

    "png": [
        [btn("• ᴧᴅᴅ мᴇ ʙᴧʙʏ •", url=ADD_BOT_URL)],
        [btn("⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE")],
    ],

    "back": [
        [btn("⦿ ʙᴀᴄᴋ ⦿", callback_data="BACK")],
    ],

    "help": [
        [btn("🐳 ᴄʜᴀᴛʙᴏᴛ 🐳", callback_data="CHATBOT_CMD"),
         btn("🎄 ᴛᴏᴏʟs 🎄", callback_data="TOOLS_DATA")],
        [btn("⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE")],
    ],

    "close": [
        [btn("⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE")],
    ],

    "chatbot_toggle": [
        [btn("ᴇɴᴀʙʟᴇ", callback_data="enable_chatbot"),
         btn("ᴅɪsᴀʙʟᴇ", callback_data="disable_chatbot")],
    ],

    "music_back": [
        [btn("sᴏᴏɴ", callback_data="soom")],
    ],

    "s_back": [
        [btn("⦿ ʙᴀᴄᴋ ⦿", callback_data="SBACK"),
         btn("⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE")],
    ],

    "chatbot_back": [
        [btn("⦿ ʙᴀᴄᴋ ⦿", callback_data="CHATBOT_BACK"),
         btn("⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE")],
    ],

    "help_start": [
        [btn("« ʜᴇʟᴘ »", callback_data="HELP"),
         btn("🐳 ᴄʟᴏsᴇ 🐳", callback_data="CLOSE")],
    ],

    "help_btn": [
        [btn("« ʜᴇʟᴘ »", url=HELP_URL),
         btn("⦿ ᴄʟᴏsᴇ ⦿", callback_data="CLOSE")],
    ],

    "about": [
        [btn("🎄 sᴜᴘᴘᴏʀᴛ 🎄", url=UPDATE_URL),
         btn("« ʜᴇʟᴘ »", callback_data="HELP")],
        [btn("🍾 ᴏᴡɴᴇʀ 🍾", user_id=OWNER)],
        [btn("🐳 ᴜᴘᴅᴀᴛᴇs 🐳", url=UPDATE_URL),
         btn("⦿ ʙᴀᴄᴋ ⦿", callback_data="BACK")],
    ],
}
