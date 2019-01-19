from django.forms import ModelForm
from django.contrib.auth import get_user_model
User = get_user_model()


class UserForm(ModelForm):
	class Meta():
		model = User
		fields = ['username', 'email', 'password']