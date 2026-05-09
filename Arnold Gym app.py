import tkinter as tk
from tkinter import Toplevel, ttk
from PIL import Image, ImageTk
import requests
import pygame
import random
import imageio

# ElevenLabs API Details
API_KEY = "sk_296621bddf94606ddc982ed06ad83fe30386b48737657d1f"  # Replace with your ElevenLabs API key
VOICE_ID = "QiMmWHTbk1X4hvZaXhay"  # Replace with your ElevenLabs voice ID

# Exercise Data with GIFs and Instructions
gym_data = {
    "underweight": [
        {"exercise": "Push-up", "calories_per_rep": 7, "sets": 3, "gif": "pushup.gif", "instruction": "7 reps! Keep your body straight as you lower yourself."},
        {"exercise": "Deadlift", "calories_per_rep": 25, "sets": 3, "gif": "deadlift.gif", "instruction": "25 reps! Keep your back straight as you lift the weight."},
        {"exercise": "Plank", "calories_per_rep": 5, "sets": 3, "gif": "plank.gif", "instruction": "5 reps! Hold your core tight and keep your body aligned."},
        {"exercise": "Dumbbell Rows", "calories_per_rep": 15, "sets": 3, "gif": "rows.gif", "instruction": "5 reps! Pull the dumbbell towards your waist in a controlled motion."},
        {"exercise": "Squats", "calories_per_rep": 20, "sets": 3, "gif": "squats.gif", "instruction": "20 reps! Keep your back straight as you lower into a squat position."},
    ],
    "normal": [
        {"exercise": "Bench Press", "calories_per_rep": 20, "sets": 3, "gif": "benchpress.gif", "instruction": "20 reps! Push the barbell upwards in a controlled motion."},
        {"exercise": "Chest Fly", "calories_per_rep": 15, "sets": 3, "gif": "chestfly.gif", "instruction": "15 reps! Keep a slight bend in your elbows as you bring the weights together."},
        {"exercise": "Pull-ups", "calories_per_rep": 8, "sets": 3, "gif": "pullups.gif", "instruction": "8 reps! Pull your chin above the bar while keeping your body straight."},
        {"exercise": "Barbell Rows", "calories_per_rep": 25, "sets": 3, "gif": "rows2.gif", "instruction": "25 reps! Pull the barbell towards your waist with a straight back."},
        {"exercise": "Lunges", "calories_per_rep": 10, "sets": 3, "gif": "lunges.gif", "instruction": "10 reps! Step forward and lower your hips until both knees are bent at 90 degrees."},
    ],
    "overweight": [
        {"exercise": "Jumping Jacks", "calories_per_rep": 5, "sets": 3, "gif": "jumpingjacks.gif", "instruction": "5 reps! Jump with your hands and feet moving outward simultaneously."},
        {"exercise": "Burpees", "calories_per_rep": 8, "sets": 3, "gif": "burpees.gif", "instruction": "8 reps! Start in a standing position, then jump back into a plank and return."},
        {"exercise": "Mountain Climbers", "calories_per_rep": 6, "sets": 3, "gif": "mountainclimbers.gif", "instruction": "6 reps! Keep your core tight as you alternate legs in a running motion."},
        {"exercise": "High Knees", "calories_per_rep": 7, "sets": 3, "gif": "highknees.gif", "instruction": "7 reps! Run in place, bringing your knees up to your chest."},
        {"exercise": "Squats", "calories_per_rep": 20, "sets": 3, "gif": "squats.gif", "instruction": "20 reps! Keep your back straight as you lower into a squat position."},
    ],
}
# Diet Plan Data
diet_dishes_data = {
    "underweight": {
        "breakfast": ["Avocado Toast", "Greek Yogurt", "Fruit Smoothie"],
        "lunch": ["Grilled Chicken Salad", "Quinoa Bowl", "Vegetable Soup"],
        "dinner": ["Salmon and Brown Rice", "Pasta with Pesto", "Stir-Fried Vegetables"]
    },
    "normal": {
        "breakfast": ["Oatmeal with Berries", "Eggs and Toast", "Banana Pancakes"],
        "lunch": ["Turkey Sandwich", "Chicken Wrap", "Mixed Veggie Bowl"],
        "dinner": ["Grilled Fish and Sweet Potatoes", "Beef Stir-Fry", "Spaghetti Bolognese"]
    },
    "overweight": {
        "breakfast": ["Green Smoothie", "Boiled Eggs", "Whole Wheat Toast"],
        "lunch": ["Chicken Caesar Salad", "Grilled Tofu", "Lentil Soup"],
        "dinner": ["Baked Cod with Asparagus", "Turkey Meatballs", "Zucchini Noodles"]
    }
}


motivational_quotes = [
    "Don't quit now! You're stronger than you think.",
    "Remember why you started!",
    "Pain is temporary, but glory is forever!",
    "Keep going! You've got this!",
]

difficulty = ""
bmi_category = ""
workout_plan = {}
daily_calories = 0
total_calories = 0
current_day = 1




# Function to play Arnold's voice
def play_arnold_voice(text):
    try:
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
        headers = {"xi-api-key": API_KEY, "Content-Type": "application/json"}
        data = {"text": text, "voice_settings": {"stability": 0.75, "similarity_boost": 0.75}}
        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            if pygame.mixer.get_init():
                pygame.mixer.music.stop()
                pygame.mixer.quit()

            with open("voice_feedback.mp3", "wb") as audio_file:
                audio_file.write(response.content)

            pygame.mixer.init()
            pygame.mixer.music.load("voice_feedback.mp3")
            pygame.mixer.music.play()
        else:
            print("Error generating audio:", response.status_code, response.json())
    except Exception as e:
        print("Error:", e)


# Function to update Arnold's picture dynamically
def update_picture(image_file):
    try:
        arnold_image = Image.open(image_file)
        arnold_image = arnold_image.resize((200, 200), Image.Resampling.LANCZOS)
        arnold_photo = ImageTk.PhotoImage(arnold_image)
        picture_label.config(image=arnold_photo)
        picture_label.image = arnold_photo
    except FileNotFoundError:
        chatbot_label.config(text=f"Arnold: Sorry, the image '{image_file}' is missing!")


# Function to greet the user
def greet_user():
    update_picture("greeting.png")
    chatbot_label.config(text="Hello! I'm Arnold, Your Fitness Guide. Let's get Started")
    play_arnold_voice("Hello! I'm Arnold, Your Fitness Guide. Let's get started!")


# Function to set difficulty
def set_difficulty():
    global difficulty
    difficulty = difficulty_var.get()
    difficulty_frame.pack_forget()
    display_bmi_input()


# Function to display BMI input
def display_bmi_input():
    update_picture("bmi.png")
    chatbot_label.config(text="Enter your weight and height to calculate your BMI.")
    play_arnold_voice("Great, Now Enter your weight and height to calculate your BMI.")
    bmi_frame.pack()


# Function to calculate BMI
def calculate_bmi():
    global bmi_category

    weight_value = float(weight.get())
    height_value = float(height.get())
    bmi = weight_value / ((height_value / 100) ** 2)

    bmi_frame.pack_forget()

    if bmi < 18.5:
        bmi_category = "underweight"
        update_picture("underweight.png")
    elif 18.5 <= bmi < 24.9:
        bmi_category = "normal"
        update_picture("normal.png")
    else:
        bmi_category = "overweight"
        update_picture("overweight.png")

    chatbot_label.config(text=f"Arnold: You are {bmi_category}. Let's customize your plan!")
    play_arnold_voice(f"You are {bmi_category}. Let's customize your plan!")
    training_days_frame.pack()

def show_diet_plan():
    """Displays a diet plan based on the number of training days and BMI category."""
    diet_window = Toplevel(app)
    diet_window.title("Diet Plan")
    diet_window.geometry("500x600")

    # Add Arnold's picture
    try:
        arnold_image = Image.open("arnold_diet.png")
        arnold_image = arnold_image.resize((200, 200), Image.Resampling.LANCZOS)
        arnold_photo = ImageTk.PhotoImage(arnold_image)
        arnold_label = tk.Label(diet_window, image=arnold_photo)
        arnold_label.image = arnold_photo
        arnold_label.pack(pady=10)
    except FileNotFoundError:
        tk.Label(diet_window, text="Arnold's image missing!", font=("Arial", 12)).pack(pady=10)

    # Introduction text
    tk.Label(
        diet_window,
        text="Here's your personalized diet plan:",
        font=("Arial", 14),
        wraplength=450,
        justify="center"
    ).pack(pady=10)

    # Play Arnold's voice narration
    play_arnold_voice("Here's your personalized diet plan!")

    # Create a scrollable frame
    canvas = tk.Canvas(diet_window)
    scrollbar = ttk.Scrollbar(diet_window, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Generate diet plan based on training days and BMI
    for day in range(1, len(workout_plan) + 1):
        day_label = tk.Label(scrollable_frame, text=f"Day {day} Diet Plan:", font=("Arial", 12, "bold"))
        day_label.pack(pady=10)

        for meal_type, dishes in diet_dishes_data[bmi_category].items():
            meal_label = tk.Label(
                scrollable_frame,
                text=f"{meal_type.capitalize()}: {', '.join(random.sample(dishes, 3))}",
                font=("Arial", 10)
            )
            meal_label.pack(anchor="w", padx=10, pady=2)

    # Add Close button
    close_button = tk.Button(scrollable_frame, text="Close", command=diet_window.destroy)
    close_button.pack(pady=10)



# Function to generate the workout plan
def generate_workout_plan():
    global workout_plan
    global diet_dishes_data

    try:
        days = int(training_days.get())
        workout_plan = {f"Day {i + 1}": random.sample(gym_data[bmi_category], 5) for i in range(days)}
        chatbot_label.config(text=f"Arnold: Your {days}-day workout plan is ready! Check below!")
        play_arnold_voice(f"Your {days}-day workout plan is ready! TIME TO GRIND")

        # Clear the existing content in the workout_plan_frame
        for widget in workout_plan_frame.winfo_children():
            widget.destroy()

        # Create a Canvas and Scrollbar for scrolling
        canvas = tk.Canvas(workout_plan_frame)
        scrollbar = ttk.Scrollbar(workout_plan_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Pack the canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Add the workout plan content to the scrollable frame
        for day, exercises in workout_plan.items():
            day_label = tk.Label(scrollable_frame, text=f"{day}:", font=("Arial", 12), anchor="w")
            day_label.pack(fill="x", padx=10, pady=5)

            for exercise in exercises:
                exercise_label = tk.Label(
                    scrollable_frame,
                    text=f"  - {exercise['exercise']} ({exercise['sets']} sets, {exercise['calories_per_rep']} calories/rep)",
                    font=("Arial", 10),
                    anchor="w"
                )
                exercise_label.pack(fill="x", padx=20)

        # Add the Start Workout button at the end of the scrollable frame
        start_workout_button = tk.Button(scrollable_frame, text="Start Workout", command=start_workout)
        start_workout_button.pack(pady=10)

        workout_plan_frame.pack(fill="both", expand=True)
        # Buttons for diet plan 

        view_diet_button = tk.Button(scrollable_frame, text="View Diet Plan", command=show_diet_plan)
        view_diet_button.pack(pady=10)

        workout_plan_frame.pack(fill="both", expand=True)


    except ValueError:
        chatbot_label.config(text="Arnold: Please enter a valid number of training days!")


# Function to start the workout
def start_workout():
    global current_day, daily_calories, total_calories
    daily_calories = 0
    workout_window = Toplevel(app)
    workout_window.title("Workout Session")
    workout_window.geometry("500x600")

    def show_day_congratulations(day):
        for widget in workout_window.winfo_children():
            widget.destroy()
        try:
            arnold_image = Image.open("day_congrats.png")
            arnold_image = arnold_image.resize((200, 200), Image.Resampling.LANCZOS)
            arnold_photo = ImageTk.PhotoImage(arnold_image)
            image_label = tk.Label(workout_window, image=arnold_photo)
            image_label.image = arnold_photo
            image_label.pack(pady=10)
        except FileNotFoundError:
            tk.Label(workout_window, text="Image missing!", font=("Arial", 12)).pack(pady=10)
        tk.Label(workout_window, text=f"Congratulations! You've completed {day}!", font=("Arial", 14)).pack(pady=10)
        tk.Label(workout_window, text=f"Calories Burned Today: {daily_calories} calories!", font=("Arial", 14)).pack(pady=10)
        play_arnold_voice(f"Congratulations! You've completed {day}! You burned {daily_calories} calories today.")
        tk.Button(workout_window, text="Start Next Day", command=lambda: workout_session(current_day - 1)).pack(pady=20)

    def show_final_congratulations():
        for widget in workout_window.winfo_children():
            widget.destroy()
        try:
            arnold_image = Image.open("final_congrats.png")
            arnold_image = arnold_image.resize((200, 200), Image.Resampling.LANCZOS)
            arnold_photo = ImageTk.PhotoImage(arnold_image)
            image_label = tk.Label(workout_window, image=arnold_photo)
            image_label.image = arnold_photo
            image_label.pack(pady=10)
        except FileNotFoundError:
            tk.Label(workout_window, text="Image missing!", font=("Arial", 12)).pack(pady=10)
        tk.Label(workout_window, text="Great job! You've completed all workout days!", font=("Arial", 14)).pack(pady=10)
        tk.Label(workout_window, text=f"Total Calories Burned: {total_calories} calories! Hasta La Vista!", font=("Arial", 14)).pack(pady=10)
        play_arnold_voice(f"Great job! You've completed all workout days! You burned a total of {total_calories} calories!")
        play_arnold_voice(f"Hasta La Vista!")
        tk.Button(workout_window, text="Close", command=workout_window.destroy).pack(pady=20)

    def workout_session(day_index=current_day - 1, exercise_index=0, set_number=1):
        global current_day 
        global daily_calories
        global total_calories

        for widget in workout_window.winfo_children():
            widget.destroy()
        
        days = list(workout_plan.keys())
        if day_index >= len(days):
            show_final_congratulations()
            return
        day = days[day_index]
        exercises = workout_plan[day]
        if exercise_index >= len(exercises):
            current_day += 1
            total_calories += daily_calories
            show_day_congratulations(day)
            return
        exercise = exercises[exercise_index]
        if set_number > exercise["sets"]:
            workout_session(day_index, exercise_index + 1)
            return
        tk.Label(workout_window, text=f"{day} - {exercise['exercise']} - Set {set_number} of {exercise['sets']}", font=("Arial", 12)).pack(pady=10)
        tk.Label(workout_window, text=f"Instruction: {exercise['instruction']}", font=("Arial", 10)).pack(pady=10)
        
        # Animate GIF
        gif_label = tk.Label(workout_window)
        gif_label.pack(pady=10)

        def animate_gif(label, gif_path):
            try:
                gif = imageio.get_reader(gif_path)
                frames = [ImageTk.PhotoImage(Image.fromarray(frame).resize((200, 200), Image.Resampling.LANCZOS))
                        for frame in gif]
                total_frames = len(frames)

                def update_frame(idx=0):
                    label.config(image=frames[idx])
                    label.image = frames[idx]
                    label.after(100, update_frame, (idx + 1) % total_frames)

                update_frame()
            except Exception as e:
                print(f"Error animating GIF: {e}")
                label.config(text=f"Error loading GIF: {gif_path}")

        try:
            animate_gif(gif_label, exercise["gif"])
        except FileNotFoundError:
            tk.Label(workout_window, text=f"GIF for {exercise['exercise']} is missing!", font=("Arial", 10)).pack(pady=5)

        def continue_workout():
            nonlocal set_number
            global daily_calories
            daily_calories += exercise["calories_per_rep"]
            workout_session(day_index, exercise_index, set_number + 1)

        def quit_workout():
            motivational_quote = random.choice(motivational_quotes)
            tk.Label(workout_window, text=motivational_quote, font=("Arial", 12), wraplength=450).pack(pady=10)
            play_arnold_voice(motivational_quote)

        tk.Button(workout_window, text="Continue", command=continue_workout).pack(pady=5)
        tk.Button(workout_window, text="Quit", command=quit_workout).pack(pady=5)

    workout_session()


# Main Application
app = tk.Tk()
app.title("Arnold's Fitness Guide")
app.geometry("500x700")

# Picture Label for Arnold's image
picture_label = tk.Label(app)
picture_label.pack(pady=10)

# Chatbot Label
chatbot_label = tk.Label(app, text="", font=("Arial", 12), wraplength=450, justify="left")
chatbot_label.pack(pady=10)

# Difficulty Frame
difficulty_frame = tk.Frame(app)
difficulty_frame.pack(pady=10)
tk.Label(difficulty_frame, text="Are you a Beginner, Intermediate, or Advanced?", font=("Arial", 12)).pack(pady=10)
difficulty_var = tk.StringVar(value="Beginner")
difficulty_menu = tk.OptionMenu(difficulty_frame, difficulty_var, "Beginner", "Intermediate", "Advanced")
difficulty_menu.pack(pady=5)
tk.Button(difficulty_frame, text="Submit Difficulty", command=set_difficulty).pack(pady=10)

# BMI Frame
bmi_frame = tk.Frame(app)
tk.Label(bmi_frame, text="Enter your Weight (kg) and Height (cm):", font=("Arial", 12)).pack(pady=10)
weight = tk.StringVar()
height = tk.StringVar()
tk.Entry(bmi_frame, textvariable=weight, font=("Arial", 12)).pack(pady=5)
tk.Entry(bmi_frame, textvariable=height, font=("Arial", 12)).pack(pady=5)
tk.Button(bmi_frame, text="Submit BMI", command=calculate_bmi).pack(pady=10)

# Training Days Frame
training_days_frame = tk.Frame(app)
tk.Label(training_days_frame, text="How many days will you train per week?", font=("Arial", 12)).pack(pady=10)
training_days = tk.StringVar()
tk.Entry(training_days_frame, textvariable=training_days, font=("Arial", 12)).pack(pady=5)
tk.Button(training_days_frame, text="Submit Days", command=generate_workout_plan).pack(pady=10)

# Workout Plan Frame
workout_plan_frame = tk.Frame(app)
plan_label = tk.Label(workout_plan_frame, text="", font=("Arial", 12), wraplength=450, justify="left")
plan_label.pack(pady=10)
tk.Button(workout_plan_frame, text="Start Workout", command=start_workout).pack(pady=10)

# Greet the user on startup
app.after(500, greet_user)

# Run the Application
app.mainloop()