document.addEventListener('alpine:init', () => {
    

    Alpine.data('formValidation', () => ({
        successMessage: '',
        errorMessage: '',
        LgNameError: '',
        LgPassError: '',
        RegNameError: '',
        RegEmailError: '',
        RegPassError: '',
        RegConfPassError: '',
        isLoginFormValid: false,
        isRegisterFormValid: false,
        lg_username: '',
        lg_password: '',
        reg_username: '',
        reg_email: '',
        reg_password: '',
        reg_confirm_password: '',
        
        validateLoginForm() {
            if (this.lg_password && this.lg_username) {
                this.isLoginFormValid = true;
            } else {
                this.isLoginFormValid = false;
                this.errorMessage = 'This field is required.';
            }
        },

        validateLoginUsername() {
            if (this.lg_username) {
                this.LgNameError = '';
            } else {
                this.LgNameError = 'Username field is required.';
            }
        },

        validateLoginPassword() {
            if (this.lg_password) {
                this.LgPassError = '';
            } else {
                this.LgPassError = 'Password field is required.';
            }
        },

        validateRegisterForm() {
            if (this.reg_username && this.reg_email && this.reg_password && this.reg_confirm_password) {
                this.isRegisterFormValid = true;
            } else {
                this.isRegisterFormValid = false;
                this.errorMessage = 'This field is required.';
            }
        },
        validateRegUsername() {
            if (this.lg_username) {
                this.RegNameError = '';
            } else {
                this.RegNameError = 'Username field is required.';
            }
        },
        validateRegEmail() {
            if (this.lg_username) {
                this.RegEmailError = '';
            } else {
                this.RegEmailError = 'Email field is required.';
            }
        },
        validateRegPass() {
            if (this.lg_username) {
                this.RegPassError = '';
            } else {
                this.RegPassError = 'Password field is required.';
            }
        },
        validateRegConfPass() {
            if (this.lg_username) {
                this.RegConfPassError = '';
            } else {
                this.RegConfPassError = 'Confirm Password field is required.';
            }
        },

    }));

    document.body.addEventListener('htmx:afterSwap', function(event) {
        var response = event.detail.xhr.response;
        try {
            var jsonResponse = JSON.parse(response);
            if (jsonResponse.status === 'success' && jsonResponse.redirect) {
                window.location.href = jsonResponse.redirect;
            }
            if (jsonResponse.type == 'login') {
                let form_error = document.getElementById(`form_error_login_${jsonResponse.error_field}`);
                let errorMessage = JSON.parse(response).error

                form_error.innerHTML = `<p>${errorMessage}</p>`;
            }
            if (jsonResponse.type == 'registration') {
                console.log('obj:', `form_error_registration_${jsonResponse.error_field}`,document.getElementById(`form_error_registration_${jsonResponse.error_field}`), JSON.parse(response))
                let form_error = document.getElementById(`form_error_registration_${jsonResponse.error_field}`);
                let errorMessage = JSON.parse(response).error

                form_error.innerHTML = `<p>${errorMessage}</p>`;
            }
    
        } catch (e) {
            console.error('An error while json rendered ', e);
        }
    });
});

