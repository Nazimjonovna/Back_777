from rest_framework.views import APIView
from rest_framework.response import Response
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

    @swagger_auto_schema(request_body=UserSerializer)
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

        pass







































