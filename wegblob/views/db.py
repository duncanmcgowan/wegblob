"""
db.py

Simple interface to whatever DB engine Django is providing

DM May 2015
"""
from django.db import connection
from datetime import datetime

def _process_date(results, short_format=False):
   """
   Private func to convert timestamp tp readable date string
   in format: "Sunday, 01 April 2014 08:35"
   """
   for i, result in enumerate(results):
      dt = datetime.fromtimestamp(result['timestamp'])
      if not short_format:
         results[i]['date'] = dt.strftime("%A, %d %B %Y %H:%M")
      else:
         results[i]['date'] = dt.strftime("%d %B %Y")
      
   return results


def _fetch(stmt):
   """
   Execute a statement and fetch results.
   Return as list of dictionaries
   """
   cursor = connection.cursor()
   cursor.execute ( stmt )
   desc = cursor.description
   results = [ dict(zip([col[0] for col in desc],row)) for row in cursor.fetchall() ]
   return results


def fetch_one(blog_id=None):
   """
   Fetch a single blog entry. If blog_id is None, fetch last entry.
   """
   cursor = connection.cursor()
   stmt = None
   if blog_id is None:
      stmt = "select * from blog where timestamp = (select max(timestamp) from blog)"
   else:
      stmt = "select * from blog where id=%d" % blog_id
   cursor.execute ( stmt )
   desc = cursor.description
   result = dict(zip([col[0] for col in desc],cursor.fetchone()))
   
   dt = datetime.fromtimestamp(result['timestamp'])
   result['date'] = dt.strftime("%A, %d %B %Y %H:%M")
   
   return result


def fetch_all():
   """
   Fetch and return all entries
   """
   stmt = "select * from blog order by timestamp desc"
   results = _fetch(stmt)
   return _process_date(results, short_format=True)


def fetch_last_entries(last_entries, exclude=None):
   """
   Get last entries.
   If 'exclude' = 0 then exclude the last entry
   """
   stmt = "select * from blog"
   if exclude is not None:
      if exclude == 0:
         stmt += " where timestamp <> (select max(timestamp) from blog)"
      else:
         stmt += " where id <> %d" % exclude
   stmt += " order by timestamp desc limit 0, %d" % last_entries
   results = _fetch(stmt)
   return _process_date(results)
   

def fetch_related_entries (current_entry_id, last_entries=None):
   """
   Get related entries
   """
   current_entry = fetch_one(current_entry_id)
   tags = current_entry['tags'].split("|")
   
   stmt = "select * from blog where ("
   for i, tag in enumerate(tags):
      stmt += "tags like '%s' " % ("%%" + tag.strip() + "%%")
      if i < len(tags)-1:
         stmt += " or "
         
   stmt += ") and id <> %d order by timestamp desc" % int(current_entry_id)
   
   if last_entries is not None:
      stmt += " limit 0, %d" % last_entries
      
   results = _fetch(stmt)
   return _process_date(results)
   

def fetch_entries_by_tag(tag):
   """
   Fetch entries containing 'tag' in 'tags' column
   """
   stmt = "select * from blog where tags like '%s' order by timestamp desc" % ("%%" + tag + "%%")
   results = _fetch(stmt)
   return _process_date(results)
   

def get_tags ():
   """
   Return a list of dictionaries representing the contents of the 'tags' table
   """
   return _fetch("select * from tags order by name asc")

