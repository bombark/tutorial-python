import yaml


f=open("schedules.yaml", "r")
raw = f.read()
f.close()

data = yaml.load(raw)

schedules = data["schedules"]

print(schedules[0])
