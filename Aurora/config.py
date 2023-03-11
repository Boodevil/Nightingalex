import json
import os


def get_user_list(config, key):
    with open('{}/Aurora/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]

class Config(object):
    LOGGER=True
    URL=False
    ALLOW_CHATS=True
    ALLOW_EXCL=False
    TEMP_DOWNLOAD_DIRECTORY=""
    DEL_CMDS=False
    BAN_STICKER=""
    CERT_PATH=""
    PORT=8443
    WORKERS=8
    LOAD=""
    NO_LOAD="translation"
    MONGO_DB=""
    WEBHOOK=False
    BOT_API_URL="5970006962:"
    #kacrmdi
    WOLVES=[]
    BOT_ID="5970006962" 
    SQLALCHEMY_DATABASE_URI="postgresql://ycslfwhc:AZyv9qmLy4h3MqSxPg3RNZ53EuJJ1YIu@salt.db.elephantsql.com/ycslfwhc" 
    JOIN_LOGGER="-1001745971242" 
    API_HASH="c1b434defccacad6063758c9a7d76d5d" 
    INFOPIC=True
    TIGERS=[]
    API_ID="13849191"
    BL_CHATS=[1]
    DB_URL="postgres://ycslfwhc:AZyv9qmLy4h3MqSxPg3RNZ53EuJJ1YIu@salt.db.elephantsql.com/ycslfwhc" 
    TOKEN="5970006962:"
    DEV_USERS=[]
    DRAGONS=[]
    SPAMWATCH_API=""
    WALL_API=""
    DEMONS=[]
    SUPPORT_CHAT="LucyBotSupport"
    OWNER_USERNAME="XTheAnonymous"
    DONATION_LINK="lwdaalay"
    EVENT_LOGS="-1001862167968" 
    OWNER_ID="5531584953" 
    TIME_API_KEY=""
    ERROR_LOGS="-1001862167968" 
    BOT_NAME="LucyPro_bot"
    STRICT_GBAN=True
    REDIS_URL="redis://OKI:Izaya123@+@redis-18548.c277.us-east-1-3.ec2.cloud.redislabs.com:18548/OKI-free-db"
    UPDATE_CHANNEL="AstorPro"
    MONGO_DB_URI="mongodb://haitham:haitham123@ac-qyf5dda-shard-00-00.fwvg6ry.mongodb.net:27017,ac-qyf5dda-shard-00-01.fwvg6ry.mongodb.net:27017,ac-qyf5dda-shard-00-02.fwvg6ry.mongodb.net:27017/?ssl=true&replicaSet=atlas-vm6xg9-shard-0&authSource=admin&retryWrites=true&w=majority"
    BOT_USERNAME="Lucy_ProBot"
    REM_BG_API_KEY=""
    CASH_API_KEY=""
    AI_API_KEY=""
    SPAMWATCH_SUPPORT_CHAT="SpamWatchSupport"
    OPENWEATHERMAP_ID=""
    LOG_GROUP_ID="-1001862167968"
    STRICT_GMUTE=False
    SPAMWATCH_API=""
    OWNER_NAME="U N K N O W N"
    BANCODES=""
    REPOSITORY="GitHub.com/Unknown-san/Lucy"
    ARQ_API_KEY="HRINZL-XDAQVW-AZYEPT-ZZJZSH-ARQ"
    ARQ_API_URL="HRINZL-XDAQVW-AZYEPT-ZZJZSH-ARQ"
    COTB=""
    

class Production(Config):
    LOGGER=True


class Development(Config):
    LOGGER=True
