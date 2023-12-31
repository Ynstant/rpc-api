# rpc-api
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 3.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/Ynstant/rpc-api.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Ynstant/rpc-api.git`)

Then import the package:
```python
import rpc_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import rpc_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = rpc_api.AttestationApi(rpc_api.ApiClient(configuration))
body = rpc_api.CertificatesBody() # CertificatesBody | 

try:
    # Créer un certificat
    api_response = api_instance.certificate_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttestationApi->certificate_create: %s\n" % e)

# Configure API key authorization: token
configuration = rpc_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rpc_api.AttestationApi(rpc_api.ApiClient(configuration))
body = rpc_api.UuidAttachmentBody() # UuidAttachmentBody | 
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Identifiant du certificat précédemment créé.

try:
    # Télécharger une attestation
    api_instance.certificate_download(body, uuid)
except ApiException as e:
    print("Exception when calling AttestationApi->certificate_download: %s\n" % e)

# Configure API key authorization: token
configuration = rpc_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rpc_api.AttestationApi(rpc_api.ApiClient(configuration))
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Identifiant du certificat précédemment créé.

try:
    # Vérifier un certificat
    api_response = api_instance.certificate_verify(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttestationApi->certificate_verify: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.covoiturage.beta.gouv.fr/v3*

| Class            | Method                                                                  | HTTP request                                    | Description                                    |
| ---------------- | ----------------------------------------------------------------------- | ----------------------------------------------- | ---------------------------------------------- |
| *AttestationApi* | [**certificate_create**](docs/AttestationApi.md#certificate_create)     | **POST** /certificates                          | Créer un certificat                            |
| *AttestationApi* | [**certificate_download**](docs/AttestationApi.md#certificate_download) | **POST** /certificates/{uuid}/attachment        | Télécharger une attestation                    |
| *AttestationApi* | [**certificate_verify**](docs/AttestationApi.md#certificate_verify)     | **GET** /certificates/{uuid}                    | Vérifier un certificat                         |
| *GeoApi*         | [**geo_point_by_address_get**](docs/GeoApi.md#geo_point_by_address_get) | **GET** /geo/point/by_address                   | Geocoding à partir d&#x27;une adresse litérale |
| *GeoApi*         | [**geo_point_by_insee_get**](docs/GeoApi.md#geo_point_by_insee_get)     | **GET** /geo/point/by_insee                     | Geocoding à partir d&#x27;un code insee        |
| *GeoApi*         | [**geo_route_get**](docs/GeoApi.md#geo_route_get)                       | **GET** /geo/route                              | Calcul théorique de la distance et de la durée |
| *SimulerApi*     | [**policies_simulate_post**](docs/SimulerApi.md#policies_simulate_post) | **POST** /policies/simulate                     | Simuler une incitation sur un trajet           |
| *TrajetApi*      | [**acquisition_cancel**](docs/TrajetApi.md#acquisition_cancel)          | **POST** /journeys/{operator_journey_id}/cancel | Invalider un trajet envoyé                     |
| *TrajetApi*      | [**acquisition_create**](docs/TrajetApi.md#acquisition_create)          | **POST** /journeys                              | Envoyer un trajet                              |
| *TrajetApi*      | [**acquisition_status**](docs/TrajetApi.md#acquisition_status)          | **GET** /journeys/{operator_journey_id}         | Vérifier le statut d&#x27;un trajet envoyé     |
| *TrajetApi*      | [**acquisition_update**](docs/TrajetApi.md#acquisition_update)          | **PATCH** /journeys/{operator_journey_id}       | Mettre à jour un trajet                        |
| *TrajetApi*      | [**journeys_get**](docs/TrajetApi.md#journeys_get)                      | **GET** /journeys                               | Liste des trajets                              |

## Documentation For Models

 - [CertificateData](docs/CertificateData.md)
 - [CertificateDataTotal](docs/CertificateDataTotal.md)
 - [CertificateDataTrips](docs/CertificateDataTrips.md)
 - [CertificatesBody](docs/CertificatesBody.md)
 - [CertificatesuuidattachmentMeta](docs/CertificatesuuidattachmentMeta.md)
 - [CertificatesuuidattachmentMetaIdentity](docs/CertificatesuuidattachmentMetaIdentity.md)
 - [Distance](docs/Distance.md)
 - [Driver](docs/Driver.md)
 - [Duration](docs/Duration.md)
 - [FraudcheckLabel](docs/FraudcheckLabel.md)
 - [Geopoint](docs/Geopoint.md)
 - [Identity](docs/Identity.md)
 - [IdentityTravelPass](docs/IdentityTravelPass.md)
 - [Identitycert](docs/Identitycert.md)
 - [IncentiveCounterparts](docs/IncentiveCounterparts.md)
 - [IncentiveCounterpartsInner](docs/IncentiveCounterpartsInner.md)
 - [Incentives](docs/Incentives.md)
 - [IncentivesInner](docs/IncentivesInner.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2001Identity](docs/InlineResponse2001Identity.md)
 - [InlineResponse2001Operator](docs/InlineResponse2001Operator.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse201](docs/InlineResponse201.md)
 - [InlineResponse2011](docs/InlineResponse2011.md)
 - [InlineResponse201Meta](docs/InlineResponse201Meta.md)
 - [JourneysBody](docs/JourneysBody.md)
 - [JourneysOperatorJourneyIdBody](docs/JourneysOperatorJourneyIdBody.md)
 - [Lat](docs/Lat.md)
 - [LicencePlate](docs/LicencePlate.md)
 - [Limit](docs/Limit.md)
 - [Lon](docs/Lon.md)
 - [ModelDatetime](docs/ModelDatetime.md)
 - [Offset](docs/Offset.md)
 - [OneOfidentityDrivingLicense](docs/OneOfidentityDrivingLicense.md)
 - [OperatorClass](docs/OperatorClass.md)
 - [OperatorJourneyId](docs/OperatorJourneyId.md)
 - [OperatorJourneyIdCancelBody](docs/OperatorJourneyIdCancelBody.md)
 - [OperatorTripId](docs/OperatorTripId.md)
 - [Pagination](docs/Pagination.md)
 - [Passenger](docs/Passenger.md)
 - [Payments](docs/Payments.md)
 - [PaymentsInner](docs/PaymentsInner.md)
 - [PoliciesSimulateBody](docs/PoliciesSimulateBody.md)
 - [Status](docs/Status.md)
 - [TimeGeopoint](docs/TimeGeopoint.md)
 - [Total](docs/Total.md)
 - [UuidAttachmentBody](docs/UuidAttachmentBody.md)

## Documentation For Authorization


## token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

technique@covoiturage.beta.gouv.fr
