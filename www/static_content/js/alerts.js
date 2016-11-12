/**
 * Created by Nuno Machado on 22/09/16.
 */

cookSocial.Alerts = (function () {
    'use strict';

    // Alerts are launched in javascript (alert('message'))
    // This class capturesthe message and shows a custom alert window.

    function Alerts() {
        this._init();
        this._alert = null;
        this._message = null;
        this._button = null;
    }

    Alerts.prototype._buttonAction = function () {
        // Disable button after being pressed.
        this._disableButton();

        // Hides custom alert box.
        this._alert.style.display = 'none';
    };

    Alerts.prototype._disableButton = function () {
        // Removes listener to alert window button.
        this._button.removeEventListener('click', this._buttonEventBind, false);
    };

    Alerts.prototype._enableButton = function () {
        // Adds listener to alert window button.
        this._buttonEventBind = this._buttonAction.bind(this);
        this._button.addEventListener('click', this._buttonEventBind, false);
    };

    Alerts.prototype._showAlert = function (message) {
        if (this._alert === null) {
            // If this.alert does not exists, get reference to it.
            this._getAlertReferences();
        }

        if (this._alert) {
            // If alert exists, show captured message.
            this._message.innerHTML = message;

            // Enable alert window button.
            this._enableButton();

            // Show alert.
            this._alert.style.display = 'block';
        }
    };

    Alerts.prototype._overrideDefaultAlert = function () {
        // Override default browser alert window.
        window.alert = function (message) {
            // If alert is launched, capture message and show custom alert window.
            this._showAlert(message);
        }.bind(this);
    };

    Alerts.prototype._getAlertReferences = function () {
        // Get reference to alert elements.
        this._alert = document.getElementsByClassName('alert-custom')[0];
        this._message = this._alert.getElementsByTagName('p')[0];
        this._button = this._alert.getElementsByClassName('button')[0];
    };

    Alerts.prototype._init = function () {
        // Override default browser alert window.
        this._overrideDefaultAlert();
    };

    return Alerts;
})();