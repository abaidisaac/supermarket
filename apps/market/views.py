from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerial
from .models import Product
from django.contrib.auth.models import User
from django.shortcuts import render


@api_view(['GET'])
def get(request):
    if request.method == 'GET':
        model = Product.objects.filter(user=request.user.id)
        serializer = ProductSerial(model, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def post(request):
    if request.method == 'POST':
        data = {'user': request.user.id, 'title': request.data.get('title'),
                'quantity': request.data.get('quantity')}
        serializer = ProductSerial(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data['id'], status=200)
        return Response(serializer.data.error, status=200)


@api_view(['PUT'])
def update(request, id):
    if request.method == 'PUT':
        data = request.data
        product = Product.objects.get(id=id)
        serializer = ProductSerial(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete(request, id):
    if request.method == 'DELETE':
        product = Product.objects.get(id=id)
        product.delete()
        return Response(status=200)


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            usernames = User.objects.get(username=username)
            return Response(status=200)
        except:
            user = User.objects.create_user(
                username=username, password=password)
            user.save()
        return Response(status=200)


def home(request):
    return render(request, 'index.html')


def market(request):
    return render(request, 'market.html')
