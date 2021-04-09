setTimeout(function () {
    richTextField.document.body.innerHTML = $('#id_body')[0].value;
}, 500);

$(document).ready(function () {
    $('.ask-question-button').click(function (){
        $('#id_body')[0].value = richTextField.document.body.innerHTML;
    });
});