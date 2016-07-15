(function(){
    "use strict";
    angular.module("MagazineApp")
        .controller("GuideListCtrl", ['$http','ngToast', GuideListCtrl]);

    function GuideListCtrl($http, ngToast){
        var vm = this;
        //inicializamos la lista de guias
        $http.get("/api/guides")
          .then(function(response){
              vm.guides = response.data;
              vm.guias = response.data;
          }
        );


        //filtramos por ragno de fechas
        vm.rango_fecha = function(){
            if (vm.fecha1==null) {
              vm.fecha1 = '2015/01/01';
            }
            if (vm.fecha2==null) {
              vm.fecha2 = new Date();
            }
            //realizamos la logica de filtro
            vm.guias = [];
            for (var i = 0; i < vm.guides.length; i++) {
              var fecha = new Date(vm.guides[i].created)
              if (fecha<=vm.fecha2 && fecha >= vm.fecha1) {
                vm.guias.push(vm.guides[i]);
              }
              else {
                console.log('False');
              }
            }
        }
  }
}());
