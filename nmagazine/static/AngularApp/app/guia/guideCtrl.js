(function(){
    "use strict";
    angular.module("MagazineApp")
        .controller("GuideCtrl", ['$http', GuideCtrl]);

    function GuideCtrl($http){
        var vm = this;
        //inicializamos json Guia
        vm.guide = {};
        //inicializamos la lista de proveedores
        $http.get("/api/provider")
          .then(function(response){
              vm.providers = response.data;
          }
        );
        //inicializamos los valores de dairios desde el servidor
        $http.get("/api/magazine")
          .then(function(response){
              vm.diarios = response.data;
          }
        );


        //declaramos array que enviaremos para diarios y cantidad
        vm.cant = {};
        vm.prod = {};


        vm.choices = [{id:'choice1'},{id:'choice2'}];
        vm.cantidad = [{id:0},{id:1}];
        //metodo que agraga campos dinamicamente
        vm.addNewChoice = function(){
            var newItemNo = vm.cantidad.length;
            vm.choices.push({'id':'choice'+newItemNo});
            vm.cantidad.push({'id':newItemNo});
        };

        //metodo que elimina un formulario
        vm.removeChoice = function() {
            var lastItem = vm.cantidad.length-1;
            vm.choices.splice(lastItem);
            vm.cantidad.splice(lastItem);
        };


        //funcion para enviar datos

        vm.enviar = function(){
            //ingresamos las cantidades no eliminadas al json
            console.log('=============');
            console.log(vm.guide.afecto);
            var counts_magazines = [];
            var prod_magazines = []
            for (var i = 0; i < vm.cantidad.length; i++) {
                counts_magazines.push(vm.count.item[i]);
                prod_magazines.push(vm.prod.item[i]);
            }
            vm.guide.counts = counts_magazines;
            vm.guide.prods = prod_magazines;
            console.log(vm.guide);
            $http.post("/api/save/guide/", vm.guide)
                .success(function(res){
                    console.log(res);
                });
        }

    }
}())
