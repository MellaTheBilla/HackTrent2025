from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import shutil
from model import model, exercise_mapping, muscle_colors

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/generate_plan")
async def generate_plan(
    images: List[UploadFile],
    days: List[str] = Form(...),
    start_times: List[str] = Form(...),
    end_times: List[str] = Form(...)
):
    detected_equipment = set()

    for img in images:
        temp_path = f"temp_{img.filename}"
        with open(temp_path, "wb") as f:
            shutil.copyfileobj(img.file, f)
        results = model(temp_path)
        for box in results[0].boxes:
            cls = int(box.cls)
            detected_equipment.add(model.names[cls])

    eq_list = list(detected_equipment)
    plan = []

    for i, day in enumerate(days):
        eq = eq_list[i % len(eq_list)] if eq_list else "General"
        data = exercise_mapping.get(eq, {"muscle": "General", "exercises": ["General Strength Training"]})
        plan.append({
            "day": day,
            "equipment": eq,
            "muscle_group": data["muscle"],
            "exercises": data["exercises"],
            "color": muscle_colors.get(data["muscle"], "#EFEFEF"),
            "start_time": start_times[i] if i < len(start_times) else "N/A",
            "end_time": end_times[i] if i < len(end_times) else "N/A"
        })

    return {"plan": plan}
