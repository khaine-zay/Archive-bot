from pony.orm import *
from pyrogram.types import Message
from os import listdir

# ========= DB build =========
db = Database()


class User(db.Entity):
    uid = PrimaryKey(int, auto=True, sql_type='BIGINT')
    status = Required(int)  # status-user: "INSERT"/"NOT-INSERT"


db.bind(provider='sqlite', filename='zipbot.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


# ========= helping func =========
def dir_work(uid: int) -> str:
    """ static-user folder """
    return f"static/{uid}/"


def zip_work(uid: int) -> str:
    """ zip-archive file """
    return f'static/{uid}.zip'


def list_dir(uid: int) -> list:
    """ items in static-user folder """
    return listdir(dir_work(uid))


def up_progress(current, total, msg: Message):
    """ edit status-msg with progress of the uploading """
    msg.edit(f"**התקדמות ההעלאה: {current * 100 / total:.1f}%**")


# ========= MSG class =========
class Msg:

    def start(msg: Message) -> str:
        """return start-message text"""
        txt = f"[‏](https://github.com/M100achuz2/archive-bot.git)Hey {msg.from_user.mention}!\n" \
              "With this bot, you can compress files into an archive. Send /zip to begin, and follow the instructions." \
              "\n\nThis robot was created by [Yeuda-By](t.me/m100achuzBots) from the team [Robotrick](t.me/robottrick)." \
              "\nFor the source code, [click here](https://github.com/M100achuz2/archive-bot)."
        return txt

    zip = "Send the files you want to compress, and when you're done, send /stopzip after all files have been uploaded. \n`The bot supports files up to 20MB each, " \
          "and up to 20 files per archive.`"
    too_big = "The file is too large."
    too_much = "You can only compress up to 20 files."
    send_zip = "Use the /zip command to compress files (:"
    zipping = "Starting to compress {} files..."
    uploading = "Uploading the archive..."
    unknow_error = "An unknown error occurred. \nPlease check the sequence of actions, you can start over by sending /start. \nMake sure " \
                   "you sent files for compression and waited for all of them to be uploaded. \nPlease send this to the developer:\n ```{}```"
    downloading = "Downloading file:"
    zero_files = "No files were sent."
