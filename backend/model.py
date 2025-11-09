from ultralytics import YOLO

# Load YOLO model (weights stored in weights/best.pt)
model = YOLO("weights/best.pt")

# Mapping of equipment to muscle group and exercises
exercise_mapping = {
    "Chest Press machine": {"muscle": "Chest", "exercises": ["Bench Press", "Push-Ups", "Incline Dumbbell Press"]},
    "Lat Pull Down": {"muscle": "Back", "exercises": ["Lat Pulldown", "Pull-Ups", "Seated Rows"]},
    "Seated Cable Rows": {"muscle": "Back", "exercises": ["Seated Cable Rows", "Bent-over Rows"]},
    "arm curl machine": {"muscle": "Biceps", "exercises": ["Bicep Curls", "Hammer Curls"]},
    "chest fly machine": {"muscle": "Chest", "exercises": ["Chest Fly"]},
    "chinning dipping": {"muscle": "Back", "exercises": ["Pull-Ups", "Chin-Ups"]},
    "lateral raises machine": {"muscle": "Shoulders", "exercises": ["Lateral Raises"]},
    "leg extension": {"muscle": "Quadriceps", "exercises": ["Leg Extensions"]},
    "leg press": {"muscle": "Legs", "exercises": ["Leg Press"]},
    "reg curl machine": {"muscle": "Biceps", "exercises": ["Bicep Curl"]},
    "seated dip machine": {"muscle": "Triceps", "exercises": ["Tricep Dips"]},
    "shoulder press machine": {"muscle": "Shoulders", "exercises": ["Shoulder Press"]},
    "smith machine": {"muscle": "Full Body", "exercises": ["Smith Machine Squats", "Bench Press"]}
}

# Optional: color code by muscle group
muscle_colors = {
    "Chest": "#FFB3B3",
    "Back": "#A7C7E7",
    "Biceps": "#FFD580",
    "Triceps": "#FF9999",
    "Shoulders": "#B3FFB3",
    "Legs": "#FFDB99",
    "Quadriceps": "#FFD1DC",
    "Full Body": "#D1B3FF",
    "General": "#EFEFEF"
}
