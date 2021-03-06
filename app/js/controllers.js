'use strict';

/* Controllers */

angular.module('myApp.controllers', ['tableSort']).
	controller('HomeCtrl', ['$scope', '$route', '$filter', 'Property', 'Building', 'Sales',
				function($scope, $route, $filter, Property, Building, Sales) {
        $scope.resultType = 'map';
		$scope.markers = new Array();
		$scope.avgLatitude = 0;
		$scope.avgLongitude = 0;
		$scope.center = {latitude: $scope.avgLatitude, longitude: $scope.avgLongitude};
		
		var properties = Property.query(function() {
			angular.forEach(properties, function(property) {
				property.showDrawer = false;
				property.DisplayAddress1 = property.SitusNumber + " " + property.SitusStreet;
				property.building = {};
				property.building.Bedrooms = 0;
				property.sales = {};
				Building.get(property.ParcelNumber, function(data) {
					property.building = data[0];
					Sales.get(property.ParcelNumber, function(data) {
						property.sales = data[0];
						property.infoWindow = "<h5><a ng-href='/property/" + property.ParcelNumber + "'>" + property.DisplayAddress1 + "</a></h5><p>Beds: " + property.building.Bedrooms + "</p><p>Baths: " + property.building.Baths + "</p><p>Square Feet: " + $filter('number')(property.BldgSquareFeet, 0) + "</p><p>Last Sale Price: " + $filter('currency')(property.sales.SaleAmount) + "</p>";
						$scope.markers.push({latitude: property.Latitude, longitude: property.Longitude, infoWindow:property.infoWindow});
					});
				});
				$scope.avgLatitude += parseFloat(property.Latitude);
				$scope.avgLongitude += parseFloat(property.Longitude);
			});
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

