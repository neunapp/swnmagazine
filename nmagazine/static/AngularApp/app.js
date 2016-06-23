(function(){
    var app = angular.module("MagazineApp",
                                      ["common.services"])
        .config(
        function($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    }
);
}());
