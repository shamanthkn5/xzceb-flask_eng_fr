"""
Author : https://github.com/shamanthkn5
"""
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(URL)

def english_to_french(english_text):
    """
    Translates from English to French
    """
    french_text = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = french_text['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    Translates from French to English
    """
    english_text = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = english_text['translations'][0]['translation']
    return english_text
