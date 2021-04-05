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
        // If 'vote up' button is disabled, means the user voted the question before.
        let votedBefore = voteUpButton.attr('disabled') === 'disabled';

        // AJAX POST
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
        let currentVotes = parseInt($('#question-votes')[0].innerText);  // Current vote number
        currentVotes--;  // Decrease votes by 1.

        if (votedBefore) {  // If user voted this question before:
            voteUpButton.attr('disabled', false);  // Enable the 'vote up' button.
            voteUpButton.css('color', '#bbc0c4');  // Change 'vote up' buttons color to grey.
        } else {  // If user didn't vote this question before:
            $(this).attr('disabled', true);  // Disable the 'vote down' button.
            $('.question-vote-down').css('color', '#c3212a');  // Change 'vote up' buttons color to green.
        }

        $(`#question-votes`)[0].innerText = currentVotes;  // Change the vote number to current.
    });

    // VOTE QUESTION COMMENT UP
    const questionCommentVoteButtonsUp = $('.question-comment-vote-button-up');  // Get all 'vote up' buttons.
    if (questionCommentVoteButtonsUp.length > 0) {  // If there is any 'vote up' button:
        for (let questionCommentVoteButtonsUpElement of questionCommentVoteButtonsUp) {
            let pk = questionCommentVoteButtonsUpElement.id.split('--')[1];  // Question comments primary key is 'pk'.

            $('#question-comment-vote-button-up--' + pk).click(function () {
                let voteDownButton = $('#question-comment-vote-button-down--' + pk);  // Select specific 'vote down' button using 'pk'.
                // If 'vote down' button is disabled, means the user has already voted the question comment before.
                let votedBefore = voteDownButton.attr('disabled') === 'disabled';

                //AJAX POST
                $.ajax({
                   url: '',
                   type: 'post',
                   data: {
                       type: 'vote_up',
                       object: 'question_comment',
                       pk: pk,  // Specifies the 'pk' for proper saving.
                       voted_before: votedBefore,
                       csrfmiddlewaretoken: csrf
                   }
                });

                // Get the element that displays current comment score:
                let currVotesObj = $('#question-comment-votes-text--' + pk)[0]
                // Get that elements inner text, which is number or blank. (Blank means 0).
                let currentVotes = currVotesObj.innerText;
                let currentVoteNumber = 0;

                if (currentVotes === '') {
                    // If innerText is blank, comment has 0 vote score.
                    currentVoteNumber = 0;
                } else {
                    // Else get the vote score as integer.
                    currentVoteNumber = parseInt(currentVotes);
                }
                currentVoteNumber++;  // Increase the votes by 1.

                if (currentVoteNumber === 0) {
                    // After increasing the votes, if vote score is 0, score needs to displayed as blank:
                    currVotesObj.innerText = '';
                } else {
                    // Else display final score:
                    currVotesObj.innerText = currentVoteNumber;
                }

                if (votedBefore) {  // If comment voted before:
                    voteDownButton.attr('disabled', false);  // Enable the 'vote down' button'.
                    // Change the score numbers color to grey:
                    $('#question-comment-votes-text--' + pk).css('color', '#bbc0c4');
                } else {
                    $(this).attr('disabled', true);  // Disable the 'vote up' button.
                    // Change the score numbers color to green:
                    $('#question-comment-votes-text--' + pk).css('color', '#32a246');
                }
            });
        }
    }

    // VOTE QUESTION COMMENT DOWN
    const questionCommentVoteButtonsDown = $('.question-comment-vote-button-down'); // Get all 'vote down' buttons.
    if (questionCommentVoteButtonsDown.length > 0) {  // If there is any 'vote down' button:
        for (let questionCommentVoteButtonsDownElement of questionCommentVoteButtonsDown) {
            let pk = questionCommentVoteButtonsDownElement.id.split('--')[1];  // Question comments primary key is 'pk'.

            $('#question-comment-vote-button-down--' + pk).click(function () {

                let voteUpButton = $('#question-comment-vote-button-up--' + pk);  // Select specific 'vote down' button using 'pk'.
                // If 'vote down' button is disabled, means the user voted the question comment before.
                let votedBefore = voteUpButton.attr('disabled') === 'disabled';

                //AJAX POST
                $.ajax({
                   url: '',
                   type: 'post',
                   data: {
                       type: 'vote_down',
                       object: 'question_comment',
                       pk: pk,  // Specifies the 'pk' for proper saving.
                       voted_before: votedBefore,
                       csrfmiddlewaretoken: csrf
                   }
                });

                // Get the element that displays current comment score:
                let currVotesObj = $('#question-comment-votes-text--' + pk)[0]
                // Get that elements inner text, which is number or blank. (Blank means 0).
                let currentVotes = currVotesObj.innerText;
                let currentVoteNumber = 0;

                if (currentVotes === '') {
                    // If innerText is blank, comment has 0 vote score.
                    currentVoteNumber = 0;
                } else {
                    // Else get the vote score as integer.
                    currentVoteNumber = parseInt(currentVotes);
                }
                currentVoteNumber--; // Decrease the votes by 1.

                if (currentVoteNumber === 0) {
                    // After increasing the votes, if vote score is 0, score needs to displayed as blank:
                    currVotesObj.innerText = '';
                } else {
                    // Else display final score:
                    currVotesObj.innerText = currentVoteNumber;
                }

                if (votedBefore) {  // If comment voted before:
                    voteUpButton.attr('disabled', false);  // Enable the 'vote up' button'.
                    // Change the score numbers color to grey:
                    $('#question-comment-votes-text--' + pk).css('color', '#bbc0c4');

                } else {
                    $(this).attr('disabled', true);  // Disable the 'vote down' button.
                    // Change the score numbers color to red:
                    $('#question-comment-votes-text--' + pk).css('color', '#c3212a');
                }
            });
        }
    }
    // VOTE ANSWERS
    const answerVoteUpButtons = $('.question-answer-vote-button-up');  // Get all 'vote up' buttons.
    const answerVoteDownButtons = $('.question-answer-vote-button-down');  // Get all 'vote down' buttons.

    // VOTE ANSWER UP
    if (answerVoteUpButtons.length > 0) {  // If there is any 'vote up' button:
        for (let answerVoteUpButton of answerVoteUpButtons) {
            let pk = answerVoteUpButton.id.split('--')[1];  // Answers primary key is 'pk'.

            $('#question-answer-vote-button-up--' + pk).click(function () {
                let voteDownButton = $('#question-answer-vote-button-down--' + pk);  // Select specific 'vote down' button using 'pk'.
                // If 'vote down' button is disabled, means the user has already voted the answer before:
                let votedBefore = voteDownButton.attr('disabled') === 'disabled';

                //AJAX POST
                $.ajax({
                    url: '',
                    type: 'post',
                    data: {
                        type: 'vote_up',
                        object: 'answer',
                        pk: pk,  // Specifies the 'pk' for proper saving.
                        voted_before: votedBefore,
                        csrfmiddlewaretoken: csrf
                    }
                });
                // Get the current votes:
                let currentVotes = parseInt($('#question-answer-votes--' + pk)[0].innerText);
                currentVotes++;  // Increase the votes by 1.

                if (votedBefore) {  // If answer voted before:
                    voteDownButton.attr('disabled', false);  // Enable the 'vote down' button'.
                    // Change the score 'vote down' buttons color to grey:
                    voteDownButton.css('color', '#bbc0c4');
                } else {
                    $(this).attr('disabled', true);  // Disable the 'vote up' button.
                    // Change the score 'vote up' buttons color to green:
                    $('#question-answer-vote-button-up--' + pk).css('color', '#32a246');
                }

                $(`#question-answer-votes--` + pk)[0].innerText = currentVotes;  // Change the vote number to current.
            });
        }
    }

    // VOTE ANSWER DOWN
    if (answerVoteDownButtons.length > 0) {  // If there is any 'vote down' button:
        for (let answerVoteDownButton of answerVoteDownButtons) {
            let pk = answerVoteDownButton.id.split('--')[1];  // Answers primary key is 'pk'.

            $('#question-answer-vote-button-down--' + pk).click(function () {
                let voteUpButton = $('#question-answer-vote-button-up--' + pk);  // Select specific 'vote down' button using 'pk'.
                // If 'vote down' button is disabled, means the user has already voted the answer before:
                let votedBefore = voteUpButton.attr('disabled') === 'disabled';

                //AJAX POST
                $.ajax({
                    url: '',
                    type: 'post',
                    data: {
                        type: 'vote_down',
                        object: 'answer',
                        pk: pk,  // Specifies the 'pk' for proper saving.
                        voted_before: votedBefore,
                        csrfmiddlewaretoken: csrf
                    }
                });
                // Get the current votes:
                let currentVotes = parseInt($('#question-answer-votes--' + pk)[0].innerText);
                currentVotes--;  // Decrease the votes by 1.

                if (votedBefore) {  // If answer voted before:
                    voteUpButton.attr('disabled', false);  // Enable the 'vote up' button'.
                    // Change the score 'vote down' buttons color to grey:
                    voteUpButton.css('color', '#bbc0c4');
                } else {
                    $(this).attr('disabled', true);  // Disable the 'vote down' button.
                    // Change the score 'vote up' buttons color to red:
                    $('#question-answer-vote-button-down--' + pk).css('color', '#c3212a');
                }

                $(`#question-answer-votes--` + pk)[0].innerText = currentVotes;  // Change the vote number to current.
            })
        }
    }

    // VOTE ANSWER COMMENTS
    const answerCommentUpButtons = $('.question-answer-comment-vote-button-up');  // Get all 'vote up' buttons.
    const answerCommentDownButtons = $('.question-answer-comment-vote-button-down');  // Get all 'vote down' buttons.

    // VOTE ANSWER COMMENT UP
    if (answerVoteUpButtons.length > 0) {  // If there is any 'vote up' button:
        for (let answerCommentUpButton of answerCommentUpButtons) {
            let pk = answerCommentUpButton.id.split('--')[1];  // Answer comments primary key is 'pk'.

            $('#question-answer-comment-vote-button-up--' + pk).click(function () {

                let voteDownButton = $('#question-answer-comment-vote-button-down--' + pk);  // Select specific 'vote down' button using 'pk'.
                // If 'vote down' button is disabled, means the user has already voted the answer comment before.
                let votedBefore = voteDownButton.attr('disabled') === 'disabled';

                //AJAX POST
                $.ajax({
                   url: '',
                   type: 'post',
                   data: {
                       type: 'vote_up',
                       object: 'answer_comment',
                       pk: pk,  // Specifies the 'pk' for proper saving.
                       voted_before: votedBefore,
                       csrfmiddlewaretoken: csrf
                   }
                });

                // Get the element that displays current comment score:
                let currVotesObj = $('#question-answer-comment-votes--' + pk)[0];
                // Get that elements inner text, which is number or blank. (Blank means 0).
                let currentVotes = currVotesObj.innerText;
                let currentVoteNumber = 0;

                if (currentVotes === '') {
                    // If innerText is blank, comment has 0 vote score.
                    currentVoteNumber = 0;
                } else {
                    // Else get the vote score as integer.
                    currentVoteNumber = parseInt(currentVotes);
                }
                currentVoteNumber++;  // Increase the votes by 1.

                if (currentVoteNumber === 0) {
                    // After increasing the votes, if vote score is 0, score needs to displayed as blank:
                    currVotesObj.innerText = '';
                } else {
                    // Else display final score:
                    currVotesObj.innerText = currentVoteNumber;
                }

                if (votedBefore) {  // If comment voted before:
                    voteDownButton.attr('disabled', false);  // Enable the 'vote down' button'.
                    // Change the score numbers color to grey:
                    $('#question-answer-comment-votes--' + pk).css('color', '#bbc0c4');
                } else {
                    $(this).attr('disabled', true);  // Disable the 'vote up' button.
                    // Change the score numbers color to green:
                    $('#question-answer-comment-votes--' + pk).css('color', '#32a246');
                }
            });
        }
    }

    // VOTE ANSWER COMMENT DOWN
    if (answerCommentDownButtons.length > 0) {  // If there is any 'vote down' button:
        for (let answerCommentDownButton of answerCommentDownButtons) {
            let pk = answerCommentDownButton.id.split('--')[1];  // Answer comments primary key is 'pk'.

            $('#question-answer-comment-vote-button-down--' + pk).click(function () {

                let voteUpButton = $('#question-answer-comment-vote-button-up--' + pk);  // Select specific 'vote down' button using 'pk'.
                // If 'vote down' button is disabled, means the user voted the answer comment before.
                let votedBefore = voteUpButton.attr('disabled') === 'disabled';

                //AJAX POST
                $.ajax({
                   url: '',
                   type: 'post',
                   data: {
                       type: 'vote_down',
                       object: 'answer_comment',
                       pk: pk,  // Specifies the 'pk' for proper saving.
                       voted_before: votedBefore,
                       csrfmiddlewaretoken: csrf
                   }
                });

                // Get the element that displays current comment score:
                let currVotesObj = $('#question-answer-comment-votes--' + pk)[0];
                // Get that elements inner text, which is number or blank. (Blank means 0).
                let currentVotes = currVotesObj.innerText;
                let currentVoteNumber = 0;

                if (currentVotes === '') {
                    // If innerText is blank, comment has 0 vote score.
                    currentVoteNumber = 0;
                } else {
                    // Else get the vote score as integer.
                    currentVoteNumber = parseInt(currentVotes);
                }
                currentVoteNumber--;  // Decrease the votes by 1.

                if (currentVoteNumber === 0) {
                    // After increasing the votes, if vote score is 0, score needs to displayed as blank:
                    currVotesObj.innerText = '';
                } else {
                    // Else display final score:
                    currVotesObj.innerText = currentVoteNumber;
                }

                if (votedBefore) {  // If comment voted before:
                    voteUpButton.attr('disabled', false);  // Enable the 'vote up' button'.
                    // Change the score numbers color to grey:
                    $('#question-answer-comment-votes--' + pk).css('color', '#bbc0c4');
                } else {
                    $(this).attr('disabled', true);  // Disable the 'vote down' button.
                    // Change the score numbers color to red:
                    $('#question-answer-comment-votes--' + pk).css('color', '#c3212a');
                }
            });
        }
    }

    // Slide for question comment section:
    $('#add-question-comment').click(function () {  // When clicked 'Add a comment' button,
        $(this).slideUp('fast');  // Slide up the 'Add a comment' button,
        $('#add-question-comment-area').slideDown();  // Slide down the 'comment' input.
        $('#add-question-comment-input').focus();  // Focus to the input.
    });

    // Slide for answer comment sections:
    let addAnswerCommentButtons = $('.add-answer-comment');  // Get all 'answer comment' buttons.

    for (let addAnswerCommentButton of addAnswerCommentButtons) {
        let pk = addAnswerCommentButton.id.split('--')[1];  // Get 'primary key' of the button.

        $('#add-answer-comment--' + pk).click(function () {  // When clicked 'Add a comment' button with specified 'pk',
            $(this).slideUp('fast');  // Slide up the 'Add a comment' button,
            $('#add-answer-comment-area--' + pk).slideDown();  // Slide down the 'comment' input with specified 'pk'.
        });
    }

    // ADD QUESTION COMMENT
    $('#add-question-comment-submit').click(function () {
        let commentBody = $('#add-question-comment-input')[0].value;  // Get the inputs content.

        if (commentBody.length < 3) {
            // If comment is less than 3 characters, create error message:
            let errorMessage = document.createElement('i');
            errorMessage.innerText = 'Comment must be at least 3 characters.';
            errorMessage.className = 'add-question-comment-error-message'

            $('#add-question-comment-add')[0].appendChild(errorMessage);  // Display the error message.
            // Change the inputs border color to red:
            $('#add-question-comment-input').css('border-color', 'red');
            $('#add-question-comment-input').focus();  // Focus to the input:
        } else {
            if ($('.add-question-comment-error-message').length > 0) {
                // If there is error message:
                $('.add-question-comment-error-message').remove();  // Remove the error message,
                // Change the inputs border color to the origin:
                $('#add-question-comment-input').css('border-color', '#bdc3c9');
            }

            // AJAX POST
            $.ajax({
                url: '',
                type: 'post',
                data: {
                    type: 'comment',
                    object: 'question_comment',
                    content: commentBody,
                    csrfmiddlewaretoken: csrf
                },
                success: function (response) {
                    // Clone the first comment element to display:
                    let newComment = $('.question-comment')[0].cloneNode(true);
                    newComment.children[0].children[0].innerText = '';  // It has 0 votes.
                    newComment.children[1].children[0].innerText = response.comment;  // Comment body.
                    newComment.children[1].children[1].innerText = response.user;  // Username of the user.
                    newComment.children[1].children[2].innerText = response.date;  // Post date which is now.

                    // Append modified element to bottom:
                    $('#question-comments-area')[0].appendChild(newComment);
                    // Slide the input area up:
                    $('#add-question-comment-area').slideUp();
                    // Slide the 'add a comment' button down:
                    $('#add-question-comment').slideDown();
                }
            });
        }

    });

    // ADD ANSWER COMMENT

    let answerCommentButtons = $('.add-answer-comment-submit');

    for (let answerCommentButton of answerCommentButtons) {
        let pk = answerCommentButton.id.split('--')[1];

        $('#add-answer-comment-submit--' + pk).click(function () {
            let commentBody = $('#add-answer-comment-input--' + pk)[0].value;  // Get the inputs content.

            if (commentBody.length < 3) {
                // If comment is less than 3 characters, create error message:
                let errorMessage = document.createElement('i');
                errorMessage.innerText = 'Comment must be at least 3 characters.';
                errorMessage.className = 'add-question-comment-error-message'

                $('#add-answer-comment-add--' + pk)[0].appendChild(errorMessage);  // Display the error message.
                // Change the inputs border color to red:
                $('#add-answer-comment-input--' + pk).css('border-color', 'red');
                $('#add-answer-comment-input--' + pk).focus();  // Focus to the input:
            } else {
                if ($('.add-question-comment-error-message').length > 0) {
                    // If there is error message:
                    $('.add-question-comment-error-message').remove();  // Remove the error message,
                    // Change the inputs border color to the origin:
                    $('#add-answer-comment-input--' + pk).css('border-color', '#bdc3c9');
                }

                // AJAX POST
                $.ajax({
                    url: '',
                    type: 'post',
                    data: {
                        type: 'comment',
                        object: 'answer_comment',
                        pk: pk,
                        content: commentBody,
                        csrfmiddlewaretoken: csrf
                    },
                    success: function (response) {
                        // Clone the first comment element to display:
                        let newComment = $('.question-comment')[0].cloneNode(true);
                        newComment.children[0].children[0].innerText = '';  // It has 0 votes.
                        newComment.children[1].children[0].innerText = response.comment;  // Comment body.
                        newComment.children[1].children[1].innerText = response.user;  // Username of the user.
                        newComment.children[1].children[2].innerText = response.date;  // Post date which is now.

                        // Append modified element to bottom:
                        $('#answer-comments-area--' + pk)[0].appendChild(newComment);
                        // Slide the input area up:
                        $('#add-answer-comment-area--' + pk).slideUp();
                        // Slide the 'add a comment' button down:
                        $('#add-answer-comment--' + pk).slideDown();
                    }
                });
            }
        });
    }

    $('#add-answer-button').click(function () {
        $.post({
            url: '',
            type: 'POST',
            data: {
                type: 'answer',
                content: richTextField.document.body.innerHTML,
                csrfmiddlewaretoken: csrf
            },
            success: location.reload()
        });
    });
});

function setBestAnswer(answer_pk) {
    $.ajax({
        url: '',
        type: 'POST',
        data: {
            type: 'set_best_answer',
            pk: answer_pk,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function (response) {
            if (response.data === 'success') {
                $('#unset_best_answer--' + answer_pk.toString()).css('display', 'block');
                $('#set-best-answer--' + answer_pk.toString()).css('display', 'none');
            }
        }
    });
}

function unsetBestAnswer(answer_pk) {
    $.ajax({
        url: '',
        type: 'POST',
        data: {
            type: 'unset_best_answer',
            pk: answer_pk,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function (response) {
            if (response.data === 'success') {
                $('#unset_best_answer--' + answer_pk.toString()).css('display', 'none');
                $('#set-best-answer--' + answer_pk.toString()).css('display', 'block');
            }
        }
    });
}

$('.add-comment-area').slideUp('fast');  // Slide all comment inputs up at start.

for (code of $('font')) {
    code.parentNode.style.backgroundColor = '#f6f6f6'
}

