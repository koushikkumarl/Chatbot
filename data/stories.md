## Generated Story -1379461494582542013
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_CheckLocation
    - utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email
* ask_email{"emailID": "koushik.feb11@gmail.com"}
    - slot{"emailID": "koushik.feb11@gmail.com"}
    - action_email
    - export

## Generated Story -7468666327370873288
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_CheckLocation
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - export

## Generated Story 2375336889497663877
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "bangalore"}
    - slot{"cuisine": "italian"}
    - slot{"location": "bangalore"}
    - action_CheckLocation
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_email
    - utter_ask_email
* ask_email{"emailID": "koushik.feb11@gmail.com"}
    - slot{"emailID": "koushik.feb11@gmail.com"}
    - action_email
    - utter_thankyou
* restaurant_search
    - export