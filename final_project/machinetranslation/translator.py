"""Module providing fuction to conver Eng Text to French Text and Vice-versa"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator=IAMAuthenticator(apikey)
language_translator=LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


#function to convert from Eng to French

def english_to_french(english_text):
    """fuction to convert Eng Text to French Text """
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    result=json.loads(json.dumps(translation, indent=2, ensure_ascii=False))

    return result['translations'][0]['translation']


#Func to convert French Text to English Text
def french_to_english(french_text):
    """Function to Convert French to English Text"""
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    result=json.loads(json.dumps(translation, indent=2, ensure_ascii=False))
    return result['translations'][0]['translation']
