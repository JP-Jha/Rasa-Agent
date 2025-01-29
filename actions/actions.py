# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# ---2
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# from twilio.rest import Client

# # Define custom actions
# class ActionPlaySpotify(Action):
#     def name(self) -> str:
#         return "action_play_spotify"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
#         # Initialize Spotify API credentials (use your credentials here)
#         sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="3fb1846897864809ac9694b20ae73d8b",
#                                                         client_secret="8e64d0bf253449d8b655537d01fd02b3",
#                                                         redirect_uri="http://localhost:3000"))

#         song = tracker.get_slot('song')
#         artist = tracker.get_slot('artist')

#         if song:
#             sp.search(song)
#             dispatcher.utter_message(text=f"Playing the song: {song}")
#         elif artist:
#             sp.search(artist)
#             dispatcher.utter_message(text=f"Now playing music by {artist}")
#         else:
#             dispatcher.utter_message(text="Sorry, I couldn't find the song or artist.")

#         return []

# class ActionSendWhatsappMessage(Action):
#     def name(self) -> str:
#         return "action_send_whatsapp_message"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
#         # Initialize Twilio credentials (use your Twilio credentials here)
#         client = Client("ACb4d775453eb32f7d7cdc218c84fc3eaa", "18c3bb92780c7f9b88729ac17373f9b1")

#         recipient_name = tracker.get_slot('name')
#         message = tracker.get_slot('message')

#         if recipient_name and message:
#             # Send WhatsApp message (ensure the phone number is in the proper format)
#             message = client.messages.create(
#                 body=message,
#                 from_='whatsapp:+16205361348',  # Your Twilio WhatsApp number
#                 to=f'whatsapp:{recipient_name}'  # The recipient's phone number
#             )
#             dispatcher.utter_message(text=f"Message sent to {recipient_name}.")
#         else:
#             dispatcher.utter_message(text="I need both a name and a message to send.")

#         return []

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import SlotSet
# import spotipy
# import sys
# from spotipy.oauth2 import SpotifyOAuth
# from spotipy.oauth2 import SpotifyClientCredentials
# from twilio.rest import Client

# # Define custom actions
# class ActionPlaySpotify(Action):
#     def name(self) -> str:
#         return "action_play_spotify"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
#         # Initialize Spotify API credentials (use your credentials here)
#         sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="3fb1846897864809ac9694b20ae73d8b",
#                                                         client_secret="8e64d0bf253449d8b655537d01fd02b3",
#                                                         redirect_uri="http://localhost:3000"))

#         song = tracker.get_slot('song')
#         artist = tracker.get_slot('artist')

#         if song:
#             # Search for the song and play it if available
#             results = sp.search(q=song, type='track', limit=1)
#             if results['tracks']['items']:
#                 track_uri = results['tracks']['items'][0]['uri']
#                 sp.start_playback(uris=[track_uri])  # Start playback
#                 dispatcher.utter_message(text=f"Playing the song: {song}")
#             else:
#                 dispatcher.utter_message(text=f"Sorry, I couldn't find the song: {song}")
        
#         elif artist:
#             # Search for the artist and play their music
#             results = sp.search(q=artist, type='artist', limit=1)
#             if results['artists']['items']:
#                 artist_uri = results['artists']['items'][0]['uri']
#                 sp.start_playback(uris=[artist_uri])  # Start playback
#                 dispatcher.utter_message(text=f"Now playing music by {artist}")
#             else:
#                 dispatcher.utter_message(text=f"Sorry, I couldn't find music by {artist}")
        
#         else:
#             dispatcher.utter_message(text="Sorry, I couldn't find the song or artist.")

#         return []

# class ActionSendWhatsappMessage(Action):
#     def name(self) -> str:
#         return "action_send_whatsapp_message"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
#         # Initialize Twilio credentials (use your Twilio credentials here)
#         client = Client("ACb4d775453eb32f7d7cdc218c84fc3eaa", "18c3bb92780c7f9b88729ac17373f9b1")

#         recipient_name = tracker.get_slot('name')
#         message = tracker.get_slot('message')

#         if recipient_name and message:
#             # Ensure recipient_name is in the correct phone number format
#             # Example: `+1234567890` for a valid WhatsApp number
#             to_number = f'whatsapp:{recipient_name}'  # Assuming recipient_name holds the phone number

#             # Send WhatsApp message using Twilio API
#             message = client.messages.create(
#                 body=message,
#                 from_='whatsapp:+16205361348',  # Your Twilio WhatsApp number
#                 to=to_number  # The recipient's phone number in WhatsApp format
#             )

#             dispatcher.utter_message(text=f"Message sent to {recipient_name}.")
#         else:
#             dispatcher.utter_message(text="I need both a name and a message to send.")

#         return []
    
#     class ActionGreet(Action):

#         def name(self) -> str:
#             return "action_greet"

#         def run(self, dispatcher: CollectingDispatcher,
#                 tracker: Tracker,
#                 domain: dict) -> list:
#             dispatcher.utter_message(text="Hello! How can I assist you?")
#             return
import os
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from twilio.rest import Client

class ActionPlaySpotify(Action):
    def name(self) -> str:
        return "action_play_spotify"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        # Get Spotify credentials from environment variables
        client_id = os.getenv("SPOTIPY_CLIENT_ID")
        client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
        redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

        # Initialize Spotify client
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                        client_secret=client_secret,
                                                        redirect_uri=redirect_uri))

        song = tracker.get_slot('song')
        artist = tracker.get_slot('artist')

        if song:
            results = sp.search(q=song, type='track', limit=1)
            if results['tracks']['items']:
                track_uri = results['tracks']['items'][0]['uri']
                sp.start_playback(uris=[track_uri])
                dispatcher.utter_message(text=f"Playing the song: {song}")
            else:
                dispatcher.utter_message(text=f"Sorry, I couldn't find the song: {song}")
        elif artist:
            results = sp.search(q=artist, type='artist', limit=1)
            if results['artists']['items']:
                artist_uri = results['artists']['items'][0]['uri']
                sp.start_playback(uris=[artist_uri])
                dispatcher.utter_message(text=f"Now playing music by {artist}")
            else:
                dispatcher.utter_message(text=f"Sorry, I couldn't find music by {artist}")
        else:
            dispatcher.utter_message(text="Sorry, I couldn't find the song or artist.")
        return []

class ActionSendWhatsappMessage(Action):
    def name(self) -> str:
        return "action_send_whatsapp_message"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        # Get Twilio credentials from environment variables
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")

        # Initialize Twilio client
        client = Client(account_sid, auth_token)

        recipient_name = tracker.get_slot('name')
        message = tracker.get_slot('message')

        if recipient_name and message:
            to_number = f'whatsapp:{recipient_name}'  # Assuming recipient_name is a phone number
            message = client.messages.create(
                body=message,
                from_='whatsapp:+16205361348',  # Your Twilio WhatsApp number
                to=to_number
            )
            dispatcher.utter_message(text=f"Message sent to {recipient_name}.")
        else:
            dispatcher.utter_message(text="I need both a name and a message to send.")
        return []
