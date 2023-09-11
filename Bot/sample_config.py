class Config(object):
    LOGGER = True
    TOKEN = ""
    DB_URI = ""
    OWNER_ID = ""


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
