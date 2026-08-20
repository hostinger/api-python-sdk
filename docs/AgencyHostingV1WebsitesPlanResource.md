# AgencyHostingV1WebsitesPlanResource

Website plan details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**has_cdn** | **bool** |  | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_websites_plan_resource import AgencyHostingV1WebsitesPlanResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1WebsitesPlanResource from a JSON string
agency_hosting_v1_websites_plan_resource_instance = AgencyHostingV1WebsitesPlanResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1WebsitesPlanResource.to_json())

# convert the object into a dict
agency_hosting_v1_websites_plan_resource_dict = agency_hosting_v1_websites_plan_resource_instance.to_dict()
# create an instance of AgencyHostingV1WebsitesPlanResource from a dict
agency_hosting_v1_websites_plan_resource_from_dict = AgencyHostingV1WebsitesPlanResource.from_dict(agency_hosting_v1_websites_plan_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


