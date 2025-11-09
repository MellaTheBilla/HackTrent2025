# FitnessMate
A full-stack gym scheduler app that generates personalized workout schedules based on available equipment and preferred time slots.

Frontend: React + Material-UI (MUI)  
Backend: FastAPI + YOLO for gym equipment detection

Users can upload equipment images, select available days and times, and generate a personalized workout schedule.

---

## Features

- Upload gym equipment images
- Select available days and time slots
- Generate workout schedules with exercises, muscle groups, and equipment used
- Dark-themed responsive UI
- Schedule table with time, equipment, and exercises
- Color-coded by muscle group

---

## Frontend Setup

- Go to the frontend folder
- Install dependencies using npm
- Start the development server
- Open http://localhost:3000 in a browser

Dependencies: react, axios, @mui/material, @mui/icons-material, @mui/x-date-pickers, dayjs

---

## Backend Setup

- Go to the backend folder
- Install dependencies using pip
- Run the FastAPI server
- Backend runs at http://localhost:8000

---

## Backend API

POST /generate_plan

Request data:

- images: List of uploaded equipment images
- days: List of days
- start_times: List of start times
- end_times: List of end times

Response example:

day: Monday  
start_time: 08:00  
end_time: 09:00  
equipment: Dumbbells  
muscle_group: Chest  
exercises: Bench Press, Push-Ups

---

## Notes

- CORS enabled for http://localhost:3000  
- YOLO weights stored in backend/weights/best.pt  
- Schedule table color-coded by muscle group  
- Images are optional; default plan generated if none uploaded
