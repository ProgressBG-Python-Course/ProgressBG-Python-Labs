academic_hour_minutes = 40
break_minutes = 20
session_length = 4 # 4 академични часа за сесия
astronomical_hour_minutes = 60
academic_hours_total = 64 # Общо академични часове на курса

# Продължителност на една сесия в минути
sessions = session_length*academic_hour_minutes + break_minutes

# Продължителност на една сесия в астрономически часове
sessions_astronomical = sessions / astronomical_hour_minutes

# Брой сесии
sessions_total = academic_hours_total / session_length

# Брой астрономически часове
astronomical_hours_total = sessions_total * sessions_astronomical
print(f"Total duration in astronomical hours: {astronomical_hours_total:.2f}")