# DomainsV1WHOISProfileResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | WHOIS Profile ID | [optional] 
**tld** | **str** | TLD to which contact profile can be applied to | [optional] 
**country** | **str** | ISO 3166 2-letter country code | [optional] 
**entity_type** | **str** | WHOIS profile entity type | [optional] 
**whois_details** | **object** | WHOIS profile details | [optional] 
**tld_details** | **object** | TLD details | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.domains_v1_whois_profile_resource import DomainsV1WHOISProfileResource

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1WHOISProfileResource from a JSON string
domains_v1_whois_profile_resource_instance = DomainsV1WHOISProfileResource.from_json(json)
# print the JSON string representation of the object
print(DomainsV1WHOISProfileResource.to_json())

# convert the object into a dict
domains_v1_whois_profile_resource_dict = domains_v1_whois_profile_resource_instance.to_dict()
# create an instance of DomainsV1WHOISProfileResource from a dict
domains_v1_whois_profile_resource_from_dict = DomainsV1WHOISProfileResource.from_dict(domains_v1_whois_profile_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


