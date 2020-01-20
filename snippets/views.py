from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import renderer_classes
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer, UserSerializer
# Create your views here.
@csrf_exempt
def snippet_list(request):
    """
    get:
        Return all snippets.
    post:
        Create a new snippet instance.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)




@csrf_exempt   #注解来标识一个视图可以被跨域访问
def snippet_detail(request, pk):
    """
    get:
        Return a snippet instance.
    put:
        Update a snippet instance.
    patch:
        Update a snippet instance.
    delete:
        Delete a snippet instance.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents code snippets.
    The `highlight` field presents a hyperlink to the highlighted HTML
    representation of the code snippet.
    The **owner** of the code snippet may update or delete instances
    of the code snippet.
    Try it yourself by logging in as one of these four users: **amy**, **max**,
    **jose** or **aziz**.  The passwords are the same as the usernames.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @renderer_classes(renderer_classes=(renderers.StaticHTMLRenderer,))
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint presents the users in the system.
    As you can see, the collection of snippet instances owned by a user are
    serialized using a hyperlinked representation.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer