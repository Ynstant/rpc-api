# rpc_api.SimulerApi

All URIs are relative to *https://api.covoiturage.beta.gouv.fr/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policies_simulate_post**](SimulerApi.md#policies_simulate_post) | **POST** /policies/simulate | Simuler une incitation sur un trajet

# **policies_simulate_post**
> InlineResponse2004 policies_simulate_post(body)

Simuler une incitation sur un trajet

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
api_instance = rpc_api.SimulerApi(rpc_api.ApiClient(configuration))
body = rpc_api.PoliciesSimulateBody() # PoliciesSimulateBody | 

try:
    # Simuler une incitation sur un trajet
    api_response = api_instance.policies_simulate_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulerApi->policies_simulate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PoliciesSimulateBody**](PoliciesSimulateBody.md)|  | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

