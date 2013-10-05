'use strict';

/* Controllers */

angular.module('myApp.controllers', ['tableSort']).
	controller('MyCtrl1', ['$scope', function($scope) {
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
	.controller('MyCtrl2', [function() {

	}]);
