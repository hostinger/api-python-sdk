# DomainsV1WHOISStoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tld** | **str** | TLD of the domain (without leading dot) | 
**country** | **str** | ISO 3166 2-letter country code | 
**entity_type** | **str** | Legal entity type | 
**tld_details** | **object** | TLD details | [optional] 
**whois_details** | **object** | WHOIS details | 

## Example

```python
from hostinger_api.models.domains_v1_whois_store_request import DomainsV1WHOISStoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1WHOISStoreRequest from a JSON string
domains_v1_whois_store_request_instance = DomainsV1WHOISStoreRequest.from_json(json)
# print the JSON string representation of the object
print(DomainsV1WHOISStoreRequest.to_json())

# convert the object into a dict
domains_v1_whois_store_request_dict = domains_v1_whois_store_request_instance.to_dict()
# create an instance of DomainsV1WHOISStoreRequest from a dict
domains_v1_whois_store_request_from_dict = DomainsV1WHOISStoreRequest.from_dict(domains_v1_whois_store_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


