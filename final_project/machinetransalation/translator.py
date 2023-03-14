"""
Translation Module using IBM Watson AI
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

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
    #write the code here
    """
    Translate from English to French
    """
    if english_text is None:
        return "Nothing to Translate"
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translation.get("translations")[0].get("translation")
    return french_text

def french_to_english(french_text):
    #write the code here
    """
    Translate from French to English
    """
    if french_text is None:
        return "Nothing to Translate"
    translation = language_translator.translate(
        text=french_text,
        model_id='en-fr').get_result()
    english_text = translation.get("translations")[0].get("translation")
    return english_text
