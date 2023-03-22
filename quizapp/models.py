from django.db import models

class QuizCategory(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()
    image = models.ImageField(upload_to="cat_image/")

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.title


class QuizQuestion(models.Model):
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    question=models.TextField()
    opt_1=models.CharField(max_length=255)
    opt_2=models.CharField(max_length=255)
    opt_3=models.CharField(max_length=255)
    opt_4=models.CharField(max_length=255)
    level=models.CharField(max_length=255)
    time_limit=models.IntegerField()
    right_opt=models.CharField(max_length=255)


    class Meta:
        verbose_name_plural='Questions'


    def __str__(self):
        return self.question

