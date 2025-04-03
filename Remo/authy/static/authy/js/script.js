// Switch displays between login and registration forms

document.getElementById('to_register').addEventListener('click', function() {
    document.getElementById('login_').classList.add('hidden');
    document.getElementById('registration_').classList.remove('hidden');
});

document.getElementById('to_login').addEventListener('click', function() {
    document.getElementById('registration_').classList.add('hidden');
    document.getElementById('login_').classList.remove('hidden');
});

// Register input, remove errors if user update input

document.querySelector('#login_password_input').addEventListener('blur', function() {
    let form_error = document.querySelector('#form_error_login_Username')
    form_error.innerHTML = '';
});
document.querySelector('#login_password_input').addEventListener('blur', function() {
    let form_error = document.querySelector('#form_error_login_Password')
    form_error.innerHTML = '';
});

// Register input, remove errors if user update input

document.querySelector('#reg_username_input').addEventListener('blur', function() {
    let form_error = document.querySelector('#form_error_registration_Username')
    form_error.innerHTML = '';
});
document.querySelector('#reg_email_input').addEventListener('blur', function() {
    let form_error = document.querySelector('#form_error_registration_Email')
    form_error.innerHTML = '';
});

// Check Password and Confirm password by cofirm password input

document.querySelector('#reg_confirm_password_input').addEventListener('blur', function() {
    let password = document.querySelector('#reg_password_input')
    let confirm_password = document.querySelector('#reg_confirm_password_input')

    if (password.value != confirm_password.value) {
        let form_error = document.getElementById(`form_error_registration_ConfPass`);
        form_error.innerHTML = `Passwords do not match.`;
    } else {
        let form_error = document.getElementById(`form_error_registration_ConfPass`);
        form_error.innerHTML = ``;
    }
});

// Check Password and Confirm password by password input

document.querySelector('#reg_password_input').addEventListener('blur', function() {
    let password = document.querySelector('#reg_password_input')
    let confirm_password = document.querySelector('#reg_confirm_password_input')

    if (password.value != confirm_password.value) {
        let form_error = document.getElementById(`form_error_registration_ConfPass`);
        form_error.innerHTML = `Passwords do not match.`;
    } else {
        let form_error = document.getElementById(`form_error_registration_ConfPass`);
        form_error.innerHTML = ``;
    }
});
