# VPSV1FirewallListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[VPSV1FirewallFirewallResource]**](VPSV1FirewallFirewallResource.md) | Array of [&#x60;VPS.V1.Firewall.FirewallResource&#x60;](#model/vpsv1firewallfirewallresource) | [optional] 
**meta** | [**CommonSchemaPaginationMetaSchema**](CommonSchemaPaginationMetaSchema.md) |  | [optional] 

## Example

```python
from hostinger_api.models.vpsv1_firewall_list_response import VPSV1FirewallListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VPSV1FirewallListResponse from a JSON string
vpsv1_firewall_list_response_instance = VPSV1FirewallListResponse.from_json(json)
# print the JSON string representation of the object
print(VPSV1FirewallListResponse.to_json())

# convert the object into a dict
vpsv1_firewall_list_response_dict = vpsv1_firewall_list_response_instance.to_dict()
# create an instance of VPSV1FirewallListResponse from a dict
vpsv1_firewall_list_response_from_dict = VPSV1FirewallListResponse.from_dict(vpsv1_firewall_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


