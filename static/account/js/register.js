$(document).ready(function () {
    const csrf = $('input[name=csrfmiddlewaretoken]').val();

    $('#id_username').keydown(function () {
        let $field = $(this);

        setTimeout(function() {
            let username = $field.val();
            if (username.length > 3) {
                $.ajax({
                    url: '',
                    type: 'POST',
                    data: {
                        type: 'check_username',
                        data: username,
                        csrfmiddlewaretoken: csrf
                    },
                    success: function (response) {
                        if (response.result === 'available') {
                            $field.css('box-shadow', '0 0 0 0.2rem rgb(118 255 0 / 25%)');
                            document.getElementById('username-control').innerHTML = `<span class="username-control-available">"${username}" is available.</span>`;
                        } else {
                            $field.css('box-shadow', '0 0 0 0.2rem rgb(255 70 0 / 25%)');
                            document.getElementById('username-control').innerHTML = `<span class="username-control-unavailable">"${username}" is unavailable.</span>`;
                        }
                    }
                });
            } else if (username === '') {
                $field.css('box-shadow', '');
                document.getElementById('username-control').innerHTML = ``;
            } else {
                $field.css('box-shadow', '0 0 0 0.2rem rgb(255 70 0 / 25%)');
                document.getElementById('username-control').innerHTML = `<span class="username-control-unavailable">"${username}" is too short.</span>`;
            }
        }, 0);
    });

    $('#id_email').keydown(function () {
        let $field = $(this);

        setTimeout(function() {
            let email = $field.val();
            if (email.includes('@')) {
                $.ajax({
                    url: '',
                    type: 'POST',
                    data: {
                        type: 'check_email',
                        data: email,
                        csrfmiddlewaretoken: csrf
                    },
                    success: function (response) {
                        if (response.result === 'available') {
                            $field.css('box-shadow', '0 0 0 0.2rem rgb(118 255 0 / 25%)');
                            document.getElementById('email-control').innerHTML = `<span class="username-control-available">"${email}" is available.</span>`;
                        } else {
                            $field.css('box-shadow', '0 0 0 0.2rem rgb(255 70 0 / 25%)');
                            document.getElementById('email-control').innerHTML = `<span class="username-control-unavailable">"${email}" is unavailable.</span>`;
                        }
                    }
                });
            } else if (email === '') {
                $field.css('box-shadow', '');
                document.getElementById('email-control').innerHTML = ``;
            } else {
                $field.css('box-shadow', '0 0 0 0.2rem rgb(255 70 0 / 25%)');
                document.getElementById('email-control').innerHTML = `<span class="username-control-unavailable">"${email}" is not a valid email.</span>`;
            }
        }, 0);
    });

    $('#id_password1').keydown(function () {
        const numbers = /[0-9]/g;
        const upperCaseLetters = /[A-Z]/g;
        const lowerCaseLetters = /[a-z]/g;

        let username = $('#id_username').val();
        if (username === '') {
            username = null;
        }
        let email = $('#id_email').val();
        if (email === '') {
            email = null;
        }
        let $field = $(this);

        setTimeout(function() {
            let password = $field.val();

            if (password === '') {
                $('#password1-info').css('display', 'block')
                $field.css('box-shadow', '');
                document.getElementById('password1-control').innerHTML = ``;
            } else if (password.length < 8) {
                $('#password1-info').css('display', 'none')
                $field.css('box-shadow', '0 0 0 0.2rem rgb(255 70 0 / 25%)');
                document.getElementById('password1-control').innerHTML = `<span class="username-control-unavailable">Password is too short.</span>`;
            } else {
                $('#password1-info').css('display', 'none')
                if (password.includes(email)) {
                    $field.css('box-shadow', '0 0 0 0.2rem rgb(255 70 0 / 25%)');
                    document.getElementById('password1-control').innerHTML = `<span class="username-control-unavailable">Password cannot contains your email.</span>`;
                } else if (password.includes(username)) {
                    $field.css('box-shadow', '0 0 0 0.2rem rgb(255 70 0 / 25%)');
                    document.getElementById('password1-control').innerHTML = `<span class="username-control-unavailable">Password cannot contains your username.</span>`;
                } else {
                    if (! password.match(numbers)) {
                        $field.css('box-shadow', '0 0 0 0.2rem rgb(255 70 0 / 25%)');
                        document.getElementById('password1-control').innerHTML = `<span class="username-control-unavailable">Password must contain number.</span>`;
                    } else {
                        if (! password.match(upperCaseLetters)) {
                            $field.css('box-shadow', '0 0 0 0.2rem rgb(255 70 0 / 25%)');
                            document.getElementById('password1-control').innerHTML = `<span class="username-control-unavailable">Password must contain upper case character.</span>`;
                        } else if (! password.match(lowerCaseLetters)) {
                            $field.css('box-shadow', '0 0 0 0.2rem rgb(255 70 0 / 25%)');
                            document.getElementById('password1-control').innerHTML = `<span class="username-control-unavailable">Password must contain lower case character.</span>`;
                        } else {
                            $field.css('box-shadow', '0 0 0 0.2rem rgb(118 255 0 / 25%)');
                            document.getElementById('password1-control').innerHTML = `<span class="username-control-available">"Password is valid.</span>`;
                        }
                    }
                }

            }
        }, 0);
    });

    $('#id_password2').keydown(function () {
        let $field = $(this);

        setTimeout(function () {
            let password1 = $('#id_password1').val();
            let password2 = $field.val();

            if (password2 === '') {
                $('#password2-info').css('display', 'block');
                $field.css('box-shadow', '');
                document.getElementById('password2-control').innerHTML = ``;
            } else if (password2 === password1) {
                $('#password2-info').css('display', 'none');
                $field.css('box-shadow', '0 0 0 0.2rem rgb(118 255 0 / 25%)');
                document.getElementById('password2-control').innerHTML = `<span class="username-control-available">Passwords matches.</span>`;
            } else {
                $('#password2-info').css('display', 'none');
                $field.css('box-shadow', '0 0 0 0.2rem rgb(255 70 0 / 25%)');
                document.getElementById('password2-control').innerHTML = `<span class="username-control-unavailable">Passwords doesn't match.</span>`;
            }
        }, 0)
    });
});