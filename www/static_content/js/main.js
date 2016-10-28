/**
 * Created by Nuno Machado on 27/10/16.
 */

cookSocial.Main=(function(){
    'use strict';

    function Main(){
        this._init();
    }

    Main.prototype._checkIfCustomClass=function(){
        if(cookSocial.CustomClass){
            this._customClass=new cookSocial.CustomClass();
        }
    };

    Main.prototype._setUpPopupBar=function(){
        this._popubBar=new cookSocial.PopupBar();
    };

    Main.prototype._init=function(){
        this._setUpPopupBar();

        //esta custom class existe apenas se uma determinada pagina necessitar de funcionalidades extra
        this._checkIfCustomClass();
    };

    return Main;
})();

cookSocial.main=new cookSocial.Main();