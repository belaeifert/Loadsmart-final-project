from finalProject.api.serializers import LoadSerializer
from rest_framework import generics, viewsets
from rest_framework import mixins
from rest_framework import generics
from finalProject.shipper.models import Load

class LoadViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Load.objects.all()
    serializer_class = LoadSerializer

'''
class LoadList(generics.ListCreateAPIView):
    queryset = Load.objects.all()
    serializer_class = LoadSerializer


class LoadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Load.objects.all()
    serializer_class = LoadSerializer


class LoadList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Load.objects.all()
    serializer_class = LoadSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class LoadDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Load.objects.all()
    serializer_class = LoadSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

'''

