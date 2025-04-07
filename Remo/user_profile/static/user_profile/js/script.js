document.getElementById('updateProfileLink').addEventListener('click', function () {
const profileLocationEls = document.querySelectorAll('.profileLocation');
const userAboutEls = document.querySelectorAll('.profileBio');
const updateUserLocationEls = document.querySelectorAll('.updateUserLocation');
const updateUserAboutEls = document.querySelectorAll('.updateUserAbout');

const isEditing = this.textContent === 'Cancel';

this.textContent = isEditing ? 'Update profile' : 'Cancel';

profileLocationEls.forEach(el => el.classList.toggle('hidden'));
userAboutEls.forEach(el => el.classList.toggle('hidden'));
updateUserLocationEls.forEach(el => el.classList.toggle('hidden'));
updateUserAboutEls.forEach(el => el.classList.toggle('hidden'));
});
