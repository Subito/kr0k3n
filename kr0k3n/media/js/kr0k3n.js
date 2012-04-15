$(function(){
    $('.nav_top').hover(
        function() { $(this).addClass('ui-state-hover'); }, 
	function() { $(this).removeClass('ui-state-hover'); }
    );
    $('#dialog_link, ul#icons li').hover(
	function() { $(this).addClass('ui-state-hover'); }, 
	function() { $(this).removeClass('ui-state-hover'); }
    );
    
});
