# from api.helloasso_api import *
from helloasso_pyapi.api.helloasso_api import *
from humanfriendly import format_timespan
import json

def save_auth_tokens(res):
    with open("save_auth.txt", 'w') as f:
        for x, y in res.items():
            f.write(f"{x}: {y}\n\n")
    # print(res["expires_in"])
    sec = res["expires_in"]
    print(f"{format_timespan(sec)}")

def save_asso_infos(res):
    with open("save_asso_infos.txt", 'w') as f:
        for x, y in res.items():
            # print(f"{x}: {y}")
            f.write(f"{x}: {y}\n")

def get_members(form):
    data_set = form["data"]
    userlist = {}
    x=0
    for element in range(len(data_set)):
        x+=1
        data = data_set[element]
        # print(data["user"], "\n")
        customFields = data["customFields"]
        # print(type(customFields))
        firstname = data["user"]["firstName"]
        lastname = data["user"]["lastName"]
        user_discord = ""
        for i in customFields:
            name, answer = i["name"], i["answer"]
            discord_box = "Pseudo Discord (ex: Louis#1234)"
            if name == discord_box : user_discord = answer
            # print(f"{name}: {answer}\t")
        print(f"firstname: {firstname}\t\tlastname: {lastname}\t\tdiscord: {user_discord}")
        userdict = {"firstname":firstname, "lastname":lastname, "discord":user_discord}
        userlist[f"user{x}"] = userdict
    with open("short_memberlist.json", 'w') as f: json.dump(userlist, f, indent=4)


def run_api():
    auth = authenticate()
    save_auth_tokens(auth)
    access_token = auth["access_token"]
    
    asso_infos = association_infos(access_token)
    save_asso_infos(asso_infos)

    member_form = dir_forms(access_token)
    with open("membership_form_2022-2023.json", 'w') as f: json.dump(member_form, f, indent=4)
    get_members(member_form)


if __name__ == "__main__":
    auth = authenticate()
    save_auth_tokens(auth)
    access_token = auth["access_token"]
    
    asso_infos = association_infos(access_token)
    save_asso_infos(asso_infos)

    member_form = dir_forms(access_token)
    with open("membership_form_2022-2023.json", 'w') as f: json.dump(member_form, f, indent=4)
    get_members(member_form)