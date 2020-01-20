from currency_modules.parsers import JsonParser, XMLParser
import json


def test_json_parser():
    sample_data = {
        "Date": "2020-01-18T11:30:00+03:00",
        "PreviousDate": "2020-01-17T11:30:00+03:00",
        "PreviousURL": "www.cbr-xml-daily.ru/archive/2020/01/17/daily_json.js",
        "Timestamp": "2020-01-19T18:00:00+03:00",
        "Valute": {
            "AUD": {
                "ID": "R01010",
                "NumCode": "036",
                "CharCode": "AUD",
                "Nominal": 1,
                "Name": "Австралийский доллар",
                "Value": 42.5134,
                "Previous": 42.5691
            },
            "AZN": {
                "ID": "R01020A",
                "NumCode": "944",
                "CharCode": "AZN",
                "Nominal": 1,
                "Name": "Азербайджанский манат",
                "Value": 36.2707,
                "Previous": 36.292
            },
            "GBP": {
                "ID": "R01035",
                "NumCode": "826",
                "CharCode": "GBP",
                "Nominal": 1,
                "Name": "Фунт стерлингов Соединенного королевства",
                "Value": 80.4917,
                "Previous": 80.3111
            },
            "AMD": {
                "ID": "R01060",
                "NumCode": "051",
                "CharCode": "AMD",
                "Nominal": 100,
                "Name": "Армянских драмов",
                "Value": 12.8261,
                "Previous": 12.8336
            },
            "BYN": {
                "ID": "R01090B",
                "NumCode": "933",
                "CharCode": "BYN",
                "Nominal": 1,
                "Name": "Белорусский рубль",
                "Value": 28.9814,
                "Previous": 28.9725
            },
            "BGN": {
                "ID": "R01100",
                "NumCode": "975",
                "CharCode": "BGN",
                "Nominal": 1,
                "Name": "Болгарский лев",
                "Value": 35.0358,
                "Previous": 35.1143
            },
            "BRL": {
                "ID": "R01115",
                "NumCode": "986",
                "CharCode": "BRL",
                "Nominal": 1,
                "Name": "Бразильский реал",
                "Value": 14.7029,
                "Previous": 14.745
            },
            "HUF": {
                "ID": "R01135",
                "NumCode": "348",
                "CharCode": "HUF",
                "Nominal": 100,
                "Name": "Венгерских форинтов",
                "Value": 20.4423,
                "Previous": 20.6035
            },
            "HKD": {
                "ID": "R01200",
                "NumCode": "344",
                "CharCode": "HKD",
                "Nominal": 10,
                "Name": "Гонконгских долларов",
                "Value": 79.1955,
                "Previous": 79.2103
            },
            "DKK": {
                "ID": "R01215",
                "NumCode": "208",
                "CharCode": "DKK",
                "Nominal": 10,
                "Name": "Датских крон",
                "Value": 91.6929,
                "Previous": 91.9042
            },
            "USD": {
                "ID": "R01235",
                "NumCode": "840",
                "CharCode": "USD",
                "Nominal": 1,
                "Name": "Доллар США",
                "Value": 61.5333,
                "Previous": 61.5694
            },
            "EUR": {
                "ID": "R01239",
                "NumCode": "978",
                "CharCode": "EUR",
                "Nominal": 1,
                "Name": "Евро",
                "Value": 68.5358,
                "Previous": 68.656
            },
            "INR": {
                "ID": "R01270",
                "NumCode": "356",
                "CharCode": "INR",
                "Nominal": 100,
                "Name": "Индийских рупий",
                "Value": 86.5843,
                "Previous": 86.8502
            },
            "KZT": {
                "ID": "R01335",
                "NumCode": "398",
                "CharCode": "KZT",
                "Nominal": 100,
                "Name": "Казахстанских тенге",
                "Value": 16.3535,
                "Previous": 16.3176
            },
            "CAD": {
                "ID": "R01350",
                "NumCode": "124",
                "CharCode": "CAD",
                "Nominal": 1,
                "Name": "Канадский доллар",
                "Value": 47.2135,
                "Previous": 47.2122
            },
            "KGS": {
                "ID": "R01370",
                "NumCode": "417",
                "CharCode": "KGS",
                "Nominal": 100,
                "Name": "Киргизских сомов",
                "Value": 88.0916,
                "Previous": 88.2118
            },
            "CNY": {
                "ID": "R01375",
                "NumCode": "156",
                "CharCode": "CNY",
                "Nominal": 10,
                "Name": "Китайских юаней",
                "Value": 89.7105,
                "Previous": 89.4215
            },
            "MDL": {
                "ID": "R01500",
                "NumCode": "498",
                "CharCode": "MDL",
                "Nominal": 10,
                "Name": "Молдавских леев",
                "Value": 35.0917,
                "Previous": 35.2833
            },
            "NOK": {
                "ID": "R01535",
                "NumCode": "578",
                "CharCode": "NOK",
                "Nominal": 10,
                "Name": "Норвежских крон",
                "Value": 69.2132,
                "Previous": 69.511
            },
            "PLN": {
                "ID": "R01565",
                "NumCode": "985",
                "CharCode": "PLN",
                "Nominal": 1,
                "Name": "Польский злотый",
                "Value": 16.1742,
                "Previous": 16.229
            },
            "RON": {
                "ID": "R01585F",
                "NumCode": "946",
                "CharCode": "RON",
                "Nominal": 1,
                "Name": "Румынский лей",
                "Value": 14.3334,
                "Previous": 14.3659
            },
            "XDR": {
                "ID": "R01589",
                "NumCode": "960",
                "CharCode": "XDR",
                "Nominal": 1,
                "Name": "СДР (специальные права заимствования)",
                "Value": 85.0606,
                "Previous": 85.0557
            },
            "SGD": {
                "ID": "R01625",
                "NumCode": "702",
                "CharCode": "SGD",
                "Nominal": 1,
                "Name": "Сингапурский доллар",
                "Value": 45.7225,
                "Previous": 45.7323
            },
            "TJS": {
                "ID": "R01670",
                "NumCode": "972",
                "CharCode": "TJS",
                "Nominal": 10,
                "Name": "Таджикских сомони",
                "Value": 63.4691,
                "Previous": 63.5063
            },
            "TRY": {
                "ID": "R01700J",
                "NumCode": "949",
                "CharCode": "TRY",
                "Nominal": 1,
                "Name": "Турецкая лира",
                "Value": 10.4945,
                "Previous": 10.4562
            },
            "TMT": {
                "ID": "R01710A",
                "NumCode": "934",
                "CharCode": "TMT",
                "Nominal": 1,
                "Name": "Новый туркменский манат",
                "Value": 17.6061,
                "Previous": 17.6164
            },
            "UZS": {
                "ID": "R01717",
                "NumCode": "860",
                "CharCode": "UZS",
                "Nominal": 10000,
                "Name": "Узбекских сумов",
                "Value": 64.4936,
                "Previous": 64.4654
            },
            "UAH": {
                "ID": "R01720",
                "NumCode": "980",
                "CharCode": "UAH",
                "Nominal": 10,
                "Name": "Украинских гривен",
                "Value": 25.4428,
                "Previous": 25.5742
            },
            "CZK": {
                "ID": "R01760",
                "NumCode": "203",
                "CharCode": "CZK",
                "Nominal": 10,
                "Name": "Чешских крон",
                "Value": 27.2127,
                "Previous": 27.3545
            },
            "SEK": {
                "ID": "R01770",
                "NumCode": "752",
                "CharCode": "SEK",
                "Nominal": 10,
                "Name": "Шведских крон",
                "Value": 64.8415,
                "Previous": 65.0722
            },
            "CHF": {
                "ID": "R01775",
                "NumCode": "756",
                "CharCode": "CHF",
                "Nominal": 1,
                "Name": "Швейцарский франк",
                "Value": 63.7189,
                "Previous": 63.9284
            },
            "ZAR": {
                "ID": "R01810",
                "NumCode": "710",
                "CharCode": "ZAR",
                "Nominal": 10,
                "Name": "Южноафриканских рэндов",
                "Value": 42.8374,
                "Previous": 42.7975
            },
            "KRW": {
                "ID": "R01815",
                "NumCode": "410",
                "CharCode": "KRW",
                "Nominal": 1000,
                "Name": "Вон Республики Корея",
                "Value": 53.1461,
                "Previous": 53.1499
            },
            "JPY": {
                "ID": "R01820",
                "NumCode": "392",
                "CharCode": "JPY",
                "Nominal": 100,
                "Name": "Японских иен",
                "Value": 55.8302,
                "Previous": 55.9875
            }
        }
    }

    json_parser = JsonParser()
    jsoned = json.dumps(sample_data)
    result = json_parser.parse(jsoned)
    assert result == 68.54


def test_xml_parser():
    sample_data = """<?xml version="1.0" encoding="UTF-8"?>
        <gesmes:Envelope xmlns:gesmes="http://www.gesmes.org/xml/2002-08-01" xmlns="http://www.ecb.int/vocabulary/2002-08-01/eurofxref">
            <gesmes:subject>Reference rates</gesmes:subject>
            <gesmes:Sender>
                <gesmes:name>European Central Bank</gesmes:name>
            </gesmes:Sender>
            <Cube>
                <Cube time='2020-01-17'>
                    <Cube currency='USD' rate='1.1108'/>
                    <Cube currency='JPY' rate='122.31'/>
                    <Cube currency='BGN' rate='1.9558'/>
                    <Cube currency='CZK' rate='25.147'/>
                    <Cube currency='DKK' rate='7.4729'/>
                    <Cube currency='GBP' rate='0.85105'/>
                    <Cube currency='HUF' rate='335.59'/>
                    <Cube currency='PLN' rate='4.2367'/>
                    <Cube currency='RON' rate='4.7803'/>
                    <Cube currency='SEK' rate='10.5450'/>
                    <Cube currency='CHF' rate='1.0736'/>
                    <Cube currency='ISK' rate='137.40'/>
                    <Cube currency='NOK' rate='9.8890'/>
                    <Cube currency='HRK' rate='7.4378'/>
                    <Cube currency='RUB' rate='68.2495'/>
                    <Cube currency='TRY' rate='6.5323'/>
                    <Cube currency='AUD' rate='1.6122'/>
                    <Cube currency='BRL' rate='4.6390'/>
                    <Cube currency='CAD' rate='1.4498'/>
                    <Cube currency='CNY' rate='7.6186'/>
                    <Cube currency='HKD' rate='8.6292'/>
                    <Cube currency='IDR' rate='15184.91'/>
                    <Cube currency='ILS' rate='3.8372'/>
                    <Cube currency='INR' rate='78.9567'/>
                    <Cube currency='KRW' rate='1288.37'/>
                    <Cube currency='MXN' rate='20.8338'/>
                    <Cube currency='MYR' rate='4.5041'/>
                    <Cube currency='NZD' rate='1.6782'/>
                    <Cube currency='PHP' rate='56.548'/>
                    <Cube currency='SGD' rate='1.4960'/>
                    <Cube currency='THB' rate='33.746'/>
                    <Cube currency='ZAR' rate='16.0582'/>
                </Cube>
            </Cube>
            </gesmes:Envelope>
    """
    xml_parser = XMLParser()
    result = xml_parser.parse(sample_data)
    assert result is None
