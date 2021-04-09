$(document).ready(function () {
    const allPosts = ['#top-posts-post-all', '#top-posts-post-questions',
        '#top-posts-post-answers', '#top-posts-post-all-sorted',
        '#top-posts-post-questions-sorted', '#top-posts-post-answers-sorted'];

    const selectButtons = ['#top-posts-all', '#top-posts-questions', '#top-posts-answers'];
    const sortButtons = ['#top-posts-votes', '#top-posts-newest'];

    function activateSelectButton(activate_index) {
        for (let selectButton of selectButtons) {
            $(selectButton)[0].classList.remove('btn-active');
        }
        $(selectButtons[activate_index])[0].classList.add('btn-active');
    }

    function activateSortButton(activate_index) {
        for (let sortButton of sortButtons) {
            $(sortButton)[0].classList.remove('btn-active');
        }
        $(sortButtons[activate_index])[0].classList.add('btn-active');
    }

    function hideAllShowOne(showIndex) {
        for (let posts of allPosts) {
            $(posts).css('display', 'none');
        }
        $(allPosts[showIndex]).css('display', 'block');
    }

    $('#top-posts-all').click(function () {
        if (this.className.includes('btn-active')) {
        } else {
            if ($('#top-posts-votes')[0].className.includes('btn-active')) {
                hideAllShowOne(0);
            } else {
                hideAllShowOne(3);
            }
            activateSelectButton(0);
        }
    });
    $('#top-posts-questions').click(function () {
        if (this.className.includes('btn-active')) {
        } else {
            if ($('#top-posts-votes')[0].className.includes('btn-active')) {
                hideAllShowOne(1);
            } else {
                hideAllShowOne(4);
            }
            activateSelectButton(1);
        }
    });
    $('#top-posts-answers').click(function () {
        if (this.className.includes('btn-active')) {
        } else {
            if ($('#top-posts-votes')[0].className.includes('btn-active')) {
                hideAllShowOne(2);
            } else {
                hideAllShowOne(5);
            }
            activateSelectButton(2);
        }
    });
    $('#top-posts-votes').click(function () {
        if (this.className.includes('btn-active')) {
        } else {
            if ($('#top-posts-all')[0].className.includes('btn-active')) {
                hideAllShowOne(0);
            } else if ($('#top-posts-questions')[0].className.includes('btn-active')) {
                hideAllShowOne(1);
            } else {
                hideAllShowOne(2);
            }
            activateSortButton(0);
        }
    });
    $('#top-posts-newest').click(function () {
        if (this.className.includes('btn-active')) {
        } else {
            if ($('#top-posts-all')[0].className.includes('btn-active')) {
                hideAllShowOne(3);
            } else if ($('#top-posts-questions')[0].className.includes('btn-active')) {
                hideAllShowOne(4);
            } else {
                hideAllShowOne(5);
            }
            activateSortButton(1);
        }
    });
});