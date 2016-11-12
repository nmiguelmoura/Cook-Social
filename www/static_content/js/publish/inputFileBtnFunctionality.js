cookSocial.InputFileBtnFunctionality = (function () {
    'use strict';

    function InputFileBtnFunctionality(type, btn, image) {
        // Sets the type of input expected. This allows to add new functionality in future.
        this._type = type || 'image';

        this._btn = btn;
        this._image = image;

        // Allowed extensions.
        this.IMAGE_EXTENSIONS = ['png', 'jpg', 'gif'];

        this._init();
    }

    InputFileBtnFunctionality.prototype._displayImage = function (input) {
        if (input.files && input.files[0]) {
            // Read uploaded file.
            var fileReader = new FileReader();
            fileReader.readAsDataURL(input.files[0]);

            fileReader.addEventListener('load', function (event) {
                // When file is loaded, display it on image tag.
                var result = event.target.result;
                this._image.src = result;
            }.bind(this), false);
        }
    };

    InputFileBtnFunctionality.prototype._checkFileExtension = function (extension) {
        var extensionsToCheck;

        if (this._type === 'image') {
            // If it is an image, check allowed extensions.
            extensionsToCheck = this.IMAGE_EXTENSIONS;
        }

        var i, length = extensionsToCheck.length;
        for (i = 0; i < length; i++) {
            // Loop through extensions.
            if (extension === extensionsToCheck[i]) {
                // If given extension is allowed, return True
                return true;
            }
        }

        // Return false if file extension is not allowed
        return false;
    };

    InputFileBtnFunctionality.prototype._getFileProperties = function (path) {
        // Get filename. Remove fakepath from file path.
        var fileName = path.split("fakepath")[1],
            // Get extension spliting on point value.
            extension = fileName.split('.')[1];

        // Return filename and extension.
        return {
            fileName: fileName,
            extension: extension
        }
    };

    InputFileBtnFunctionality.prototype._btnChanged = function (event) {
        // Run if input file btn has changed.

        // Get upload file path.
        var path = event.currentTarget.value,
            // Get filename and extension.
            properties = this._getFileProperties(path);

        // Check if extension is allowed.
        var extensionAllowed = this._checkFileExtension(properties.extension);

        if (extensionAllowed) {
            // Run if extension is allowed.
            if (this._type === 'image') {
                // If type matches image, get it and display it.
                this._displayImage(event.currentTarget);
            }
        }
        else {
            event.currentTarget.value = '';
            alert('Submeta um ficheiro de imagem válido (*.jpg, *.png, *.gif)');
        }
    };

    InputFileBtnFunctionality.prototype._init = function () {
        // Add listener to input file button.
        this._btn.addEventListener('change', this._btnChanged.bind(this), false);
    };

    return InputFileBtnFunctionality;
})();