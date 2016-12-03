/**
 * Created by nmiguel on 02/11/16.
 */
cookSocial.CustomClass = (function () {
    'use strict';

    function CustomClass() {
        this.INITIAL_VALUE = 2;
        this._ingredientsMax = null;
        this._stepsMax = null;
        this._init();
    }

    CustomClass.prototype._getInputFileBtnFunctionality = function () {
        // Get reference to input file button that allows picture selection.
        var fileSelectBtn = document.getElementsByClassName('input-file-btn')[0],

            //Get reference to image tag that will display uselected image.
            imgTag = document.getElementsByClassName('image-selected')[0];

        // Instantiate class that manages input file system.
        this._inputFile = new cookSocial.InputFileBtnFunctionality('image', fileSelectBtn, imgTag);

    };

    CustomClass.prototype._hide = function (divToHide) {
        // Hide selected div.
        divToHide.div.style.display = 'none';

        // Clear input on selected div.
        divToHide.input.value = '';
    };

    CustomClass.prototype._show = function (divToShow) {
        // Show selected div.
        divToShow.div.style.display = 'block';
    };

    CustomClass.prototype._setInputNumber = function (type, length, num) {
        var i;
        for (i = 0; i < length; i++) {
            // Loop through inputs according to type (ingredients or steps).
            if (i >= num) {
                // Hide inputs and divs with index greater or equal to number selected.
                this._hide(type[i]);
            } else {
                if (type[i].div.style.display === 'none') {
                    // Shows hidden inputs and divs with index minor than number selected.
                    this._show(type[i]);
                }
            }
        }
    };

    CustomClass.prototype._selectChange = function (event) {
        // Run if select box has changed.
        var tagExpected = 'SELECT',
            key = event.currentTarget.key,
            value = parseInt(event.currentTarget.value),
            tagName = event.currentTarget.tagName;

        if (event.currentTarget && tagName === tagExpected) {
            // Run if current target matches select box.
            var type,
                length;
            if (key === 0) {
                // If key == 0 refers to ingredients.
                type = this._ingredients;
                length = this._ingredientsMax;
            } else {
                // If key != 0 refers to steps.
                type = this._steps;
                length = this._stepsMax;
            }

            // Set number of inputs available according to user choice.
            this._setInputNumber(type, length, value);
        }
    };

    CustomClass.prototype._addListeners = function () {
        var i, length = this._selectNums.length;
        for (i = 0; i < length; i++) {
            // Adds an index value to each select box.
            this._selectNums[i].key = i;
            // Adds listeners to both select boxes.
            this._selectNums[i].addEventListener('change', this._selectChange.bind(this), false);
        }
    };

    CustomClass.prototype._getInputDivs = function (className, inputType) {
        // Store temporary var with ingredients or steps div.
        var temp = document.getElementsByClassName(className)[0],
            // Store temporary var with div for each ingredient or step.
            tempSoloDiv = temp.getElementsByClassName('label'),
            // Store temporary var with input for each ingredient or step.
            tempSoloInput = temp.getElementsByTagName(inputType);

        var i, length = tempSoloDiv.length,
            // Create an empty object to store divs and inputs.
            obj = {};
        for (i = 0; i < length; i++) {
            // Stores divs and inputs in object
            obj[i] = {
                div: tempSoloDiv[i],
                input: tempSoloInput[i]
            };
        }

        // Return object and object length.
        return {
            obj: obj,
            maxLength: length
        }
    };

    CustomClass.prototype._getPreSelectNumValues = function(){
        var i, length = this._selectNums.length;
        var preValue,
            preValues = [];

        for(i=0;i < length; i++){
            // Loop through select box to check if there are pre selected values. Thsi values are injected by server when needed.
            // If there are no pre selected values, user INITIAL_VALUE.
            preValue = this._selectNums[i].getAttribute('data-pre-value') !== ''?this._selectNums[i].getAttribute('data-pre-value'):this.INITIAL_VALUE;

            // Make select value equal to preValue.
            this._selectNums[i].value = preValue;

            // Push value in preVAlues array.
            preValues.push(preValue);
        }

        // Set initial number of ingredient and step inputs
        this._setInputNumber(this._ingredients, this._ingredientsMax, preValues[0]);
        this._setInputNumber(this._steps, this._stepsMax, preValues[1]);
    };

    CustomClass.prototype._getPreSelectCategoryValues = function(){
        if(this._category.hasAttribute('data-pre-value-category')) {
            var preValue = this._category.getAttribute('data-pre-value-category') !== ''?this._category.getAttribute('data-pre-value-category'):'0';
            this._category.value = preValue;
        }
    };

    CustomClass.prototype._getReferences = function () {
        //Get select box for categories reference
        this._category = document.getElementsByClassName('category')[0];

        // Get select boxes for ingredient and step num references.
        this._selectNums = document.getElementsByClassName('num_select');

        // Get ingredient divs and inputs.
        var ingredients = this._getInputDivs('ingredients', 'input');

        // Store ingredients divs and inputs in global variable.
        this._ingredients = ingredients.obj;
        this._ingredientsMax = ingredients.maxLength;

        // Get step divs and inputs.
        var steps = this._getInputDivs('steps', 'textArea');

        // Store steps divs and inputs in global variable.
        this._steps = steps.obj;
        this._stepsMax = steps.maxLength;
    };

    CustomClass.prototype._init = function () {
        // Get necessary references.
        this._getReferences();

        //Get category select box pre value
        this._getPreSelectCategoryValues();

        // Get select box pre values.
        this._getPreSelectNumValues();

        // Add listeners to select box.
        this._addListeners();

        // Instantiate input file manager class.
        this._getInputFileBtnFunctionality();
    };

    return CustomClass;
})();