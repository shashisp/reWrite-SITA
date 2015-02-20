"""
models.py

App Engine datastore models

"""


from google.appengine.ext import ndb


class ExampleModel(ndb.Model):
    """Example Model"""
    example_name = ndb.StringProperty(required=True)
    example_description = ndb.TextProperty(required=True)
    added_by = ndb.UserProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)


class SchoolModel(ndb.Model):
	name = ndb.StringProperty(required=True)
	place = ndb.StringProperty(required=True)
	added_by = ndb.UserProperty()
	timestamp = ndb.DateTimeProperty(auto_now_add=True)
	score = ndb.IntegerProperty()
