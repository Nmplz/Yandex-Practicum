world_champions = {
    2002: "Бразилия",
    2006: "Италия",
    2010: "Испания",
    2014: "Германия",
    2018: "Франция",
}

world_champions[2022] = "Аргентина"

for year, country in world_champions.items():
    print(f"{year} - {country}")

country = "Италия"
for year, country_winner in world_champions.items():
    if country_winner == country:
        print("Италия cтановилась чемпионом мира по футболу в 21 веке!")
        break
    else:
        continue
else:
    print("Италия не выигрывала чемпионат мира по футболу в 21 веке.")
