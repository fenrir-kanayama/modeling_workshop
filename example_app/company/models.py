from django.db import models

# ここから下に貼り付けてください
class Type(models.Model):
    no = models.IntegerField('番号', blank=False, primary_key=True)
    name = models.CharField('タイプ名', blank=True, primary_key=False, max_length=255)
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name="タイプ"
        verbose_name_plural="タイプ"

class Pokemon(models.Model):
    typeId = models.ForeignKey(Type, verbose_name='タイプ', on_delete=models.CASCADE, blank=False, null=False)
    no = models.IntegerField('図鑑番号', blank=False, primary_key=True)
    name = models.CharField('名前', blank=False, primary_key=False, max_length=255)
    def __str__(self):
        return f'{self.typeId}/{self.name}'
    class Meta:
        verbose_name="ポケモン"
        verbose_name_plural="ポケモン"

