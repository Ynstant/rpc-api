# Identity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_key** | **str** | Correspond au sha d&#x27;une chaîne concaténée tel que : sha256(*phone_number*-*last_name*) ou - &#x60;phone_number&#x60; correspond au numéro de téléphone complet au format international sans espace ni tiret. Exemple : +33601020304 - &#x60;last_name&#x60; correspond au nom de famille complet en majuscule, sans accent ni tiret ni apostrophe (regexp: [A-Z ]*) Par exemple, M. D&#x27;Hérûg-de-l&#x27;Hérault ayant le numéro 07 01 02 03 04 doit être formatté comme suit \&quot;+33701020304-D HERUG DE L HERAULT\&quot;  | 
**travel_pass** | [**IdentityTravelPass**](IdentityTravelPass.md) |  | [optional] 
**phone** | **str** | Numéro de téléphone à 10 chiffre au format ITU E.164 | [optional] 
**phone_trunc** | **str** | Numéro de téléphone à 8 chiffres. Obligatoire si le numéro de téléphone complet n&#x27;est pas fournit. | [optional] 
**driving_license** | **OneOfidentityDrivingLicense** | Numéro de permis de conduire (également appelé code driving_license) cf https://permisdeconduire.ants.gouv.fr/tout-savoir-sur-le-permis/le-numero-de-dossier-sur-un-permis-au-format-carte-bancaire   | [optional] 
**operator_user_id** | **str** | Identifiant de l&#x27;utilisateur chez l&#x27;opérateur. Obligatoire si le numéro de téléphone complet n&#x27;est pas fournit. | 
**over_18** | **bool** | Applicable seulement au passager.   - true si majeur   - false si mineur   - null si non fournit  &gt; De nombreuses campagnes utilisent cette information pour s&#x27;assurer que les bénéficiaires d&#x27;incitations sont majeures. La valeur &#x60;NULL&#x60; les exclues.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

