/**
 * Created by Nuno Machado on 20/09/16.
 */

cookSocial.PopupBar = (function () {
    'use strict';

    function PopupBar() {
        this._popupIsVisible = false;
        this._init();
    }

    PopupBar.prototype._backgroundAction = function (event) {
        // Hides popup bar.
        this._hidePopup();
    };

    PopupBar.prototype._disableBackground = function () {
        // Disables darken background inputs and hides it.
        this._background.style.display = 'none';
        this._background.removeEventListener('click', this._backgroundActionEventBinding, false);
    };

    PopupBar.prototype._enableBackground = function () {
        // Disables darken background inputs and shows it.
        this._background.style.display = 'block';

        // This var allows to add and remove listeners.
        this._backgroundActionEventBinding = this._backgroundActionEventBinding || this._backgroundAction.bind(this);
        this._background.addEventListener('click', this._backgroundActionEventBinding, false);
    };

    PopupBar.prototype._changeButtonStyle = function (style) {
        // Change classname to reflect on or off button state.
        // CSS class changes background image and color accordingly.
        this._button.className = "col-sm-2-12 col-md-1-12 menu-btn menu-btn-" + style;
    };

    PopupBar.prototype._hidePopup = function () {
        if (this._popupIsVisible) {
            // If popup bar is visible, hide it.
            this._popupIsVisible = false;
            this._popupBar.style.display = 'none';

            // Change class name.
            this._changeButtonStyle('off');
            // Hide darken background.
            this._disableBackground();
        }
    };

    PopupBar.prototype._showPopup = function () {
        if (!this._popupIsVisible) {
            // If popup is not visible, show it.
            this._popupIsVisible = true;
            this._popupBar.style.display = 'block';

            // Change class name.
            this._changeButtonStyle('on');

            // Show darken background.
            this._enableBackground();
        }
    };

    PopupBar.prototype._buttonAction = function (event) {
        var elementClicked = event.currentTarget,
            tagExpected = 'DIV';

        if (elementClicked && elementClicked.tagName === tagExpected) {
            // Run only if clicked element is the expected element
            if (!this._popupIsVisible) {
                // If popup bar is hidden, show it.
                this._showPopup();
            } else {
                // If popup bar is shown, hide it.
                if (this._popupIsVisible) {
                    // If clicked btn is the same as active tab, hide it.
                    // This allows to add more buttons in future if needed.
                    this._hidePopup();
                }
            }
        }
    };

    PopupBar.prototype._addListeners = function () {
        // Adds event to menu button.
        this._button.addEventListener('click', this._buttonAction.bind(this), false);
    };

    PopupBar.prototype._getButtonReference = function () {
        // Get reference to menu btn.
        this._button = document.getElementsByClassName('menu-btn')[0];
    };

    PopupBar.prototype._getPopupReferences = function () {
        //Get reference to popup bar.
        this._popupBar = document.getElementsByTagName('nav')[0];

        // Get reference to darken background div.
        this._background = document.getElementsByClassName('fade-background')[0];
    };

    PopupBar.prototype._init = function () {
        // Get reference to popup bar.
        this._getPopupReferences();

        // Get reference to menu button.
        this._getButtonReference();

        // Add listeners to menu button.
        this._addListeners();
    };

    return PopupBar;
})();
