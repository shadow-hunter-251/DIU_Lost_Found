const mobileMenuButton = document.getElementById(
    'mobile-menu-button'
);

const mobileMenu = document.getElementById(
    'mobile-menu'
);

if (mobileMenuButton && mobileMenu) {

    mobileMenuButton.addEventListener(
        'click',
        function () {

            mobileMenu.classList.toggle(
                'hidden'
            );

        }
    );

}


console.log("DIU Lost & Found loaded");


const imageInput = document.querySelector(
    'input[type="file"][name="image"]'
);

const imagePreviewContainer = document.getElementById(
    'image-preview-container'
);

const imagePreview = document.getElementById(
    'image-preview'
);


if (imageInput && imagePreviewContainer && imagePreview) {

    imageInput.addEventListener('change', function () {

        const file = this.files[0];

        if (!file) {

            imagePreviewContainer.classList.add('hidden');

            return;

        }


        const reader = new FileReader();


        reader.onload = function (event) {

            imagePreview.src = event.target.result;

            imagePreviewContainer.classList.remove(
                'hidden'
            );

        };


        reader.readAsDataURL(file);

    });

}
