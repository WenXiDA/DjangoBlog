from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms
from firstapp.models import Blog, User,Comment
from firstapp import my_form
from django.core.exceptions import ValidationError
import logging;logging.basicConfig(level=logging.INFO)
from django.contrib.auth.decorators import login_required
# Create your views here.

def path_to_session(func):
	def wrapper(*args,**kw):
		# print(args[0].path)
		if args[0].session.get("url"):
			print(args[0].session["url"])
			del args[0].session["url"]
		args[0].session["url"] = args[0].path
		print(args[0].session["url"])
		print(args[0].path)
		return func(*args,**kw)
	return wrapper


@path_to_session
def blogs(request):
	# try:
	# 	user_name = request.session["user"]
	# 	user = User.objects.filter(name=user_name).first()
	# except KeyError:
	# 	user = None
	context = {}
	blogs = Blog.objects.all()
	context["blogs"] = blogs
	# context["user"] = user
	return render(request, "blogs.html", context)

@path_to_session
def blog(request,name):
	logging.info("belong blog--->",name)
	blog = Blog.objects.get(name = name)
	form = discuss(request,blog)
	if isinstance(form,forms.Form):
		return render(request, "blog.html", {"blog":blog,"form":form})
	else:
		return form


def regist(request):
	request.session.clear()
	user = None
	if request.method == "GET":
		form = my_form.RegistForm
	if request.method == "POST":
		form = my_form.RegistForm(request.POST)
		if form.is_valid():
			user_name = form.cleaned_data["user_name"]
			pass_word = form.cleaned_data["pass_word"]
			email = form.cleaned_data["email"]
			user = User(name = user_name, passwd = pass_word, email = email)
			user.save()
			request.session["is_login"] = True
			request.session["user"] = user_name
			return redirect(to=request.session["url"]) if request.session.get("url") else redirect(to="blogs")
	context = {}
	context["form"] = form
	context["user"] = user
	return render(request,"regist.html",context)


def login(request):
	request.session.clear()
	if request.method == "GET":
		form = my_form.LoginForm
	if request.method == "POST":
		form = my_form.LoginForm(request.POST)
		if form.is_valid():
			user_name = form.cleaned_data["user_name"]
			pass_word = form.cleaned_data["pass_word"]
			user = User.objects.filter(name=user_name).first()
			if user:
				if user.name == user_name and user.passwd == pass_word:
					request.session["is_login"] = True
					request.session["user"] = user_name
					return redirect(to=request.session["url"]) if request.session.get("url") else redirect(to="blogs")
				else:
					form.errors["用户名和密码错误"] = ""
		else:
			errors = form.errors
			logging.info("form-->",form)
			logging.info("form.errors--->",form.errors)
			logging.info("errors--->",form.errors)

	context = {}
	context["form"] = form
	context["user"] = None
	return render(request,"login.html",context)


def logout(request):
	# print("request.session.__dict__------------------>",request.session.__dict__)
	print("request.session['url']------------------>",request.session.get("url"))
	try:
		del request.session["is_login"]
		del request.session["user"]
	except KeyError:
		pass
	return redirect(to=request.session["url"]) if request.session.get("url") else redirect(to="blogs")


def discuss(request,belong):
	if request.method == "GET":
		form = my_form.CommentForm()
	if request.method == "POST":
		form = my_form.CommentForm(request.POST)
		print("belong--->",belong)
		if form.is_valid():
			user_name = request.session.get("user")
			if user_name:
				content = form.cleaned_data["comment"]
				comment = Comment(user_name = user_name,belong = belong, comment = content)
				comment.save()
				return redirect(to="blog",name=belong.name)
			else:
				print(isinstance(form.errors,list))
				form.errors["未登录"] = ",请先登录在评论"
				print("errors--->",form.errors)
	print("form--->",form)
	return form


def myblogs(request):
	user_name = request.session.get("user")
	if user_name:
		context = {}
		user = User.objects.get(name=user_name)
		blogs = user.under_blog.all
		context["blogs"] = blogs
		return render(request, "myblogs.html", context)
	else:
		return redirect(to="login")


def myblog(request,name):
	user_name = request.session.get("user")
	print("belong blog--->",user_name)
	if user_name:
		print("belong blog--->",name)
		try:
			blog = Blog.objects.get(name = name)
			print("myblog------------->blog:",blog)
			form = discuss(request,blog)
			if isinstance(form,forms.Form):
				return render(request, "blog.html", {"blog":blog,"form":form})
			else:
				return form
		except:
			raise
	else:
		return redirect(to="login")


def myblog_del(request,name):
	if request.session.get("user"):
		blog = Blog.objects.get(name = name)
		blog.delete()
		print("delete ok")
		return redirect(to="myblogs")
	else:
		return redirect(to="login")


def myblog_edit(request,blog_name = None):
	user = request.session.get("user")
	if user:
		if blog_name:
			blog = Blog.objects.get(name = blog_name)
			if request.method == "GET":
				form = my_form.BlogForm({"blog_name":blog.name,"blog_summary":blog.summary,"blog_content":blog.content})
				print(dir(form))
				print("myblog_edit________________>",form)
			if request.method == "POST":
				form = my_form.BlogForm(request.POST)
				if request.session.get("user") and form.is_valid():
					data = form.cleaned_data
					blog.name = data["blog_name"]
					blog.summary = data["blog_summary"]
					blog.content = data["blog_content"]
					print("===="*30)
					blog.save()
					return redirect(to="myblog",name = blog.name)
				else:
					return redirect(to="login")
		else:
			if request.method == "GET":
				form = my_form.BlogForm
			if request.method == "POST":
				form = my_form.BlogForm(request.POST)
				if request.session.get("user") and form.is_valid():
					data = form.cleaned_data
					blog = Blog(
						user_name = User.objects.get(name = user),
						name =data["blog_name"],
						summary = data["blog_summary"],
						content = data["blog_content"]
						)
					blog.save()
					return redirect(to="myblog",name = blog.name)
				else:
					return redirect(to="login")
		return render(request, "myblog_edit.html", {"form":form})
	else:
		return redirect(to="login")
















def test(request):
	if request.method == "GET":
		form = my_form.TestForm
		print("form get--->",form)
	if request.method == "POST":
		form = my_form.TestForm(request.POST)
		print("form post--->",form)
		print("form.is_valid()--->",form.is_valid())
		if form.is_valid():
			contnet = form.cleaned_data["comment"]
			return redirect(to="test")
		print("form--->",form)
		print("form errors--->",form.errors)
	return render(request,"test.html",{"form":form})