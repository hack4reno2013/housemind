'use strict';

/* Controllers */

angular.module('myApp.controllers', ['tableSort']).
	controller('HomeCtrl', ['$scope', 'Property', 'Building', 'Sales',
				function($scope, Property, Building, Sales) {
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
		
		$scope.items = [
			{id: "01", name: "A", price: "1.00", quantity: "1"},
			{id: "02", name: "B", price: "10.00", quantity: "1"},
			{id: "04", name: "C", price: "9.50", quantity: "10"},
			{id: "03", name: "a", price: "9.00", quantity: "2"},
			{id: "06", name: "b", price: "100.00", quantity: "2"},
			{id: "05",name: "c", price: "1.20", quantity: "2"},
		];
		
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

	}]);
