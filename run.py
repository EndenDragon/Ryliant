from Ryliant.bot import Ryliant
from config import CONFIG

ryliant = Ryliant(CONFIG["command_prefix"], CONFIG["modmail_channel_id"], CONFIG["verify_channel_id"])
ryliant.run(CONFIG["bot_token"])