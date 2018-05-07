from django import forms
from django.forms import widgets,fields




class LoginForm(forms.Form):
	user_name = forms.CharField(
		required = True,
		widget = widgets.TextInput(attrs={"class":"form-control","placeholder":"Please enter user name"}),
		min_length = 5,
		max_length = 16,
		strip = True,
		error_messages = {"required":"user name can not be empty"}
		)
	pass_word = forms.CharField(
		required = True,
		widget = widgets.PasswordInput(attrs={"class":"form-control","placeholder":"Please enter password"}),
		min_length = 5,
		max_length = 16,
		strip = True,
		error_messages = {"required":"password can not be empty"}
		)


class RegistForm(forms.Form):
	user_name = forms.CharField(
		required = True,
		widget = widgets.TextInput(attrs={"class":"form-control","placeholder":"Please enter user name"}),
		min_length = 5,
		max_length = 16,
		strip = True,
		error_messages = {"required":"user name can not be empty"}
		)
	pass_word = forms.CharField(
		required = True,
		widget = widgets.PasswordInput(attrs={"class":"form-control","placeholder":"Please enter password"}),
		min_length = 5,
		max_length = 16,
		strip = True,
		error_messages = {"required":"password can not be empty"}
		)
	email = forms.CharField(
		required = True,
		widget = widgets.TextInput(attrs={"class":"form-control","placeholder":"Please enter email"}),
		min_length = 5,
		max_length = 16,
		strip = True,
		error_messages = {"required":"email can not be empty"}
	)


class CommentForm(forms.Form):
	comment = forms.CharField(
		required = True,
		widget = widgets.Textarea(attrs={"class":"form-control","palceholder":"Please enter your comment"}),
		min_length = 10,
		error_messages = {"required":"comment can not be empty"},
		strip = True
		)


class BlogForm(forms.Form):
	blog_name = forms.CharField(
		required = True,
		min_length = 1,
		error_messages = {"required":"comment can not be empty"},
		strip = True
		)
	blog_summary = forms.CharField(
		required = True,
		widget = widgets.Textarea(attrs = {"class":"form-control"}),
		min_length = 5,
		error_messages = {"required":"comment can not be empty"},
		strip = True
		)
	blog_content = forms.CharField(
		required = True,
		widget = widgets.Textarea(attrs = {"class":"form-control"}),
		min_length = 5,
		error_messages = {"required":"comment can not be empty"},
		strip = True
		)
	news = forms.CharField(
	    required = False,
	    widget = widgets.CheckboxInput(attrs = {"class":"form-control","value":"news"})
       )
	editors = forms.CharField(
	    required = False,
	    widget = widgets.CheckboxInput(attrs = {"value":"editors"})
       )

class TestForm(forms.Form):
	comment = fields.CharField(
		required = True,
		min_length = 2,
		error_messages = {"required":"comment can not be empty","invalid":"长度不够"},
		strip = True
		)
