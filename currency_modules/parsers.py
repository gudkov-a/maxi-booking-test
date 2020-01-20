from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET


class Parser(ABC):

    def parse(self, data):
        result = 0

        as_python_obj = self.deserialize_raw_data(data)

        list_of_elements = self.get_tree(as_python_obj)
        for element in list_of_elements:
            result = self.search(element)
            if result:
                break
        return self.__round(result)

    @abstractmethod
    def get_tree(self, obj) -> list:
        pass

    @abstractmethod
    def search(self, obj) -> str:
        pass

    def deserialize_raw_data(self, data):
        pass

    def __round(self, value) -> float:
        return round(value, 2) if value else value


class JsonParser(Parser):

    def get_tree(self, obj) -> list:
        result = []
        valutes = obj.get('Valute')
        for key, value in valutes.items():
            result.append((key, value))
        return result

    def search(self, obj) -> float:
        name, attributes = obj
        if name == 'EUR':
            return attributes.get('Value')

    def deserialize_raw_data(self, data) -> dict:
        return json.loads(data, encoding='utf-8')


class XMLParser(Parser):

    def get_tree(self, root) -> list:
        return root.iter()

    def search(self, obj) -> float:
        if obj.attrib.get('currency') == 'RUB':
            return float(obj.attrib.get('rate'))

    def deserialize_raw_data(self, data) -> str:
        return ET.fromstring(data)
