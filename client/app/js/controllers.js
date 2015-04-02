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
}).
controller('createController', function ($scope, $location, pollsAPIservice) {
    $scope.description = "";
    $scope.choices = [{'position': 1}, {'position': 2}, {'position': 3}];
    $scope.buttonDisabled = false;

    $scope.addNewChoice = function() {
        var position = $scope.choices.length + 1;
        $scope.choices.push({'position': position});
    };

    // TODO: Do not add empty choices. Or do not allow empty choices?
    $scope.createPoll = function() {
        $scope.buttonDisabled = true;

        var poll = {'description': $scope.description};
        poll.candidates = []
        for (var i = 0; i < $scope.choices.length; i++) {
            poll.candidates.push({'description': $scope.choices[i].description});
        }

        pollsAPIservice.createPoll(poll).
            success(function (data) {
                $location.path('/poll/' + data.poll_id);
            }).
            error(function(data, status, headers, config) {
                console.error(status);
            });
    };
});

