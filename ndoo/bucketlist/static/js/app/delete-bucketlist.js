function deleteBucketlist(bucketlist_id) {
    UIkit.modal.confirm("Are you sure you want to delete this Ndoo? All related Ndoo items will be deleted", function(){
        var current_bucketlist_form = "#delete-bucketlist-" + bucketlist_id + "-form";
        var form_data = $(current_bucketlist_form + " :input").serializeArray();
        $.post("/delete-bucketlist/", data=form_data, function(response) {
            if (response.message === 'success') {
                window.location.href = "/dashboard";
            }
            else if (response.message === "Object Doesn't Exist") {
                console.log(response.log);
            }
        });
    });
}