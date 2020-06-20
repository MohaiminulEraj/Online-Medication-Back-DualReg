from django.db import models
from users.models import RegDoctor, RegPatient


class PostedArticle(models.Model):
    title = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='myfile', default='default.jpg')
    causes = models.TextField(blank=True)
    stages = models.TextField(blank=True)
    image2 = models.ImageField(upload_to='myfile2', default='default.jpg')
    consequences = models.TextField(blank=True)
    remedies_and_treatment = models.TextField(blank=True)
    image3 = models.ImageField(upload_to='myfile3', default='default.jpg')
    question_and_answer = models.TextField(blank=True)
    prevention = models.TextField(blank=True)
    adverse = models.TextField(blank=True)
    side_effect = models.TextField(blank=True)
    diagnosis = models.CharField(max_length=100)
    symptomps = models.CharField(max_length=100)
    # user_id = models.ForeignKey(RegDoctor, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=100)
    doc_user_id = models.CharField(max_length=100)
    ref_link = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} {self.topic}"
