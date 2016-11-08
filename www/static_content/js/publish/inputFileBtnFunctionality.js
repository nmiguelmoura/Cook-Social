cookSocial.InputFileBtnFunctionality = (function () {
    'use strict';

    function InputFileBtnFunctionality(type, btn, image, fileNameParagraph) {
        this._type = type || 'image';
        this._btn = btn;
        this._image = image;
        this._fileNameParagraph = fileNameParagraph;

        this.IMAGE_EXTENSIONS = ['png', 'jpg', 'gif'];
        this.RED_EXTENSIONS = [];

        this._init();
    }

    InputFileBtnFunctionality.prototype._displayImage = function (input) {
        console.log(input.files);

        if (input.files && input.files[0]) {
            var fileReader = new FileReader();
            fileReader.readAsDataURL(input.files[0]);

            fileReader.addEventListener('load', function (event) {
                var result = event.target.result;
                this._image.src = result;
            }.bind(this), false);
        }
    };

    InputFileBtnFunctionality.prototype._checkFileExtension = function (extension) {
        var extensionsToCheck;

        if (this._type === 'image') {
            extensionsToCheck = this.IMAGE_EXTENSIONS;
        } else if (this._type === 'red') {
            extensionsToCheck = this.RED_EXTENSIONS;
        }

        var i, length = extensionsToCheck.length;
        for (i = 0; i < length; i++) {
            if (extension === extensionsToCheck[i]) {
                return true;
            }
        }
        return false;
    };

    InputFileBtnFunctionality.prototype._getFileProperties = function (path) {
        var fileName = path.split("fakepath")[1],
            extension = fileName.split('.')[1];

        return {
            fileName: fileName,
            extension: extension
        }
    };

    InputFileBtnFunctionality.prototype._btnChanged = function (event) {
        var path = event.currentTarget.value,
            properties = this._getFileProperties(path);

        var extensionAllowed = this._checkFileExtension(properties.extension);

        if (extensionAllowed) {
            //this._fileNameParagraph.innerHTML='<b>Ficheiro:</b> '+properties.fileName;
            if (this._type === 'image') {
                this._displayImage(event.currentTarget);
            }
        }
        else {
            event.currentTarget.value = '';
            alert('Submeta um ficheiro de imagem válido (*.jpg, *.png, *.gif)');
        }
    };

    InputFileBtnFunctionality.prototype._init = function () {
        this._btn.addEventListener('change', this._btnChanged.bind(this), false);
    };

    return InputFileBtnFunctionality;
})();