def time_to_text(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    print(f"{hours} heures et {remaining_minutes} minutes")

time_to_text(90)