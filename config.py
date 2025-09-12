import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler


TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8154426339")
APP_ID = int(os.environ.get("APP_ID", "")) #Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "") #Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002170811388")) #Your db channel Id
OWNER = os.environ.get("OWNER", "colossals") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "7328629001")) # Owner id
#--------------------------------------------
PORT = os.environ.get("PORT", "8001")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluooo")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "10"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/colossals")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "https://i.ibb.co/N69nBvYL/file-1922.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://i.ibb.co/jkWnPpD0/file-1924.jpg")
#--------------------------------------------

HELP_TXT = "<b><blockquote>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ ᴀᴅᴅʏ\n\n❏ ᴀᴅᴍɪɴ/ᴄʜᴀɴɴᴇʟ\n├ᴀᴅᴍɪɴ : t.me/colossals\n├ᴄʜᴀɴɴᴇʟ : t.me/PythonPortalz\n└ɢʀᴏᴜᴘ : ʏᴇᴛ, ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ\n\nᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ꜰᴏʀ ʙᴇꜱᴛ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ, ꜰʀᴇᴇ ᴘʏᴛʜᴏɴ ᴛᴏᴏʟꜱ!\n\n</blockquote></b>"
ABOUT_TXT = "<b><blockquote>🤖 ʙᴏᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ\n\n◈ ɴᴀᴍᴇ : ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ\n◈ ᴠᴇʀsɪᴏɴ : 2.0\n◈ ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ\n◈ ғʀᴀᴍᴇᴡᴏʀᴋ : ᴘʏʀᴏɢʀᴀᴍ\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : ᴀᴅᴅʏ\n\nI ᴀᴍ ᴀ sɪᴍᴘʟᴇ ʙᴏᴛ ᴛʜᴀᴛ ʜᴇʟᴘs ʏᴏᴜ ᴛᴏ sᴛᴏʀᴇ ғɪʟᴇs ᴀɴᴅ ɢᴇɴᴇʀᴀᴛᴇ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋs.\n</blockquote></b>"

START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ, {first}\n\n<blockquote> ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</blockquote></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

CMD_TXT = """<blockquote><b>» ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs:</b></blockquote>

<b>›› /dlt_time :</b> sᴇᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /check_dlt_time :</b> ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /dbroadcast :</b> ʙʀᴏᴀᴅᴄᴀsᴛ ᴅᴏᴄᴜᴍᴇɴᴛ / ᴠɪᴅᴇᴏ
<b>›› /ban :</b> ʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /unban :</b> ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /banlist :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ʙᴀɴɴᴇᴅ ᴜsᴇʀs
<b>›› /addchnl :</b> ᴀᴅᴅ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /delchnl :</b> ʀᴇᴍᴏᴠᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /listchnl :</b> ᴠɪᴇᴡ ᴀᴅᴅᴇᴅ ᴄʜᴀɴɴᴇʟs
<b>›› /fsub_mode :</b> ᴛᴏɢɢʟᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴍᴏᴅᴇ
<b>›› /pbroadcast :</b> sᴇɴᴅ ᴘʜᴏᴛᴏ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀs
<b>›› /add_admin :</b> ᴀᴅᴅ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /deladmin :</b> ʀᴇᴍᴏᴠᴇ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /admins :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ᴀᴅᴍɪɴs
"""

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @colossals</b>")
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "ʙᴏᴛ ᴜᴘᴛɪᴍᴇ\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

# ✅ New Bot Settings Text
BOT_SETTINGS_TEXT = """<b><blockquote>⚙️ ʙᴏᴛ sᴇᴛᴛɪɴɢs</blockquote>

◈ ᴛᴏᴛᴀʟ ғᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ: {total_channels}
◈ ᴛᴏᴛᴀʟ ᴀᴅᴍɪɴs: {total_admins}
◈ ᴛᴏᴛᴀʟ ʙᴀɴɴᴇᴅ ᴜsᴇʀs: {total_banned}
◈ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴍᴏᴅᴇ: {autodel_time}
◈ ᴘʀᴏᴛᴇᴄᴛ ᴄᴏɴᴛᴇɴᴛ: {protect_status}
◈ ʀᴇǫᴜᴇsᴛ ғsᴜʙ ᴍᴏᴅᴇ: {fsub_mode}</b>
"""

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
