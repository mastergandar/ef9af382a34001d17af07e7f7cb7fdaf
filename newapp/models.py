from django.db import models

# Create your models here.


class Test(models.Model):
    GraphId = models.AutoField('ID', primary_key=True, null=False)
    GraphImage = models.ImageField('График', upload_to='func_folder/', null=True)
    GraphImageEx = models.TextField('Exception', null=True)
    GraphFunction = models.CharField('Функция', max_length=255)
    GraphFuncId = models.CharField('TaskId', max_length=255, default='')
    GraphInterval = models.IntegerField('глубина периода моделирования в днях')
    GraphDt = models.IntegerField('Шаг в часах')
    GraphDateTime = models.DateTimeField('Дата', null=True, blank=True)

    def __int__(self):
        return self.GraphId
