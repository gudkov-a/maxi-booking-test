from currency_modules.factories import JsonFactory, XMLFactory


def test_getters():
    for f in [JsonFactory, XMLFactory]:
        factory = f()
        url, getter, parser = factory.get_source(), factory.get_receiver(), factory.get_parser()
        content = getter(url).get()
        print(content)