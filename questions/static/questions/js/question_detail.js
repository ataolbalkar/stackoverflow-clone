$(document).ready(function () {
    // CSRF TOKEN
    const csrf = $('input[name=csrfmiddlewaretoken]').val();

    // VOTE QUESTION UP
    $('.question-vote-up').click(function () {
        let voteButtonDown = $('.question-vote-down');  // Vote down button
        // If 'vote down' button is disabled, means the user voted the question before.
        let votedBefore = voteButtonDown.attr('disabled') === 'disabled';  // Boolean

        // AJAX POST
        $.ajax({
            url: '',
            type: 'post',
            data: {
                type: 'vote_up',
                object: 'question',
                voted_before: votedBefore,
                csrfmiddlewaretoken: csrf
            }
        })
        let currentVotes = parseInt($('#question-votes')[0].innerText);  // Current vote number
        currentVotes++;  // Increase votes by 1.

        if (votedBefore){  // If user voted this question before:
            voteButtonDown.attr('disabled', false);  // Enable the 'vote down' button.
            voteButtonDown.css('color', '#bbc0c4');  // Change 'vote down' buttons color to grey.
        } else {  // If user didn't vote this question before:
            $(this).attr('disabled', true);  // Disable the 'vote up' button.
            $('.question-vote-up').css('color', '#50c37b');  // Change 'vote up' buttons color to green.
        }

        $(`#question-votes`)[0].innerText = currentVotes;  // Change the vote number to current.
    });

    // VOTE QUESTION DOWN
    $('.question-vote-down').click(function () {
        let voteUpButton = $('.question-vote-up');  // Vote up button
        // If 'vote down' button is disabled, means the user voted the question before.
        let votedBefore = voteUpButton.attr('disabled') === 'disabled';

        $.ajax({
            url: '',
            type: 'post',
            data: {
                type: 'vote_down',
                object: 'question',
                voted_before: votedBefore,
                csrfmiddlewaretoken: csrf
            }
        })
        let currentVotes = parseInt($('#question-votes')[0].innerText);
        currentVotes--;

        if (votedBefore) {
            voteUpButton.attr('disabled', false);
            voteUpButton.css('color', '#bbc0c4');
        } else {
            $(this).attr('disabled', true);
            $('.question-vote-down').css('color', '#c3212a');
        }

        $(`#question-votes`)[0].innerText = currentVotes;
    });

    const questionCommentVoteButtonsUp = $('.question-comment-vote-button-up');
    if (questionCommentVoteButtonsUp.length > 0) {
        for (let questionCommentVoteButtonsUpElement of questionCommentVoteButtonsUp) {
            let pk = questionCommentVoteButtonsUpElement.id.split('--')[1];

            $('#question-comment-vote-button-up--' + pk).click(function () {

                let voteDownButton = $('#question-comment-vote-button-down--' + pk);
                let votedBefore = voteDownButton.attr('disabled') === 'disabled';

                $.ajax({
                   url: '',
                   type: 'post',
                   data: {
                       type: 'vote_up',
                       object: 'question_comment',
                       pk: pk,
                       voted_before: votedBefore,
                       csrfmiddlewaretoken: csrf
                   }
                });

                let currVotesObj = $('#question-comment-votes-text--' + pk)[0]
                let currentVotes = currVotesObj.innerText;
                let currentVoteNumber = 0;

                if (currentVotes === '') {
                    currentVoteNumber = 0;
                } else {
                    currentVoteNumber = parseInt(currentVotes);
                }
                currentVoteNumber++;

                if (currentVoteNumber === 0) {
                    currVotesObj.innerText = '';
                } else {
                    currVotesObj.innerText = currentVoteNumber;
                }

                if (votedBefore) {
                    voteDownButton.attr('disabled', false);
                    $('#question-comment-votes-text--' + pk).css('color', '#bbc0c4');
                } else {
                    $(this).attr('disabled', true);
                    $('#question-comment-votes-text--' + pk).css('color', '#32a246');
                }
            });
        }
    }

    const questionCommentVoteButtonsDown = $('.question-comment-vote-button-down');
    if (questionCommentVoteButtonsDown.length > 0) {
        for (let questionCommentVoteButtonsDownElement of questionCommentVoteButtonsDown) {
            let pk = questionCommentVoteButtonsDownElement.id.split('--')[1];

            $('#question-comment-vote-button-down--' + pk).click(function () {

                let voteUpButton = $('#question-comment-vote-button-up--' + pk);
                let votedBefore = voteUpButton.attr('disabled') === 'disabled';

                $.ajax({
                   url: '',
                   type: 'post',
                   data: {
                       type: 'vote_down',
                       object: 'question_comment',
                       pk: pk,
                       voted_before: votedBefore,
                       csrfmiddlewaretoken: csrf
                   }
                });

                let currVotesObj = $('#question-comment-votes-text--' + pk)[0]
                let currentVotes = currVotesObj.innerText;
                let currentVoteNumber = 0;

                if (currentVotes === '') {
                    currentVoteNumber = 0;
                } else {
                    currentVoteNumber = parseInt(currentVotes);
                }
                currentVoteNumber--;

                if (currentVoteNumber === 0) {
                    currVotesObj.innerText = '';
                } else {
                    currVotesObj.innerText = currentVoteNumber;
                }

                if (votedBefore) {
                    voteUpButton.attr('disabled', false);
                    $('#question-comment-votes-text--' + pk).css('color', '#bbc0c4');

                } else {
                    $(this).attr('disabled', true);
                    $('#question-comment-votes-text--' + pk).css('color', '#c3212a');
                }
            });
        }
    }

    const answerVoteUpButtons = $('.question-answer-vote-button-up');
    const answerVoteDownButtons = $('.question-answer-vote-button-down');

    if (answerVoteUpButtons.length > 0) {
        for (let answerVoteUpButton of answerVoteUpButtons) {
            let pk = answerVoteUpButton.id.split('--')[1];

            $('#question-answer-vote-button-up--' + pk).click(function () {
                let voteDownButton = $('#question-answer-vote-button-down--' + pk);
                let votedBefore = voteDownButton.attr('disabled') === 'disabled';

                $.ajax({
                    url: '',
                    type: 'post',
                    data: {
                        type: 'vote_up',
                        object: 'answer',
                        pk: pk,
                        voted_before: votedBefore,
                        csrfmiddlewaretoken: csrf
                    }
                });
                let currentVotes = parseInt($('#question-answer-votes--' + pk)[0].innerText);
                currentVotes++;

                if (votedBefore) {
                    voteDownButton.attr('disabled', false);
                    voteDownButton.css('color', '#bbc0c4');
                } else {
                    $(this).attr('disabled', true);
                    $('#question-answer-vote-button-up--' + pk).css('color', '#c3212a');
                }

                $(`#question-answer-votes--` + pk)[0].innerText = currentVotes;
            });
        }
    }

    if (answerVoteDownButtons.length > 0) {
        for (let answerVoteDownButton of answerVoteDownButtons) {
            let pk = answerVoteDownButton.id.split('--')[1];

            $('#question-answer-vote-button-down--' + pk).click(function () {
                let voteUpButton = $('#question-answer-vote-button-up--' + pk);
                let votedBefore = voteUpButton.attr('disabled') === 'disabled';

                $.ajax({
                    url: '',
                    type: 'post',
                    data: {
                        type: 'vote_down',
                        object: 'answer',
                        pk: pk,
                        voted_before: votedBefore,
                        csrfmiddlewaretoken: csrf
                    }
                });
                let currentVotes = parseInt($('#question-answer-votes--' + pk)[0].innerText);
                currentVotes--;

                if (votedBefore) {
                    voteUpButton.attr('disabled', false);
                    voteUpButton.css('color', '#bbc0c4');
                } else {
                    $(this).attr('disabled', true);
                    $('#question-answer-vote-button-down--' + pk).css('color', '#c3212a');
                }

                $(`#question-answer-votes--` + pk)[0].innerText = currentVotes;
            })
        }
    }

    const answerCommentUpButtons = $('.question-answer-comment-vote-button-up');
    const answerCommentDownButtons = $('.question-answer-comment-vote-button-down');

    if (answerVoteUpButtons.length > 0) {
        for (let answerCommentUpButton of answerCommentUpButtons) {
            let pk = answerCommentUpButton.id.split('--')[1];

            $('#question-answer-comment-vote-button-up--' + pk).click(function () {

                let voteDownButton = $('#question-answer-comment-vote-button-down--' + pk);
                let votedBefore = voteDownButton.attr('disabled') === 'disabled';

                $.ajax({
                   url: '',
                   type: 'post',
                   data: {
                       type: 'vote_up',
                       object: 'answer_comment',
                       pk: pk,
                       voted_before: votedBefore,
                       csrfmiddlewaretoken: csrf
                   }
                });

                let currVotesObj = $('#question-answer-comment-votes--' + pk)[0];
                let currentVotes = currVotesObj.innerText;
                let currentVoteNumber = 0;

                if (currentVotes === '') {
                    currentVoteNumber = 0;
                } else {
                    currentVoteNumber = parseInt(currentVotes);
                }
                currentVoteNumber++;

                if (currentVoteNumber === 0) {
                    currVotesObj.innerText = '';
                } else {
                    currVotesObj.innerText = currentVoteNumber;
                }

                if (votedBefore) {
                    voteDownButton.attr('disabled', false);
                    $('#question-answer-comment-votes--' + pk).css('color', '#bbc0c4');
                } else {
                    $(this).attr('disabled', true);
                    $('#question-answer-comment-votes--' + pk).css('color', '#32a246');
                }
            });
        }
    }

    if (answerCommentDownButtons.length > 0) {
        for (let answerCommentDownButton of answerCommentDownButtons) {
            let pk = answerCommentDownButton.id.split('--')[1];

            $('#question-answer-comment-vote-button-down--' + pk).click(function () {

                let voteUpButton = $('#question-answer-comment-vote-button-up--' + pk);
                let votedBefore = voteUpButton.attr('disabled') === 'disabled';

                $.ajax({
                   url: '',
                   type: 'post',
                   data: {
                       type: 'vote_down',
                       object: 'answer_comment',
                       pk: pk,
                       voted_before: votedBefore,
                       csrfmiddlewaretoken: csrf
                   }
                });

                let currVotesObj = $('#question-answer-comment-votes--' + pk)[0];
                let currentVotes = currVotesObj.innerText;
                let currentVoteNumber = 0;

                if (currentVotes === '') {
                    currentVoteNumber = 0;
                } else {
                    currentVoteNumber = parseInt(currentVotes);
                }
                currentVoteNumber--;

                if (currentVoteNumber === 0) {
                    currVotesObj.innerText = '';
                } else {
                    currVotesObj.innerText = currentVoteNumber;
                }

                if (votedBefore) {
                    voteUpButton.attr('disabled', false);
                    $('#question-answer-comment-votes--' + pk).css('color', '#bbc0c4');
                } else {
                    $(this).attr('disabled', true);
                    $('#question-answer-comment-votes--' + pk).css('color', '#c3212a');
                }
            });
        }
    }
});
