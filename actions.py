# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionWeather(Action):
#
    def name(self) -> Text:
        return "action_weather"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#       
        city = tracker.get_slot('city')
        print('city got:', city)
        wtext = get_weather(city)

        dispatcher.utter_message(text=wtext)
#
        return []

def get_weather(city):
    if city.lower() == 'delhi':
        return "weather is warm"
    elif city.lower() == 'mumbai':
        return "weather is rainy"
    elif city.lower() == 'chennai':
        return "weatehr is hot"
    else:
        return f"sorry cannot get the weather of {city}"
