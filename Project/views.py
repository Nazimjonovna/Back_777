from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from .serializer import *
from .models import *
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class UserRegister(APIView):

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        serializers = UserSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            user = serializers.data
            access = AccessToken.for_user(user)
            refresh = RefreshToken.for_user(user)
            return Response({
                "user":serializers.data,
                "access":str(access),
                "refresh":str(refresh)
            })
        else:
            return Response(serializers.errors)


class LoginView(APIView):

    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        ism = request.data.get('ism')
        phone = request.data.get('phone')
        user = User.objects.filter(ism = ism, phone = phone)
        if user.exists():
            access = AccessToken.for_user(user)
            refresh = RefreshToken.for_user(user)
            serializers = UserSerializer(user)
            return Response({
                "user":serializers.data,
                'access':str(access),
                "refresh":str(refresh)
            })

class EditPasswordAdminView(APIView):
    def patch(self, request, pk):
        user = User.objects.filter(id = pk).first()
        if user:
            user.ism = request.data.get('ism')
            user.save()
            serializers = UserSerializer(user, partial=True)
            return Response(serializers.data)
        else:
            return Response('Bunday user yo')


class DeleteUserView(APIView):

    def delete(self, request, pk):
        user = User.objects.filter(id = pk).first()
        if user:
            user.delete()
            return Response("Malades o'chdi")
        else:
            return Response("bunday user yo")

class AddProduct(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        serializers = AddProductSRL(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)


class GetProductView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request, pk):
        admin = Admin.objects.filter(id =pk).first()
        if admin:
            product = Product.objects.filter(admin = admin.id)
            serializers = AddProductSRL(product, many=True)
            serializer = AdminSRL(admin, many=True)
            return Response({
                "admin":serializer.data,
                "products":serializers.data
            })
        else:
            return Response("Bunday admin yo")


class BossAdminView(APIView):

    def get(self, request, id):
        s = 0
        result = {}
        admin = Admin.objects.filter(id = id).first()
        if admin.is_boss == True:
            admins = Admin.objects.all()
            for admin in admins:
                products = Product.objects.filter(admin = admin.id)
                for product in products:
                    s += 1
                    result[f'{admin.username}'] = s
            return Response(result)
        else:
            return Response("Sizga bunday malumotlar taqdim etilmaydi")





























