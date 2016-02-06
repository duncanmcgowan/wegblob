"""
The main blog view module

DM May 2015
"""

from django.shortcuts import render_to_response, RequestContext
import wegblob.wegblob_settings as wegblob_settings
import db

def blog_main(request):
   """
   This is the main blog entry point. It;
   - gets config data
   - sets up nav and other options based on the config data
   - returns the templated page
   """
   context = wegblob_settings.config 
   entry_id = request.GET.get("entry_id")
   if entry_id is not None:
      entry_id = int(entry_id)
      
   context['entry'] = db.fetch_one(blog_id=entry_id)
   context['entry']['base_path'] = "/static/content/"
   context['entry']['template'] = context['entry']['rel_path'] + "/index.html"
      
   """
   A bit of code to set up the nav panels to the right of the content area
   """
   
   for nav in wegblob_settings.config['nav_panels']:
      
      # Recent posts if entry_id = None, else show related posts >>>
      # ============================================================
      if nav['title'] == wegblob_settings.NAV_PANEL_LAST_POSTS and nav['display']:
         num_posts = 5 if 'num_posts' not in nav else nav['num_posts']
         if entry_id is None:
            context['recent_related_title'] = "LAST POSTS"
            context['last_entries'] = db.fetch_last_entries(num_posts,exclude=0)
         else:
            context['recent_related_title'] = "RELATED POSTS"
            context['last_entries'] = db.fetch_related_entries(entry_id,num_posts) 
            
      # Tag cloud >>>
      # =============
      elif nav['title'] == wegblob_settings.NAV_PANEL_TAGS and nav['display']:
         context['tags'] = _format_post_tags(context['entry']['tags']) #db.get_tags()
         
   return render_to_response('wegblob-main.html', context, context_instance=RequestContext(request))
   

def category(request):
   """
   Returns a page containing a list of blogs containing a given category (or tag)
   """
   context = wegblob_settings.config
   tag = request.GET.get("tag")
   if tag is None:
      context['message'] = 'Missing tag/category'
      return render_to_response('wegblob-error.html', context, context_instance=RequestContext(request))
   
   context['entries'] = db.fetch_entries_by_tag(tag)
   for i, entry in enumerate(context['entries']):
      context['entries'][i]['tags'] = _format_post_tags(entry['tags'])
   context['tag'] = tag
   return render_to_response('wegblob-category-entries.html', context, context_instance=RequestContext(request))


def archive(request):
   """
   Returns a full archive (list) of all entries, most recent at top
   """
   context = wegblob_settings.config
   context['archive'] = db.fetch_all()
   for i, entry in enumerate(context['archive']):
      context['archive'][i]['tags'] = _format_post_tags(entry['tags'])
      
   response = render_to_response('wegblob-archive.html', context, context_instance=RequestContext(request))   
   return response


def categories(request):
   """
   Returns a page-full of categories (like a tag cloud)
   """
   context = wegblob_settings.config
   context['tags'] = db.get_tags()
   return render_to_response('wegblob-categories.html', context, context_instance=RequestContext(request))


def handler404(request):
   """
   404 handler
   """
   response = render_to_response('404.html', {}, 
         context_instance=RequestContext(request))
   response.status_code = 404
   return response


def _format_post_tags(tags):
   """
   Private function to convert post tags (eg, "JavaScript | Bootstrap | CSS") into
   a dict
   """
   lst = map(str.strip, str(tags).split("|"))
   lst.sort()

   results = list()
   for itm in lst:
      results.append( { 'name': itm })
   return results
