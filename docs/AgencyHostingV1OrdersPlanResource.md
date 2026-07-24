# AgencyHostingV1OrdersPlanResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Plan display name | [optional] 
**key** | **str** | Plan key | [optional] 

## Example

```python
from hostinger_api.models.agency_hosting_v1_orders_plan_resource import AgencyHostingV1OrdersPlanResource

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1OrdersPlanResource from a JSON string
agency_hosting_v1_orders_plan_resource_instance = AgencyHostingV1OrdersPlanResource.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1OrdersPlanResource.to_json())

# convert the object into a dict
agency_hosting_v1_orders_plan_resource_dict = agency_hosting_v1_orders_plan_resource_instance.to_dict()
# create an instance of AgencyHostingV1OrdersPlanResource from a dict
agency_hosting_v1_orders_plan_resource_from_dict = AgencyHostingV1OrdersPlanResource.from_dict(agency_hosting_v1_orders_plan_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


