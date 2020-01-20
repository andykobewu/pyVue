from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
#老式写法
# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     # 利用字段标志控制序列化器渲染到HTML页面时的的显示模板
#     code = serializers.CharField(style={'base_template': 'textarea.html'})#控制序列化器渲染到HTML页面时的的显示模板，至于为什么要这样做，是因为这对于控制如何显示可浏览的API特别有用，这将在后面的文章中看到。
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#     # 给定经过验证的数据，创建并返回一个新的 Snippet 实例
#     def create(self, validated_data):
#         return Snippet.objects.create(**validated_data)
#
#     # 给定经过验证的数据，更新并返回一个已经存在的 Snippet 实例
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance
##新式写法，rest_framework
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(queryset=Snippet.objects.all(), view_name='snippet-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'snippets')