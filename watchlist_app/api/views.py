
from rest_framework.views import APIView
from .serializers import WatchListSerializer,StreamPlatformSerializer
from rest_framework.response import Response
from rest_framework import status
from ..models import WatchList,StreamPlatform


class StreamPlatformAV(APIView):
    def get(self,request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform,many=True,context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StreamPlatformDetailAV(APIView):

    def get(self, request,pk):
        try:
            movie = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error':'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(movie)
        return Response(serializer.data)


    def put(self, request,pk):
        try:
            movie = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error':'Movie does not exists'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request,pk):
        try:
            movie = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error':'Movie does not exists'}, status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WatchListAV(APIView):

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class WatchDetailAV(APIView):

    def get(self, request,pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error':'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)


    def put(self, request,pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error':'Movie does not exists'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request,pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error':'Movie does not exists'}, status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)












# before apiview (5. serializers requests and status code)

# from ..models import Movie
# from .serializers import MovieSerializer
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':    
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies,many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

# @api_view(['GET','PUT','DELETE'])
# def movie_detail(request,pk):
#     if request.method == 'GET':     
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error':'Movie does not exists'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error':'Movie does not exists'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

#     if request.method == 'DELETE':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error':'Movie does not exists'}, status=status.HTTP_404_NOT_FOUND)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)







# befor django restframwork.(3. API With Django)

# from django.shortcuts import render
# from ..models import Movie
# from django.http import JsonResponse

# def movie_list(request):
#     movies = Movie.objects.all()
#     print(list(movies.values()))
#     data = {'movies':list(movies.values())}
#     return JsonResponse(data)

# def movie_detail(request,pk):
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         'name':movie.name,
#         'description':movie.description,
#         'active':movie.active
#     }
#     return JsonResponse(data)