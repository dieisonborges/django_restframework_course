from tabnanny import verbose
from django.db import models

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Course(Base):
    title = models.CharField(verbose_name='Título', max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['id']

    def __str__(self):
        return self.title

class Evaluation(Base):
    course = models.ForeignKey(Course, verbose_name='Curso', related_name='evaluation', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Nome', max_length=255)
    email = models.EmailField()
    comment = models.TextField(verbose_name='Comentário', blank=True, default='')
    score = models.DecimalField(verbose_name='Avaliação', max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['email', 'course']

    def __str__(self):
        return f'{self.name} avaliou o curso {self.course} com nota {self.score}'
