from django import forms
from .models import Escort


LOCATION_CHOICES = (
	('Nairobi CBD', 'Nairobi CBD'),
	('Eastern Bypass', 'Eastern Bypass'),
	('Eastlands', 'Eastlands'),
	('Jogoo Road', 'Jogoo Road'),
	('Kamiti Road', 'Kamiti Road'),
	('Kangudo Road', 'Kangudo Road'),
	('Langata Road', 'Langata Road'),
	('Manyanja Road', 'Manyanja Road'),
	('Mbagathi Way', 'Mbagathi Way'),
	('Ngong Road', 'Ngong Road'),
	('Mombasa Road', 'Mombasa Road'),
	('Naivasha Road', 'Naivasha Road'),
	('Outering Road', 'Outering Road'),
	('Thika Road', 'Thika Road'),
	('Waiyaki Way', 'Waiyaki Way'),
	('Athi River', 'Athi River'),
	('Allsops', 'Allsops'),
	('Buruburu', 'Buruburu'),
	('Donholm', 'Donholm'),
	('Embakasi', 'Embakasi'),
	('Eastleigh', 'Eastleigh'),
	('Githurai', 'Githurai'),
	('Homeland', 'Homeland'),
	('Hurlingham', 'Hurlingham'),
	('Imara Daima', 'Imara Daima'),
	('Kasarani', 'Kasarani'),
	('Juja', 'Juja'),
	('Karen', 'Karen'),
	('Kabete', 'Kabete'),
	('Kahawa Wendani', 'Kahawa Wendani'),
	('Kahawa West', 'Kahawa West'),
	('Kahawa Sukari', 'Kahawa Sukari'),
	('Kayole', 'Kayole'),
	('Kawangware', 'Kawangware'),
	('Kileleshwa', 'Kileleshwa'),
	('Kilimani', 'Kilimani'),
	('Kiambu', 'Kiambu'),
	('Kikuyu Town', 'Kikuyu Town'),
	('Kitengela', 'Kitengela'),
	('Langata', 'Langata'),
	('Madaraka', 'Madaraka'),
	('Milimani', 'Milimani'),
	('Mlolongo', 'Mlolongo'),
	('Muthaiga', 'Muthaiga'),
	('Mwiki', 'Mwiki'),
	('Nairobi West', 'Nairobi West'),
	('Eastleigh', 'Eastleigh'),
	('Lavington', 'Lavington'),
	('Ngara', 'Ngara'),
	('Pangani', 'Pangani'),
	('Parklands', 'Parklands'),
	('Ruaka', 'Ruaka'),
	('Ruiru', 'Ruiru'),
	('Rongai', 'Rongai'),
	('Roysambu', 'Roysambu'),
	('Ruai', 'Ruai'),
	('Runda', 'Runda'),
	('South C', 'South C'),
	('South B', 'South B'),
	('Syokimau', 'Syokimau'),
	('Thome', 'Thome'),
	('Umoja', 'Umoja'),
	('Upper Hill', 'Upper Hill'),
	('Utawala', 'Utawala'),
	('Westlands', 'Westlands'),
	('Yaya', 'Yaya'),
	('Bungoma', 'Bungoma'),
	('Diani', 'Diani'),
	('Eldoret', 'Eldoret'),
	('Emali', 'Emali'),
	('Embu', 'Embu'),
	('Isiolo', 'Isiolo'),
	('Kericho', 'Kericho'),
	('Kakamega', 'Kakamega'),
	('Karatina', 'Karatina'),
	('Kilifi', 'Kilifi'),
	('Kirinyaga', 'Kirinyaga'),
	('Kisumu', 'Kisumu'),
	('Kitale', 'Kitale'),
	('Kisii', 'Kisii'),
	('Limuru', 'Limuru'),
	('Lodwar', 'Lodwar'),
	('Loitoktok', 'Loitoktok'),
	('Machakos', 'Machakos'),
	('Mai Mahiu', 'Mai Mahiu'),
	('Malindi', 'Malindi'),
	('Meru', 'Meru'),
	('Naivasha', 'Naivasha'),
	('Mombasa', 'Mombasa'),
	('Nakuru', 'Nakuru'),
	('Nanyuki', 'Nanyuki'),
	('Nyahururu', 'Nyahururu'),
	('Nyeri', 'Nyeri'),
	('Thika', 'Thika'),
	('Voi', 'Voi'),
)


ORIENTATION_CHOICES = (
	('Straight', 'Straight'),
	('Homosexual', 'Homosexual'),
	('Bisexual', 'Bisexual'),
)


ETHNICITY_CHOICES = (
	('Kenyan', 'Kenyan'),
	('Somali', 'Somali'),
	('Tanzanian', 'Tanzanian'),
	('Ugandan', 'Ugandan'),
	('Rwandese', 'Rwandese'),
	('American', 'American'),
	('European', 'European'),
	('Australian', 'Australian'),
)


SKIN_COLOR_CHOICES = (
	('Light Skin', 'Light Skin'),
	('Chocolate', 'Chocolate'),
	('Dark Skin', 'Dark Skin'),
)


HAIR_COLOR_CHOICES = (
	('Black', 'Black'),
	('Blonde', 'Blonde'),
	('Brunette', 'Brunette'),
	('Red', 'Red'),
)

class EscortForm(forms.ModelForm):
	class Meta:
		model = Escort
		fields = ('profile_pic', 'Image1', 'Image2', 'Image3', 'author', 'name', 'age', 'phone', 'ethnicity', 'orientation', 'location', 'area', 'skin_color', 'hair_color', 'services', 'membership', 'about_me')

		widgets = {
			'profile_pic': forms.ClearableFileInput(attrs={'class': 'form-control'}),
			'Image1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
			'Image2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
			'Image3': forms.ClearableFileInput(attrs={'class': 'form-control'}),
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
			'age': forms.TextInput(attrs={'class': 'form-control'}),
			'about_me': forms.Textarea(attrs={'class':'form-control'}),
			'phone': forms.TextInput(attrs={'class':'form-control'}),
			'ethnicity': forms.Select(choices=ETHNICITY_CHOICES, attrs={'class':'form-control'}),
			'orientation': forms.Select(choices=ORIENTATION_CHOICES, attrs={'class':'form-control'}),
			'location': forms.Select(choices=LOCATION_CHOICES, attrs={'class':'form-control'}),
			'area': forms.TextInput(attrs={'class':'form-control'}),
			'skin_color': forms.Select(choices=SKIN_COLOR_CHOICES, attrs={'class':'form-control'}),
			'hair_color': forms.Select(choices=HAIR_COLOR_CHOICES, attrs={'class':'form-control'}),
			'services': forms.Textarea(attrs={'class':'form-control',}),
			'membership': forms.Select(attrs={'class':'form-control'}),
			'created_at': forms.DateInput(attrs={'class':'form-control'}),

		}


class EditEscortForm(forms.ModelForm):
	class Meta:
		model = Escort
		fields = ('profile_pic', 'Image1', 'Image2', 'Image3', 'author', 'name', 'age', 'phone', 'ethnicity', 'orientation', 'location', 'area', 'skin_color', 'hair_color', 'services', 'about_me')

		widgets = {
			'profile_pic': forms.ClearableFileInput(attrs={'class': 'form-control'}),
			'Image1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
			'Image2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
			'Image3': forms.ClearableFileInput(attrs={'class': 'form-control'}),
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
			'age': forms.TextInput(attrs={'class': 'form-control'}),
			'about_me': forms.Textarea(attrs={'class':'form-control'}),
			'phone': forms.TextInput(attrs={'class':'form-control'}),
			'ethnicity': forms.Select(choices=ETHNICITY_CHOICES, attrs={'class':'form-control'}),
			'orientation': forms.Select(choices=ORIENTATION_CHOICES, attrs={'class':'form-control'}),
			'location': forms.Select(choices=LOCATION_CHOICES, attrs={'class':'form-control'}),
			'area': forms.TextInput(attrs={'class':'form-control'}),
			'skin_color': forms.Select(choices=SKIN_COLOR_CHOICES, attrs={'class':'form-control'}),
			'hair_color': forms.Select(choices=HAIR_COLOR_CHOICES, attrs={'class':'form-control'}),
			'services': forms.Textarea(attrs={'class':'form-control',}),
			'created_at': forms.DateInput(attrs={'class':'form-control'}),

		}