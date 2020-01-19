from abc import ABC, abstractmethod
from settings import *
from currency_modules.getters import BaseGetter
from currency_modules.parsers import JsonParser, XMLParser


class AbstractFactory(ABC):

    @abstractmethod
    def get_source(self):
        pass

    @abstractmethod
    def get_receiver(self):
        pass

    @abstractmethod
    def get_parser(self):
        pass


class JsonFactory(AbstractFactory):

    def __init__(self):
        self.__url = json_source

    def get_source(self) -> str:
        return self.__url

    def get_receiver(self) -> BaseGetter:
        return BaseGetter(self.__url)

    def get_parser(self) -> JsonParser:
        return JsonParser()


class XMLFactory(AbstractFactory):

    def __init__(self):
        self.__url = xml_source

    def get_source(self) -> str:
        return self.__url

    def get_receiver(self) -> BaseGetter:
        return BaseGetter(self.__url)

    def get_parser(self) -> XMLParser:
        return XMLParser()
