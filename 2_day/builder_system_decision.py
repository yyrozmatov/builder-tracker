# Noaniqlik drill

ism = input("Ismingizni kiriting?: ")
ish_soat = int(input("Bugun ishlagan soatingiz?: "))
task = int(input("Nechta vazifa bajardingiz?: "))

if ish_soat >= 6 and task >= 20:
	status = "EXCELLENT"
elif ish_soat >= 4 and task >= 10:
	status = "GOOD"
elif ish_soat >= 2:
	status = "NEED MORE WORK"
else:
	status = "RESET"


print(f"===== BUILDER DECISION ===== \nIsm: {ism.capitalize()} \nSoat: {ish_soat} soat \nTask: {task} ta vazifa \nStatus: {status} \nNext action: Continue tomorrow")


