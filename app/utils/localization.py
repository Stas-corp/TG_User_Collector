TRANSLATIONS = {
    "en": {
        "help_text": (
            "<b>Available commands:</b>\n"
            "/start - register user and chat\n"
            "/help - show this help\n"
            "/me - show your profile\n"
        ),
        "start_greeting": "👋 Hi, {name}! I've saved info about you.",
        "no_information": "Hmm... I don't have any information about you. Call the /start",
        "profile_title": "Your profile",
        "user_id": "User ID",
        "username": "Username",
        "first_name": "First name",
        "last_name": "Last name",
        "language": "Language",
        "registered": "Registered",
        "last_updated": "Last updated",
    },
    "uk": {
        "help_text": (
            "<b>Доступні команди:</b>\n"
            "/start - зареєструвати користувача та чат\n"
            "/help - показати цю довідку\n"
            "/me - показати твій профіль\n"
        ),
        "start_greeting": "👋 Привіт, {name}! Я зберіг інформацію про тебе",
        "no_information": "Хмм... Не маю інформації про тебе. Виконуй /start.",
        "profile_title": "Твій профіль",
        "user_id": "ID користувача",
        "username": "Ім'я користувача",
        "first_name": "Ім'я",
        "last_name": "Прізвище",
        "language": "Мова",
        "registered": "Зареєстрований",
        "last_updated": "Останнє оновлення",
    },
}


def get_text(key: str, lang: str | None = "en") -> str:
    if not lang:
        lang = "en"
    lang = lang.lower()[:2]
    if lang not in TRANSLATIONS:
        lang = "en"
    return TRANSLATIONS[lang].get(key, key)