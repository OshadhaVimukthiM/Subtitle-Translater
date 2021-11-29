from pyrogram.types import InlineKeyboardButton
from creds import cred

welcome = "**ඔබට translate කිරීමට අවශ්‍ය උපසිරැසිය Upload කරන්න.**"
about = (
    "**Bot**      : [Subtitle Translator Bot](t.me/SubtitleTRBot)\n\n**මෙම බොට් මගින් ඔබට කුමක් හෝ භාෂාවකින් ඇති උපසිරසියක් තවත් භාෂාවකට පරිවර්තනය කල හැක.** "
)
help_text = (
    "**Steps to follow**\n\n**මෙය එකක භාෂාව පරිවර්තනය කිරීම සඳහා නිර්මාණය කල කෙනෙකි.**\n**1.** **පරිවර්තනය කිරීම සඳහා අවශ්‍ය ෆයිල් එක Upload කරන්න.**\n**2.** **පරිවර්තනය කල යුතු භාෂාව තෝරන්න (එකක් පමණක් යොදන්න).**\n**3.** **පරිවර්තනය සම්පූර්ණ වන තෙක් යම් කාලයක් රැඳී සිටින්න**\n\n**මතක තබා ගන්න**\n\n**1.** **ඔබට එකවර පරිවර්තනය කළ හැක්කේ එක් උපසිරැසියක් පමණි** \n**2.** **උපසිරැසි ගොනු කිහිපයක් එකවර යොමු නොකරන්න.**\n\n **Contact: @OshadhaPMbot**\n\n **To Back : /start** "
)
eta_text = (
    "**File name :** `{}`\n**Done** `{}` **of** `{}`\n**Percentage:** {}%\n**Speed:** {} lines/sec\n**ETA:** {}\n[{"
    "}{}] "
)
caption = f"Translated by {cred.BOT_NAME}"
empty = "`You need to send a subtitle(srt) file inorder to translate it`"
mmtypes = [
    "text/plain",
    "application/x-subrip",
    "application/octet-stream",
    "application/binary",
]
err1 = "**__One subtitle is processing wait sometime__**"
err2 = "**__This is not a subtitle(srt) file__**"
err3 = "**Todays limit exceeded**"
err4 = "**Unsupported characters in file**"
err5 = "**Some errors happened Try again..**"

langs = [
    [
        InlineKeyboardButton("മലയാളം", callback_data="Malayalam"),
        InlineKeyboardButton("தமிழ்", callback_data="Tamil"),
        InlineKeyboardButton("हिन्दी", callback_data="Hindi"),
    ],
    [
        InlineKeyboardButton("ಕನ್ನಡ", callback_data="Kannada"),
        InlineKeyboardButton("తెలుగు", callback_data="Telugu"),
        InlineKeyboardButton("मराठी", callback_data="Marathi"),
    ],
    [
        InlineKeyboardButton("ગુજરાતી", callback_data="Gujarati"),
        InlineKeyboardButton("ଓଡ଼ିଆ", callback_data="Odia"),
        InlineKeyboardButton("বাংলা", callback_data="bn"),
    ],
    [
        InlineKeyboardButton("ਪੰਜਾਬੀ", callback_data="Punjabi"),
        InlineKeyboardButton("فارسی", callback_data="Persian"),
        InlineKeyboardButton("English", callback_data="English"),
    ],
    [
        InlineKeyboardButton("español", callback_data="Spanish"),
        InlineKeyboardButton("français", callback_data="French"),
        InlineKeyboardButton("русский", callback_data="Russian"),
    ],
    [
        InlineKeyboardButton("עִברִית", callback_data="hebrew"),
        InlineKeyboardButton("العربية", callback_data="arabic"),
        InlineKeyboardButton("සිංහල",callback_data="sinhala"),
    ],
]
