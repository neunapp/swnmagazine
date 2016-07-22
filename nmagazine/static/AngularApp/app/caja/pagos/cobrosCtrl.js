(function(){
    "use strict";
    angular.module("MagazineApp")
        .controller("CobrosCtrl",  ['$http','uiGridConstants','ngToast', CobrosCtrl]);

    function CobrosCtrl($http,uiGridConstants,ngToast){
      var vm = this;

      vm.gridOptions = {
        infiniteScrollRowsFromEnd: 40,
        infiniteScrollUp: true,
        columnDefs : [
          {
            name: 'magazine',
            enableColumnMenu: false,
            sort: {
              direction: uiGridConstants.ASC,
              priority: 0
            },
            displayName: 'Diarios Productos',
            enableCellEdit: false,
            width: 200
          },
          {
            name: 'entregado',
            displayName: 'Entregado',
            enableColumnMenu: false,
            enableCellEdit: false,
            enableCellEditOnFocus:false
          },
          {
            name: 'devuelto',
            displayName: 'Devuelto',
            enableColumnMenu: false,
            enableCellEditOnFocus:false
          },
          {
            name: 'cuenta',
            displayName: 'A Cuenta',
            enableColumnMenu: false,
            enableCellEditOnFocus:false
          },
          {
            name: 'pagar',
            displayName: 'Pagar',
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
      vm.gridOptions.data = [
        {
          'magazine':'PERU 21 Lunes a Sabado',
          'entregado':'15',
          'devuelto':'1',
          'cuenta':'5',
          'pagar':'9',
        },
        {
          'magazine':'Ojo Lunes a Sabado',
          'entregado':'15',
          'devuelto':'1',
          'cuenta':'5',
          'pagar':'9',
        },
        {
          'magazine':'Neunapp Lunes a Sabado',
          'entregado':'15',
          'devuelto':'1',
          'cuenta':'5',
          'pagar':'9',
        },
        {
          'magazine':'Comercio Lunes a Sabado',
          'entregado':'15',
          'devuelto':'1',
          'cuenta':'5',
          'pagar':'9',
        },
        {
          'magazine':'Trome Lunes a Sabado',
          'entregado':'15',
          'devuelto':'1',
          'cuenta':'5',
          'pagar':'9',
        },
      ];
      vm.gridOptions.enableCellEditOnFocus = true;
      vm.currentFocused = "";

      vm.gridOptions.onRegisterApi = function(gridApi){
        vm.gridApi = gridApi;

      };

    }
}())
