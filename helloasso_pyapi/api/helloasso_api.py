from datetime import timedelta
# from humanfriendly import format_timespan
from helloasso_api import ApiV5Client, HaApiV5
from helloasso_pyapi.api.api_secrets import clientId, clientSecret, access_token, refresh_token, organizationSlug
# from api.api_secrets import clientId, clientSecret, access_token, refresh_token, organizationSlug
from requests import get, post
from os import system

api = HaApiV5(
        api_base='api.helloasso.com',
        client_id=clientId,
        client_secret=clientSecret,
        timeout=60
    )

def authenticate():
    headers = {"Content-type": "application/x-www-form-urlencoded"}
    data = {
        "client_id": clientId,
        "client_secret": clientSecret,
        "grant_type": "client_credentials",
        }

    req = post("https://api.helloasso.com/oauth2/token", headers=headers, data=data)
    response = req.json()
    # access_token = response["access_token"]
    # refresh_token = response["refresh_token"]
    # token_type = response["token_type"]
    # expires_in = response["expires_in"]
    response["expires_in"] = timedelta(seconds=response["expires_in"])
    return response


def association_infos(access_token):
    headers = {"authorization": f"Bearer {access_token}"}
    req = get(f"https://api.helloasso.com/v5/organizations/{organizationSlug}", headers=headers)
    response = req.json()
    return response

def dir_forms(access_token):
    headers = {"authorization": f"Bearer {access_token}"}
    formType = "Membership"
    formSlug = "inscription-a-efrei-3d-2022-2023"
    page = 1
    # req = get(f"https://api.helloasso.com/v5organizations/{organizationSlug}/forms/{formType}/{formSlug}/public", headers=headers)
    req = get(f"https://api.helloasso.com/v5/organizations/{organizationSlug}/forms/{formType}/{formSlug}/items?tierTypes=Membership&withDetails=true&pageIndex={page}", headers=headers)
    response = req.json()
    return response



