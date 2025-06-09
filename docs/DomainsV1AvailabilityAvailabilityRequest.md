# DomainsV1AvailabilityAvailabilityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain name (without TLD) | 
**tlds** | **List[str]** | TLDs list | 
**with_alternatives** | **bool** | Should response include alternatives | [optional] [default to False]

## Example

```python
from hostinger_api.models.domains_v1_availability_availability_request import DomainsV1AvailabilityAvailabilityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1AvailabilityAvailabilityRequest from a JSON string
domains_v1_availability_availability_request_instance = DomainsV1AvailabilityAvailabilityRequest.from_json(json)
# print the JSON string representation of the object
print(DomainsV1AvailabilityAvailabilityRequest.to_json())

# convert the object into a dict
domains_v1_availability_availability_request_dict = domains_v1_availability_availability_request_instance.to_dict()
# create an instance of DomainsV1AvailabilityAvailabilityRequest from a dict
domains_v1_availability_availability_request_from_dict = DomainsV1AvailabilityAvailabilityRequest.from_dict(domains_v1_availability_availability_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


