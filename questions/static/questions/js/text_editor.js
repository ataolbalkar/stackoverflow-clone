function enableEditMode() {
        richTextField.document.designMode = 'On';
        try {
            tagEditor.document.designMode = 'On';
        }
        catch (e) {

        }
}

function enableEditModeText() {
        richTextField.document.designMode = 'On';
}

function enableEditModeTag() {
        tagEditor.document.designMode = 'On';
}

var buttons = ['#links-button', '#images-button', '#styling-button', '#lists-button',
'#blockquotes-button', '#codes-button', '#HTMLs-button', '#tables-button'];

var descriptions = ['#links', '#images', '#styling', '#lists',
'#blockquotes', '#codes', '#HTMLs', '#tables'];

function execCmd(command) {
    richTextField.document.execCommand(command, false, null);
}
function execCmdWithArg(command, arg) {
    richTextField.document.execCommand(command, false, arg);
}

function addLink() {
    let is_url = richTextField.document.getSelection().focusNode.parentElement.tagName;

    if (is_url === 'A') {
        richTextField.document.execCommand('unlink', false, null);
    }
    else {
        richTextField.document.execCommand('createLink', false, prompt('Enter a URL', 'http://'));
    }
}
function addCode() {
    richTextField.document.execCommand('fontName', false, 'monospace');
    richTextField.document.execCommand('backColor', false, '#f1f1f1');
}
function addHeading() {
    let curr_heading = richTextField.document.getSelection().focusNode.parentElement.tagName;

    if (curr_heading === 'H1') {
        richTextField.document.execCommand('formatBlock', false, 'h2');
    } else if (curr_heading === 'H2') {
        richTextField.document.execCommand('formatBlock', false, 'p');
    } else {
        richTextField.document.execCommand('formatBlock', false, 'h1');
    }
}
function firstHide(element) {
    $(element).hide();
}

$(document).ready(function () {
    $('.text-button').click(function () {
        $('.button-descriptions').slideToggle();
    });
});

function addSlide(button, field) {
    $(document).ready(function () {
        $(button).click(function () {
            var dCopy = descriptions.slice();
            var idx = descriptions.indexOf(field);
            dCopy.splice(idx, 1)

            for (description of dCopy) {
                $(description).slideUp();
            }
            $(field).slideToggle();
        });
    });
}
for (var i = 0; i < 8; i++) {
    addSlide(buttons[i], descriptions[i]);
}