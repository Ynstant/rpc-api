# rpc_api.TrajetApi

All URIs are relative to *https://api.covoiturage.beta.gouv.fr/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acquisition_cancel**](TrajetApi.md#acquisition_cancel) | **POST** /journeys/{operator_journey_id}/cancel | Invalider un trajet envoyé
[**acquisition_create**](TrajetApi.md#acquisition_create) | **POST** /journeys | Envoyer un trajet
[**acquisition_status**](TrajetApi.md#acquisition_status) | **GET** /journeys/{operator_journey_id} | Vérifier le statut d&#x27;un trajet envoyé
[**acquisition_update**](TrajetApi.md#acquisition_update) | **PATCH** /journeys/{operator_journey_id} | Mettre à jour un trajet
[**journeys_get**](TrajetApi.md#journeys_get) | **GET** /journeys | Liste des trajets

# **acquisition_cancel**
> acquisition_cancel(operator_journey_id, body=body)

Invalider un trajet envoyé

Annule un trajet déjà envoyé dans le registre. S'il détecte un comportement inhabituel ou une fraude avérée, un opérateur doit communiquer auprès du service l'invalidation du trajet concerné dès lors qu'il est déjà inscrit dans le registre.  Cette invalidation doit avoir lieu dès que l'opérateur a connaissance de cette irrégularité à tout moment. 

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
api_instance = rpc_api.TrajetApi(rpc_api.ApiClient(configuration))
operator_journey_id = rpc_api.OperatorJourneyId() # OperatorJourneyId | operator_journey_id of the journey created
body = rpc_api.OperatorJourneyIdCancelBody() # OperatorJourneyIdCancelBody |  (optional)

try:
    # Invalider un trajet envoyé
    api_instance.acquisition_cancel(operator_journey_id, body=body)
except ApiException as e:
    print("Exception when calling TrajetApi->acquisition_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_journey_id** | [**OperatorJourneyId**](.md)| operator_journey_id of the journey created | 
 **body** | [**OperatorJourneyIdCancelBody**](OperatorJourneyIdCancelBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **acquisition_create**
> InlineResponse2011 acquisition_create(body)

Envoyer un trajet

Un trajet est un couple passager.ère / conducteur.rice ayant des points et de horaires de départ et d'arrivée. Si une conductrice covoiture avec plusieurs passagères, plusieurs trajets sont déclarés.  ### Unités de mesure  Les unités utilisées pour les valeurs sont :  - montants financiers en **centimes d'Euros** - distances en **mètres**  ### Données financières  Le principe est de coller au plus près avec la réalité comptable \\(transaction usager\\) et d'avoir suffisamment d'informations pour recalculer le coût initial du trajet. Ainsi, les propriétés `passenger.contribution` et `driver.revenue` combinées au tableau `incentives` doivent permettre ce calcul. Ceci afin de s'assurer du respect de la définition du covoiturage et de la bonne application des politiques incitatives gérées par le registre. > Les données envoyées en `passenger.contribution` et `driver.revenue` sont utilisées dans les attestations de covoiturage à destination des employeurs (Forfait Mobilités Durables).  ### Validation Le schéma de données est présenté au format [JSON Schema Draft-07](https://json-schema.org/understanding-json-schema/index.html).  ### Vérification Dans le cadre de la fraude inter opérateurs, les opérateurs sont tenus de vérifier le statut du trajet au plus tôt 24h après la réalisation de celui-ci. Ces trajets seront retournés avec un champs `status` à `fraud_error` et un label dans `fraud_error_labels` à `interoperator_fraud`. Le statut ne peut plus changer 48h après la date de fin du trajet.  En cas d'indisponibilité du service, le trajet est considéré comme `ok` après 48h L'algorithme de détection de fraude inter opérateurs est appliqué sur tous les trajets envoyés. 

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
api_instance = rpc_api.TrajetApi(rpc_api.ApiClient(configuration))
body = rpc_api.JourneysBody() # JourneysBody | 

try:
    # Envoyer un trajet
    api_response = api_instance.acquisition_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrajetApi->acquisition_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JourneysBody**](JourneysBody.md)|  | 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **acquisition_status**
> InlineResponse2003 acquisition_status(operator_journey_id)

Vérifier le statut d'un trajet envoyé

Lors de l'envoi d'un trajet, un code 201 et un payload avec le `operator_journey_id` et la date de création vous sont renvoyés. Le trajet est alors enregistré dans notre base. Le processus de validation par lequel vont passer les données est complexe, asynchrone et dépend de différents services ayant de temps de réponse variables. Les trajets ne seront visibles dans l'interface utilisateurs que **24 heures** après leur envoi.  Il est possible de vérifier le statut d'un trajet envoyé directement pour s'assurer qu'il n'y pas pas eu d'erreur de format ou de traitement.  Dans le cadre de la fraude inter opérateurs, les opérateurs sont tenus de vérifier le statut du trajet au plus tôt 24h après la réalisation de celui-ci. Un trajet detecté sera retourné avec un champ `status` à `fraud_error`. Le statut ne peut plus changer 48h après la date de fin du trajet. En cas d'indisponibilité du service, le trajet est considéré comme ok après les 48h  L'algorithme de détection de fraude inter opérateurs est appliqué sur tous les trajets envoyés. 

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
api_instance = rpc_api.TrajetApi(rpc_api.ApiClient(configuration))
operator_journey_id = rpc_api.OperatorJourneyId() # OperatorJourneyId | operator_journey_id of the journey created

try:
    # Vérifier le statut d'un trajet envoyé
    api_response = api_instance.acquisition_status(operator_journey_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrajetApi->acquisition_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_journey_id** | [**OperatorJourneyId**](.md)| operator_journey_id of the journey created | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **acquisition_update**
> acquisition_update(body, operator_journey_id)

Mettre à jour un trajet

Permet de mettre à jour un trajet qui est en erreur suite à un problème de validation sur le payload. Par exemple suite à un problème de validation sur les coordonnées géographiques envoyées 

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
api_instance = rpc_api.TrajetApi(rpc_api.ApiClient(configuration))
body = rpc_api.JourneysOperatorJourneyIdBody() # JourneysOperatorJourneyIdBody | 
operator_journey_id = rpc_api.OperatorJourneyId() # OperatorJourneyId | operator_journey_id of the journey created

try:
    # Mettre à jour un trajet
    api_instance.acquisition_update(body, operator_journey_id)
except ApiException as e:
    print("Exception when calling TrajetApi->acquisition_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JourneysOperatorJourneyIdBody**](JourneysOperatorJourneyIdBody.md)|  | 
 **operator_journey_id** | [**OperatorJourneyId**](.md)| operator_journey_id of the journey created | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journeys_get**
> list[InlineResponse2002] journeys_get(status, limit=limit, start=start, end=end, offset=offset)

Liste des trajets

La liste est toujours ordonnée de manière antechronologique. Les trajets apparaissent au plus tard 24h après leur envoi. Dans le cadre de la fraude inter-opérateurs, les opérateurs sont tenus de vérifier le statut du trajet au plus tôt 48h après la réalisation de celui-ci. Ces trajets peuvent être listés en passant un paramètre `status` à `fraud_error`. 

### Example
```python
from __future__ import print_function
import time
import rpc_api
from rpc_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rpc_api.TrajetApi()
status = rpc_api.Status() # Status | Statut du trajet
limit = rpc_api.Limit() # Limit | Limite, par défaut 50. (optional)
start = rpc_api.ModelDatetime() # ModelDatetime | Date de début de recherche, par défaut dans la semaine qui précède. (optional)
end = rpc_api.ModelDatetime() # ModelDatetime | Date de fin de recherche, par défaut le jour même. (optional)
offset = rpc_api.Offset() # Offset | Offset, par défaut 0. (optional)

try:
    # Liste des trajets
    api_response = api_instance.journeys_get(status, limit=limit, start=start, end=end, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrajetApi->journeys_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**Status**](.md)| Statut du trajet | 
 **limit** | [**Limit**](.md)| Limite, par défaut 50. | [optional] 
 **start** | [**ModelDatetime**](.md)| Date de début de recherche, par défaut dans la semaine qui précède. | [optional] 
 **end** | [**ModelDatetime**](.md)| Date de fin de recherche, par défaut le jour même. | [optional] 
 **offset** | [**Offset**](.md)| Offset, par défaut 0. | [optional] 

### Return type

[**list[InlineResponse2002]**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

