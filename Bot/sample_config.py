class Config(object):
    LOGGER = True
    TOKEN = "6177854513:AAHJ1pFLeCSpU5sc8-CDk5JbbxKkTjfZWho"
    DB_URI = "mongodb+srv://animebot:animesdkbot@cluster0.cybneuo.mongodb.net/?retryWrites=true&w=majority"
    OWNER_ID = "5729587090"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
