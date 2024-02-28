# company/views.py
from rest_framework import viewsets
from .models import Company
from .serializers import CompanySerializer
from rest_framework.response import Response
from rest_framework import status


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # You can add custom logic here before or after deletion
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
