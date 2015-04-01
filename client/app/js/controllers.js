angular.module('PollApp.controllers', []).
controller('pollsController', function($scope, pollsAPIservice) {
    $scope.poll = null;
    $scope.candidates = [];

    pollsAPIservice.getPoll().
    success(function(data) {
        $scope.poll = data.poll;
        $scope.candidates = data.poll.candidates;
    }).
    error(function(data, status, headers, config) {
        $scope.poll = status;
        console.error(status);
    });
});

//angular.module('F1FeederApp.controllers', []).
//controller('driversController', function($scope, ergastAPIservice) {
//    // $scope.driversList = [
//    //   {
//    //       Driver: {
//    //           givenName: 'Sebastian',
//    //           familyName: 'Vettel'
//    //       },
//    //       points: 322,
//    //       nationality: "German",
//    //       Constructors: [
//    //           {name: "Red Bull"}
//    //       ]
//    //   },
//    //   {
//    //       Driver: {
//    //       givenName: 'Fernando',
//    //           familyName: 'Alonso'
//    //       },
//    //       points: 207,
//    //       nationality: "Spanish",
//    //       Constructors: [
//    //           {name: "Ferrari"}
//    //       ]
//    //   }
//    // ];
//    $scope.driversList = [];
//
//    ergastAPIservice.getDrivers().success(function(response) {
//        $scope.driversList = response.MRData.StandingsTable.StandingsLists[0].DriverStandings;
//    });
//}).


