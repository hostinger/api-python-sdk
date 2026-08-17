# AgencyHostingV1PhpUpdateExtensionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extensions** | **List[str]** | Extension names, exactly as returned by the extensions endpoint. | 

## Example

```python
from hostinger_api.models.agency_hosting_v1_php_update_extensions_request import AgencyHostingV1PhpUpdateExtensionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyHostingV1PhpUpdateExtensionsRequest from a JSON string
agency_hosting_v1_php_update_extensions_request_instance = AgencyHostingV1PhpUpdateExtensionsRequest.from_json(json)
# print the JSON string representation of the object
print(AgencyHostingV1PhpUpdateExtensionsRequest.to_json())

# convert the object into a dict
agency_hosting_v1_php_update_extensions_request_dict = agency_hosting_v1_php_update_extensions_request_instance.to_dict()
# create an instance of AgencyHostingV1PhpUpdateExtensionsRequest from a dict
agency_hosting_v1_php_update_extensions_request_from_dict = AgencyHostingV1PhpUpdateExtensionsRequest.from_dict(agency_hosting_v1_php_update_extensions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


