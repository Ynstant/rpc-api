# CertificatesBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity** | [**Identitycert**](Identitycert.md) |  | 
**tz** | **str** | fuseau horaire | 
**start_at** | **datetime** | Date de début au format ISO. Sélectionne les trajet &gt;&#x3D; date | [optional] 
**end_at** | **datetime** | Date de fin au format ISO nécessairement supérieur à start_at. Sélectionne les trajets &lt; date | [optional] 
**positions** | [**list[Geopoint]**](Geopoint.md) | Pour sélectionner des trajets en fonction de leur point de départ et d&#x27;arrivée, il est possible de les préciser avec la clé &#x60;positions&#x60;. Tous les trajets ayant un départ **et** une arrivée dans un rayon de &#x60;1km&#x60; autour des points donnés seront inclus à l&#x27;attestation.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

