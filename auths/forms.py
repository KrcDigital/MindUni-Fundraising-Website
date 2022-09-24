from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User



from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):  
        class Meta:  
            model = User  
            fields = ('email', 'first_name', 'last_name', 'username')





class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Kullanıcı Adı Veya E-Posta Adresi')
    password = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)


    def clean_username(self):
        username=self.cleaned_data['username']
        
        if '@' in username:
            user=User.objects.filter(email=username)
            if len(user)==1:
                user=user.first()
                return user.username

            elif len(user) > 1:
                raise forms.ValidationError('Kullanıcı Adınız İle Giriş Yapmayı Deneyin')

            else:
                raise forms.ValidationError('Kullanıcı Adı Veya E-Posta Kayıtlı Değil')

        return username            



    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Kullanıcı adını veya şifreyi yanlış girdiniz!")
        return super(LoginForm, self).clean()


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label='Kullanıcı Adı')
    email=forms.EmailField(max_length=100,label="Email")
    
    password1 = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput)
   

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            
            'email',
            
        ]

    

class UserProfileUpdateForm(forms.ModelForm):
    foto=forms.ImageField(required=False)
    bio=forms.CharField(widget=forms.Textarea,required=False)
    
    class Meta:
        model=User
        fields=['email','foto','bio',]        

    def __init__(self, *args, **kwargs):
        super(UserProfileUpdateForm,self).__init__(*args, **kwargs)    
        for field in self.fields:
            self.fields[field].widget.attrs={'class':'form-control'}
            self.fields['bio'].widget.attrs['rows']= 10