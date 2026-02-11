import time
Sunday = 0
Monday = 0
Tuesday = 0
Wednesday = 0
Thursday = 0
Friday = 0
Saturday = 0

sunday = 0
monday = 0
tuesday = 0
wednesday = 0
thursday = 0
friday = 0
saturday = 0

happy = 0
total = 0
print("=====MOOD TRACKER====")
print("by Gminecrafter487")
while True:
    option = int(input("Choose:\n1. Log mood\n2. Check stats\nChoose one: "))
    if option == 1 or option == 2:
        break
if option == 1:
    import datetime
    current = datetime.datetime.now()
    date = current.strftime("%A/%d/%m/%y")
    try: open("moods.txt", "x")
    except FileExistsError: pass
    try: mood_today = int(input("""how are you feeling?
1. Happy
2. Sad
3. Angry
4. Upset
5. Neutral
6. Bored
7. Other
Choose a number: """))
    except:
        while True:
            for i in range(6):
                if mood_today != i+1:
                    continue
                else: break
            while True:
                try: mood_today = int(input("Choose a number from above: "))
                except: number = False
                if number == True:
                    break
            break
    if mood_today == 7:
        final_mood = input("What are you feeling? ").lower()
    elif mood_today == 6:
        final_mood = "bored"
    elif mood_today == 5:
        final_mood = "neutral"
    elif mood_today == 4:
        final_mood = "upset"
    elif mood_today == 3:
        final_mood = "angry"
    elif mood_today == 2:
        final_mood = "sad"
    elif mood_today == 1:
        final_mood = "happy"
    final = f"{date}: {final_mood.capitalize()}\n"
    with open("moods.txt", "a") as f:
        f.write(final)
    print("=====MOOD SAVED=====")
    print("")
    input("Press enter to exit")
elif option == 2:

    with open("moods.txt", "r") as f:
        past_moods = f.read()
        if past_moods.strip() == "":
            print("You have not logged any past moods")
            print("")
            input("Press enter to exit")
            exit()
        past_moods = past_moods.splitlines()

    for line in past_moods:
        if ": " in line:
            date, mood = line.split(": ")
            weekday, day, month, year = date.split("/")
            date = date.lower()
            mood = mood.lower()
            weekday = weekday.lower()

            if weekday == "sunday" and mood == "happy": Sunday += 1
            elif weekday == "monday" and mood == "happy": Monday += 1
            elif weekday == "tuesday" and mood == "happy": Tuesday += 1
            elif weekday == "wednesday" and mood == "happy": Wednesday += 1
            elif weekday == "thursday" and mood == "happy": Thursday += 1
            elif weekday == "friday" and mood == "happy": Friday += 1
            elif weekday == "saturday" and mood == "happy": Saturday += 1

            elif weekday == "sunday": sunday += 1
            elif weekday == "monday": monday += 1
            elif weekday == "tuesday": tuesday += 1
            elif weekday == "wednesday": wednesday += 1
            elif weekday == "thursday": thursday += 1
            elif weekday == "friday": friday += 1
            elif weekday == "saturday": saturday += 1
            
            if mood == "happy":
                happy += 1
            total += 1
    print(f"On Sundays you were happy on {Sunday} out of {sunday}.")
    print(f"On Mondays you were happy on {Monday} out of {monday}.")
    print(f"On Tuesdays you were happy on {Tuesday} out of {tuesday}.")
    print(f"On Wednesdays you were happy on {Wednesday} out of {wednesday}.")
    print(f"On Thursday you were happy on {Thursday} out of {thursday}.")
    print(f"On Fridays you were happy on {Friday} out of {friday}.")
    print(f"On Saturdays you were happy on {Saturday} out of {saturday}.")
    print(f"You were happy on {happy} out of {total}.")
    print("")
    input("Press enter to exit")
exit()
            
        

    


    
