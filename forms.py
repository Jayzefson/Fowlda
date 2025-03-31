from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CadastroForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label="Confirme a senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este e-mail já está cadastrado.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("As senhas não coincidem.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get('email')  # Usa o email como username
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()
        return user

class FeedForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['mensagem', 'avaliacao']
        labels = {
            'mensagem': '',
            'avaliacao': 'Avalie o site',
        }
        widgets = {
            'avaliacao': forms.Select(
                choices=[(i, f"{i} Estrela{'s' if i > 1 else ''}") for i in range(1, 6)]
            ),
        }

    def __init__(self, *args, **kwargs):
        super(FeedForm, self).__init__(*args, **kwargs)
        self.fields['mensagem'].label = ''


class RespostaFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['resposta']
        labels = {'resposta': 'Responder'}

class AvaliacaoFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['avaliacao']
        labels = {'avaliacao': 'Dê uma avaliação'}

class ArquivoForm(forms.ModelForm):
    class Meta:
        model = Arquivo
        fields = ['arquivo', 'chave', 'usuario']
    def __init__(self, *args, **kwargs):
        super(ArquivoForm, self).__init__(*args, **kwargs)
        self.fields['chave'].widget.attrs.update({'style': 'display:none'})
        self.fields['usuario'].widget.attrs.update({'id': 'CampoUsu', 'style': 'display:none'})
        self.fields['chave'].label = ''
        self.fields['usuario'].label = ''