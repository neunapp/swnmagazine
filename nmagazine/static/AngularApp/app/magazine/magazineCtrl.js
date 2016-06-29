(function(){
    "use strict";
    angular.module("MagazineApp")
        .controller("MagazineCtrl",  ['$http', MagazineCtrl]);

    //MagazineCtrl.$inject = ["NgTableParams"];

    function MagazineCtrl($http){
      var vm = this;
      // recuperamos el get del servidor
      $http.get("/api/magazin")
        .then(
            function(response){
              vm.diarios = response.data;
              console.log(vm.diarios);
            }
        );
    }
}())
