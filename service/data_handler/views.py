import pandas as pd
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import UploadedFile
from .serializers import UploadedFileSerializer

class UploadedFileViewSet(viewsets.ModelViewSet):
    queryset = UploadedFile.objects.all()
    serializer_class = UploadedFileSerializer

    @action(detail=True, methods=['get'])
    def get_columns(self, request, pk=None):
        uploaded_file = self.get_object()
        file_path = uploaded_file.file.path
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
            columns = df.columns.tolist()
            return Response(columns)
        else:
            return Response({'Ошибка': 'Поддерживаются только файлы CSV.'})

    @action(detail=True, methods=['get'])
    def get_data(self, request, pk=None):
        uploaded_file = self.get_object()
        file_path = uploaded_file.file.path
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)

            data = df.to_dict(orient='records')
            return Response(data)
        else:
            return Response({'Ошибка': 'Поддерживаются только файлы CSV.'})
