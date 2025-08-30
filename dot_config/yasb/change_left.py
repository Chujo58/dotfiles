import subprocess, json

result = subprocess.run(
    "komorebic state > C:/Users/chloe/.config/yasb/temp.json",
    shell=True,
    capture_output=True,
    text=True,
)

with open("C:/Users/chloe/.config/yasb/temp.json", "r") as file:
    data = json.load(file)

current_workspace = data["monitors"]["elements"][0]["workspaces"]["focused"]

subprocess.run(
    f"komorebic.exe focus-workspace {max(current_workspace-1, 0)}", shell=True
)
