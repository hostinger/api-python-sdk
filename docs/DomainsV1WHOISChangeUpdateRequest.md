# DomainsV1WHOISChangeUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_whois_id** | **int** | WHOIS profile ID to assign to the domain | 
**domain** | **str** | Domain name | 
**change_for** | **List[str]** | Contact roles to repoint to the new WHOIS profile | 

## Example

```python
from hostinger_api.models.domains_v1_whois_change_update_request import DomainsV1WHOISChangeUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1WHOISChangeUpdateRequest from a JSON string
domains_v1_whois_change_update_request_instance = DomainsV1WHOISChangeUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(DomainsV1WHOISChangeUpdateRequest.to_json())

# convert the object into a dict
domains_v1_whois_change_update_request_dict = domains_v1_whois_change_update_request_instance.to_dict()
# create an instance of DomainsV1WHOISChangeUpdateRequest from a dict
domains_v1_whois_change_update_request_from_dict = DomainsV1WHOISChangeUpdateRequest.from_dict(domains_v1_whois_change_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


