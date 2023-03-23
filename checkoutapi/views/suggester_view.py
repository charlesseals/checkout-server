from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from checkoutapi.models import OpenaiSuggestion
from rest_framework import serializers, status
from django.shortcuts import render
import openai, os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)
openai.api_key = api_key

class SuggesterView(ViewSet):

    def create(self, request):

        # chatbot_response = None
        response = None

        if api_key is not None and request.method =='POST':
            user_input = request.data.get('user_input')
            prompt = f"if the question is related to improving the performance of an airbnb or rental property - answer it: {user_input}, else say: CAN'T ANSWER THIS"

            response = openai.Completion.create(
                engine = 'text-davinci-003',
                prompt = prompt,
                max_tokens = 256,
                # stop = "."
                temperature = 0.5
            )
            print(response)
            chatbot_response = response["choices"][0]["text"]
            # serializer = SuggesterSerializer(response)
            return Response({"response": chatbot_response}, status=status.HTTP_201_CREATED)

        #     return render(request, 'main.html', {})
        # # Return a 400 Bad Request response if the API key is not defined
        return Response({'error': 'API key not defined'}, status=status.HTTP_400_BAD_REQUEST)
    

