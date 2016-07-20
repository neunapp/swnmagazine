(function(){
    "use strict";
    angular.module("MagazineApp")
        .controller("PautaDinamicaCtrl",  ['$http','uiGridConstants','ngToast', PautaDinamicaCtrl]);

    //MagazineCtrl.$inject = ["NgTableParams"];

    function PautaDinamicaCtrl($http,uiGridConstants,ngToast){
      var vm = this;

      vm.column = {};
      vm.row = [];

      //metodo para inicializar la tabla dinamica
      vm.cargar_tabla = function(){
        $http.get("/api/pautas/dinamica/generar/")
          .then(function(response){
              vm.canillas = response.data;

              if (vm.canillas.length > 0) {
                var diarios = vm.canillas[0].product
                for (var i = 0; i < diarios.length; i++) {
                  vm.column.push({'1':diarios[i]});
                }
              }
              else {
                console.log('no funiona');
              }
          }
        );
        //cargamos las columnas
        console.log(vm.column);
      }
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


      vm.gridOptions.enableCellEditOnFocus = true;
      vm.currentFocused = "";

      vm.gridOptions.onRegisterApi = function(gridApi){
        vm.gridApi = gridApi;

      };

      vm.exportar = function(){
          vm.gridApi.exporter.pdfExport('all', 'selected');
      }

    }
}())
