from django.db import models

from redactor.fields import RedactorField
from taggit.managers import TaggableManager

import datetime

# The blog post model
class Post(models.Model):
	title = models.CharField(max_length=100, blank=True, default="No Title")
	text = RedactorField(
		redactor_options={
		'autosave': '/blog/admincontent/saved/',
		'autosaveName': 'blog-text',
		'focus': True
		},
		upload_to='blog',
		allow_file_upload=True,
		allow_image_upload=True)
	created_time = models.DateTimeField(default=datetime.datetime.now)
	last_modified_time = models.DateTimeField(null=True, blank=True, default=None)
	published = models.BooleanField(default=False)
	category = models.ForeignKey(
		'Category',
		blank=True,
		null=True,
		default=None,
		)
	slug = models.SlugField(allow_unicode=True, blank=True, null=True)
	tags = TaggableManager(blank=True)

	class Meta:
		ordering = ['-created_time']

	def __str__(__self__):
		return __self__.title

	def created_timestamp(__self__):
		return __self__.created_time.strftime('%I:%M %p, %A %B %-m, %Y')

	def modified(__self__):
		if __self__.last_modified_time:
			return True
		else:
			return False

	def modified_timestamp(__self__):
		return __self__.last_modified_time.strftime('%I:%M %p, %A %B %-m, %Y')

# Post category
class Category(models.Model):
	name = models.CharField(max_length=30)

	class Meta:
		verbose_name_plural = 'categories'

	def __str__(__self__):
		return __self__.name

# Files associated with blog posts
# http://paltman.com/how-to-setup-upload-handler-for-redactor/
class File(models.Model):
	upload = models.FileField(upload_to='%Y/%m/%d')
	created_time = models.DateTimeField(default=datetime.datetime.now)
	is_image = models.BooleanField(default=True)