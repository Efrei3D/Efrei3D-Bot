from helloasso_pyapi.api.helloasso_api import *
from humanfriendly import format_timespan
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import openpyxl


def get_members(form):
    user_db = []
    data_set = form["data"]
    for element in range(len(data_set)):
        data = data_set[element]
        # print(data["user"], "\n")
        customFields = data["customFields"]
        # print(type(customFields))
        firstname = data["user"]["firstName"]
        lastname = data["user"]["lastName"]
        user_discord = ""
        for i in customFields:
            name, answer = i["name"], i["answer"]
            discord_box = "Pseudo discord"
            if name == discord_box : user_discord = answer
        # print(f"firstname: {firstname}\t\tlastname: {lastname}\t\tdiscord: {user_discord}")
        user = {
            "firstname": firstname,
            "lastname": lastname,
            "discord": user_discord
        }
        user_db.append(user)
    # for i in user_db: print(i)
    return user_db



def show_members_discord():
    auth = authenticate()
    access_token = auth["access_token"]
    asso_infos = association_infos(access_token)

    member_form = dir_forms(access_token)
    member_list = get_members(member_form)

    # PANDAS
    df = pd.DataFrame(member_list)
    return tabulate(df, headers='keys', tablefmt='pretty', showindex=False)




if __name__ == "__main__":
    auth = authenticate()
    access_token = auth["access_token"]
    asso_infos = association_infos(access_token)

    member_form = dir_forms(access_token)
    member_list = get_members(member_form)

# PANDAS
    df = pd.DataFrame(member_list)
    # print(tabulate(df, headers='keys', tablefmt='psql'))
    # df.to_excel('pandas_to_excel.xlsx', index=False, freeze_panes=(1,3))