jQuery("document").ready(function(){
    jQuery(".likevideo").on('click', function(){
        console.log("hello");
            var id = jQuery(this).attr('id');
            console.log(id);
            jQuery.ajax({
                type: "GET",

                url: "/video/addlike/ajax/",

                data:{ "addlike" : id,},

                dataType: "text",

                catch: false,

                success: function(data){
                    console.log(data)
                    jQuery("#" + id + "video").html(data);
                }
            });
    });
});
