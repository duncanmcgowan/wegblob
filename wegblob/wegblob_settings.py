"""
wegblob_settings.py

Add wegblob-specific config data here

DM May 2015
"""

NAV_PANEL_LAST_POSTS = 'Last Posts'
NAV_PANEL_TAGS       = 'Tag Cloud'
NAV_PANEL_PROJECTS   = 'Projects'
NAV_PANEL_MORE       = 'More'
NAV_PANEL_ABOUT      = 'About'

config = {
   'main_page_title'    : 'WegBlob: a Django blog framework',
   'page_header_text'   : '{weg:blob}',
   'page_header_subtext': '',
   'footer_inner_text'  : '&copy; Duncan McGowan',
   'entry_id'           : 'last',
   'nav_panels'         : [
      { 'title' : NAV_PANEL_LAST_POSTS,   'display' : True,  'num_posts' : 5                    },
      { 'title' : NAV_PANEL_TAGS,         'display' : True     },
      { 'title' : NAV_PANEL_PROJECTS,     'display' : True,  'url'       : 'projects.html'      },
      { 'title' : NAV_PANEL_ABOUT,        'display' : True,  'url'       : 'about.html'         },
      { 'title' : NAV_PANEL_MORE,         'display' : True,  'url'       : 'more.html'          }
      ]
   }

"""
app_status controls availability of site - use this in middleware to allow/restrict access
(set 'available' to False and give reason when site is down)
"""

app_status = {
   'available' : True,
   'message'   : "BLOGNAME is currently unavailable",
   'reason'    : "Website down for routine maintenance"
   }

