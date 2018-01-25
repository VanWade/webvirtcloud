from django.db import models
from computes.models import Compute


# class Instance(models.Model):
#     compute = models.ForeignKey(Compute)
#     name = models.CharField(max_length=20)
#     uuid = models.CharField(max_length=36)
#     is_template = models.BooleanField(default=False)
#
#     def __unicode__(self):
#         return self.name


class Instance(models.Model):
    compute = models.ForeignKey(Compute)
    name = models.CharField(max_length=32)
    status = models.IntegerField(default=0)
    vcpu = models.IntegerField(default=4)
    memory = models.IntegerField(default=512)
    description = models.CharField(max_length=64, default='')
    title = models.CharField(max_length=32, default='')
    uuid = models.CharField(max_length=36)

    def __unicode__(self):
        return self.name

    class Meta:
        # unique index
        unique_together = ("name", "compute")
        index_together = ("name", "compute")
