/* TAG EDITOR */

tagEditor.document.body.style.margin = '4px 0'; // Resetting margin of body to prevent overflow.

function addList() {
    // Function to add tags as list items and some settings.

    if (tagEditor.document.head.innerHTML === '') {  // If there is no link to stylesheet in the iframe:
        let style = document.head.children[11].cloneNode(true);  // Clone the stylesheet of main document,
        tagEditor.document.head.appendChild(style);  // Append it to iframe's head.
    }

    // Control the body for 'ul' element's existence.
    for (let child of tagEditor.document.body.children) {
        if (child.nodeName === 'UL') {
            return;
        }
    }

    // Create the 'ul' and 'li' elements.
    tagEditor.document.execCommand('insertUnorderedList', false, null);

    // Set 'ul' element's class name for styling.
    let tagList = tagEditor.document.getElementsByTagName('ul')[0];
    if(!tagList.decorated) {
        tagList.className = 'tag-list';
        tagList.decorated = true;
    }

    // Set 'li' element's class name for styling.
    for (let item of tagEditor.document.getElementsByTagName('li')) {
        if (item.decorated !== true) {
            item.className = 'tag-list-item';
            item.decorated = true;
        }
    }
}

// Run the 'addList()' function when iframe clicked and create list.
tagEditor.document.addEventListener('click', function () {
    addList()
});

let frame = tagEditor.document.getElementsByTagName('body')[0];
frame.addEventListener('keydown', function (event) {
    if (event.keyCode === 13) {
        // If pressed enter inside iframe:

        if (tagEditor.document.getElementsByTagName('li').length === 0) {
            //If there is no list item, prevent key press to line break.
            event.preventDefault();
        }

        addList()  // Create list elements if not exists.

        // Add function to list items to remove when clicked on them.
        let listItems = tagEditor.document.getElementsByTagName('li');  // Select all list items.
        for (item of listItems) {
            item.addEventListener('click', function () {
                // When clicked onto a list item, remove that item.
                this.remove();
            });
        }
    }
});

// Dropdowns

const hintButtons = ['#question-hint-area-button-one', '#question-hint-area-button-two',
    '#description-dropdown-button-one', '#description-dropdown-button-two', '#description-dropdown-button-three'];

const hintFields = ['#question-description-area-one', '#question-description-area-two',
    '#description-dropdown-menu-one', '#description-dropdown-menu-two', '#description-dropdown-menu-three'];

function addSlide(button, field) {
    $(document).ready(function () {
        $(button).click(function () {
            $(field).slideToggle();
        });
    });
}

for (let i = 0; i < buttons.length; i++) {
    addSlide(hintButtons[i], hintFields[i]);
    $(hintFields[i]).slideUp();
}

// Form

document.getElementsByClassName('title-form')[0].addEventListener('keydown', function () {
    document.getElementById('id_title').value = this.value;
});

richTextField.document.getElementsByTagName('body')[0].addEventListener('keydown', function () {
    document.getElementById('id_body').value = document.getElementsByName('richTextField')[0].contentWindow.document.body.innerHTML;
});



