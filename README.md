# Hostinger API Python SDK

[![PyPI version](https://badge.fury.io/py/hostinger_api.svg)](https://badge.fury.io/py/hostinger_api)

## About
This is a Python SDK for the [Hostinger API](https://developers.hostinger.com).

For more information, please visit [https://developers.hostinger.com](https://developers.hostinger.com).

## Requirements.

Python 3.9+

## Installation & Usage
### pip install

Setup new virtual environment (optional but recommended):
```sh
python3 -m venv venv
source venv/bin/activate
```

Install the package via [pip](https://pypi.org/project/pip/):
```sh
pip install hostinger_api
```

Then import the package:
```python
import hostinger_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import hostinger_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import hostinger_api
from hostinger_api.rest import ApiException
from pprint import pprint


# Configure Bearer authorization: apiToken
configuration = hostinger_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with hostinger_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hostinger_api.BillingCatalogApi(api_client)
    category = 'VPS' # str | Filter catalog items by category (optional)
    name = '.COM*' # str | Filter catalog items by name. Use `*` for wildcard search, e.g. `.COM*` to find .com domain (optional)

    try:
        # Get catalog item list
        api_response = api_instance.get_catalog_item_list_v1(category=category, name=name)
        print("The response of BillingCatalogApi->get_catalog_item_list_v1:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingCatalogApi->get_catalog_item_list_v1: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://developers.hostinger.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BillingCatalogApi* | [**get_catalog_item_list_v1**](docs/BillingCatalogApi.md#get_catalog_item_list_v1) | **GET** /api/billing/v1/catalog | Get catalog item list
*BillingPaymentMethodsApi* | [**delete_payment_method_v1**](docs/BillingPaymentMethodsApi.md#delete_payment_method_v1) | **DELETE** /api/billing/v1/payment-methods/{paymentMethodId} | Delete payment method
*BillingPaymentMethodsApi* | [**get_payment_method_list_v1**](docs/BillingPaymentMethodsApi.md#get_payment_method_list_v1) | **GET** /api/billing/v1/payment-methods | Get payment method list
*BillingPaymentMethodsApi* | [**set_default_payment_method_v1**](docs/BillingPaymentMethodsApi.md#set_default_payment_method_v1) | **POST** /api/billing/v1/payment-methods/{paymentMethodId} | Set default payment method
*BillingSubscriptionsApi* | [**disable_auto_renewal_v1**](docs/BillingSubscriptionsApi.md#disable_auto_renewal_v1) | **DELETE** /api/billing/v1/subscriptions/{subscriptionId}/auto-renewal/disable | Disable auto-renewal
*BillingSubscriptionsApi* | [**enable_auto_renewal_v1**](docs/BillingSubscriptionsApi.md#enable_auto_renewal_v1) | **PATCH** /api/billing/v1/subscriptions/{subscriptionId}/auto-renewal/enable | Enable auto-renewal
*BillingSubscriptionsApi* | [**get_subscription_list_v1**](docs/BillingSubscriptionsApi.md#get_subscription_list_v1) | **GET** /api/billing/v1/subscriptions | Get subscription list
*DNSSnapshotApi* | [**get_dns_snapshot_list_v1**](docs/DNSSnapshotApi.md#get_dns_snapshot_list_v1) | **GET** /api/dns/v1/snapshots/{domain} | Get DNS snapshot list
*DNSSnapshotApi* | [**get_dns_snapshot_v1**](docs/DNSSnapshotApi.md#get_dns_snapshot_v1) | **GET** /api/dns/v1/snapshots/{domain}/{snapshotId} | Get DNS snapshot
*DNSSnapshotApi* | [**restore_dns_snapshot_v1**](docs/DNSSnapshotApi.md#restore_dns_snapshot_v1) | **POST** /api/dns/v1/snapshots/{domain}/{snapshotId}/restore | Restore DNS snapshot
*DNSZoneApi* | [**delete_dns_records_v1**](docs/DNSZoneApi.md#delete_dns_records_v1) | **DELETE** /api/dns/v1/zones/{domain} | Delete DNS records
*DNSZoneApi* | [**get_dns_records_v1**](docs/DNSZoneApi.md#get_dns_records_v1) | **GET** /api/dns/v1/zones/{domain} | Get DNS records
*DNSZoneApi* | [**reset_dns_records_v1**](docs/DNSZoneApi.md#reset_dns_records_v1) | **POST** /api/dns/v1/zones/{domain}/reset | Reset DNS records
*DNSZoneApi* | [**update_dns_records_v1**](docs/DNSZoneApi.md#update_dns_records_v1) | **PUT** /api/dns/v1/zones/{domain} | Update DNS records
*DNSZoneApi* | [**validate_dns_records_v1**](docs/DNSZoneApi.md#validate_dns_records_v1) | **POST** /api/dns/v1/zones/{domain}/validate | Validate DNS records
*DomainAccessVerifierVerificationsApi* | [**get_domain_verifications_direct**](docs/DomainAccessVerifierVerificationsApi.md#get_domain_verifications_direct) | **GET** /api/v2/direct/verifications/active | Get domain verifications
*DomainsAvailabilityApi* | [**check_domain_availability_v1**](docs/DomainsAvailabilityApi.md#check_domain_availability_v1) | **POST** /api/domains/v1/availability | Check domain availability
*DomainsForwardingApi* | [**create_domain_forwarding_v1**](docs/DomainsForwardingApi.md#create_domain_forwarding_v1) | **POST** /api/domains/v1/forwarding | Create domain forwarding
*DomainsForwardingApi* | [**delete_domain_forwarding_v1**](docs/DomainsForwardingApi.md#delete_domain_forwarding_v1) | **DELETE** /api/domains/v1/forwarding/{domain} | Delete domain forwarding
*DomainsForwardingApi* | [**get_domain_forwarding_v1**](docs/DomainsForwardingApi.md#get_domain_forwarding_v1) | **GET** /api/domains/v1/forwarding/{domain} | Get domain forwarding
*DomainsPortfolioApi* | [**disable_domain_lock_v1**](docs/DomainsPortfolioApi.md#disable_domain_lock_v1) | **DELETE** /api/domains/v1/portfolio/{domain}/domain-lock | Disable domain lock
*DomainsPortfolioApi* | [**disable_privacy_protection_v1**](docs/DomainsPortfolioApi.md#disable_privacy_protection_v1) | **DELETE** /api/domains/v1/portfolio/{domain}/privacy-protection | Disable privacy protection
*DomainsPortfolioApi* | [**enable_domain_lock_v1**](docs/DomainsPortfolioApi.md#enable_domain_lock_v1) | **PUT** /api/domains/v1/portfolio/{domain}/domain-lock | Enable domain lock
*DomainsPortfolioApi* | [**enable_privacy_protection_v1**](docs/DomainsPortfolioApi.md#enable_privacy_protection_v1) | **PUT** /api/domains/v1/portfolio/{domain}/privacy-protection | Enable privacy protection
*DomainsPortfolioApi* | [**get_domain_details_v1**](docs/DomainsPortfolioApi.md#get_domain_details_v1) | **GET** /api/domains/v1/portfolio/{domain} | Get domain details
*DomainsPortfolioApi* | [**get_domain_list_v1**](docs/DomainsPortfolioApi.md#get_domain_list_v1) | **GET** /api/domains/v1/portfolio | Get domain list
*DomainsPortfolioApi* | [**purchase_new_domain_v1**](docs/DomainsPortfolioApi.md#purchase_new_domain_v1) | **POST** /api/domains/v1/portfolio | Purchase new domain
*DomainsPortfolioApi* | [**update_domain_nameservers_v1**](docs/DomainsPortfolioApi.md#update_domain_nameservers_v1) | **PUT** /api/domains/v1/portfolio/{domain}/nameservers | Update domain nameservers
*DomainsWHOISApi* | [**create_whois_profile_v1**](docs/DomainsWHOISApi.md#create_whois_profile_v1) | **POST** /api/domains/v1/whois | Create WHOIS profile
*DomainsWHOISApi* | [**delete_whois_profile_v1**](docs/DomainsWHOISApi.md#delete_whois_profile_v1) | **DELETE** /api/domains/v1/whois/{whoisId} | Delete WHOIS profile
*DomainsWHOISApi* | [**get_whois_profile_list_v1**](docs/DomainsWHOISApi.md#get_whois_profile_list_v1) | **GET** /api/domains/v1/whois | Get WHOIS profile list
*DomainsWHOISApi* | [**get_whois_profile_usage_v1**](docs/DomainsWHOISApi.md#get_whois_profile_usage_v1) | **GET** /api/domains/v1/whois/{whoisId}/usage | Get WHOIS profile usage
*DomainsWHOISApi* | [**get_whois_profile_v1**](docs/DomainsWHOISApi.md#get_whois_profile_v1) | **GET** /api/domains/v1/whois/{whoisId} | Get WHOIS profile
*EcommercePaymentsApi* | [**enable_manual_payment_method_v1**](docs/EcommercePaymentsApi.md#enable_manual_payment_method_v1) | **POST** /api/ecommerce/v1/stores/{store_id}/payment-methods/manual | Enable manual payment method
*EcommerceProductsApi* | [**create_digital_product_v1**](docs/EcommerceProductsApi.md#create_digital_product_v1) | **POST** /api/ecommerce/v1/stores/{store_id}/products/digital | Create digital product
*EcommerceProductsApi* | [**create_physical_product_v1**](docs/EcommerceProductsApi.md#create_physical_product_v1) | **POST** /api/ecommerce/v1/stores/{store_id}/products/physical | Create physical product
*EcommerceShippingApi* | [**set_store_shipping_v1**](docs/EcommerceShippingApi.md#set_store_shipping_v1) | **POST** /api/ecommerce/v1/stores/{store_id}/shipping | Set store shipping
*EcommerceStoresApi* | [**create_store_v1**](docs/EcommerceStoresApi.md#create_store_v1) | **POST** /api/ecommerce/v1/stores | Create store
*EcommerceStoresApi* | [**delete_store_v1**](docs/EcommerceStoresApi.md#delete_store_v1) | **DELETE** /api/ecommerce/v1/stores/{store_id} | Delete store
*EcommerceStoresApi* | [**get_stores_v1**](docs/EcommerceStoresApi.md#get_stores_v1) | **GET** /api/ecommerce/v1/stores | Get stores
*HorizonsWebsitesApi* | [**create_website_v1**](docs/HorizonsWebsitesApi.md#create_website_v1) | **POST** /api/horizons/v1/websites | Create website
*HorizonsWebsitesApi* | [**get_website_v1**](docs/HorizonsWebsitesApi.md#get_website_v1) | **GET** /api/horizons/v1/websites/{websiteId} | Get website
*HostingCronJobsApi* | [**create_account_cron_job_v1**](docs/HostingCronJobsApi.md#create_account_cron_job_v1) | **POST** /api/hosting/v1/accounts/{username}/cron-jobs | Create account cron job
*HostingCronJobsApi* | [**delete_account_cron_job_v1**](docs/HostingCronJobsApi.md#delete_account_cron_job_v1) | **DELETE** /api/hosting/v1/accounts/{username}/cron-jobs/{uid} | Delete account cron job
*HostingCronJobsApi* | [**get_cron_job_output_v1**](docs/HostingCronJobsApi.md#get_cron_job_output_v1) | **GET** /api/hosting/v1/accounts/{username}/cron-jobs/{uid}/output | Get cron job output
*HostingCronJobsApi* | [**list_account_cron_jobs_v1**](docs/HostingCronJobsApi.md#list_account_cron_jobs_v1) | **GET** /api/hosting/v1/accounts/{username}/cron-jobs | List account cron jobs
*HostingDatabasesApi* | [**change_database_password_v1**](docs/HostingDatabasesApi.md#change_database_password_v1) | **PATCH** /api/hosting/v1/accounts/{username}/databases/{name}/change-password | Change database password
*HostingDatabasesApi* | [**create_account_database_remote_connection_v1**](docs/HostingDatabasesApi.md#create_account_database_remote_connection_v1) | **POST** /api/hosting/v1/accounts/{username}/databases/{name}/remote-connections | Create account database remote connection
*HostingDatabasesApi* | [**create_account_database_v1**](docs/HostingDatabasesApi.md#create_account_database_v1) | **POST** /api/hosting/v1/accounts/{username}/databases | Create account database
*HostingDatabasesApi* | [**delete_account_database_remote_connection_v1**](docs/HostingDatabasesApi.md#delete_account_database_remote_connection_v1) | **DELETE** /api/hosting/v1/accounts/{username}/databases/{name}/remote-connections | Delete account database remote connection
*HostingDatabasesApi* | [**delete_account_database_v1**](docs/HostingDatabasesApi.md#delete_account_database_v1) | **DELETE** /api/hosting/v1/accounts/{username}/databases/{name} | Delete account database
*HostingDatabasesApi* | [**get_php_my_admin_link_v1**](docs/HostingDatabasesApi.md#get_php_my_admin_link_v1) | **GET** /api/hosting/v1/accounts/{username}/databases/{name}/phpmyadmin-link | Get phpMyAdmin link
*HostingDatabasesApi* | [**list_account_database_remote_connections_v1**](docs/HostingDatabasesApi.md#list_account_database_remote_connections_v1) | **GET** /api/hosting/v1/accounts/{username}/databases/remote-connections | List account database remote connections
*HostingDatabasesApi* | [**list_account_databases_v1**](docs/HostingDatabasesApi.md#list_account_databases_v1) | **GET** /api/hosting/v1/accounts/{username}/databases | List account databases
*HostingDatabasesApi* | [**repair_database_v1**](docs/HostingDatabasesApi.md#repair_database_v1) | **PATCH** /api/hosting/v1/accounts/{username}/databases/{name}/repair | Repair database
*HostingDatacentersApi* | [**list_available_datacenters_v1**](docs/HostingDatacentersApi.md#list_available_datacenters_v1) | **GET** /api/hosting/v1/datacenters | List available datacenters
*HostingDomainsApi* | [**create_website_parked_domain_v1**](docs/HostingDomainsApi.md#create_website_parked_domain_v1) | **POST** /api/hosting/v1/accounts/{username}/websites/{domain}/parked-domains | Create website parked domain
*HostingDomainsApi* | [**create_website_subdomain_v1**](docs/HostingDomainsApi.md#create_website_subdomain_v1) | **POST** /api/hosting/v1/accounts/{username}/websites/{domain}/subdomains | Create website subdomain
*HostingDomainsApi* | [**delete_website_parked_domain_v1**](docs/HostingDomainsApi.md#delete_website_parked_domain_v1) | **DELETE** /api/hosting/v1/accounts/{username}/websites/{domain}/parked-domains/{parkedDomain} | Delete website parked domain
*HostingDomainsApi* | [**delete_website_subdomain_v1**](docs/HostingDomainsApi.md#delete_website_subdomain_v1) | **DELETE** /api/hosting/v1/accounts/{username}/websites/{domain}/subdomains/{subdomain} | Delete website subdomain
*HostingDomainsApi* | [**generate_a_free_subdomain_v1**](docs/HostingDomainsApi.md#generate_a_free_subdomain_v1) | **POST** /api/hosting/v1/domains/free-subdomains | Generate a free subdomain
*HostingDomainsApi* | [**list_website_parked_domains_v1**](docs/HostingDomainsApi.md#list_website_parked_domains_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/parked-domains | List website parked domains
*HostingDomainsApi* | [**list_website_subdomains_v1**](docs/HostingDomainsApi.md#list_website_subdomains_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/subdomains | List website subdomains
*HostingDomainsApi* | [**verify_domain_ownership_v1**](docs/HostingDomainsApi.md#verify_domain_ownership_v1) | **POST** /api/hosting/v1/domains/verify-ownership | Verify domain ownership
*HostingNodeJSApi* | [**create_node_js_build_from_archive_v1**](docs/HostingNodeJSApi.md#create_node_js_build_from_archive_v1) | **POST** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/builds/from-archive | Create NodeJS build from archive
*HostingNodeJSApi* | [**get_node_js_build_logs_v1**](docs/HostingNodeJSApi.md#get_node_js_build_logs_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/builds/{uuid}/logs | Get NodeJS build logs
*HostingNodeJSApi* | [**list_node_js_builds_v1**](docs/HostingNodeJSApi.md#list_node_js_builds_v1) | **GET** /api/hosting/v1/accounts/{username}/websites/{domain}/nodejs/builds | List NodeJS builds
*HostingOrdersApi* | [**list_orders_v1**](docs/HostingOrdersApi.md#list_orders_v1) | **GET** /api/hosting/v1/orders | List orders
*HostingWebsitesApi* | [**create_website_v1**](docs/HostingWebsitesApi.md#create_website_v1) | **POST** /api/hosting/v1/websites | Create website
*HostingWebsitesApi* | [**list_websites_v1**](docs/HostingWebsitesApi.md#list_websites_v1) | **GET** /api/hosting/v1/websites | List websites
*ReachContactsApi* | [**create_a_new_contact_v1**](docs/ReachContactsApi.md#create_a_new_contact_v1) | **POST** /api/reach/v1/contacts | Create a new contact
*ReachContactsApi* | [**create_new_contacts_v1**](docs/ReachContactsApi.md#create_new_contacts_v1) | **POST** /api/reach/v1/profiles/{profileUuid}/contacts | Create new contacts
*ReachContactsApi* | [**delete_a_contact_v1**](docs/ReachContactsApi.md#delete_a_contact_v1) | **DELETE** /api/reach/v1/contacts/{uuid} | Delete a contact
*ReachContactsApi* | [**list_contact_groups_v1**](docs/ReachContactsApi.md#list_contact_groups_v1) | **GET** /api/reach/v1/contacts/groups | List contact groups
*ReachContactsApi* | [**list_contacts_v1**](docs/ReachContactsApi.md#list_contacts_v1) | **GET** /api/reach/v1/contacts | List contacts
*ReachProfilesApi* | [**get_profile_domain_dns_status_v1**](docs/ReachProfilesApi.md#get_profile_domain_dns_status_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/domains/dns-status | Get profile domain DNS status
*ReachProfilesApi* | [**list_profiles_v1**](docs/ReachProfilesApi.md#list_profiles_v1) | **GET** /api/reach/v1/profiles | List Profiles
*ReachSegmentsApi* | [**create_a_new_contact_segment_v1**](docs/ReachSegmentsApi.md#create_a_new_contact_segment_v1) | **POST** /api/reach/v1/segmentation/segments | Create a new contact segment
*ReachSegmentsApi* | [**get_segment_details_v1**](docs/ReachSegmentsApi.md#get_segment_details_v1) | **GET** /api/reach/v1/segmentation/segments/{segmentUuid} | Get segment details
*ReachSegmentsApi* | [**list_profile_segment_contacts_v1**](docs/ReachSegmentsApi.md#list_profile_segment_contacts_v1) | **GET** /api/reach/v1/profiles/{profileUuid}/segmentation/segments/{segmentUuid}/contacts | List profile segment contacts
*ReachSegmentsApi* | [**list_segment_contacts_v1**](docs/ReachSegmentsApi.md#list_segment_contacts_v1) | **GET** /api/reach/v1/segmentation/segments/{segmentUuid}/contacts | List segment contacts
*ReachSegmentsApi* | [**list_segments_v1**](docs/ReachSegmentsApi.md#list_segments_v1) | **GET** /api/reach/v1/segmentation/segments | List segments
*VPSActionsApi* | [**get_action_details_v1**](docs/VPSActionsApi.md#get_action_details_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/actions/{actionId} | Get action details
*VPSActionsApi* | [**get_actions_v1**](docs/VPSActionsApi.md#get_actions_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/actions | Get actions
*VPSBackupsApi* | [**get_backups_v1**](docs/VPSBackupsApi.md#get_backups_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/backups | Get backups
*VPSBackupsApi* | [**restore_backup_v1**](docs/VPSBackupsApi.md#restore_backup_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/backups/{backupId}/restore | Restore backup
*VPSDataCentersApi* | [**get_data_center_list_v1**](docs/VPSDataCentersApi.md#get_data_center_list_v1) | **GET** /api/vps/v1/data-centers | Get data center list
*VPSDockerManagerApi* | [**create_new_project_v1**](docs/VPSDockerManagerApi.md#create_new_project_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/docker | Create new project
*VPSDockerManagerApi* | [**delete_project_v1**](docs/VPSDockerManagerApi.md#delete_project_v1) | **DELETE** /api/vps/v1/virtual-machines/{virtualMachineId}/docker/{projectName}/down | Delete project
*VPSDockerManagerApi* | [**get_project_containers_v1**](docs/VPSDockerManagerApi.md#get_project_containers_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/docker/{projectName}/containers | Get project containers
*VPSDockerManagerApi* | [**get_project_contents_v1**](docs/VPSDockerManagerApi.md#get_project_contents_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/docker/{projectName} | Get project contents
*VPSDockerManagerApi* | [**get_project_list_v1**](docs/VPSDockerManagerApi.md#get_project_list_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/docker | Get project list
*VPSDockerManagerApi* | [**get_project_logs_v1**](docs/VPSDockerManagerApi.md#get_project_logs_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/docker/{projectName}/logs | Get project logs
*VPSDockerManagerApi* | [**restart_project_v1**](docs/VPSDockerManagerApi.md#restart_project_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/docker/{projectName}/restart | Restart project
*VPSDockerManagerApi* | [**start_project_v1**](docs/VPSDockerManagerApi.md#start_project_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/docker/{projectName}/start | Start project
*VPSDockerManagerApi* | [**stop_project_v1**](docs/VPSDockerManagerApi.md#stop_project_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/docker/{projectName}/stop | Stop project
*VPSDockerManagerApi* | [**update_project_v1**](docs/VPSDockerManagerApi.md#update_project_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/docker/{projectName}/update | Update project
*VPSFirewallApi* | [**activate_firewall_v1**](docs/VPSFirewallApi.md#activate_firewall_v1) | **POST** /api/vps/v1/firewall/{firewallId}/activate/{virtualMachineId} | Activate firewall
*VPSFirewallApi* | [**create_firewall_rule_v1**](docs/VPSFirewallApi.md#create_firewall_rule_v1) | **POST** /api/vps/v1/firewall/{firewallId}/rules | Create firewall rule
*VPSFirewallApi* | [**create_new_firewall_v1**](docs/VPSFirewallApi.md#create_new_firewall_v1) | **POST** /api/vps/v1/firewall | Create new firewall
*VPSFirewallApi* | [**deactivate_firewall_v1**](docs/VPSFirewallApi.md#deactivate_firewall_v1) | **POST** /api/vps/v1/firewall/{firewallId}/deactivate/{virtualMachineId} | Deactivate firewall
*VPSFirewallApi* | [**delete_firewall_rule_v1**](docs/VPSFirewallApi.md#delete_firewall_rule_v1) | **DELETE** /api/vps/v1/firewall/{firewallId}/rules/{ruleId} | Delete firewall rule
*VPSFirewallApi* | [**delete_firewall_v1**](docs/VPSFirewallApi.md#delete_firewall_v1) | **DELETE** /api/vps/v1/firewall/{firewallId} | Delete firewall
*VPSFirewallApi* | [**get_firewall_details_v1**](docs/VPSFirewallApi.md#get_firewall_details_v1) | **GET** /api/vps/v1/firewall/{firewallId} | Get firewall details
*VPSFirewallApi* | [**get_firewall_list_v1**](docs/VPSFirewallApi.md#get_firewall_list_v1) | **GET** /api/vps/v1/firewall | Get firewall list
*VPSFirewallApi* | [**sync_firewall_v1**](docs/VPSFirewallApi.md#sync_firewall_v1) | **POST** /api/vps/v1/firewall/{firewallId}/sync/{virtualMachineId} | Sync firewall
*VPSFirewallApi* | [**update_firewall_rule_v1**](docs/VPSFirewallApi.md#update_firewall_rule_v1) | **PUT** /api/vps/v1/firewall/{firewallId}/rules/{ruleId} | Update firewall rule
*VPSMalwareScannerApi* | [**get_scan_metrics_v1**](docs/VPSMalwareScannerApi.md#get_scan_metrics_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/monarx | Get scan metrics
*VPSMalwareScannerApi* | [**install_monarx_v1**](docs/VPSMalwareScannerApi.md#install_monarx_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/monarx | Install Monarx
*VPSMalwareScannerApi* | [**uninstall_monarx_v1**](docs/VPSMalwareScannerApi.md#uninstall_monarx_v1) | **DELETE** /api/vps/v1/virtual-machines/{virtualMachineId}/monarx | Uninstall Monarx
*VPSOSTemplatesApi* | [**get_template_details_v1**](docs/VPSOSTemplatesApi.md#get_template_details_v1) | **GET** /api/vps/v1/templates/{templateId} | Get template details
*VPSOSTemplatesApi* | [**get_templates_v1**](docs/VPSOSTemplatesApi.md#get_templates_v1) | **GET** /api/vps/v1/templates | Get templates
*VPSPTRRecordsApi* | [**create_ptr_record_v1**](docs/VPSPTRRecordsApi.md#create_ptr_record_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/ptr/{ipAddressId} | Create PTR record
*VPSPTRRecordsApi* | [**delete_ptr_record_v1**](docs/VPSPTRRecordsApi.md#delete_ptr_record_v1) | **DELETE** /api/vps/v1/virtual-machines/{virtualMachineId}/ptr/{ipAddressId} | Delete PTR record
*VPSPostInstallScriptsApi* | [**create_post_install_script_v1**](docs/VPSPostInstallScriptsApi.md#create_post_install_script_v1) | **POST** /api/vps/v1/post-install-scripts | Create post-install script
*VPSPostInstallScriptsApi* | [**delete_post_install_script_v1**](docs/VPSPostInstallScriptsApi.md#delete_post_install_script_v1) | **DELETE** /api/vps/v1/post-install-scripts/{postInstallScriptId} | Delete post-install script
*VPSPostInstallScriptsApi* | [**get_post_install_script_v1**](docs/VPSPostInstallScriptsApi.md#get_post_install_script_v1) | **GET** /api/vps/v1/post-install-scripts/{postInstallScriptId} | Get post-install script
*VPSPostInstallScriptsApi* | [**get_post_install_scripts_v1**](docs/VPSPostInstallScriptsApi.md#get_post_install_scripts_v1) | **GET** /api/vps/v1/post-install-scripts | Get post-install scripts
*VPSPostInstallScriptsApi* | [**update_post_install_script_v1**](docs/VPSPostInstallScriptsApi.md#update_post_install_script_v1) | **PUT** /api/vps/v1/post-install-scripts/{postInstallScriptId} | Update post-install script
*VPSPublicKeysApi* | [**attach_public_key_v1**](docs/VPSPublicKeysApi.md#attach_public_key_v1) | **POST** /api/vps/v1/public-keys/attach/{virtualMachineId} | Attach public key
*VPSPublicKeysApi* | [**create_public_key_v1**](docs/VPSPublicKeysApi.md#create_public_key_v1) | **POST** /api/vps/v1/public-keys | Create public key
*VPSPublicKeysApi* | [**delete_public_key_v1**](docs/VPSPublicKeysApi.md#delete_public_key_v1) | **DELETE** /api/vps/v1/public-keys/{publicKeyId} | Delete public key
*VPSPublicKeysApi* | [**get_public_keys_v1**](docs/VPSPublicKeysApi.md#get_public_keys_v1) | **GET** /api/vps/v1/public-keys | Get public keys
*VPSRecoveryApi* | [**start_recovery_mode_v1**](docs/VPSRecoveryApi.md#start_recovery_mode_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/recovery | Start recovery mode
*VPSRecoveryApi* | [**stop_recovery_mode_v1**](docs/VPSRecoveryApi.md#stop_recovery_mode_v1) | **DELETE** /api/vps/v1/virtual-machines/{virtualMachineId}/recovery | Stop recovery mode
*VPSSnapshotsApi* | [**create_snapshot_v1**](docs/VPSSnapshotsApi.md#create_snapshot_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/snapshot | Create snapshot
*VPSSnapshotsApi* | [**delete_snapshot_v1**](docs/VPSSnapshotsApi.md#delete_snapshot_v1) | **DELETE** /api/vps/v1/virtual-machines/{virtualMachineId}/snapshot | Delete snapshot
*VPSSnapshotsApi* | [**get_snapshot_v1**](docs/VPSSnapshotsApi.md#get_snapshot_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/snapshot | Get snapshot
*VPSSnapshotsApi* | [**restore_snapshot_v1**](docs/VPSSnapshotsApi.md#restore_snapshot_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/snapshot/restore | Restore snapshot
*VPSVirtualMachineApi* | [**get_attached_public_keys_v1**](docs/VPSVirtualMachineApi.md#get_attached_public_keys_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/public-keys | Get attached public keys
*VPSVirtualMachineApi* | [**get_metrics_v1**](docs/VPSVirtualMachineApi.md#get_metrics_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId}/metrics | Get metrics
*VPSVirtualMachineApi* | [**get_virtual_machine_details_v1**](docs/VPSVirtualMachineApi.md#get_virtual_machine_details_v1) | **GET** /api/vps/v1/virtual-machines/{virtualMachineId} | Get virtual machine details
*VPSVirtualMachineApi* | [**get_virtual_machines_v1**](docs/VPSVirtualMachineApi.md#get_virtual_machines_v1) | **GET** /api/vps/v1/virtual-machines | Get virtual machines
*VPSVirtualMachineApi* | [**purchase_new_virtual_machine_v1**](docs/VPSVirtualMachineApi.md#purchase_new_virtual_machine_v1) | **POST** /api/vps/v1/virtual-machines | Purchase new virtual machine
*VPSVirtualMachineApi* | [**recreate_virtual_machine_v1**](docs/VPSVirtualMachineApi.md#recreate_virtual_machine_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/recreate | Recreate virtual machine
*VPSVirtualMachineApi* | [**reset_hostname_v1**](docs/VPSVirtualMachineApi.md#reset_hostname_v1) | **DELETE** /api/vps/v1/virtual-machines/{virtualMachineId}/hostname | Reset hostname
*VPSVirtualMachineApi* | [**restart_virtual_machine_v1**](docs/VPSVirtualMachineApi.md#restart_virtual_machine_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/restart | Restart virtual machine
*VPSVirtualMachineApi* | [**set_hostname_v1**](docs/VPSVirtualMachineApi.md#set_hostname_v1) | **PUT** /api/vps/v1/virtual-machines/{virtualMachineId}/hostname | Set hostname
*VPSVirtualMachineApi* | [**set_nameservers_v1**](docs/VPSVirtualMachineApi.md#set_nameservers_v1) | **PUT** /api/vps/v1/virtual-machines/{virtualMachineId}/nameservers | Set nameservers
*VPSVirtualMachineApi* | [**set_panel_password_v1**](docs/VPSVirtualMachineApi.md#set_panel_password_v1) | **PUT** /api/vps/v1/virtual-machines/{virtualMachineId}/panel-password | Set panel password
*VPSVirtualMachineApi* | [**set_root_password_v1**](docs/VPSVirtualMachineApi.md#set_root_password_v1) | **PUT** /api/vps/v1/virtual-machines/{virtualMachineId}/root-password | Set root password
*VPSVirtualMachineApi* | [**setup_purchased_virtual_machine_v1**](docs/VPSVirtualMachineApi.md#setup_purchased_virtual_machine_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/setup | Setup purchased virtual machine
*VPSVirtualMachineApi* | [**start_virtual_machine_v1**](docs/VPSVirtualMachineApi.md#start_virtual_machine_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/start | Start virtual machine
*VPSVirtualMachineApi* | [**stop_virtual_machine_v1**](docs/VPSVirtualMachineApi.md#stop_virtual_machine_v1) | **POST** /api/vps/v1/virtual-machines/{virtualMachineId}/stop | Stop virtual machine
*WordPressInstallationsApi* | [**install_word_press_v1**](docs/WordPressInstallationsApi.md#install_word_press_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/installations | Install WordPress
*WordPressInstallationsApi* | [**list_word_press_installations_v1**](docs/WordPressInstallationsApi.md#list_word_press_installations_v1) | **GET** /api/hosting/v1/wordpress/installations | List WordPress installations
*WordPressPluginsApi* | [**activate_word_press_plugin_v1**](docs/WordPressPluginsApi.md#activate_word_press_plugin_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/{software}/plugins/activate | Activate WordPress plugin
*WordPressPluginsApi* | [**check_if_woo_commerce_is_installed_v1**](docs/WordPressPluginsApi.md#check_if_woo_commerce_is_installed_v1) | **GET** /api/hosting/v1/wordpress/plugins/is-woocommerce-installed | Check if WooCommerce is installed
*WordPressPluginsApi* | [**deactivate_word_press_plugin_v1**](docs/WordPressPluginsApi.md#deactivate_word_press_plugin_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/{software}/plugins/deactivate | Deactivate WordPress plugin
*WordPressPluginsApi* | [**install_word_press_plugins_v1**](docs/WordPressPluginsApi.md#install_word_press_plugins_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/{software}/plugins/install | Install WordPress plugins
*WordPressPluginsApi* | [**list_available_word_press_plugins_v1**](docs/WordPressPluginsApi.md#list_available_word_press_plugins_v1) | **GET** /api/hosting/v1/accounts/{username}/wordpress/{software}/plugins/available | List available WordPress plugins
*WordPressPluginsApi* | [**list_installed_word_press_plugins_v1**](docs/WordPressPluginsApi.md#list_installed_word_press_plugins_v1) | **GET** /api/hosting/v1/accounts/{username}/wordpress/{software}/plugins | List installed WordPress plugins
*WordPressPluginsApi* | [**list_suggested_word_press_plugins_v1**](docs/WordPressPluginsApi.md#list_suggested_word_press_plugins_v1) | **GET** /api/hosting/v1/wordpress/plugins/suggested | List suggested WordPress plugins
*WordPressPluginsApi* | [**search_word_press_plugins_v1**](docs/WordPressPluginsApi.md#search_word_press_plugins_v1) | **GET** /api/hosting/v1/wordpress/plugins | Search WordPress plugins
*WordPressPluginsApi* | [**uninstall_word_press_plugins_v1**](docs/WordPressPluginsApi.md#uninstall_word_press_plugins_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/{software}/plugins/uninstall | Uninstall WordPress plugins
*WordPressPluginsApi* | [**update_hostinger_word_press_plugin_v1**](docs/WordPressPluginsApi.md#update_hostinger_word_press_plugin_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/{software}/plugins/hostinger/update | Update Hostinger WordPress plugin
*WordPressPluginsApi* | [**update_word_press_plugins_v1**](docs/WordPressPluginsApi.md#update_word_press_plugins_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/{software}/plugins/update | Update WordPress plugins
*WordPressThemesApi* | [**activate_word_press_theme_v1**](docs/WordPressThemesApi.md#activate_word_press_theme_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/{software}/themes/activate | Activate WordPress theme
*WordPressThemesApi* | [**install_word_press_theme_v1**](docs/WordPressThemesApi.md#install_word_press_theme_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/{software}/themes/install | Install WordPress theme
*WordPressThemesApi* | [**list_installed_word_press_themes_v1**](docs/WordPressThemesApi.md#list_installed_word_press_themes_v1) | **GET** /api/hosting/v1/accounts/{username}/wordpress/{software}/themes | List installed WordPress themes
*WordPressThemesApi* | [**list_word_press_themes_v1**](docs/WordPressThemesApi.md#list_word_press_themes_v1) | **GET** /api/hosting/v1/wordpress/themes | List WordPress themes
*WordPressThemesApi* | [**uninstall_word_press_themes_v1**](docs/WordPressThemesApi.md#uninstall_word_press_themes_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/{software}/themes/uninstall | Uninstall WordPress themes
*WordPressThemesApi* | [**update_word_press_themes_v1**](docs/WordPressThemesApi.md#update_word_press_themes_v1) | **POST** /api/hosting/v1/accounts/{username}/wordpress/{software}/themes/update | Update WordPress themes


## Documentation For Models

 - [BillingV1CatalogCatalogItemPriceResource](docs/BillingV1CatalogCatalogItemPriceResource.md)
 - [BillingV1CatalogCatalogItemResource](docs/BillingV1CatalogCatalogItemResource.md)
 - [BillingV1OrderOrderBillingAddressResource](docs/BillingV1OrderOrderBillingAddressResource.md)
 - [BillingV1OrderOrderResource](docs/BillingV1OrderOrderResource.md)
 - [BillingV1OrderVirtualMachineOrderResource](docs/BillingV1OrderVirtualMachineOrderResource.md)
 - [BillingV1PaymentMethodPaymentMethodResource](docs/BillingV1PaymentMethodPaymentMethodResource.md)
 - [BillingV1SubscriptionCancelRequest](docs/BillingV1SubscriptionCancelRequest.md)
 - [BillingV1SubscriptionSubscriptionResource](docs/BillingV1SubscriptionSubscriptionResource.md)
 - [CommonSchemaPaginationMetaSchema](docs/CommonSchemaPaginationMetaSchema.md)
 - [CommonSuccessEmptyResource](docs/CommonSuccessEmptyResource.md)
 - [DNSV1SnapshotSnapshotResource](docs/DNSV1SnapshotSnapshotResource.md)
 - [DNSV1SnapshotSnapshotWithContentResource](docs/DNSV1SnapshotSnapshotWithContentResource.md)
 - [DNSV1ZoneDestroyRequest](docs/DNSV1ZoneDestroyRequest.md)
 - [DNSV1ZoneDestroyRequestFiltersInner](docs/DNSV1ZoneDestroyRequestFiltersInner.md)
 - [DNSV1ZoneNameRecordResource](docs/DNSV1ZoneNameRecordResource.md)
 - [DNSV1ZoneRecordResource](docs/DNSV1ZoneRecordResource.md)
 - [DNSV1ZoneResetRequest](docs/DNSV1ZoneResetRequest.md)
 - [DNSV1ZoneUpdateRequest](docs/DNSV1ZoneUpdateRequest.md)
 - [DNSV1ZoneUpdateRequestZoneInner](docs/DNSV1ZoneUpdateRequestZoneInner.md)
 - [DNSV1ZoneUpdateRequestZoneInnerRecordsInner](docs/DNSV1ZoneUpdateRequestZoneInnerRecordsInner.md)
 - [DomainAccessVerifierV2VerificationsActiveVerificationsCollection](docs/DomainAccessVerifierV2VerificationsActiveVerificationsCollection.md)
 - [DomainAccessVerifierV2VerificationsActiveVerificationsCollectionData](docs/DomainAccessVerifierV2VerificationsActiveVerificationsCollectionData.md)
 - [DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataPENDING](docs/DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataPENDING.md)
 - [DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataPENDINGDOMAINTLD](docs/DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataPENDINGDOMAINTLD.md)
 - [DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataPENDINGDOMAINTLDVERIFICATIONTYPE](docs/DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataPENDINGDOMAINTLDVERIFICATIONTYPE.md)
 - [DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataVERIFIED](docs/DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataVERIFIED.md)
 - [DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataVERIFIEDDOMAINTLD](docs/DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataVERIFIEDDOMAINTLD.md)
 - [DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataVERIFIEDDOMAINTLDVERIFICATIONTYPE](docs/DomainAccessVerifierV2VerificationsActiveVerificationsCollectionDataVERIFIEDDOMAINTLDVERIFICATIONTYPE.md)
 - [DomainAccessVerifierV2VerificationsListRequest](docs/DomainAccessVerifierV2VerificationsListRequest.md)
 - [DomainsV1AvailabilityAvailabilityRequest](docs/DomainsV1AvailabilityAvailabilityRequest.md)
 - [DomainsV1AvailabilityAvailabilityResource](docs/DomainsV1AvailabilityAvailabilityResource.md)
 - [DomainsV1DomainDomainExtendedResource](docs/DomainsV1DomainDomainExtendedResource.md)
 - [DomainsV1DomainDomainExtendedResourceDomainContacts](docs/DomainsV1DomainDomainExtendedResourceDomainContacts.md)
 - [DomainsV1DomainDomainExtendedResourceNameServers](docs/DomainsV1DomainDomainExtendedResourceNameServers.md)
 - [DomainsV1DomainDomainResource](docs/DomainsV1DomainDomainResource.md)
 - [DomainsV1ForwardingForwardingResource](docs/DomainsV1ForwardingForwardingResource.md)
 - [DomainsV1ForwardingStoreRequest](docs/DomainsV1ForwardingStoreRequest.md)
 - [DomainsV1PortfolioPurchaseRequest](docs/DomainsV1PortfolioPurchaseRequest.md)
 - [DomainsV1PortfolioPurchaseRequestDomainContacts](docs/DomainsV1PortfolioPurchaseRequestDomainContacts.md)
 - [DomainsV1PortfolioUpdateNameserversRequest](docs/DomainsV1PortfolioUpdateNameserversRequest.md)
 - [DomainsV1WHOISProfileResource](docs/DomainsV1WHOISProfileResource.md)
 - [DomainsV1WHOISStoreRequest](docs/DomainsV1WHOISStoreRequest.md)
 - [EcommerceGetStoresV1200Response](docs/EcommerceGetStoresV1200Response.md)
 - [EcommerceV1PaymentEnableManualPaymentRequest](docs/EcommerceV1PaymentEnableManualPaymentRequest.md)
 - [EcommerceV1PaymentManualPaymentResource](docs/EcommerceV1PaymentManualPaymentResource.md)
 - [EcommerceV1PaymentManualPaymentResourcePaymentMethod](docs/EcommerceV1PaymentManualPaymentResourcePaymentMethod.md)
 - [EcommerceV1ProductCreateDigitalProductRequest](docs/EcommerceV1ProductCreateDigitalProductRequest.md)
 - [EcommerceV1ProductCreatePhysicalProductRequest](docs/EcommerceV1ProductCreatePhysicalProductRequest.md)
 - [EcommerceV1ProductProductCreationResource](docs/EcommerceV1ProductProductCreationResource.md)
 - [EcommerceV1ProductProductCreationResourceProduct](docs/EcommerceV1ProductProductCreationResourceProduct.md)
 - [EcommerceV1ShippingSetShippingRequest](docs/EcommerceV1ShippingSetShippingRequest.md)
 - [EcommerceV1ShippingShippingResource](docs/EcommerceV1ShippingShippingResource.md)
 - [EcommerceV1ShippingShippingResourceShippingOption](docs/EcommerceV1ShippingShippingResourceShippingOption.md)
 - [EcommerceV1StoreStoreCreationResource](docs/EcommerceV1StoreStoreCreationResource.md)
 - [EcommerceV1StoreStoreCreationResourceSalesChannel](docs/EcommerceV1StoreStoreCreationResourceSalesChannel.md)
 - [EcommerceV1StoreStoreCreationResourceStore](docs/EcommerceV1StoreStoreCreationResourceStore.md)
 - [EcommerceV1StoreStoreDeleteResource](docs/EcommerceV1StoreStoreDeleteResource.md)
 - [EcommerceV1StoreStoreRequest](docs/EcommerceV1StoreStoreRequest.md)
 - [EcommerceV1StoreStoreRequestSalesChannel](docs/EcommerceV1StoreStoreRequestSalesChannel.md)
 - [EcommerceV1StoreStoreResource](docs/EcommerceV1StoreStoreResource.md)
 - [HorizonsV1WebsitesCreateWebsiteRequest](docs/HorizonsV1WebsitesCreateWebsiteRequest.md)
 - [HorizonsV1WebsitesCreateWebsiteRequestMessageInner](docs/HorizonsV1WebsitesCreateWebsiteRequestMessageInner.md)
 - [HorizonsV1WebsitesCreatedWebsiteResource](docs/HorizonsV1WebsitesCreatedWebsiteResource.md)
 - [HorizonsV1WebsitesWebsiteUrlResource](docs/HorizonsV1WebsitesWebsiteUrlResource.md)
 - [HostingListAccountDatabasesV1200Response](docs/HostingListAccountDatabasesV1200Response.md)
 - [HostingListNodeJSBuildsV1200Response](docs/HostingListNodeJSBuildsV1200Response.md)
 - [HostingListOrdersV1200Response](docs/HostingListOrdersV1200Response.md)
 - [HostingListWebsitesV1200Response](docs/HostingListWebsitesV1200Response.md)
 - [HostingV1CronJobsCreateCronJobRequest](docs/HostingV1CronJobsCreateCronJobRequest.md)
 - [HostingV1CronJobsCronJobOutputResource](docs/HostingV1CronJobsCronJobOutputResource.md)
 - [HostingV1CronJobsCronJobResource](docs/HostingV1CronJobsCronJobResource.md)
 - [HostingV1DatabasesChangeDatabasePasswordRequest](docs/HostingV1DatabasesChangeDatabasePasswordRequest.md)
 - [HostingV1DatabasesCreateDatabaseRequest](docs/HostingV1DatabasesCreateDatabaseRequest.md)
 - [HostingV1DatabasesDatabaseResource](docs/HostingV1DatabasesDatabaseResource.md)
 - [HostingV1DatabasesPhpMyAdminLinkResource](docs/HostingV1DatabasesPhpMyAdminLinkResource.md)
 - [HostingV1DatabasesRemoteConnectionsCreateRemoteConnectionRequest](docs/HostingV1DatabasesRemoteConnectionsCreateRemoteConnectionRequest.md)
 - [HostingV1DatabasesRemoteConnectionsRemoteConnectionResource](docs/HostingV1DatabasesRemoteConnectionsRemoteConnectionResource.md)
 - [HostingV1DatacenterCoordinatesResource](docs/HostingV1DatacenterCoordinatesResource.md)
 - [HostingV1DatacenterDatacenterResource](docs/HostingV1DatacenterDatacenterResource.md)
 - [HostingV1DatacentersListRequest](docs/HostingV1DatacentersListRequest.md)
 - [HostingV1DomainsCreateParkedDomainRequest](docs/HostingV1DomainsCreateParkedDomainRequest.md)
 - [HostingV1DomainsCreateSubdomainRequest](docs/HostingV1DomainsCreateSubdomainRequest.md)
 - [HostingV1DomainsDomainAccessResource](docs/HostingV1DomainsDomainAccessResource.md)
 - [HostingV1DomainsFreeSubdomainResource](docs/HostingV1DomainsFreeSubdomainResource.md)
 - [HostingV1DomainsParkedDomainResource](docs/HostingV1DomainsParkedDomainResource.md)
 - [HostingV1DomainsSubdomainResource](docs/HostingV1DomainsSubdomainResource.md)
 - [HostingV1DomainsVerifyOwnershipRequest](docs/HostingV1DomainsVerifyOwnershipRequest.md)
 - [HostingV1NodeJsBuildLogsResource](docs/HostingV1NodeJsBuildLogsResource.md)
 - [HostingV1NodeJsBuildOptionsResource](docs/HostingV1NodeJsBuildOptionsResource.md)
 - [HostingV1NodeJsBuildResource](docs/HostingV1NodeJsBuildResource.md)
 - [HostingV1NodeJsCreateFromArchiveRequest](docs/HostingV1NodeJsCreateFromArchiveRequest.md)
 - [HostingV1NodeJsSourceOptionsResource](docs/HostingV1NodeJsSourceOptionsResource.md)
 - [HostingV1OrdersOrderResource](docs/HostingV1OrdersOrderResource.md)
 - [HostingV1OrdersPlanResource](docs/HostingV1OrdersPlanResource.md)
 - [HostingV1WebsitesCreateWebsiteRequest](docs/HostingV1WebsitesCreateWebsiteRequest.md)
 - [HostingV1WebsitesWebsiteResource](docs/HostingV1WebsitesWebsiteResource.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InlineObject2](docs/InlineObject2.md)
 - [InlineObject2Errors](docs/InlineObject2Errors.md)
 - [ReachListContactsV1200Response](docs/ReachListContactsV1200Response.md)
 - [ReachListProfileSegmentContactsV1200Response](docs/ReachListProfileSegmentContactsV1200Response.md)
 - [ReachV1ContactsContactResource](docs/ReachV1ContactsContactResource.md)
 - [ReachV1ContactsGroupsContactGroupResource](docs/ReachV1ContactsGroupsContactGroupResource.md)
 - [ReachV1ContactsSegmentsContactSegmentResource](docs/ReachV1ContactsSegmentsContactSegmentResource.md)
 - [ReachV1ContactsSegmentsSegmentResource](docs/ReachV1ContactsSegmentsSegmentResource.md)
 - [ReachV1ContactsSegmentsSegmentationContactResource](docs/ReachV1ContactsSegmentsSegmentationContactResource.md)
 - [ReachV1ContactsSegmentsStoreRequest](docs/ReachV1ContactsSegmentsStoreRequest.md)
 - [ReachV1ContactsSegmentsStoreRequestConditionsInner](docs/ReachV1ContactsSegmentsStoreRequestConditionsInner.md)
 - [ReachV1ContactsSegmentsStoreRequestConditionsInnerValue](docs/ReachV1ContactsSegmentsStoreRequestConditionsInnerValue.md)
 - [ReachV1ContactsStoreRequest](docs/ReachV1ContactsStoreRequest.md)
 - [ReachV1ProfilesDomainsDnsRecordStatus](docs/ReachV1ProfilesDomainsDnsRecordStatus.md)
 - [ReachV1ProfilesDomainsDnsRecordStatusActualInner](docs/ReachV1ProfilesDomainsDnsRecordStatusActualInner.md)
 - [ReachV1ProfilesDomainsDnsRecordStatusSuggestedInner](docs/ReachV1ProfilesDomainsDnsRecordStatusSuggestedInner.md)
 - [ReachV1ProfilesDomainsDnsStatusResource](docs/ReachV1ProfilesDomainsDnsStatusResource.md)
 - [ReachV1ProfilesProfileResource](docs/ReachV1ProfilesProfileResource.md)
 - [ReachV1ProfilesProfileResourceLimits](docs/ReachV1ProfilesProfileResourceLimits.md)
 - [ReachV1ProfilesProfileResourceProfilesInner](docs/ReachV1ProfilesProfileResourceProfilesInner.md)
 - [VPSGetActionsV1200Response](docs/VPSGetActionsV1200Response.md)
 - [VPSGetBackupsV1200Response](docs/VPSGetBackupsV1200Response.md)
 - [VPSGetFirewallListV1200Response](docs/VPSGetFirewallListV1200Response.md)
 - [VPSGetPostInstallScriptsV1200Response](docs/VPSGetPostInstallScriptsV1200Response.md)
 - [VPSGetPublicKeysV1200Response](docs/VPSGetPublicKeysV1200Response.md)
 - [VPSV1ActionActionResource](docs/VPSV1ActionActionResource.md)
 - [VPSV1BackupBackupResource](docs/VPSV1BackupBackupResource.md)
 - [VPSV1DataCenterDataCenterResource](docs/VPSV1DataCenterDataCenterResource.md)
 - [VPSV1DockerManagerContainerPortResource](docs/VPSV1DockerManagerContainerPortResource.md)
 - [VPSV1DockerManagerContainerResource](docs/VPSV1DockerManagerContainerResource.md)
 - [VPSV1DockerManagerContainerStatsResource](docs/VPSV1DockerManagerContainerStatsResource.md)
 - [VPSV1DockerManagerContentResource](docs/VPSV1DockerManagerContentResource.md)
 - [VPSV1DockerManagerLogEntryResource](docs/VPSV1DockerManagerLogEntryResource.md)
 - [VPSV1DockerManagerLogsResource](docs/VPSV1DockerManagerLogsResource.md)
 - [VPSV1DockerManagerProjectResource](docs/VPSV1DockerManagerProjectResource.md)
 - [VPSV1FirewallFirewallResource](docs/VPSV1FirewallFirewallResource.md)
 - [VPSV1FirewallFirewallRuleResource](docs/VPSV1FirewallFirewallRuleResource.md)
 - [VPSV1FirewallRulesStoreRequest](docs/VPSV1FirewallRulesStoreRequest.md)
 - [VPSV1FirewallStoreRequest](docs/VPSV1FirewallStoreRequest.md)
 - [VPSV1IPAddressIPAddressResource](docs/VPSV1IPAddressIPAddressResource.md)
 - [VPSV1MalwareMetricsResource](docs/VPSV1MalwareMetricsResource.md)
 - [VPSV1MetricsMetricsCollection](docs/VPSV1MetricsMetricsCollection.md)
 - [VPSV1MetricsMetricsResource](docs/VPSV1MetricsMetricsResource.md)
 - [VPSV1PostInstallScriptPostInstallScriptResource](docs/VPSV1PostInstallScriptPostInstallScriptResource.md)
 - [VPSV1PostInstallScriptStoreRequest](docs/VPSV1PostInstallScriptStoreRequest.md)
 - [VPSV1PublicKeyAttachRequest](docs/VPSV1PublicKeyAttachRequest.md)
 - [VPSV1PublicKeyPublicKeyResource](docs/VPSV1PublicKeyPublicKeyResource.md)
 - [VPSV1PublicKeyStoreRequest](docs/VPSV1PublicKeyStoreRequest.md)
 - [VPSV1SnapshotSnapshotResource](docs/VPSV1SnapshotSnapshotResource.md)
 - [VPSV1TemplateTemplateResource](docs/VPSV1TemplateTemplateResource.md)
 - [VPSV1VirtualMachineDockerManagerUpRequest](docs/VPSV1VirtualMachineDockerManagerUpRequest.md)
 - [VPSV1VirtualMachineHostnameUpdateRequest](docs/VPSV1VirtualMachineHostnameUpdateRequest.md)
 - [VPSV1VirtualMachineMetricGetRequest](docs/VPSV1VirtualMachineMetricGetRequest.md)
 - [VPSV1VirtualMachineNameserversUpdateRequest](docs/VPSV1VirtualMachineNameserversUpdateRequest.md)
 - [VPSV1VirtualMachinePTRStoreRequest](docs/VPSV1VirtualMachinePTRStoreRequest.md)
 - [VPSV1VirtualMachinePanelPasswordUpdateRequest](docs/VPSV1VirtualMachinePanelPasswordUpdateRequest.md)
 - [VPSV1VirtualMachinePurchaseRequest](docs/VPSV1VirtualMachinePurchaseRequest.md)
 - [VPSV1VirtualMachineRecoveryStartRequest](docs/VPSV1VirtualMachineRecoveryStartRequest.md)
 - [VPSV1VirtualMachineRecreateRequest](docs/VPSV1VirtualMachineRecreateRequest.md)
 - [VPSV1VirtualMachineRootPasswordUpdateRequest](docs/VPSV1VirtualMachineRootPasswordUpdateRequest.md)
 - [VPSV1VirtualMachineSetupRequest](docs/VPSV1VirtualMachineSetupRequest.md)
 - [VPSV1VirtualMachineSetupRequestPublicKey](docs/VPSV1VirtualMachineSetupRequestPublicKey.md)
 - [VPSV1VirtualMachineVirtualMachineResource](docs/VPSV1VirtualMachineVirtualMachineResource.md)
 - [WordPressV1CommonVulnerabilityResource](docs/WordPressV1CommonVulnerabilityResource.md)
 - [WordPressV1InstallationsInstallWordPressRequest](docs/WordPressV1InstallationsInstallWordPressRequest.md)
 - [WordPressV1InstallationsInstallWordPressRequestCredentials](docs/WordPressV1InstallationsInstallWordPressRequestCredentials.md)
 - [WordPressV1InstallationsInstallWordPressRequestDatabase](docs/WordPressV1InstallationsInstallWordPressRequestDatabase.md)
 - [WordPressV1InstallationsWordPressInstallationResource](docs/WordPressV1InstallationsWordPressInstallationResource.md)
 - [WordPressV1PluginsActivatePluginRequest](docs/WordPressV1PluginsActivatePluginRequest.md)
 - [WordPressV1PluginsAvailablePluginResource](docs/WordPressV1PluginsAvailablePluginResource.md)
 - [WordPressV1PluginsDeactivatePluginRequest](docs/WordPressV1PluginsDeactivatePluginRequest.md)
 - [WordPressV1PluginsInstallPluginsRequest](docs/WordPressV1PluginsInstallPluginsRequest.md)
 - [WordPressV1PluginsInstalledPluginResource](docs/WordPressV1PluginsInstalledPluginResource.md)
 - [WordPressV1PluginsPluginResource](docs/WordPressV1PluginsPluginResource.md)
 - [WordPressV1PluginsPluginResourceIcons](docs/WordPressV1PluginsPluginResourceIcons.md)
 - [WordPressV1PluginsSuggestedPluginGroupResource](docs/WordPressV1PluginsSuggestedPluginGroupResource.md)
 - [WordPressV1PluginsSuggestedPluginResource](docs/WordPressV1PluginsSuggestedPluginResource.md)
 - [WordPressV1PluginsUninstallPluginsRequest](docs/WordPressV1PluginsUninstallPluginsRequest.md)
 - [WordPressV1PluginsUpdateHostingerPluginRequest](docs/WordPressV1PluginsUpdateHostingerPluginRequest.md)
 - [WordPressV1PluginsUpdatePluginsRequest](docs/WordPressV1PluginsUpdatePluginsRequest.md)
 - [WordPressV1PluginsWoocommerceInstalledResource](docs/WordPressV1PluginsWoocommerceInstalledResource.md)
 - [WordPressV1ThemesActivateThemeRequest](docs/WordPressV1ThemesActivateThemeRequest.md)
 - [WordPressV1ThemesInstallThemeRequest](docs/WordPressV1ThemesInstallThemeRequest.md)
 - [WordPressV1ThemesInstalledThemeResource](docs/WordPressV1ThemesInstalledThemeResource.md)
 - [WordPressV1ThemesThemeResource](docs/WordPressV1ThemesThemeResource.md)
 - [WordPressV1ThemesUninstallThemesRequest](docs/WordPressV1ThemesUninstallThemesRequest.md)
 - [WordPressV1ThemesUpdateThemesRequest](docs/WordPressV1ThemesUpdateThemesRequest.md)


