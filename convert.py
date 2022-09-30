import json

json_data = json.load(open("data.json", "r"))
print(json_data)

temp_env_var_string = ""

for key in json_data.keys():
    temp_env_var_string += "${env:"+key+"} = \""+json_data[key]+"\"\n"

with open("temp_env_var.txt", "w") as file:
    file.write(temp_env_var_string)

permanent_env_var_string = ""

for key in json_data.keys():
    permanent_env_var_string += f"setx {key} $"+"{env:"+key+"}\n"

with open("permanent_env_var.txt", "w") as file:
    file.write(permanent_env_var_string)
