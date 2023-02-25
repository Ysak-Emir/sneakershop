from rest_framework import serializers
from orders.models import Order, OrderItem, Payment, Product



class ProductSerializer(serializers.ModelSerializer):
    slug = serializers.HiddenField(default='')

    class Meta:
        model = Product
        fields = (
            'name', 'slug', 'image', 'description', 'price', 'categories', 'subcategories', 'available', 'discount')



class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "id card_number date cvc_code".split()




class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "id user first_name last_name phone_number city street_name street_type zip_code house status".split()

        def create(self, validate_data):
            return Order.objects.create(**validate_data)


class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializers()
    cost = serializers.SerializerMethodField()
    class Meta:
        model = OrderItem
        fields = "id order product quantity cost".split()

    def get_cost(self, cost):
        return cost.get_cost()








