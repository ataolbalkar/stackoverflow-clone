$('#user-profile-setting-add-tag-watch').slideUp('fast');
$('#user-profile-setting-add-tag-ignore').slideUp('fast');

function createTag(tag_name, tag_link, tag_group) {
    let tag_field = document.createElement('div');
    tag_field.className = 'user-profile-setting-tag-field';
    tag_field.id = 'user-profile-setting-tag-field--' + tag_name;

    let remove_button = document.createElement('button');
    remove_button.className = 'delete-tag-button';
    remove_button.innerHTML = '<i class="fas fa-times"></i>'

    if (tag_group === 'watch') {
        remove_button.id = 'unwatch-tag--' + tag_name;
    } else if (tag_group === 'ignore') {
        remove_button.id = 'unignore-tag--' + tag_name;
    }

    tag_field.appendChild(remove_button);

    let tag = document.createElement('a');
    tag.href = tag_link;
    tag.className = 'user-profile-setting-tag';
    tag.innerText = tag_name;

    tag_field.appendChild(tag);

    if (tag_group === 'watch') {
        document.getElementById('watching-tags').appendChild(tag_field);
    } else if (tag_group === 'ignore') {
        document.getElementById('ignored-tags').appendChild(tag_field);
    }
}

function deleteTag(tag_name, tag_group) {
    if (tag_group === 'watch') {
        $('#watching-tag-field--' + tag_name).remove();
    } else if (tag_group == 'ignore') {
        $('#ignored-tag-field--' + tag_name).remove();
    }
}

$(document).ready(function () {
    const csrf = $('input[name=csrfmiddlewaretoken]')[0].value

    $('#add-tag-button-watch').click(function () {
        $('#user-profile-setting-add-tag-watch').slideToggle();
    });

    $('#add-tag-button-ignore').click(function () {
        $('#user-profile-setting-add-tag-ignore').slideToggle();
    });

    $('#watch-tag-button').click(function () {
        let tag_name = $('#add-tag-input-watch')[0].value;
        let current_tags = [];
        let all_tags = [];

        for (let tag of $('#id_interested_tags option')) {
            all_tags.push(tag.value);
            if (tag.selected) {
                current_tags.push(tag.value);
            }
        }

        if (all_tags.includes(tag_name)) {
            if (current_tags.includes(tag_name)) {
                $('#add-tag-input-watch').css('border-color', 'red');

            } else {
                $('#add-tag-input-watch').css('border-color', '#c5cbd1');
                $.ajax({
                    url: '',
                    type: 'post',
                    data: {
                        type: 'watch_tag',
                        tag: tag_name,
                        csrfmiddlewaretoken: csrf
                    },
                    success: function (response) {
                        createTag(tag_name, response.tag_url, 'watch');
                    }
                });
            }

        } else {
            $('#add-tag-input-watch').css('border-color', 'red');
        }
    });

    $('#ignore-tag-button').click(function () {
        let tag_name = $('#add-tag-input-ignore')[0].value;
        let current_tags = [];
        let all_tags = [];

        for (let tag of $('#id_ignored_tags option')) {
            all_tags.push(tag.value);
            if (tag.selected) {
                current_tags.push(tag.value);
            }
        }

        if (all_tags.includes(tag_name)) {
            if (current_tags.includes(tag_name)) {
                $('#add-tag-input-ignore').css('border-color', 'red');

            } else {
                $('#add-tag-input-ignore').css('border-color', '#c5cbd1');
                $.ajax({
                    url: '',
                    type: 'post',
                    data: {
                        type: 'ignore_tag',
                        tag: tag_name,
                        csrfmiddlewaretoken: csrf
                    },
                    success: function (response) {
                        createTag(tag_name, response.tag_url, 'ignore');
                    }
                });
            }

        } else {
            $('#add-tag-input-ignore').css('border-color', 'red');
        }
    });

    $('.unwatch-button').click(function () {
        let tag = this.id.split('--')[1];

        $.ajax({
            url: '',
            type: 'post',
            data: {
                tag: tag,
                type: 'unwatch_tag',
                csrfmiddlewaretoken: csrf
            },
            success: function (response) {
                deleteTag(tag, 'watch');
            }
        });
    });

    $('.unignore-button').click(function () {
        let tag = this.id.split('--')[1];

        $.ajax({
            url: '',
            type: 'post',
            data: {
                tag: tag,
                type: 'unignore_tag',
                csrfmiddlewaretoken: csrf
            },
            success: function (response) {
                deleteTag(tag, 'ignore');
            }
        });
    });
});