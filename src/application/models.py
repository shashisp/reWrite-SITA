"""
models.py

App Engine datastore models

"""


from google.appengine.ext import ndb

class SchoolModel(ndb.Model):
    """"Basic Model""""
    name = ndb.StringProperty(required=True)
    place = ndb.StringProperty(required=True)
    added_by = ndb.UserProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)
    score = ndb.IntegerProperty()
