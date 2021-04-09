function enableDeleteButton() {
    if ($('#confirm-delete')[0].checked) {
        $('#delete-account-button').attr('disabled', false);
    } else {
        $('#delete-account-button').attr('disabled', 'disabled');
    }
}