document.addEventListener('alpine:init', () => {
    if (window.location.pathname === '/profile/') {
        document.getElementById('updateProfile').style.display = 'block';
    } else {
        document.getElementById('updateProfile').style.display = 'none';
    }
});

document.getElementById('updateProfileLink').addEventListener('click', function () {
    const profileLocationEls = document.querySelectorAll('.profileLocation');
    const userAboutEls = document.querySelectorAll('.profileBio');
    const updateUserLocationEls = document.querySelectorAll('.updateUserLocation');
    const updateUserAboutEls = document.querySelectorAll('.updateUserAbout');
    const submitFormBtn = document.querySelectorAll('.FormSubmitBtn');

    const isEditing = this.textContent === 'Cancel';

    this.textContent = isEditing ? 'Update profile' : 'Cancel';

    profileLocationEls.forEach(el => el.classList.toggle('hidden'));
    userAboutEls.forEach(el => el.classList.toggle('hidden'));
    updateUserLocationEls.forEach(el => el.classList.toggle('hidden'));
    updateUserAboutEls.forEach(el => el.classList.toggle('hidden'));
    submitFormBtn.forEach(el => el.classList.toggle('hidden'));
});
