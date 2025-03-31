from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    perfil = models.BooleanField(verbose_name="Perfil do usuário", default=False)

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.CharField(max_length=100, verbose_name="E-mail")
    senha = models.CharField(max_length=100, verbose_name="Senha")
    perfil = models.BooleanField(verbose_name="Perfil do usuário", default=False)
    def __str__(self):
            return f"'Usuário:' {self.email}"
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

class Categoria(models.TextChoices):
    DOCUMENTOS = "Documentos", "Documentos"
    IMAGENS = "Imagens", "Imagens"
    PLANILHAS = "Planilhas", "Planilhas"
    VIDEOS = "Vídeos", "Vídeos"

class Formato(models.Model):
    extensao = models.CharField(max_length=10, verbose_name="Extensão")
    categoria = models.CharField(
        max_length=20,
        choices=Categoria.choices,
        verbose_name="Categoria",
        default=Categoria.DOCUMENTOS,
    )

    def __str__(self):
        return f"{self.extensao} ({self.get_categoria_display()})"

    class Meta:
        verbose_name = "Formato"
        verbose_name_plural = "Formatos"

class Arquivo(models.Model):
     arquivo = models.FileField(upload_to='app/static/files')
     tempo = models.DateTimeField(auto_now_add=True)
     chave = models.CharField(max_length=25, blank=True)
     docx_file = models.FileField(upload_to='app/static/files/docx', blank=True, null=True)
     usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario", blank=True, null=True)
     def __str__(self):
          return f"'Arquivo: {self.arquivo} "
     class Meta:
        verbose_name = "Arquivo"
        verbose_name_plural = "Arquivos"

class Feedback(models.Model):
    mensagem = models.TextField(max_length=255, verbose_name="Mensagem")
    data_feedback = models.DateTimeField(auto_now_add=True, verbose_name="Data do Feedback")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Nome do Usuário")
    resposta = models.TextField(null=True, blank=True, verbose_name="Resposta do Administrador")
    avaliacao = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Avaliação (Estrelas)")

    def __str__(self):
        return f"'O usuário '{self.usuario} ' enviou a mensagem: ' {self.mensagem}"

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"