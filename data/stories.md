## story 1
* greet
  - utter_greet


## interactive_story_1
* greet
    - utter_greet
* ask_weather
    - utter_ask_city
* tell_city{"city": "mumbai"}
    - slot{"city": "mumbai"}
    - utter_is_this_correct
* affirm
    - action_weather
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* ask_weather
    - utter_ask_city
* ask_weather{"city": "kolkata"}
    - slot{"city": "kolkata"}
    - utter_is_this_correct
* affirm
    - action_weather
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* ask_weather{"city": "delhi"}
    - slot{"city": "delhi"}
    - utter_is_this_correct
* affirm
    - action_weather
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* ask_weather{"city": "pune"}
    - slot{"city": "pune"}
    - utter_is_this_correct
* affirm
    - action_weather
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* ask_weather{"city": "jaipur"}
    - slot{"city": "jaipur"}
    - utter_is_this_correct
* deny
    - utter_ask_city
* tell_city{"city": "jodhpur"}
    - slot{"city": "jodhpur"}
    - utter_is_this_correct
* affirm
    - action_weather
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* ask_weather
    - utter_ask_city
* tell_city{"city": "delhi"}
    - slot{"city": "delhi"}
    - utter_is_this_correct
* deny
    - utter_ask_city
* tell_city{"city": "mumbai"}
    - slot{"city": "mumbai"}
    - utter_is_this_correct
* affirm
    - action_weather
    - utter_goodbye

## interactive_story_2
* ask_weather{"city": "chennai"}
    - slot{"city": "chennai"}
    - utter_is_this_correct
* affirm
    - action_weather
    - utter_goodbye
