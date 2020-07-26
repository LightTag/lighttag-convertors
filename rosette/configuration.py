import yaml
import os
import threading
import functools
from abc import ABCMeta


singleton_lock = threading.Lock()


def synchronized(lock):
    """ Synchronization decorator """
    def wrap(f):
        @functools.wraps(f)
        def new_function(*args, **kw):
            with lock:
                return f(*args, **kw)
        return new_function
    return wrap


class Singleton(ABCMeta):
    def __init__(cls, name, bases, a_dict):
        super(Singleton, cls).__init__(name, bases, a_dict)
        cls.instance = None

    @synchronized(lock=singleton_lock)
    def _create_instance(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)

    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls._create_instance(*args, **kw)
        return cls.instance


class ConfigurationUtil:

    __metaclass__ = Singleton
    config = None

    @staticmethod
    def _load_configuration():
        file_dir = os.path.dirname(__file__)
        default_path = "settings.yaml"
        abs_file_path = os.path.join(file_dir, default_path)

        with open(abs_file_path, 'r') as ymlfile:
            default_settings = yaml.safe_load(ymlfile)
        ConfigurationUtil.config = default_settings

    @staticmethod
    # return config file per vendor name. if the vendor has not set some variables, it will get the default ones.
    def get_configuration():
        if not ConfigurationUtil.config:
            ConfigurationUtil._load_configuration()
        return ConfigurationUtil.config
