angular.module('PollApp.controllers', []).
controller('pollsController', function($scope, $routeParams, pollsAPIservice) {
    $scope.id = $routeParams.id;
    $scope.poll = null;
    $scope.candidates = [];

    $scope.vote = function (candidate) {
        pollsAPIservice.voteOnPoll($scope.id, candidate);
    };

    pollsAPIservice.getPoll($scope.id).
    success(function(data) {
        $scope.poll = data.poll;
        $scope.candidates = data.poll.candidates;
    }).
    error(function(data, status, headers, config) {
        $scope.poll = status;
        console.error(status);
    });
});

