from django.db import models

from django.contrib.localflavor.us.models import USStateField

# Create your models here.

class Manager(models.Model):
  """
  A manager of a given RegionalCenter or BusinessToBuy.
  """
  name = models.CharField(max_length=30)

class SocialProfile(models.Model):
  """
  A Twitter/Linkedin/Facebook profile
  """
  url = models.URLField()
  manager = models.ForeignKey(Manager)

class RegionalCenter(models.Model):
  """
  Regional centers that are looking for new applications.
  """
  name = models.CharField(max_length=100)
  state = USStateField()
  url = models.URLField(blank=True)
  money_to_raise = models.CharField(max_length=100, blank=True)
  money_raised   = models.CharField(max_length=100, blank=True)
  #manager_profiles = models.ManyToManyField(Manager, blank=True, null=True)
  #manager_profiles = models.ManyToManyField(Manager)

  def __unicode__(self):
    return "%s, %s, %s" % (self.name, self.state, self.url)

class BusinessToBuy(models.Model):
  """
  Supermarkets, etc who are looking to be purchased.
  """
  name = models.CharField(max_length=30)
  # TODO add geo-aware field

class ServiceProvider(models.Model):
  """
  Lawyers, etc who are listing their services on the site.
  """
  name = models.CharField(max_length=100)
