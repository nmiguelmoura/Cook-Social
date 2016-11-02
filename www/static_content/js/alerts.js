/**
 * Created by Nuno Machado on 22/09/16.
 */

//os alertas sao lancados por defeito (alert('mensagem'))
//caso o javascript esteja ligado, esta class capta a mensagem e mostra a caixa de alerta personalizada

cookSocial.Alerts=(function(){

    function Alerts(){
        this._init();
        this._alert=null;
        this._message=null;
        this._button=null;
    }

    Alerts.prototype._buttonAction=function(){
        this._disableButton();
        this._alert.style.display='none';
    };

    Alerts.prototype._disableButton=function(){
        this._button.removeEventListener('click',this._buttonEventBind,false);
    };

    Alerts.prototype._enableButton=function(){
        this._buttonEventBind=this._buttonAction.bind(this);
        this._button.addEventListener('click',this._buttonEventBind,false);
    };

    Alerts.prototype._showAlert=function(message){
        if(this._alert===null){
            this._getAlertReferences();
        }

        if(this._alert){
            this._message.innerHTML=message;
            this._enableButton();
            this._alert.style.display='block';
        }
    };

    Alerts.prototype._overrideDefaultAlert=function(){
        window.alert=function(message){
            this._showAlert(message);
        }.bind(this);
    };

    Alerts.prototype._getAlertReferences=function(){
        this._alert=document.getElementsByClassName('alert-custom')[0];
        this._message=this._alert.getElementsByTagName('p')[0];
        this._button=this._alert.getElementsByClassName('button')[0];
    };

    Alerts.prototype._init=function(){
        this._overrideDefaultAlert();
    };

    return Alerts;
})();