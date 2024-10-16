from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
ENVIRONMENT=env.str("ENVIRONMENT")

SECRET_KEY=env.str("SECRET_KEY")
DEBUG = env.str("DEBUG") or False
ALLOWED_HOSTS = env.str("ALLOWED_HOSTS").split(",")
ALLOWED_IPS = env.str("ALLOWED_IPS").split(",")

BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili

DB_HOST=env.str('DB_HOST')
DB_PORT=env.str('DB_PORT')
DB_NAME=env.str('DB_NAME')
DB_USER=env.str('DB_USER')
DB_PASSWORD=env.str('DB_PASSWORD')

OFFICE_IP_ADDRESSES=env.str('OFFICE_IP_ADDRESS').split(",")

TWO_STEP_AUTH_BOT_TOKEN=env.str('TWO_STEP_AUTH_BOT_TOKEN')
TWO_STEP_AUTH_CODE_RECEIVERS = env.str("TWO_STEP_AUTH_CODE_RECEIVERS").split(",")