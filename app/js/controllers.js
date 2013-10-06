'use strict';

/* Controllers */

angular.module('myApp.controllers', ['tableSort']).
	controller('HomeCtrl', ['$scope', '$route', 'Property', 'Building', 'Sales',
				function($scope, $route, Property, Building, Sales) {
        $scope.resultType = 'map';
		var properties = Property.query(function() {
			angular.forEach(properties, function(property) {
				property.showDrawer = false;
				property.DisplayAddress1 = property.SitusNumber + " " + property.SitusStreet;
				Building.get(property.ParcelNumber, function(data) {
					property.building = data[0];
				});
				Sales.get(property.ParcelNumber, function(data) {
					property.sales = data[0];
				});
			});
		});

		$scope.properties = properties;
				
		angular.extend($scope, {
			center: {
				latitude: 39.529731, // initial map center latitude
				longitude: -119.812828, // initial map center longitude
			},
			markers: [], // an array of markers,
			zoom: 13, // the zoom level
		});
	}])
	.controller('ApiCtrl', [function() {

	}])
	.controller('AboutCtrl', [function() {

	}])
	.controller('PropertyCtrl', ['$scope', '$route', 'Property', 'Building', 'Sales',
				function($scope, $route, Property, Building, Sales) {
		$scope.params = $route.current.params;
		$scope.ParcelNumber = $scope.params.ParcelNumber;
		
		var properties = Property.get({ParcelNumber:$scope.ParcelNumber}, function() {
			angular.forEach(properties, function(property) {
				property.showDrawer = false;
				property.DisplayAddress1 = property.SitusNumber + " " + property.SitusStreet;
				Building.get(property.ParcelNumber, function(data) {
					property.building = data;
				});
				Sales.get(property.ParcelNumber, function(data) {
					property.sales = data;
				});
			});
			$scope.property = properties[5];
		});
		
		
	}])	
;
