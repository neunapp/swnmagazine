(function(){
    "use strict";
    angular.module("MagazineApp")
        .controller("EntregaListCtrl", ['$http','ngToast', EntregaListCtrl]);

    function EntregaListCtrl($http, ngToast){
        var vm = this;
        //inicializamos la lista de guias
        $http.get("/api/asignations")
          .then(function(response){
              vm.asignations = response.data;
              vm.asignaciones = response.data;
          }
        );


        //filtramos por ragno de fechas
        vm.search_fecha = function(){
            if (vm.fecha1==null) {
              vm.fecha1 = new Date();
            }
            //realizamos la logica de filtro
            vm.asignaciones = [];
            for (var i = 0; i < vm.asignations.length; i++) {
              var fecha = new Date(vm.asignations[i].date);
              var fecha1 = new Date(vm.fecha1)
              if ((fecha1.getDate()==fecha.getDate()+1) && (fecha1.getMonth()==fecha.getMonth()) && (fecha.getFullYear()==fecha1.getFullYear())){
                  vm.asignaciones.push(vm.asignations[i]);
              }
            }
        }
  }
}());
