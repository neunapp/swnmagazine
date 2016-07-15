(function(){
    "use strict";
    angular.module("MagazineApp")
        .controller("GuideCtrl", ['$http','$window','ngToast', GuideCtrl]);

    function GuideCtrl($http, $window, ngToast){
        var vm = this;
        //inicializamos variables globales
        vm.choices = [{id:'choice1'},{id:'choice2'}];
        vm.cantidad = [{id:0},{id:1}];

        //inicializamos json Guia
        vm.guide = {};
        vm.guide.afecto = false;
        vm.guide.discount = 0;


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


        //inicializamos la lista de guias
        $http.get("/api/guides")
          .then(function(response){
              vm.guides = response.data;
          }
        );

        //declaramos array que enviaremos para diarios y cantidad
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
            var counts_magazines = [];
            var prod_magazines = []
            for (var i = 0; i < vm.cantidad.length; i++) {
                counts_magazines.push(vm.count.item[i]);
                prod_magazines.push(vm.prod.item[i]);
            }
            //vm.guide.provider = vm.proveedor
            vm.guide.counts = counts_magazines;
            vm.guide.prods = prod_magazines;
            //validamos descuento
            if (vm.guide.discount == null) {
              vm.guide.discount = 0;
            }
            if (vm.guide.afecto == null) {
              vm.guide.afecto = false;
            }
            if (vm.guide.invoce ==null) {
              vm.guide.invoce=0;
            }
            $http.post("/api/save/guide/", vm.guide)
                .success(function(res){
                  if (res.id=='0') {
                    ngToast.create(res.respuesta);
                    $window.location.reload();
                  }
                  else {
                    ngToast.create({
                      className: 'warning',
                      content: res.respuesta,
                    });
                  }
                  //$location.href
                })
                .error(function(res){
                  ngToast.create({
                    className: 'warning',
                    content: '<a href="#">x Error Revise los datos</a>',
                  });
                });
        };

      //========validations===========
      vm.check = true;
      vm.validations = function(bool){
        if (bool) {
          console.log('valido');
          vm.check = false;
          vm.valid = false;
          vm.valid0 = false;
          vm.valid1 = false;

        }
        else {
          console.log('no valido');
          vm.valid1 = true;
          vm.check = true;
        }
      }
  }
}());
