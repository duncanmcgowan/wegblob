/*
 * wegblob.js
 * 
 * Supporting JS for wegblob blog package
 * 
 * DM May 2015
 */

$(document).ready(function(){
	init();
});

function init()
{	
   //	Process 'loadables' (for nav panels) >>>
   $(".loadable").each( function(idx) {
      var url = $(this).data("url");
      $(this).load("/static/content/"+url);
   });
	
   //   Where an 'wegblob-content-pre' contains a 'data-tag-id', this block loads the <pre> content
   //   from the remote source specified via the 'data-tag-id' attribute, which points to the
   //   id of a script tag. This avoids pasting code into a <pre> - the actual code is loaded
   //   instead >>>
	
   $(".wegblob-content-pre").each(function(idx)
   {
      var tag = $(this).data("tag-id");
      if ( tag )
      {
         var src = $("#"+tag)[0].src;
         var elem = $(this);
         $.ajax({
            url: src,
            dataType: 'text',
            success: function(data) 
            {
               var regex = new RegExp("<", "g");
               data = data.replace(regex, "&lt;"); // Remove/replace '<' chars
         
               regex = new RegExp(">", "g");
               data = data.replace(regex, "&gt;"); // Remove/replace '>' chars
         
               elem.removeClass("prettyprinted");  // Have to do this - prettyPrint() ignores otherwise
               elem.html(data);                    // Add the incoming text
               prettyPrint();                      // Call the format function
            }
          });
      }
   });
	
   //   If you add a 'content_ready()' function in your index.html then this will be
   //   executed below, ensuring that content is fully-loaded before doing some DOM or
   //   AJAX stuff >>>
	
   if ( typeof content_ready !== "undefined" )
      content_ready();
	
   prettyPrint();
	
   //   Code to handle show/hide <pre> contents >>>
	
   $('.wegblob-code-btn').on('click', function(e)
   {
      e.preventDefault();
      var $this = $(this);
      var state = $this.attr('data-state');
	 
      if ( state === 'off' )
      {
         var html = (typeof $(this).data('hide-text') !== "undefined") ? $(this).data('hide-text') : "Hide code &laquo;";
         $this.html(html);
         $(this).attr("data-state","on");
      }
      else
      {
         var html = (typeof $(this).data('show-text') !== "undefined") ? $(this).data('show-text') : "Show code &raquo;";
         $this.html(html);
         $(this).attr("data-state","off");
      }
      var $collapse = $this.closest('.collapse-group').find('.collapse');
      $collapse.collapse('toggle');
   });
	
}
