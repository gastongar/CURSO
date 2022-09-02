capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinados = list(zip(capitales,paises))
print(type(combinados))
for cap,pai in combinados:
    print(f"La capital de {pai} es {cap}")
