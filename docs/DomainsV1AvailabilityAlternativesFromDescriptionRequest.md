# DomainsV1AvailabilityAlternativesFromDescriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Free-text description of the project the domain is needed for | 
**limit** | **int** | Amount of domain names to suggest | 

## Example

```python
from hostinger_api.models.domains_v1_availability_alternatives_from_description_request import DomainsV1AvailabilityAlternativesFromDescriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsV1AvailabilityAlternativesFromDescriptionRequest from a JSON string
domains_v1_availability_alternatives_from_description_request_instance = DomainsV1AvailabilityAlternativesFromDescriptionRequest.from_json(json)
# print the JSON string representation of the object
print(DomainsV1AvailabilityAlternativesFromDescriptionRequest.to_json())

# convert the object into a dict
domains_v1_availability_alternatives_from_description_request_dict = domains_v1_availability_alternatives_from_description_request_instance.to_dict()
# create an instance of DomainsV1AvailabilityAlternativesFromDescriptionRequest from a dict
domains_v1_availability_alternatives_from_description_request_from_dict = DomainsV1AvailabilityAlternativesFromDescriptionRequest.from_dict(domains_v1_availability_alternatives_from_description_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


