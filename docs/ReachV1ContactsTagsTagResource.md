# ReachV1ContactsTagsTagResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [optional] 
**type** | **str** | How the tag came about. &#x60;custom&#x60; covers the tags you create yourself, &#x60;form&#x60; covers the ones Reach creates for its forms. | [optional] 
**value** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from hostinger_api.models.reach_v1_contacts_tags_tag_resource import ReachV1ContactsTagsTagResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReachV1ContactsTagsTagResource from a JSON string
reach_v1_contacts_tags_tag_resource_instance = ReachV1ContactsTagsTagResource.from_json(json)
# print the JSON string representation of the object
print(ReachV1ContactsTagsTagResource.to_json())

# convert the object into a dict
reach_v1_contacts_tags_tag_resource_dict = reach_v1_contacts_tags_tag_resource_instance.to_dict()
# create an instance of ReachV1ContactsTagsTagResource from a dict
reach_v1_contacts_tags_tag_resource_from_dict = ReachV1ContactsTagsTagResource.from_dict(reach_v1_contacts_tags_tag_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


