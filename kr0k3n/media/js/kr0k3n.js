$(function(){
    $('#add_icon').bind('click', function() {
        $('#add_type').fadeToggle('fast', 'linear');
    });

    $('.nav_top').hover(
        function() { $(this).addClass('ui-state-hover'); }, 
	function() { $(this).removeClass('ui-state-hover'); }
    );
    $('#dialog_link, ul#icons li, ul#add_icon li').hover(
	function() { $(this).addClass('ui-state-hover'); }, 
	function() { $(this).removeClass('ui-state-hover'); }
    );
    $(".tag-input").tokenInput("/tag/query/", {
        theme: "facebook",
        onAdd: function(item) {
            item_id = this[0].id.split('-')[2]
            $.post('/tag/add/',
                   {
                       'id': item.id,
                       'slug': item.name,
                       'item': item_id
                   }),
            },
        onDelete: function(item) {
            item_id = this[0].id.split('-')[2]
            $.post('/tag/delete/',
                   {
                       'id': item.id,
                       'slug': item.name,
                       'item': item_id
                   });
            },
    });
});
