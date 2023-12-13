from django import forms

class AutorizeForm(forms.Form):
    email = forms.EmailField(
        label="Введите Email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-input',
                'placeholder': 'ivanov_ivan@mail.ru',
            }
        )
    )


    password = forms.CharField(
        label="Введите Пароль",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-input',
                'placeholder': 'Password',
            }
        )
    )




class RegisterForm(forms.Form):

    name = forms.CharField(
            label="Введите Имя",
            widget=forms.TextInput(
                attrs={
                    'class':'form-input',
                    'placeholder': 'Иван',
                }
            )
        )




    email = forms.EmailField(
        label="Введите Email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-input',
                'placeholder': 'ivanov_ivan@mail.ru',
            }
        )
    )


    password = forms.CharField(
        label="Введите Пароль",
        widget=forms.PasswordInput(
            attrs={
                'class':'form-input',
                'placeholder': 'Password',
            }
        )
    )