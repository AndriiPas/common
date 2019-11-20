import os


class Config:
    SECRET_KEY = 'secret_key'


class TestConfig:
    SECRET_KEY = 'secret_key1'


class ProdConfig:
    SECRET_KEY = 'secret_key2'


def run_config():
    env = os.environ.get("ENV")
    if env == "TEST":
        return TestConfig
    elif env == "PROD":
        return ProdConfig
    else:
        return Config



