'use strict';


// Declare app level module which depends on filters, and services
angular.module('myApp', [
							'myApp.filters', 
							'myApp.services', 
							'myApp.directives', 
							'myApp.controllers',
							'google-maps',
							'ngResource'
						]).
	config(['$routeProvider', function($routeProvider) {
		$routeProvider.when('/home', {templateUrl: 'partials/home.html', controller: 'HomeCtrl'});
		$routeProvider.when('/api', {templateUrl: 'partials/api.html', controller: 'ApiCtrl'});
		$routeProvider.when('/about-us', {templateUrl: 'partials/about-us.html', controller: 'AboutCtrl'});
		$routeProvider.when('/property/:ParcelNumber', {templateUrl: 'partials/property.html', controller: 'PropertyCtrl'});
		$routeProvider.otherwise({redirectTo: '/home'});
	}]);

  