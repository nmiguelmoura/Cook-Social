/**
 * Created by Nuno Machado on 27/10/16.
 */

cookSocial.Main = (function () {
    'use strict';

    function Main() {
        this._init();
    }

    Main.prototype._checkIfCustomClass = function () {
        if (cookSocial.CustomClass) {
            // If custom class exists, instantiate it.
            this._customClass = new cookSocial.CustomClass();
        }
    };

    Main.prototype._setUpPopupBar = function () {
        // Instantiate popup bar manager.
        this._popubBar = new cookSocial.PopupBar();
    };

    Main.prototype._init = function () {
        // Setup popup bar.
        this._setUpPopupBar();

        // This class exists only if extra functionality is required in a given page.
        this._checkIfCustomClass();

        // Launch customized alerts.
        this._alerts = new cookSocial.Alerts();
    };

    return Main;
})();

cookSocial.main = new cookSocial.Main();