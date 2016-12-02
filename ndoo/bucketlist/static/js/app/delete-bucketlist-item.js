function deleteBucketlistItem(item_id) {
    UIkit.modal.confirm("Are you sure you want to delete this Ndoo item?", function(){
        var current_bucketlist_item_form = "#delete-bucketlist-item-" + item_id + "-form";
        var form_data = $(current_bucketlist_item_form + " :input").serializeArray();
        $.post("/bucketlist/items/"+ item_id +"/delete/", data=form_data, function(response) {
            if (response.message === 'success') {
                window.location.href = "/dashboard";
            }
            else if (response.message === "Object Doesn't Exist") {
                console.log(response.log);
            }
        });
    });
}