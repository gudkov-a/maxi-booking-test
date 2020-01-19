from abc import ABC, abstractmethod


class Parser(ABC):

    def parse(self, data):
        result = None
        list_of_elements = self.__get_tree()
        for element in list_of_elements:
            result = self.__search(element)
            if result:
                break
        return result

    @abstractmethod
    def __get_tree(self) -> list:
        pass

    @abstractmethod
    def __search(self, obj) -> str:
        pass


class JsonParser(Parser):

    def __get_tree(self) -> list:
        return ['']

    def __search(self, obj) -> str:
        return ''


class XMLParser(Parser):
    pass
