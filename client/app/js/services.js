angular.module('PollApp.services', []).
  factory('pollsAPIservice', function($http) {

      var pollsAPI = {};

      pollsAPI.getPoll = function(id) {
          return $http({
              method: 'GET',
              //url: 'http://flask-intro-sample-app.herokuapp.com/poll/' + id
              url: 'http://localhost:5000/poll/3'
          });
      }

      pollsAPI.voteOnPoll = function(pollId, candidate) {
          return $http({
              method: 'POST',
              //url: 'http://flask-intro-sample-app.herokuapp.com/poll/' + pollId,
              url: 'http://localhost:5000/poll/' + pollId,
              data: {"candidate_description": candidate.description}
          });
      }

      return pollsAPI;
  });

