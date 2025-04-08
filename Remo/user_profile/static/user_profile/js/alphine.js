document.addEventListener('alpine:init', () => {

    document.body.addEventListener('htmx:afterSwap', function(event) {
        var response = event.detail.xhr.response;
        try {
            var jsonResponse = JSON.parse(response);
            if (jsonResponse.status === 'success') {
                let newLocation = jsonResponse.location
                let newBio = jsonResponse.bio
                console.log('success', newLocation, newBio)

                const profileLocationEls = document.querySelectorAll('.profileLocation');
                const userAboutEls = document.querySelectorAll('.profileBio');
                const updateUserLocationEls = document.querySelectorAll('.updateUserLocation');
                const updateUserAboutEls = document.querySelectorAll('.updateUserAbout');
                const submitFormBtn = document.querySelectorAll('.FormSubmitBtn');
                const updateProfileLine = document.querySelectorAll('#updateProfileLink')
                const isEditing = updateProfileLine[0].textContent === 'Cancel';  // Получаем первый элемент            
                profileLocationEls.forEach(el => {
                    el.textContent = newLocation;
                    el.classList.toggle('hidden');
                });
            
                userAboutEls.forEach(el => {
                    el.textContent = newBio;
                    el.classList.toggle('hidden');
                });
                updateProfileLine.forEach(el => {
                    el.textContent = isEditing ? 'Update profile' : 'Cancel';
                });            
                updateUserLocationEls.forEach(el => el.classList.toggle('hidden'));
                updateUserAboutEls.forEach(el => el.classList.toggle('hidden'));
                submitFormBtn.forEach(el => el.classList.toggle('hidden'));
            }
    
        } catch (e) {
            console.error('An error while json rendered ', e);
        }
    });
});

