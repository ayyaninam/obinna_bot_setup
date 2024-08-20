import bot_settings as settings
logger = settings.logging.getLogger(__name__)

async def load_all_bot_files(bot):
    logger.info(f"User: {bot.user} (ID: {bot.user.id})")
    for extension_file in settings.BOT_FILES_FOLDER.glob("*.py"):
        if extension_file.name != "__init__.py" and not extension_file.name.startswith("_"):
            await bot.load_extension(f"{settings.BOT_FILES_FOLDER.name}.{extension_file.name[:-3]}")
            logger.debug(f"Loadded FILE: {extension_file.name}")