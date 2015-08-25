from django.shortcuts import render_to_response, RequestContext
import wegblob.wegblob_settings as wegblob_settings

class WegBlobMiddleware(object):
   """
   Middleware class for EG blog
   """
    
   def __init__(self):
      """
      Constructor
      """
      self._initialised = False
        
   def _initialise(self, request):  
      """
      Authenticate user and any other one-off stuff
      """
      self._initialised = True
      
   def process_request(self, request):
      """
      Called for all requests - add conditional code here
      """
      if not self._initialised:
         try:
            self._initialise(request)
         except ValueError as e:
            return None
         
      if wegblob_settings.app_status['available'] is not True:
         return render_to_response('wegblob-unavailable.html', { 'app_status':wegblob_settings.app_status }, context_instance=RequestContext(request))
            
   def process_response(self, request, response):
      """
      Called for each response
      """
      return response
    
   