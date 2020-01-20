from urllib.request import Request, urlopen


class BaseGetter:

    def __init__(self, url):
        self.__url = url
        self.__timeout = 1

    def get(self):
        result = None
        request = self.__compose_request()
        try:
            response = urlopen(request, timeout=self.__timeout)
            if response.code == 200:
                result = response.read()
        except:
            pass

        return result

    def __get_agent(self):
        return 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                             'Chrome/35.0.1916.47 Safari/537.36'

    def __compose_request(self):
        agent = self.__get_agent()
        request = Request(self.__url, data=None, headers={'User-Agent': agent})
        return request
