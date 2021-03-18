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

const tags = [];

for (let option of document.getElementById('id_tags').options) {
    tags.push(option.value)
}

let tagEditorFrame = tagEditor.document.getElementsByTagName('body')[0];
tagEditorFrame.addEventListener('keydown', function (event) {
    if (event.keyCode === 13) {
        let myTags = [...tagEditor.document.getElementsByTagName('li')];
        for (let tag of myTags) {
            if (!(tags.includes(tag.innerText))) {
                document.getElementsByName('tagEditor')[0].style.borderColor = 'red';
            } else {
                document.getElementsByName('tagEditor')[0].style.borderColor = '#ced4da';

                let select = document.getElementById('id_tags').options;
                for (let option of select) {
                    if (option.value === tag.innerText) {
                        option.selected = true;
                    }
                }
            }
        }
    }
});
