from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=100, default='Nutri Amorim')  # Título do post
    content = models.TextField()  # Conteúdo do post (pode ser o texto ou descrição)
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação do post
    updated_at = models.DateTimeField(auto_now=True)  # Data da última atualização

    def __str__(self):
        return self.title

