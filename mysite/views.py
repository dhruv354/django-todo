from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TodoList
from .serializers import TodoListSerializer

class TodoView(APIView):
    def get(self, request):
        todos = TodoList.objects.all()
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class TodoDetailView(APIView):

    def delete(self, request, pk):
        todo = TodoList.objects.get(pk=pk)
        todo.delete()
        return Response(status=204)