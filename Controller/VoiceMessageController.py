
from starlette.endpoints import HTTPEndpoint
from twilio.twiml.voice_response import VoiceResponse


class VoiceMessageController(HTTPEndpoint):

    async def post(self, request):
        intent = request.form.get("intent", "").lower()

        if intent == "greet":
            response = "Hello! How can I assist you?"
        elif intent == "weather":
            location = request.form.get("location")
            # Your code to fetch and return the weather information for the specified location
            response = f"The weather in {location} is sunny."
        else:
            response = "Sorry, I didn't understand that command."

        return VoiceResponse().say(response)

    # Add more intent handlers as needed for other commands
