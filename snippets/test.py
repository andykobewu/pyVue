from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
snippet = Snippet(code='foo = "bar"\n')
snippet.save()
snippet = Snippet(code='print "hello, world"\n')
snippet.save()
##以上代码在python manage.py shell中运行

##查看结果,并查看：
serializer = SnippetSerializer(snippet)
serializer.data

#将数据渲染成json格式,并查看：
content = JSONRenderer().render(serializer.data)
content

#检查并保存数据
serializer = SnippetSerializer(data=data)
serializer.is_valid()

serializer.validated_data
serializer.save()
#我们可以通过在shell中的打印来检查序列化器实例中的所有字段：
from snippets.serializers import SnippetSerializer
serializer = SnippetSerializer()
print(repr(serializer)) #repr() 函数将对象转化为供解释器读取的形式