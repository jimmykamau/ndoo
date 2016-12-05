$(function() {
    $('#create-bucketlist-form').on('submit', function(e) {
        e.preventDefault();  //prevent form from submitting
        var errors = 0;
        $("#create-bucketlist-form :input").map(function(){
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
        var form_data = $("#create-bucketlist-form :input").serializeArray();
        $.post("/create-bucketlist/", data=form_data, function(response) {
            if (response.message === 'success') {
                window.location.href = "/dashboard";
            }
        });
    });
});