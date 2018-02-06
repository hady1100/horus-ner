# -*- coding: utf8 -*-

from xml.etree import ElementTree
import requests
from horus.core.config import HorusConfig
from horus.core.translation.auth import AzureAuthClient


class BingTranslator(object):

    def __init__(self):
        config = HorusConfig()
        auth_client = AzureAuthClient(config.translation_secret)
        self.final_token = 'Bearer ' + auth_client.get_access_token()
        self.headers = {"Authorization ": self.final_token}
    def detect_language(self, text):
        try:
            detectUrl = "https://api.microsofttranslator.com/V2/Http.svc/Detect?text={}".format(text)
            translationData = requests.get(detectUrl, headers=self.headers)
            if translationData.status_code != 200:
                raise(':: error: bing lang detection status code: ' + str(translationData.status_code))
            translation = ElementTree.fromstring(translationData.text.encode('utf-8'))
            return translation.text
        except:
            raise

    def translate(self, input_text, to_lang):
        try:
            translateUrl = "http://api.microsofttranslator.com/v2/Http.svc/Translate?text={}&to={}".format(input_text, to_lang)
            translationData = requests.get(translateUrl, headers=self.headers)
            if translationData.status_code != 200:
                raise(':: error: bing translation status code: ' + str(translationData.status_code))
            translation = ElementTree.fromstring(translationData.text.encode('utf-8'))
            return translation.text
        except:
            raise

if __name__ == "__main__":
    t = BingTranslator()
    print t.translate("hey what's up dude?", 'pt-br')
    print t.detect_language("Que lingua estou falando, amigo?")
    print t.detect_language("Claro que não, isso é portugues!")