# ReachV1ProfilesDomainsDisconnectRequest

Sending domain to disconnect from the profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | 

## Example

```python
from hostinger_api.models.reach_v1_profiles_domains_disconnect_request import ReachV1ProfilesDomainsDisconnectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ProfilesDomainsDisconnectRequest from a JSON string
reach_v1_profiles_domains_disconnect_request_instance = ReachV1ProfilesDomainsDisconnectRequest.from_json(json)
# print the JSON string representation of the object
print(ReachV1ProfilesDomainsDisconnectRequest.to_json())

# convert the object into a dict
reach_v1_profiles_domains_disconnect_request_dict = reach_v1_profiles_domains_disconnect_request_instance.to_dict()
# create an instance of ReachV1ProfilesDomainsDisconnectRequest from a dict
reach_v1_profiles_domains_disconnect_request_from_dict = ReachV1ProfilesDomainsDisconnectRequest.from_dict(reach_v1_profiles_domains_disconnect_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


