# rpc_api.AttestationApi

All URIs are relative to *https://api.covoiturage.beta.gouv.fr/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**certificate_create**](AttestationApi.md#certificate_create) | **POST** /certificates | Créer un certificat
[**certificate_download**](AttestationApi.md#certificate_download) | **POST** /certificates/{uuid}/attachment | Télécharger une attestation
[**certificate_verify**](AttestationApi.md#certificate_verify) | **GET** /certificates/{uuid} | Vérifier un certificat

# **certificate_create**
> InlineResponse201 certificate_create(body)

Créer un certificat

## Configuration de la requête  1. La requête est authentifiée avec un [token applicatif](/operateurs/preuves/acces) à ajouter à l'entête de la requête : `Authorization: Bearer <token>` 2. Le fuseau horaire est requis 2. L'identité est requise 3. Le filtrage géographique est optionnel 4. Les dates de début et de fin sont optionnelles 5. La date de fin la plus récente possible est J-6 6. La date de début la plus ancienne est le 1er janvier de l'année précédente  > Voir la [création avancée](#creation-avancee) pour le détail des options  ## Création simple  Les données requises pour la création ne concernent que l'identité de la personne et le fuseau horaire.  Par défaut, l'attestation sera générée pour l'année précédente sans restrictions géographiques.  Chaque appel, même si les paramètres sont les mêmes, entraine la création d'une attestation unique.  Les attestations ne peuvent être supprimées. [Contactez notre équipe](mailto:technique@covoiturage.beta.gouv.fr) au besoin.  ### Astuce Vous pouvez récupérer le fuseau horaire de l'utilisateur en Javascript. ```js const tz = Intl.DateTimeFormat().resolvedOptions().timeZone; ``` 

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
api_instance = rpc_api.AttestationApi(rpc_api.ApiClient(configuration))
body = rpc_api.CertificatesBody() # CertificatesBody | 

try:
    # Créer un certificat
    api_response = api_instance.certificate_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttestationApi->certificate_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CertificatesBody**](CertificatesBody.md)|  | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **certificate_download**
> certificate_download(body, uuid)

Télécharger une attestation

## Upload du logo opérateur  Vous pouvez personnaliser le logo opérateur présent sur l'attestation.  Contrairement aux meta-données envoyées lors de la création de l'attestation, le logo est configuré au préalable via le page de profil de votre opérateur.  - [Ajouter mon logo en production](https://app.covoiturage.beta.gouv.fr/admin/operator) - [Ajouter mon logo pour les tests](https://app.demo.covoiturage.beta.gouv.fr/admin/operator)  > _Le poids de l'image est de 2Mo maximum et sa taille de 1024x1024 pixels._  ## Téléchargement  Une fois l’attestation créée en base \\(201 created\\), on peut télécharger un PDF en y ajoutant des données permettant une identification simplifiée de la personne.  Ces meta-données optionnelles ne sont pas stockées sur nos serveurs, elles sont ajoutées au document généré à la volée.  Le PDF généré n'est pas stocké sur nos serveurs. L'appel d'API vous renvoie un fichier binaire que vous sauvegardez de votre côté. Vous pouvez générer le PDF d'une attestation plusieurs fois de suite. 

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
api_instance = rpc_api.AttestationApi(rpc_api.ApiClient(configuration))
body = rpc_api.UuidAttachmentBody() # UuidAttachmentBody | 
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Identifiant du certificat précédemment créé.

try:
    # Télécharger une attestation
    api_instance.certificate_download(body, uuid)
except ApiException as e:
    print("Exception when calling AttestationApi->certificate_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UuidAttachmentBody**](UuidAttachmentBody.md)|  | 
 **uuid** | [**str**](.md)| Identifiant du certificat précédemment créé. | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **certificate_verify**
> InlineResponse2001 certificate_verify(uuid)

Vérifier un certificat

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
api_instance = rpc_api.AttestationApi(rpc_api.ApiClient(configuration))
uuid = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Identifiant du certificat précédemment créé.

try:
    # Vérifier un certificat
    api_response = api_instance.certificate_verify(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttestationApi->certificate_verify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Identifiant du certificat précédemment créé. | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

