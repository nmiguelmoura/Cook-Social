/**
 * Created by nmiguel on 02/11/16.
 */
cookSocial.CustomClass=(function(){
    'use strict';

    function CustomClass(){
        this.INITIAL_VALUE=2;
        this._ingredientsMax=null;
        this._stepsMax=null;
        this._init();
    }

     CustomClass.prototype._getInputFileBtnFunctionality=function(){
        //botao de selecao de foto
        var fileSelectBtn=document.getElementsByClassName('input-file-btn')[0],
            imgTag=document.getElementsByClassName('image-selected')[0];

        this._inputFile=new cookSocial.InputFileBtnFunctionality('image',fileSelectBtn,imgTag);

    };

    CustomClass.prototype._hide=function(divToHide){
        divToHide.div.style.display='none';
        divToHide.input.value='';
    };

    CustomClass.prototype._show=function(divToShow){
        divToShow.div.style.display='block';
    };

    CustomClass.prototype._setInputNumber=function(type,length,num){
        var i;
        for(i=0; i<length; i++){
            if(i>=num){
                this._hide(type[i]);
            }else{
                if(type[i].div.style.display==='none'){
                    this._show(type[i]);
                }
            }
        }
    };

    CustomClass.prototype._selectChange=function(event){
        var tagExpected='SELECT',
            key=event.currentTarget.key,
            value=parseInt(event.currentTarget.value),
            tagName=event.currentTarget.tagName;

        if(event.currentTarget && tagName===tagExpected){
            var type,
                length;
            if(key===0){
                type=this._ingredients;
                length=this._ingredientsMax;
            }else{
                type=this._steps;
                length=this._stepsMax;
            }
            this._setInputNumber(type,length,value);
        }
    };

    CustomClass.prototype._addListeners=function(){
        var i,length=this._selects.length;
        for(i=0;i<length;i++){
            this._selects[i].key=i;
            this._selects[i].addEventListener('change',this._selectChange.bind(this),false);
        }
    };

    CustomClass.prototype._getInputDivs=function(className,inputType){
        //store temporary var with ingredients div
        var temp=document.getElementsByClassName(className)[0],
            //store temporary var with div for each ingredient
            tempSoloDiv=temp.getElementsByClassName('label'),
            //store temporary var with input for each ingredient
            tempSoloInput=temp.getElementsByTagName(inputType);

        var i,length=tempSoloDiv.length,
            obj={};
        for(i=0;i<length;i++){
            obj[i]={
                div: tempSoloDiv[i],
                input: tempSoloInput[i]
            };
        }

        return {
            obj:obj,
            maxLength:length
        }
    };

    CustomClass.prototype._getReferences=function(){
        this._selects=document.getElementsByTagName('select');

        var ingredients=this._getInputDivs('ingredients','input');
        this._ingredients=ingredients.obj;
        this._ingredientsMax=ingredients.maxLength;
        this._setInputNumber(this._ingredients,this._ingredientsMax,this.INITIAL_VALUE);

        var steps=this._getInputDivs('steps','textArea');
        this._steps=steps.obj;
        this._stepsMax=steps.maxLength;
        this._setInputNumber(this._steps,this._stepsMax,this.INITIAL_VALUE);
    };

    CustomClass.prototype._init=function(){
        this._getReferences();
        this._addListeners();
        this._getInputFileBtnFunctionality();
    };

    return CustomClass;
})();