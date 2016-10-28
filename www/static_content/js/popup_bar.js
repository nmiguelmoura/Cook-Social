/**
 * Created by Nuno Machado on 20/09/16.
 */

cookSocial.PopupBar=(function(){
    'use strict';

    function PopupBar(){
        this._popupIsVisible=false;
        this._init();
    }

    /*PopupBar.prototype._backgroundAction=function(event){
        //esconder a barra completa
        this._hideBar();
    };

    PopupBar.prototype._disableBackground=function(){
        this._background.removeEventListener('click',this._backgroundActionEventBinding,false);
        //this._background.removeEventListener('touchstart',this._backgroundActionEventBinding,false);
    };

    PopupBar.prototype._enableBackground=function(){
        this._backgroundActionEventBinding=this._backgroundAction.bind(this);
        this._background.addEventListener('click',this._backgroundActionEventBinding,false);
        //this._background.addEventListener('touchstart',this._backgroundActionEventBinding,false);
    };

    PopupBar.prototype._changeButtonClass=function(key,active){
        //alterar a classe dos botoes para ativo ou nao-ativo
        var currentClass=this._buttons[key].className;
        if(active){
            this._buttons[this._popupTabOn].className+=' active-nav-btn-'+(key+4).toString();
        }else{
            this._buttons[this._popupTabOn].className=currentClass.split(" ")[0];
        }
    };

    PopupBar.prototype._hideTab=function(){
        if(this._popupIsVisible){
            this._popupBar.style.display='none';
            //this._changeButtonClass(this._popupTabOn,false);
            this._popupIsVisible=false;
        }
    };

    PopupBar.prototype._showTab=function(){
        //mostrar a tab
        this._popupBar.style.display='block';
        this._popupIsVisible=true;

        //alterar a cor do botao
        //this._changeButtonClass(key,true);
    };

    PopupBar.prototype._hideBar=function(){
        //desativar o fadded-screen
        this._disableBackground();

        //alterar a cor do botao
        this._changeButtonClass(this._popupTabOn,false);

        //esconder a barra popup
        this._popupBar.style.display='none';
        this._popupIsVisible=false;

        //esconder a tab ativa para evitar conflitos da proxima vez que o utilizador clicar num botao
        this._hideTab();
    };

    PopupBar.prototype._showBar=function(key){
        //ativar o fadded-screen
        this._enableBackground();

        //mostrar a tab correspondente
        this._showTab(key);

        //mostrar a barra popup
        this._popupBar.style.display='block';
        this._popupIsVisible=true;
    };*/

    PopupBar.prototype._backgroundAction=function(event){
        //esconder a barra completa
        this._hidePopup();
    };

    PopupBar.prototype._disableBackground=function(){
        this._background.style.display='none';
        this._background.removeEventListener('click',this._backgroundActionEventBinding,false);
    };

    PopupBar.prototype._enableBackground=function(){
        this._background.style.display='block';
        this._backgroundActionEventBinding=this._backgroundActionEventBinding||this._backgroundAction.bind(this);
        this._background.addEventListener('click',this._backgroundActionEventBinding,false);
    };

    PopupBar.prototype._changeButtonStyle=function(style){
        var className="col-sm-2-12 col-md-1-12 menu-btn menu-btn-"+style;
        this._button.className=className;
    };

    PopupBar.prototype._hidePopup=function(){
        if(this._popupIsVisible){
            this._popupIsVisible=false;
            this._popupBar.style.display='none';

            //change classname
            this._changeButtonStyle('off');
            //hide background
            this._disableBackground();
        }
    };

    PopupBar.prototype._showPopup=function(){
        if(!this._popupIsVisible){
            this._popupIsVisible=true;
            this._popupBar.style.display='block';

            //change classname
            this._changeButtonStyle('on');

            //launch background
            this._enableBackground();
        }
    };

    PopupBar.prototype._buttonAction=function(event){
        var elementClicked=event.currentTarget,
            tagExpected='DIV';

        //verificar se o objeto clicado tem as carateristicas do botao
        if(elementClicked && elementClicked.tagName===tagExpected){
            if(!this._popupIsVisible){
                //caso a popupbar nao esteja visivel
                this._showPopup();
            }else{
                //caso a popupbar ja esteja no ecra
                if(this._popupIsVisible){
                    //se o botao clicado e o mesmo da tab ativa, esconder a popup bar
                    this._hidePopup();
                }
            }
        }
    };

    PopupBar.prototype._addListeners=function(){
        //adicionar os eventos aos botoes
        this._button.addEventListener('click',this._buttonAction.bind(this),false);
    };

    PopupBar.prototype._getButtonReference=function(){
        //referencias para os icones dos botoes do cabecalho
        this._button=document.getElementsByClassName('menu-btn')[0];
    };

    PopupBar.prototype._getPopupReferences=function(){
        //referencias para o popup bar
        this._popupBar=document.getElementsByTagName('nav')[0];

        //referencia para o ecra de fade
        this._background=document.getElementsByClassName('fade-background')[0];
    };

    PopupBar.prototype._init=function(){
        this._getPopupReferences();
        this._getButtonReference();
        this._addListeners();
    };

    return PopupBar;
})();
