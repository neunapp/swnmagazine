(function(){
    "use strict";
    angular.module("MagazineApp")
        .controller("EntregaCtrl",  ['$http','uiGridConstants','ngToast', EntregaCtrl]);

    //MagazineCtrl.$inject = ["NgTableParams"];

    function EntregaCtrl($http,uiGridConstants,ngToast){
      var vm = this;

      vm.total = 0;
      vm.por_entregar = 0;
      vm.resto = 0;

      vm.progres = "0%";
      vm.is_error = false;
      vm.is_warning = false;
      vm.is_good = false;

      vm.gridOptions = {
        columnDefs : [
          {
            name: 'pk',
            enableColumnMenu: false,
            sort: {
              direction: uiGridConstants.ASC,
              priority: 0
            },
            displayName: 'Codigo',
            enableCellEdit: false,
            width: 100
          },
          {
            name: 'name',
            displayName: 'Nombres',
            enableColumnMenu: false,
            enableCellEdit: false,
            enableCellEditOnFocus:false
          },
          {
            name: 'count',
            displayName: 'Cantidad',
            enableColumnMenu: false,
            enableCellEditOnFocus:false
          },
        ],
        //personalizamos el pdf
        enableGridMenu: true,
        enableSelectAll: false,
        exporterMenuCsv: false,
        exporterMenuPdf: false,
        exporterPdfDefaultStyle: {fontSize: 9},
        exporterPdfTableStyle: {margin: [10, 30, 30, 30]},
        exporterPdfTableHeaderStyle: {fontSize: 10, bold: true, italics: true, color: 'red'},
        exporterPdfHeader: { text: "Pauta de entrega", style: 'headerStyle' },
        exporterPdfFooter: function ( currentPage, pageCount ) {
          return { text: currentPage.toString() + ' de ' + pageCount.toString(), style: 'footerStyle' };
        },
        exporterPdfCustomFormatter: function ( docDefinition ) {
          docDefinition.styles.headerStyle = { fontSize: 15, bold: true, margin: [250, 0, 20, 0] };
          docDefinition.styles.footerStyle = { fontSize: 10, bold: true };
          return docDefinition;
        },
        exporterPdfOrientation: 'portrait',
        exporterPdfPageSize: 'LETTER',
        exporterPdfMaxGridWidth: 500,
      };

      //cargamos la lista de canillas
      vm.generar_pauta = function(codigo, total){
        $http.get("/api/pautas/"+codigo)
          .then(function(response){
              vm.gridOptions.data = response.data;
          }
        );
        vm.total = total;
      }
      vm.gridOptions.enableCellEditOnFocus = true;
      vm.currentFocused = "";

      vm.gridOptions.onRegisterApi = function(gridApi){
        vm.gridApi = gridApi;
        gridApi.edit.on.afterCellEdit(null,Validar);
            function Validar(){
              vm.por_entregar = 0;
              for (var i = 0; i < vm.gridOptions.data.length; i++){
                  vm.por_entregar = vm.por_entregar + parseInt(vm.gridOptions.data[i].count);
              }
              vm.resto = vm.total - vm.por_entregar;
              //seccion de validacion
              if (vm.por_entregar > vm.total) {
                console.log('error no puede exceder');
                vm.is_warning = false;
                vm.is_good = false
                vm.is_error = true;
              }
              else if (vm.por_entregar < vm.total) {
                console.log('adevertencia debe llegar a total');
                vm.is_good = false
                vm.is_error = false;
                vm.is_warning = true;
              }
              else {
                vm.is_error = false;
                vm.is_warning = false;
                vm.is_good = true;
                console.log('good');
              }
              //actualizamos la barra de progreso
              var porcentaje = (vm.por_entregar/vm.total)*100;
              vm.progres = porcentaje.toString()+"%";

            }

      };

      vm.enviar = function(codigo){
        $http.post("/api/asignacion/save/"+codigo+"/", vm.gridOptions.data)
            .success(function(res){
              vm.gridOptions.data = [];
              ngToast.create('se guardo la Entrega correctamente');
            });
      };

      vm.limpiar = function(){
          vm.gridOptions.data = [];
          vm.total = 0;
          vm.por_entregar = 0;
          vm.resto = 0;
      }

      vm.exportar = function(){
          vm.gridApi.exporter.pdfExport('all', 'selected');
      }

    }
}())
