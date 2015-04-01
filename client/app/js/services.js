angular.module('PollApp.services', []).
  factory('pollsAPIservice', function($http) {

      var pollsAPI = {};

      pollsAPI.getPoll = function(id) {
          return $http({
              method: 'GET',
              url: 'http://flask-intro-sample-app.herokuapp.com/poll/' + id

              // Other urls
              //url: 'http://localhost:5000/poll/3'
              //url: 'http://ergast.com/api/f1/2013/driverStandings.json?callback=JSON_CALLBACK'
          });
      }

      return pollsAPI;
  });

