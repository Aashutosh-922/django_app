from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    due_date = models.DateField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    status_choices = (
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    )
    status = models.CharField(max_length=7, choices=status_choices, default='OPEN')

    def __str__(self):
        return self.title



# from django.db import models

# class TodoItem(models.Model):
#     STATUS_CHOICES = (
#         ('OPEN', 'Open'),
#         ('WORKING', 'Working'),
#         ('DONE', 'Done'),
#         ('OVERDUE', 'Overdue'),
#     )

#     timestamp = models.DateTimeField(auto_now_add=True)
#     title = models.CharField(max_length=100)
#     description = models.TextField(max_length=1000)
#     due_date = models.DateField(null=True, blank=True)
#     tags = models.ManyToManyField(Tag, blank=True)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OPEN')

#     def __str__(self):
#         return self.title

# class Tag(models.Model):
#     name = models.CharField(max_length=100, unique=True)

#     def __str__(self):
#         return self.name

