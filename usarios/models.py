from django.db import models
class ErrModel(models.Model):
    lang_name = models.CharField(max_length=240, blank=False, null=False)
    err_title = models.CharField(max_length=240, blank=False, null=False)
    fixer_code = models.CharField(max_length=3000, blank=False, null=False)
    os_tech = models.CharField(max_length=240,blank=False, null=False)  
    class Meta:
     db_table = "errmodel" 
    def __str__(self):
        """A human readible representation of user object"""
        return "{0} {1} {2} {3}".format(self.lang_name, self.err_title, self.fixer_code, self.os_tech)
    
