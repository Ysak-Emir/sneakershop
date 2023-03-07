from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from rest_framework import status
from products.history import History
from products.models import Product
from products.serializers import ProductValidateSerializer
from rest_framework.views import APIView


class HistoryAddView(APIView):
    @require_POST
    def post(self, request, product_id):
        post = History(request)
        product = get_object_or_404(Product, id=product_id)
        serializer = ProductValidateSerializer(post, many=False)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors})
        else:
            post.add(product=product)
        return Response('сохранился')


class HistoryRemoveView(APIView):
    def delete(self, request, product_id):
        post = History(request)
        product = get_object_or_404(Product, id=product_id)
        post.remove(product)
        return Response('Удалено')


class HistoryClearView(APIView):
    def delete(self, request):
        post = History(request)
        post.clear()
        return Response('ВСЁ Удалено ')


class HistoryDetailView(APIView):
    def get(self, request):
        post = History(request)
        serializer = ProductValidateSerializer(post, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ProductsListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductValidateSerializer


class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductValidateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        title = serializer.validated_data.get('title')
        text = serializer.validated_data.get('text')
        price = serializer.validated_data.get('price')
        quantity = serializer.validated_data.get('quantity')
        size = serializer.validated_data.get('size')
        color = serializer.validated_data.get('color')
        data = Product.objects.create(self.create(ncΩΩFF))
        return Response(data={'post': data})


class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductValidateSerializer
    lookup_field = 'id'