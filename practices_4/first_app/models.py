from django.db import models

# Create your models here.

class modelForm(models.Model):
    name = models.CharField(max_length=10)
    email_field = models.EmailField()
    auto_field = models.AutoField(primary_key=True)
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    date_field = models.DateField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    file_field = models.FileField(upload_to='files/')
    # file_path_field = models.FilePathField(path='/path/to/files/')
    float_field = models.FloatField()
    generic_ip_address_field = models.GenericIPAddressField()
    json_field = models.JSONField()
    slug_field = models.SlugField()
    time_field = models.TimeField()
    url_field = models.URLField()
    fieldsets = [
        ('Main Information', {
            'fields': ('user', 'title', 'description','slug', 'timestamp'),
            'classes': ('wide',),
            'description': 'Enter the main details of the model.',
            'collapse': True
        }),
        # ...
    ]