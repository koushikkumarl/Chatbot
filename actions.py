from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json, operator
from flask import Flask
from flask_mail import Mail, Message



mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'testiiitb01@gmail.com',
    "MAIL_PASSWORD": 'machinelearning'
}


class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"e14a62ecced714c4f35c540a12b6d345"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location').lower()
		cuisine = tracker.get_slot('cuisine').lower()
		cost = tracker.get_slot('budget').lower()
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'chinese':25,'mexican':73,'italian':55,'american':1,'south indian':85,'north indian':50}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 1000)
		d = json.loads(results)
		response="" 
		numOfRestaurants = 0         
		if d['results_found'] == 0:
			response= "Sorry, we did not find any restaurant with mentioned criteria."
		else:			
			for restaurant in sorted(d['restaurants'],reverse = True, key = lambda sort_rating : sort_rating['restaurant']['user_rating']['aggregate_rating']):
				if(('low' in cost) and (restaurant['restaurant']['average_cost_for_two'] < 300) and (numOfRestaurants <= 5)):
					response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " is rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + " with an Avg cost for Two as " + str(restaurant['restaurant']['average_cost_for_two']) +"\n"
					numOfRestaurants += 1
				elif(('mid' in cost) and (300 <= restaurant['restaurant']['average_cost_for_two'] < 700)  and (numOfRestaurants <= 5)):
					response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " is rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + " with an Avg cost for Two as " + str(restaurant['restaurant']['average_cost_for_two']) +"\n"
					numOfRestaurants += 1
				elif(('high' in cost) and (restaurant['restaurant']['average_cost_for_two'] >= 700)  and (numOfRestaurants <= 5)):
					response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " is rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + " with an Avg cost for Two as " + str(restaurant['restaurant']['average_cost_for_two']) +"\n"
					numOfRestaurants += 1
		if(numOfRestaurants == 0):
			response= "Sorry, we did not find any restaurant with mentioned criteria."
			dispatcher.utter_message("***" + response + "***")
		elif(0 < numOfRestaurants <=5):
			dispatcher.utter_message("*** Found below restaurants as per your search criteria ***")
			distatcher.utter_message(response)

		return [SlotSet('location',loc)]

class ActionEmail(Action): 
    def name(self):
        return 'action_email'
    
    def run(self, dispatcher, tracker, domain):
        app = Flask(__name__)
        app.config.update(mail_settings)
        mail = Mail(app)
        dispatcher.utter_message("-------message1---------")
        mail.init_app(app)
        if __name__ == '__main__':
            with app.app_context():
                print("Entered the loop")
                msg = Message(subject="Hello",
                    sender=app.config.get("MAIL_USERNAME"),
                    recipients=["testiiitb01@gmail.com"], 
                    body="This is a test email I sent with Gmail and Python!")
                print("We are now here!")
                mail.send(msg)
        dispatcher.utter_message("-------message2---------")

class CheckLocation(Action):
    def name(self):
        return 'action_CheckLocation'
        
    def run(self, dispatcher, tracker, domain):
        tierCities = ['Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Ahmedabad', 'Pune', 'Agra', 'Ajmer',
        'Aligarh', 'Amravati', 'Amritsar', 'Asansol', 'Aurangabad', 'Bareilly', 'Belgaum', 'Bhavnagar', 'Bhiwandi', 'Bhopal', 'Bhubaneswar', 
        'Bikaner', 'Bilaspur', 'Bokaro Steel City', 'Chandigarh', 'Coimbatore', 'Nagpur', 'Cuttack', 'Dehradun', 'Dhanbad', 'Bhilai', 'Durgapur', 
        'Erode', 'Faridabad', 'Firozabad', 'Ghaziabad', 'Gorakhpur', 'Gulbarga', 'Guntur', 'Gwalior', 'Gurgaon', 'Guwahati', 'Hubli–Dharwad', 'Indore', 
        'Jabalpur', 'Jaipur', 'Jalandhar', 'Jammu', 'Jamnagar', 'Jamshedpur', 'Jhansi', 'Jodhpur', 'Kakinada', 'Kannur', 'Kanpur', 'Kochi', 'Kottayam', 
        'Kolhapur', 'Kollam', 'Kota', 'Kozhikode', 'Kurnool', 'Ludhiana', 'Lucknow', 'Madurai', 'Malappuram', 'Mathura', 'Goa', 'Mangalore', 'Meerut', 
        'Moradabad', 'Mysore', 'Nanded', 'Nashik', 'Nellore', 'Noida', 'Palakkad', 'Patna', 'Pondicherry', 'Purulia', 'Allahabad', 'Raipur', 'Rajkot', 
        'Rajahmundry', 'Ranchi', 'Rourkela', 'Salem', 'Sangli', 'Siliguri', 'Solapur', 'Srinagar', 'Thiruvananthapuram', 'Thrissur', 'Tiruchirappalli', 
        'Tirupati', 'Tirunelveli', 'Tiruppur', 'Tiruvannamalai', 'Ujjain', 'Bijapur', 'Vadodara', 'Varanasi', 'Vasai-Virar City', 'Vijayawada', 'Vellore', 
        'Warangal', 'Surat', 'Visakhapatnam']
        tierCitiesLower = [cities.lower() for cities in tierCities]
        userLocation = tracker.get_slot('location').lower()
        if userLocation not in tierCitiesLower: 
            dispatcher.utter_message("--- Sorry, We do not operate in that area yet ---")
            dispatcher.utter_message("*** Thank you for your query ***")
            tracker.reset_slots()
        else:
            dispatcher.utter_message("We are active in your area!")
        
