$(document).ready(function () {
    const tag = $('.tag-title')[0].id;
    const csrf = $('input[name=csrfmiddlewaretoken]')[0].value;

    $('.watch-tag-button').click(function () {
        $.ajax({
            url: '',
            type: 'POST',
            data: {
                type: 'watch_tag',
                csrfmiddlewaretoken: csrf
            },
            success: function (response) {
                $('.watch-tag-button').css('display', 'none');
                $('.unwatch-tag-button').css('display', 'block');

                if ($('.unignore-tag-button').css('display') === 'block') {
                    $('.unignore-tag-button').css('display', 'none');
                    $('.ignore-tag-button').css('display', 'block');

                    for (let ignoredTag of $('.ignored-tags')) {
                        if (ignoredTag.innerText.trim() === tag.trim()) {
                            ignoredTag.remove();
                        }
                    }
                }

                let newTag = document.createElement('a');
                newTag.className = 'tag-question-tag watched-tags';
                newTag.innerText = tag;
                newTag.href = window.location.href;

                document.getElementById('watched-tags').appendChild(newTag);

                console.log(response.data)
            }
        });
    });

    $('.unwatch-tag-button').click(function () {
        $.ajax({
            url: '',
            type: 'POST',
            data: {
                type: 'unwatch_tag',
                csrfmiddlewaretoken: csrf
            },
            success: function (response) {
                $('.watch-tag-button').css('display', 'block');
                $('.unwatch-tag-button').css('display', 'none');

                for (let watchedTag of $('.watched-tags')) {
                    if (watchedTag.innerText.trim() === tag.trim()) {
                        watchedTag.remove();
                    }
                }

                console.log(response.data)
            }
        });
    });

    $('.ignore-tag-button').click(function () {
        $.ajax({
            url: '',
            type: 'POST',
            data: {
                type: 'ignore_tag',
                csrfmiddlewaretoken: csrf
            },
            success: function (response) {
                $('.ignore-tag-button').css('display', 'none');
                $('.unignore-tag-button').css('display', 'block');

                if ($('.unwatch-tag-button').css('display') === 'block') {
                    $('.unwatch-tag-button').css('display', 'none');
                    $('.watch-tag-button').css('display', 'block');

                    for (let watchedTag of $('.watched-tags')) {
                        if (watchedTag.innerText.trim() === tag.trim()) {
                            watchedTag.remove();
                        }
                    }
                }

                let newTag = document.createElement('a');
                newTag.className = 'tag-question-tag ignored-tags';
                newTag.innerText = tag;
                newTag.href = window.location.href;

                document.getElementById('ignored-tags').appendChild(newTag);

                console.log(response.data)
            }
        });
    });

    $('.unignore-tag-button').click(function () {
        $.ajax({
            url: '',
            type: 'POST',
            data: {
                type: 'unignore_tag',
                csrfmiddlewaretoken: csrf
            },
            success: function (response) {
                $('.ignore-tag-button').css('display', 'block');
                $('.unignore-tag-button').css('display', 'none');

                for (let ignoredTag of $('.ignored-tags')) {
                    if (ignoredTag.innerText.trim() === tag.trim()) {
                        ignoredTag.remove();
                    }
                }

                console.log(response.data)
            }
        });
    });
});