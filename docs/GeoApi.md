# rpc_api.GeoApi

All URIs are relative to *https://api.covoiturage.beta.gouv.fr/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geo_point_by_address_get**](GeoApi.md#geo_point_by_address_get) | **GET** /geo/point/by_address | Geocoding à partir d&#x27;une adresse litérale
[**geo_point_by_insee_get**](GeoApi.md#geo_point_by_insee_get) | **GET** /geo/point/by_insee | Geocoding à partir d&#x27;un code insee
[**geo_route_get**](GeoApi.md#geo_route_get) | **GET** /geo/route | Calcul théorique de la distance et de la durée

# **geo_point_by_address_get**
> Geopoint geo_point_by_address_get(literal, country)

Geocoding à partir d'une adresse litérale

### Example
```python
from __future__ import print_function
import time
import rpc_api
from rpc_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
configuration = rpc_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rpc_api.GeoApi(rpc_api.ApiClient(configuration))
literal = 'literal_example' # str | Adresse littérale
country = 'country_example' # str | Nom complet du pays

try:
    # Geocoding à partir d'une adresse litérale
    api_response = api_instance.geo_point_by_address_get(literal, country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoApi->geo_point_by_address_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **literal** | **str**| Adresse littérale | 
 **country** | **str**| Nom complet du pays | 

### Return type

[**Geopoint**](Geopoint.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geo_point_by_insee_get**
> Geopoint geo_point_by_insee_get(code=code)

Geocoding à partir d'un code insee

### Example
```python
from __future__ import print_function
import time
import rpc_api
from rpc_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
configuration = rpc_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rpc_api.GeoApi(rpc_api.ApiClient(configuration))
code = 'code_example' # str | Code INSEE commune ou arrondissement de la position Pour le métropoles qui comportent un code INSEE global et des codes par arrondissement, utiliser le code arrondissement.  (optional)

try:
    # Geocoding à partir d'un code insee
    api_response = api_instance.geo_point_by_insee_get(code=code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoApi->geo_point_by_insee_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code INSEE commune ou arrondissement de la position Pour le métropoles qui comportent un code INSEE global et des codes par arrondissement, utiliser le code arrondissement.  | [optional] 

### Return type

[**Geopoint**](Geopoint.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geo_route_get**
> InlineResponse200 geo_route_get(start, end)

Calcul théorique de la distance et de la durée

### Example
```python
from __future__ import print_function
import time
import rpc_api
from rpc_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
configuration = rpc_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rpc_api.GeoApi(rpc_api.ApiClient(configuration))
start = rpc_api.Geopoint() # Geopoint | 
end = rpc_api.Geopoint() # Geopoint | 

try:
    # Calcul théorique de la distance et de la durée
    api_response = api_instance.geo_route_get(start, end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoApi->geo_route_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | [**Geopoint**](.md)|  | 
 **end** | [**Geopoint**](.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

