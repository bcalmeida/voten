angular.module('PollApp', [
  'PollApp.controllers',
  'PollApp.services',
  'ngRoute'
]).
config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when("/poll/:id", {templateUrl: "partials/poll.html", controller: "pollsController"}).
        otherwise({redirectTo: "/poll/1"});
}]);

