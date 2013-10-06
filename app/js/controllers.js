'use strict';

/* Controllers */

angular.module('myApp.controllers', ['tableSort']).
	controller('HomeCtrl', ['$scope', '$route', 'Property', 'Building', 'Sales',
				function($scope, $route, Property, Building, Sales) {
        $scope.resultType = 'map';
		$scope.refreshMap = false;
		$scope.markers = new Array();
		$scope.avgLatitude = 0;
		$scope.avgLongitude = 0;
		$scope.center = {latitude: $scope.avgLatitude, longitude: $scope.avgLongitude};
		
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
				$scope.markers.push({latitude: property.Latitude, longitude: property.Longitude, infoWindow:{content: "test"}});
				$scope.avgLatitude += parseFloat(property.Latitude);
				$scope.avgLongitude += parseFloat(property.Longitude);
			});
			$scope.refreshMap = true;
			$scope.avgLatitude = $scope.avgLatitude / properties.length;
			$scope.avgLongitude = $scope.avgLongitude / properties.length;
			$scope.center = {latitude: $scope.avgLatitude, longitude: $scope.avgLongitude};
		});

		$scope.properties = properties;
		
		angular.extend($scope, {


            center: $scope.center,
            markers: $scope.markers, // an array of markers,
            fit: true,
            zoom: 13 // the zoom level
		});

                        $scope.Math = window.Math;
                        $scope.currentPage = 1;
                        $scope.maxSize = 20;
                        $scope.pageSize = 4;
                        $scope.numOfPages = properties.length;





		$scope.setPage = function (pageNo) {
			$scope.currentPage = pageNo;
		};




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
			$scope.property = properties[1];
		});
		
		
	}])	
;

