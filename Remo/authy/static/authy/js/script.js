document.getElementById('to_register').addEventListener('click', function() {
    document.getElementById('login_').classList.add('hidden');
    document.getElementById('registration_').classList.remove('hidden');
});

document.getElementById('to_login').addEventListener('click', function() {
    document.getElementById('registration_').classList.add('hidden');
    document.getElementById('login_').classList.remove('hidden');
});
