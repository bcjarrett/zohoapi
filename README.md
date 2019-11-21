# README #

**This wrapper is out of date. The new v2 API has an officially supported wrapper that should be used: https://pypi.org/project/zcrmsdk/**

---

This is a simple wrapper for Zoho CRM's API

Example Usage:
    
    >>> from zohoapi.api import ZohoConnection
    >>> zc = ZohoConnection()
    >>> first_two_hundred_contacts = zc.Contacts.get_records()
    >>> zc.Accounts.insert_record({'First Name': 'Richard',
    ...                            'Last Name': 'Johnson'})
