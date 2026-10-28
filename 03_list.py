# Task 3: List – Justice League

justice_league = [
    "Superman", "Batman", "Wonder Woman",
    "Flash", "Aquaman", "Green Lantern"
]

# 1. Number of members
print("1. Number of members:", len(justice_league))

# 2. Add Batgirl and Nightwing
justice_league.extend(["Batgirl", "Nightwing"])
print("2. After adding Batgirl and Nightwing:")
print(justice_league)

# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("3. Wonder Woman as leader:")
print(justice_league)

# 4. Put Green Lantern between Aquaman and Flash
justice_league.remove("Green Lantern")
aquaman_index = justice_league.index("Aquaman")
justice_league.insert(aquaman_index + 1, "Green Lantern")
print("4. Green Lantern placed between Aquaman and Flash:")
print(justice_league)

# 5. Replace with new team
justice_league = [
    "Cyborg", "Shazam", "Hawkgirl",
    "Martian Manhunter", "Green Arrow"
]
print("5. New Justice League:")
print(justice_league)

# 6. Sort alphabetically
justice_league.sort()
print("6. Alphabetically sorted:")
print(justice_league)
print("New leader:", justice_league[0])
