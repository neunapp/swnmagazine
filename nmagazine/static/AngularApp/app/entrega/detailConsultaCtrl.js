(function(){
    "use strict";
    angular.module("MagazineApp")
        .controller("DetailEntregaCtrl",  ['$http','uiGridConstants','ngToast', DetailEntregaCtr]);

    //MagazineCtrl.$inject = ["NgTableParams"];

    function DetailEntregaCtr($http,uiGridConstants,ngToast){
      var vm = this;

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
            enableCellEdit: false,
            enableCellEditOnFocus:false
          },
          {
            name: 'returned',
            displayName: 'Devuelto',
            enableColumnMenu: false,
            enableCellEdit: false,
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
        exporterPdfHeader: { text: "Reporte Entrega", style: 'headerStyle' },
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

      vm.cargar_datos = function(pk, total){
      //cargamos la lista de canillas
        $http.get("/api/asignacion/consulta/"+pk+"/")
          .then(function(response){
              vm.gridOptions.data = response.data;
              vm.total = response.data[0].total;
              vm.total_retunrned = response.data[0].total_returned;
              //actualizamos barra de progreso
              var por = (vm.total/total)*100
              vm.progres1 = por.toString()+"%";
              var por2 = (vm.total_retunrned/total)*100
              vm.progres2 = por2.toString()+"%";
          }
        );
      }

      vm.gridOptions.enableCellEditOnFocus = false;
      vm.currentFocused = "";

      vm.gridOptions.onRegisterApi = function(gridApi){
        vm.gridApi = gridApi;
        gridApi.edit.on.afterCellEdit(null,metodo);
        function metodo(){
          console.log('datos completos');
        }

      };

      vm.exportar = function(){
          vm.gridApi.exporter.pdfExport('all', 'selected');
      }

    }
}())
