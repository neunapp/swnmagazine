(function(){
    "use strict";
    angular.module("MagazineApp")
        .controller("GuideCtrl",GuideCtrl);

    function GuideCtrl(guideServices){
        var me = this;

        me.choices = [{id:'choice1'},{id:'choice2'}];

        me.addNewChoice = function(){
            console.log("agregar nuevo formulario");
            var newItemNo = me.choices.length+1;
            console.log(newItemNo);
            me.choices.push({'id':'choice'+newItemNo});
        };

        me.removeChoice = function() {
            console.log("eliminar ");
            var lastItem = me.choices.length-1;
            me.choices.splice(lastItem);
        };

        guideServices.then(function(response){
            me.diarios = response.data;
        });

    }
}())
