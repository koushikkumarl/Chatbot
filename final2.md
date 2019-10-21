## Generated Story -1589453916845855596
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "bangalore"}
    - slot{"cuisine": "italian"}
    - slot{"location": "bangalore"}
    - action_CheckLocation
    - utter_ask_budget
* goodbye{"budget": "high"}
    - slot{"budget": "high"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_budget
* goodbye{"budget": "low"}
    - slot{"budget": "low"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_email
* ask_email{"emailID": "sourav79dutta@gmail.com"}
    - slot{"emailID": "sourav79dutta@gmail.com"}
    - action_email
    - utter_mail_sent
    - export

