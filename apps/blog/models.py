from django.db import models
from django.shortcuts import reverse
from django.db.models.signals import post_save


class Tags(models.Model):
    name = models.CharField(max_length=221)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=221)
    slug = models.SlugField(unique=True, max_length=221)
    description = models.TextField()
    tags = models.ManyToManyField(Tags)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def full_url(self, **kwargs):
        url = reverse('blog:blog_detail', kwargs={
            'day': self.created_date.day,
            'month': self.created_date.month,
            'year': self.created_date.year,
            'slug': self.slug
        })
        return url


class Image_blog(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/')


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=221)
    image = models.ImageField(upload_to='blog_comment', null=True, blank=True)
    message = models.TextField()
    parents_comment = models.IntegerField(blank=True, null=True)
    reply_comment = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def get_children(self):
        object_list = Comment.objects.filter(parents_comment=self.id).exclude(id=self.parents_comment)
        return object_list


def parents_post_save(instance, sender, created, *args, **kwargs):
    if created:
        parents = instance
        while parents.reply_comment:
            parents = parents.reply_comment
        instance.parents_comment = parents.id
        instance.save()
    return instance


post_save.connect(parents_post_save, sender=Comment)
