function editBucketlist(bucketlist_id) {
    var current_bucketlist_form = "#edit-bucketlist-" + bucketlist_id + "-modal";
    var errors = 0;
    $(current_bucketlist_form + " :input").map(function(){
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
    var form_data = $(current_bucketlist_form + " :input").serializeArray();
    $.post("/edit-bucketlist/", data=form_data, function(response) {
        if (response.message === 'success') {
            window.location.href = "/dashboard";
        }
    });
}