
from .models import User
from .serializers import UserActivitySerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class UserActivityViewSet(APIView):

    def get(self,request,format = None):
        queryset = User.objects.all()
        Serializer = UserActivitySerializer(queryset,many=True)
        return Response({"members":Serializer.data})
