angular.module('PollApp', [
  'PollApp.controllers',
  'PollApp.services',
  'ngRoute'
]).
config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when("/poll/:id", {templateUrl: "partials/vote.html", controller: "pollsController"}).
        when("/result/:id", {templateUrl: "partials/result.html", controller: "pollsController"}).
        otherwise({redirectTo: "/poll/5"});
}]);

