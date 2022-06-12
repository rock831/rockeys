from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "18145443"))
API_HASH = getenv("API_HASH", "dc90da21390582736a9d5b4ffce8b5bb")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","𝔸𝕒ℝ𝕦🇽 ℝ𝕠𝔹𝕠")
BOT_USERNAME = getenv("BOT_USERNAME", "AaRu_X_RoBoT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "BANNA_XD")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "AARU_SUPPORT")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "160"))
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/cede36b1f9b6d559466b1.jpg")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/cede36b1f9b6d559466b1.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5150456401").split()))
