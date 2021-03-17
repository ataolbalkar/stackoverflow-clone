// ONLOAD

let update_title = $('#id_title')[0].value;
let update_body = $('#id_body')[0].value;

$('.title-form')[0].value = update_title;

setTimeout(function () {
    richTextField.document.body.innerHTML = update_body;
}, 500);
