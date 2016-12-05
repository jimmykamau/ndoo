function createBucketlistItem(bucketlist_id) {
    var errors = 0;
    var current_bucketlist_item_form = "#create-bucketlist-"+ bucketlist_id +"-item-form";
    $(current_bucketlist_item_form + " :input").map(function(){
         if( !$(this).val() ) {
              $(this).addClass('uk-form-danger');
              errors++;
        } else if ($(this).val()) {
              $(this).removeClass('uk-form-danger');
        }   
    });
    if(errors > 0){
        UIkit.notify('Please fill all fields', {pos:'top-right', status:'danger'});
        return false;
    }
    var form_data = $(current_bucketlist_item_form + " :input").serializeArray();
    console.log(form_data);
    console.log(form_data[1].value);
    $.post("/bucketlist/"+  form_data[1].value +"/items/", data=form_data, function(response) {
        if (response.message === 'success') {
            window.location.href = "/dashboard";
        }
        else {
            console.log(response)
            UIkit.notify('Error while creating Ndoo item', {pos:'top-right', status:'danger'});
        }
    });
}