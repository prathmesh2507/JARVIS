import os

start_menu_paths = [
    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
    os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs")
]

apps = []

for path in start_menu_paths:
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".lnk"):
                apps.append(file.replace(".lnk", ""))

print("Installed Apps:")
for app in sorted(set(apps)):
    print(app)