from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from requests import Request, post
from rest_framework import status
from rest_framework.response import Response


class AuthURL(APIView):
    def get(self, request, format=None):
        scopes = "user-read-playback-state user-modify-playback-state user-read-currently-playing"

        spotify_url = 'https://accounts.spotify.com/authorize'
        data = {
            'scope': scopes,
            'response_type': 'code',
            'redirect_uri': settings.REDIRECT_URI,
            'client_id': settings.CLIENT_ID
        }
        url = Request('GET', spotify_url, params=data).prepare().url
        return Response({'url': url}, status=status.HTTP_200_OK)
