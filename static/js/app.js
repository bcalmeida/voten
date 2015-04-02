angular.module('PollApp', [
  'PollApp.controllers',
  'PollApp.services',
  'ngRoute'
]).
config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when("/poll/:id", {templateUrl: "../static/partials/vote.html", controller: "pollsController"}).
        when("/result/:id", {templateUrl: "../static/partials/result.html", controller: "pollsController"}).
        when("/create", {templateUrl: "../static/partials/create.html", controller: "createController"}).
        otherwise({redirectTo: "/create"});
}]);

