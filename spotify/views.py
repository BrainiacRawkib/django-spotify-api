from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from requests import Request, post
from rest_framework import status
from rest_framework.response import Response


REDIRECT_URI = settings.REDIRECT_URI
CLIENT_ID = settings.CLIENT_ID
CLIENT_SECRET = settings.CLIENT_SECRET


class AuthURL(APIView):
    def get(self, request, format=None):
        scopes = "user-read-playback-state user-modify-playback-state user-read-currently-playing"

        spotify_url = 'https://accounts.spotify.com/authorize'
        data = {
            'scope': scopes,
            'response_type': 'code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID
        }
        url = Request('GET', spotify_url, params=data).prepare().url
        return Response({'url': url}, status=status.HTTP_200_OK)


def spotify_callback(request, format=None):
    code = request.GET.get('code')
    error = request.GET.get('error')
    url = 'https://accounts.spotify.com/api/token'
    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    response = post(url, data=payload).json()

    access_token = response.get('access_token')
    token_type = response.get('token_type')
    refresh_token = response.get('refresh_token')
    expires_in = response.get('expires_in')
    error = response.get('error')
