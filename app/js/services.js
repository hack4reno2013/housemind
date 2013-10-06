'use strict';

/* Services */


// Demonstrate how to register services
// In this case it is a simple value service.
angular.module('myApp.services', ['ngResource'])
	.value('version', '0.1')
	.factory('Property', function($resource){
		return $resource('sample/Property.json', {}, {
			query: {
				method:'GET', 
				/*params:{
					phoneId:'phones'
				},*/ 
				isArray:true
			}
		});
	})
	.factory('Building', function($resource){
		return $resource('sample/Building.json', {}, {
			get: {
				method:'GET', 
				params:{
					ParcelNumber: 'ParcelNumber'
				},
				isArray:true,
				dataType: 'array'
			}
		});
	})
	.factory('Sales', function($resource){
		return $resource('sample/Sales.json', {}, {
			get: {
				method:'GET', 
				params:{
					ParcelNumber: 'ParcelNumber'
				},
				isArray:true
			}
		});
	})
;