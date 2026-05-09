gym_data = {
    "Chest": [
        {
            "num":1
        },
        {
            "exercise": "Push-up",
            "musclegroup": "Chest",
            "commonmistakes": "Not keeping the body in a straight line, elbows flaring out too much",
            "explaination": "Begin in a plank position, lower your body until your chest nearly touches the floor, then push back up.",
            "difficulty": "easy",
            "equipment": "None",
            "sets": 3
        },
        {
            
            "exercise": "Bench Press",
            "musclegroup": "Chest",
            "commonmistakes": "Arching the back excessively, not using full range of motion",
            "explanation": "Lie on a bench and push a barbell up and down, ensuring your arms extend fully at the top.",
            "difficulty": "Intermediate",
            "equipment": "Barbell, Bench",
            "sets": 3
        },
        {
            "exercise": "Chest Fly",
            "musclegroup": "Chest",
            "commonmistakes": "Letting the elbows bend too much, overextending the arms",
            "explanation": "Lie on a bench holding dumbbells, extend arms out and bring them together, keeping a slight bend in the elbows.",
            "difficulty": "Intermediate",
            "equipment": "Dumbbells, Bench",
            "sets": 3
        }
    ],
    "Back": [
        {
            "num":2
        },
        {
            "exercise": "Pull-up",
            "musclegroup": "Back",
            "commonmistakes": "Not engaging the lats enough, swinging the body",
            "explanation": "Hang from a bar, pull your chest towards the bar by engaging your back muscles.",
            "difficulty": "Intermediate",
            "equipment": "Pull-up Bar",
            "sets": 3
        },
        {
            "exercise": "Lat Pulldown",
            "musclegroup": "Back",
            "commonmistakes": "Using arms too much, not reaching full extension",
            "explanation": "Pull a bar down in front of your chest while sitting, focusing on engaging your back muscles.",
            "difficulty": "Beginner",
            "equipment": "Lat Pulldown Machine",
            "sets": 3
        },
        {
            "exercise": "Bent Over Row",
            "musclegroup": "Back",
            "commonmistakes": "Not keeping the back straight, jerking the weight",
            "explanation": "Bend at the hips and row a barbell or dumbbells towards your waist while keeping your back flat.",
            "difficulty": "Intermediate",
            "equipment": "Barbell or Dumbbells",
            "sets": 3
        }
    ],
    "Legs": [
        {
            "num":3
        },
        {
            "exercise": "Squats",
            "musclegroup": "Legs",
            "commonmistakes": "Knees going past the toes, arching the back",
            "explanation": "Stand with feet shoulder-width apart, squat down keeping the chest up and knees behind the toes.",
            "difficulty": "Beginner",
            "equipment": "None",
            "sets": 3
        },
        {
            "exercise": "Lunges",
            "musclegroup": "Legs",
            "commonmistakes": "Knee going too far forward, not keeping the torso upright",
            "explanation": "Take a step forward, lower the body until both knees form 90-degree angles, then return to standing.",
            "difficulty": "Intermediate",
            "equipment": "None",
            "sets": 3
        },
        {
            "exercise": "Leg Press",
            "musclegroup": "Legs",
            "commonmistakes": "Locking knees at the top, not using full range of motion",
            "explanation": "Sit on the leg press machine, press the platform away from you, and bend your knees to return the weight.",
            "difficulty": "Intermediate",
            "equipment": "Leg Press Machine",
            "sets": 3
        }
    ],
    "Biceps": [
        {
            "num":4
        },
        {
            "exercise": "Bicep Curl",
            "musclegroup": "Biceps",
            "commonmistakes": "Swinging the body, using too much weight",
            "explanation": "Stand with dumbbells in hand, curl the weight up towards your shoulders, keeping elbows stationary.",
            "difficulty": "Beginner",
            "equipment": "Dumbbells",
            "sets": 3
        },
        {
            "exercise": "Hammer Curl",
            "musclegroup": "Biceps",
            "commonmistakes": "Swinging the body, bending the wrists",
            "explanation": "Hold dumbbells with palms facing each other, curl the weights while keeping the elbows stationary.",
            "difficulty": "Intermediate",
            "equipment": "Dumbbells",
            "sets": 3
        },
        {
            "exercise": "Concentration Curl",
            "musclegroup": "Biceps",
            "commonmistakes": "Using momentum, not isolating the biceps",
            "explanation": "Sit on a bench, lean forward and curl a dumbbell with one arm, keeping the upper arm still.",
            "difficulty": "Intermediate",
            "equipment": "Dumbbells",
            "sets": 3
        }
    ],
    "Triceps": [
        {
            "num":5
        },
        {
            "exercise": "Tricep Dips",
            "musclegroup": "Triceps",
            "commonmistakes": "Flaring the elbows, not going deep enough",
            "explanation": "Place hands on a bench, lower your body by bending the arms, then push back up.",
            "difficulty": "Intermediate",
            "equipment": "Bench",
            "sets": 3
        },
        {
            "exercise": "Tricep Pushdown",
            "musclegroup": "Triceps",
            "commonmistakes": "Using the back or shoulders too much",
            "explanation": "Stand facing a cable machine, push the cable down using only your forearms.",
            "difficulty": "Intermediate",
            "equipment": "Cable Machine",
            "sets": 3
        },
        {
            "exercise": "Overhead Tricep Extension",
            "musclegroup": "Triceps",
            "commonmistakes": "Not using full range of motion, locking the elbows",
            "explanation": "Hold a dumbbell or barbell overhead and lower it behind your head, then extend your arms back up.",
            "difficulty": "Intermediate",
            "equipment": "Dumbbell or Barbell",
            "sets": 3
        }
    ]
}

calories_per_rep = {
    "Push-up": 7,
    "Bench Press": 20,
    "Chest Fly": 15,
    "Pull-up": 12,
    "Lat Pulldown": 10,
    "Bent Over Row": 18,
    "Squats": 8,
    "Lunges": 9,
    "Leg Press": 15,
    "Bicep Curl": 6,
    "Hammer Curl": 7,
    "Concentration Curl": 5,
    "Tricep Dips": 8,
    "Tricep Pushdown": 10,
    "Overhead Tricep Extension": 8
}

def diff_func():  #found user difficulty from here in terms of 1,2 and 3, storing in variable difficulty.
    while True:
        try:
            difficulty= int(input("How would you rate your gym experience? Press 1 for Beginner, 2 for Intermediate, 3 for Pro): "))
            if difficulty<1 or difficulty>3:
                print("Input out of range", end="\n")
            else:
                if difficulty==1:
                    print(f"You choosed beginner difficulty", end="\n")
                elif difficulty==2:
                    print(f"You choosed intermediate difficulty", end="\n") 
                else:
                    print(f"You choosed pro difficulty", end="\n")
                return difficulty
        except ValueError:
            print("Your input is not a number", end="\n")
def numberofmuscle():
    f=1
    while f==1:
        try:
            nmuscle=int(input("How many muscle groups do you want to train today? You can select maximum of two, press 1 for one and press 2 for two: "))
            if nmuscle!=1 and nmuscle!=2:
                print("Input 1 or 2 ONLY", end="\n")
            else:
                print(f"You choosed to train {nmuscle} muscle group(s) today", end="\n")
                f=0
                return nmuscle
        except ValueError:
            print("Your input isnt an integer", end="\n")
    #found number of muscles to train and stored in variable nmuscle.
def muscletraining(nmuscle, gym_data):
    musclist=[]
    for muscles in range(nmuscle): #main loop runs n number of times depending on jitnay muscles user na train krnay
        print("Select which muscle you want to train.", end="\n")
        for i in gym_data:
            print(f"Press {gym_data[i][0]["num"]} to train {i}", end="\n")
        fl=1
        while fl==1:
            try:
                muscle_to_train= int(input("Enter number: "))
                if muscle_to_train>5 or muscle_to_train<1:
                    print("Out of range, input valid number", end="\n")
                else:
                    for i in gym_data.keys():
                        if gym_data[i][0]["num"] == muscle_to_train:
                            print(f"You choose to train {i}", end="\n")
                            musclist.append(i)
                fl=0
            except ValueError:
                print("Input not an integer", end="\n")
    return musclist
#till here we have displayed the available opts of muscle groups to train and asked the user for which muscle group he wants to train and stored it in a list muscle_to train, 1 by 1 each muscle group exercises will get complete

def muscletraininghelp(s, exercisedone, exercise):
    if s==4:
        return exercisedone
    else:
        print(f"Starting off with your {s} set for {exercise}. ", end="\n")
        print("If you have completed this set, press 1, and if you wish to quit this exercise now, press 0 ", end="\n")
        fl=1
        while fl==1:
            try:
                n=int(input("Enter 1 to proceed and 0 to quit: "))
                if n!=0 and n!=1:
                    print("Enter a valid number. ", end="\n")
                else:
                    if n==0:
                        return exercisedone
                    elif n==1:
                        if exercise in exercisedone:
                            exercisedone[exercise]+=1
                        else:
                            exercisedone[exercise]=1
                        return muscletraininghelp(s+1, exercisedone, exercise)
                    fl=0
            except ValueError:
                print("Enter a valid integer. ", end="\n")

def calorie_counter(calories_per_rep, exercisedone, diff):
    count=0
    for i, j in exercisedone.items():
        for l,m in calories_per_rep.items():
            if i==l:
                count+=(m*j)
    if diff==1:
        count=count*7
    elif diff==2:
        count=count*10
    elif diff==3:
        count=count*15
    print(f"Total calories burned today: {count}")
def bmi_calc():
    while True:
        try:
            # Input for height
            height = float(input("Enter your height in cm (must be a positive number): "))
            if height <= 0 or height > 273:  # Valid height range
                print("Height must be greater than 0 and less than 273. Please try again.")
                continue
           
            # Input for weight
            weight = float(input("Enter your weight in kg (must be a positive number): "))
            if weight <= 0 or weight > 700:  # Valid weight range
                print("Weight must be greater than 0 and less than 700. Please try again.")
                continue

            # Convert height from cm to meters
            height = height / 100

            # Calculate BMI
            bmi = weight / (height ** 2)
            return bmi

        except ValueError:
            print("Invalid input! Please enter numbers only.")

def dietplan(bmival):
    if bmival is None:
        print("BMI calculation failed. Cannot provide a diet plan.")
        return
    print(f"Your BMI is: {bmival:.2f}")
    print("\nBased on your BMI, here is a suggested diet plan:")
   
    if bmival < 18.5:
        print("Category: Underweight")
        print("Target Calorie Intake: 2,500 - 3,000 calories/day")
        print("Diet Plan:")
        print("- Increase calorie intake with healthy fats and proteins.")
        print("- Suggested foods: Proteins, healthy fats, and complex carbs.")
        print("- Eat 5-6 smaller meals throughout the day.")

        print("Goal: Increase calorie intake with balanced, nutrient-dense meals.\n")
        print("According to your bmi, here's a suggested diet plan especially customized for you: ")


        print("Breakfast:")
        print("- 2 Parathas (600 kcal)")
        print("- 1 Egg Omelette (150 kcal)")
        print("- 1 Glass of Full-Fat Milk with 1 tsp Honey (200 kcal)")
        print("Total Calories: ~950 kcal")
        print("Cost: ~150 PKR\n")

        print("Mid-Morning Snack:")
        print("- 1 Banana (100 kcal)")
        print("- 1 Small Handful of Almonds (100 kcal)")
        print("Total Calories: ~200 kcal")
        print("Cost: ~80 PKR\n")

        print("Lunch:")
        print("- 1 Cup Chicken Biryani (400 kcal)")
        print("- 1 Small Salad with Olive Oil Dressing (50 kcal)")
        print("- 1 Roti (150 kcal)")
        print("Total Calories: ~600 kcal")
        print("Cost: ~200 PKR\n")

        print("Evening Snack:")
        print("- 1 Glass Mango Shake (300 kcal)")
        print("Cost: ~100 PKR\n")

        print("Dinner:")
        print("- 1 Cup Daal Chawal (350 kcal)")
        print("- 1 Small Kebab (150 kcal)")
        print("Total Calories: ~500 kcal")
        print("Cost: ~200 PKR\n")

        print("Bedtime Snack:")
        print("- 1 Glass Warm Milk with 1 tsp Sugar (200 kcal)")
        print("Cost: ~50 PKR\n")

        print("Daily Total Calories: ~2800 kcal")
        print("Total Cost: ~780 PKR\n")
       
    elif 18.5 <= bmival < 24.9:
        print("Category: Normal weight")
        print("Target Calorie Intake: 2,000 - 2,500 calories/day")
        print("Diet Plan:")
        print("- Maintain a balanced diet with a variety of food groups.")
        print("- Avoid excess processed foods and sugary drinks.")
        print("- Stay physically active to maintain your weight.")

        print("Goal: Maintain a balanced diet and healthy weight.\n")
        print("According to your bmi, here's a suggested diet plan especially customized for you: ")


        print("Breakfast:")
        print("- 1 Roti with Desi Ghee (150 kcal)")
        print("- 1 Boiled Egg (70 kcal)")
        print("- 1 Glass Lassi (200 kcal)")
        print("Total Calories: ~420 kcal")
        print("Cost: ~100 PKR\n")

        print("Mid-Morning Snack:")
        print("- 1 Apple (80 kcal)")
        print("- 1 Small Handful of Peanuts (150 kcal)")
        print("Total Calories: ~230 kcal")
        print("Cost: ~70 PKR\n")

        print("Lunch:")
        print("- 1 Cup Chicken Curry (300 kcal)")
        print("- 1 Roti (150 kcal)")
        print("- 1 Small Salad (30 kcal)")
        print("Total Calories: ~480 kcal")
        print("Cost: ~180 PKR\n")

        print("Evening Snack:")
        print("- 1 Cup Chana Chaat (200 kcal)")
        print("Cost: ~100 PKR\n")

        print("Dinner:")
        print("- 1 Cup Palak Paneer with Roti (300 kcal)")
        print("- 1 Small Kebab (150 kcal)")
        print("Total Calories: ~450 kcal")
        print("Cost: ~250 PKR\n")

        print("Daily Total Calories: ~2100 kcal")
        print("Total Cost: ~700 PKR\n")
   
    elif 25 <= bmival < 29.9:
        print("Category: Overweight")
        print("Target Calorie Intake: 1,500 - 2,000 calories/day")
        print("Diet Plan:")
        print("- Focus on a calorie-controlled diet with plenty of vegetables and fruits.")
        print("- Limit sugar, refined carbs, and unhealthy fats.")
        print("- Incorporate 30 minutes of moderate exercise daily.")

        print("Goal: Focus on a calorie-controlled diet with plenty of vegetables and fruits.\n")
        print("According to your bmi, here's a suggested diet plan especially customized for you: ")


        print("Breakfast:")
        print("- 2 Whole-Grain Toast with 1 tsp Butter (200 kcal)")
        print("- 1 Boiled Egg (70 kcal)")
        print("- 1 Glass of Low-Fat Milk (120 kcal)")
        print("Total Calories: ~390 kcal")
        print("Cost: ~100 PKR\n")

        print("Mid-Morning Snack:")
        print("- 1 Orange (60 kcal)")
        print("- 1 Small Handful of Walnuts (150 kcal)")
        print("Total Calories: ~210 kcal")
        print("Cost: ~80 PKR\n")

        print("Lunch:")
        print("- 1 Cup Chicken Salad with Vegetables (300 kcal)")
        print("- 1 Roti (150 kcal)")
        print("Total Calories: ~450 kcal")
        print("Cost: ~180 PKR\n")

        print("Evening Snack:")
        print("- 1 Cup Greek Yogurt (150 kcal)")
        print("- 1 Small Apple (80 kcal)")
        print("Total Calories: ~230 kcal")
        print("Cost: ~100 PKR\n")

        print("Dinner:")
        print("- 1 Cup Grilled Chicken with Steamed Vegetables (350 kcal)")
        print("- 1 Small Bowl Brown Rice (150 kcal)")
        print("Total Calories: ~500 kcal")
        print("Cost: ~200 PKR\n")

        print("Bedtime Snack:")
        print("- 1 Cup Herbal Tea (No Calories)")
        print("Cost: ~20 PKR\n")

        print("Daily Total Calories: ~2080 kcal")
        print("Total Cost: ~680 PKR\n")
   
    else:  
        print("Category: Obesity")
        print("Target Calorie Intake: 1,200 - 1,500 calories/day")
        print("Diet Plan:")
        print("- Reduce calorie intake significantly while ensuring nutritional balance.")
        print("- Avoid sugary drinks, fried foods, and processed snacks.")
        print("- Engage in low-impact exercises like walking or swimming.")
        print("- Consider consulting a healthcare provider for personalized advice.")

        print("Goal: Reduce calorie intake significantly while ensuring nutritional balance.\n")
        print("According to your bmi, here's a suggested diet plan especially customized for you: ")

        print("Breakfast:")
        print("- 1 Slice Whole-Grain Bread with 1 tsp Peanut Butter (200 kcal)")
        print("- 1 Boiled Egg (70 kcal)")
        print("- 1 Cup Green Tea (No Calories)")
        print("Total Calories: ~270 kcal")
        print("Cost: ~70 PKR\n")

        print("Mid-Morning Snack:")
        print("- 1 Small Apple (60 kcal)")
        print("Cost: ~30 PKR\n")

        print("Lunch:")
        print("- 1 Small Grilled Chicken Salad with Olive Oil and Lemon Dressing (200 kcal)")
        print("- 1 Small Piece of Whole-Grain Roti (150 kcal)")
        print("Total Calories: ~350 kcal")
        print("Cost: ~150 PKR\n")

        print("Evening Snack:")
        print("- 1 Small Bowl of Cucumber and Carrot Sticks (50 kcal)")
        print("Cost: ~20 PKR\n")

        print("Dinner:")
        print("- 1 Cup Steamed Vegetables (100 kcal)")
        print("- 1 Grilled Fish Fillet (200 kcal)")
        print("Total Calories: ~300 kcal")
        print("Cost: ~200 PKR\n")

        print("Bedtime Snack:")
        print("- 1 Cup Herbal Tea (No Calories)")
        print("Cost: ~20 PKR\n")

        print("Daily Total Calories: ~1240 kcal")
        print("Total Cost: ~490 PKR\n")



def main(gym_data):
    diff=diff_func()
    numofmusc=numberofmuscle()
    mlist=muscletraining(numofmusc, gym_data)
    exercisedone={}
    for i in mlist:
        print(f"We will be starting off with {i}", end="\n")
        for j in range(1, len(gym_data[i])):
            s=1
            exercise=gym_data[i][j]["exercise"]
            for x,z in gym_data[i][j].items():
                print(f"{x} : {z}")
            if diff==1:
                print("reps per set : 7")
            elif diff==2:
                 print("reps per set : 10")
            elif diff==3:
                 print("reps per set : 15")
            muscletraininghelp(s, exercisedone, exercise)
    print(f"Exercises and their sets that you have completed are: ", end="\n")
    for l, m in exercisedone.items():
        print(f"{m} set(s) of {l} ")
    calorie_counter(calories_per_rep, exercisedone, diff)
    bmival = bmi_calc()
    dietplan(bmival)

    
    
main(gym_data)
