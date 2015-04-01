angular.module('PollApp.controllers', []).
controller('pollsController', function($scope, $location, $routeParams, pollsAPIservice) {
    $scope.id = $routeParams.id;
    $scope.poll = null;
    $scope.candidates = [];
    $scope.voteReceived = "Not yet"

    $scope.vote = function (candidate) {
        pollsAPIservice.voteOnPoll($scope.id, candidate).
            success(function () {
                $scope.voteReceived = "Received!";
                $location.path('/result/' + $scope.id);
            }).
            error(function (data, status, headers, config) {
                $scope.voteReceived = "Failed!";
                console.error(status);
            });
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

