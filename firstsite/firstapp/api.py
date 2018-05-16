from firstapp.models import Blog
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from firstapp.coreweb import Pager



class BlogSerializer(serializers.ModelSerializer):
	class Meta:
		model = Blog
		fields = "__all__"

class PageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pager
		fields = "__all__"


@api_view(["GET"])
def blogs(request,cate = None):
	if cate =="editors":
		blogs = Blog.objects.filter(editors_choice = True)
		blogs_count = len(blogs)
	elif cate == "news":
		blogs = Blog.objects.filter(news_choice = True)
		blogs_count = len(blogs)
	else:
		blogs_count = Blog.objects.count()
	context = {}
	page_index = int(request.GET.get("page",1))
	print(page_index)
	page = Pager(blogs_count,page_index)
	if cate =="editors":
		blogs = blogs[page.offset:page.limit]
	elif cate == "news":
		blogs = blogs[page.offset:page.limit]
	else:
		blogs = Blog.objects.all()[page.offset:page.limit]
	print("blogs===================>",blogs)
	serializer = BlogSerializer(blogs, many = True)
	print("This is api blogs")
	return Response(serializer.data)
