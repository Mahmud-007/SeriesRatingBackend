from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .models import *
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import *
from django.contrib.auth.models import User
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=True,methods=['POST'])
    def rate_series(self,request,pk=None):
        if 'stars' in request.data:
            series=Series.objects.get(id=pk)
            stars=request.data['stars']
            user=request.user
            try:
                rating=Rating.objects.get(user=user.id,series=series.id)
                rating.stars=stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'rating updated','result':serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating=Rating.objects.create(user=user,series=series,stars=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'rating created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response={'message':'need to provide stars'}
            return Response (response,status=status.HTTP_400_BAD_REQUEST)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        response = {'message': 'You cant update rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': 'You cant create rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)