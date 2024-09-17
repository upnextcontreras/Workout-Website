import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('gym.db')
cursor = conn.cursor()

# Create a table to store food items
cursor.execute('''
    CREATE TABLE IF NOT EXISTS FOOD (
        id INTEGER PRIMARY KEY,
        name TEXT,
        allergies TEXT,
        calories INTEGER,
        carbohydrates FLOAT,
        proteins FLOAT,
        fats FLOAT,
        food_group TEXT
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS USER (
        CWID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME VARCHAR(255),
        WEIGHT INTEGER,
        HEIGHT INTEGER,
        AGE INTEGER,
        ALLERGIES VARCHAR(255)
    )
''')




cursor.execute('''
    CREATE TABLE IF NOT EXISTS EXERCISES (
        CWID INTEGER PRIMARY KEY AUTOINCREMENT,
        BODY_PART VARCHAR(255),
        EXERCISE_NAME VARCHAR(255),
        REPS INTEGER,
        SETS INTEGER
    )
''')



exercise_data = [

    # Legs, back, and sholders should be removed from
    #    website (covered by other catagories)

    # NEW DATA
    ('Deltoids', 'Standing Military Press', 12, 3),
    ('Deltoids', 'Lateral Raises, 15, 3'),
    ('Deltoids', 'Front Raises', 15, 3),
    ('Deltoids', 'Bent-Over Reverse Flyes', 15, 3),
    ('Deltoids', 'Arnold Press', 12, 3),
    ('Deltoids', 'Upright Row', 12, 3),

    ('Biceps', 'Bicep Curls', 12, 3),
    ('Biceps', 'Hammer Curls', 12, 3),
    ('Biceps', 'Concentration Curls', 12, 3),
    ('Biceps', 'Preacher Curls', 12, 3),
    ('Biceps', 'Incline Dumbbell Curls', 12, 3),
    ('Biceps', 'Cable Bicep Curls', 12, 3),

    ('Chest', 'Barbell Bench Press', 12, 3),
    ('Chest', 'Dumbbell Flyes', 12, 3),
    ('Chest', 'Incline Bench Press', 12, 3),
    ('Chest', 'Chest Dips', 12, 3),
    ('Chest', 'Push-Ups', 12, 3),
    ('Chest', 'Cable Crossover', 12, 3),

    ('Forearm', 'Wrist Curls', 15, 3),
    ('Forearm', 'Reverse writ curls', 15, 3),
    ('Forearm', 'Hammer curls', 12, 3),
    ('Forearm', 'Farmers walk', 45, 3),
    ('Forearm', 'Behind-the-back wrist curls', 15, 3),
    ('Forearm', 'Reverse barbell curls', 12, 3),

    ('SideAbs', 'Russian Twists', 12, 3),
    ('SideAbs', 'SidePlanks', 12, 3),
    ('SideAbs', 'Side Plank Hip Dips', 12, 3),
    ('SideAbs', 'Oblique V-ups', 12, 3),
    ('SideAbs', 'Bicycle Crunches', 12, 3),
    ('SideAbs', 'Woodchoppers', 12, 3),

    ('Abdominal', 'Crunches', 12, 3),
    ('Abdominal', 'Leg Raises', 12, 3),
    ('Abdominal', 'Planks', 12, 3),
    ('Abdominal', 'Mountain Climbers', 12, 3),
    ('Abdominal', 'Russian Twists', 12, 3),
    ('Abdominal', 'Bicycle Crunches', 12, 3),

    ('Quads', 'Barbell Squats', 12, 3),
    ('Quads', 'Leg Press', 12, 3),
    ('Quads', 'Walking Lunges', 12, 3),
    ('Quads', 'Leg Extensions', 12, 3),
    ('Quads', 'Split Squats', 12, 3),
    ('Quads', 'Step-Ups', 12, 3),

    ('Calfs', 'Standing Calf Raises', 12, 3),
    ('Calfs', 'Seated Calf Raises', 12, 3),
    ('Calfs', 'Calf Raises on Leg Press Machine', 12, 3),
    ('Calfs', 'Jump Rope', 12, 3),
    ('Calfs', 'Box Jumps', 12, 3),
    ('Calfs', 'Single-Leg Calf Raises', 12, 3),

    ('TibialAnterior', 'Toe Raises', 12, 3),
    ('TibialAnterior', 'Dorsiflexion  with Resistance Band', 12, 3),
    ('TibialAnterior', 'Tibialis Raises on Leg Press Machine', 12, 3),
    ('TibialAnterior', 'Resistance Band Dorsiflexion', 12, 3),
    ('TibialAnterior', 'Tibialis Anterior Stretch', 12, 3),
    ('TibialAnterior', 'Calf and Shin Raises', 12, 3),

    ('Upper back', 'Pull-Ups', 15, 3),
    ('Upper back', 'Bent-Over Rows', 12, 3),
    ('Upper back', 'Lat Pulldowns', 12, 3),
    ('Upper back', 'T-Bar Row', 12, 3),
    ('Upper back', 'Seated Cable Rows', 12, 3),
    ('Upper back', 'Face Pulls', 15, 3),

    ('Middle back', 'One-Arm Dumbbell Rows', 12, 3),
    ('Middle back', 'T-Bar Rows', 12, 3),
    ('Middle back', 'Seated Cable Rows with Wide Grip', 12, 3),
    ('Middle back', 'Barbell Bent-Over Rows (Underhand Grip)', 12, 3),
    ('Middle back', 'Chest-Supported Dumbbell Row', 15, 3),
    ('Middle back', 'Reverse Flyes', 15, 3),

    ('Lower back', 'Deadlifts', 10, 3),
    ('Lower back', 'Hyperextensions (Back Extensions)', 15, 3),
    ('Lower back', 'Good Mornings', 12, 3),
    ('Lower back', 'Supermans', 15, 3),
    ('Lower back', 'Romanian Deadlifts', 12, 3),
    ('Lower back', 'Bird Dogs', 10, 3),

    ('Triceps', 'Tricep Dips', 12, 3),
    ('Triceps', 'Skull Crushers (Lying Triceps Extensions)', 12, 3),
    ('Triceps', 'Tricep Pushdowns', 15, 3),
    ('Triceps', 'Close-Grip Bench Press', 12, 3),
    ('Triceps', 'Overhead Tricep Extension', 15, 3),
    ('Triceps', 'Diamond Push-Ups', 12, 3),

    ('Hamstrings', 'Romanian Deadlifts', 12, 3),
    ('Hamstrings', 'Lying Leg Curls', 15, 3),
    ('Hamstrings', 'Stiff-Legged Deadlifts', 12, 3),
    ('Hamstrings', 'Glute-Ham Raises', 10, 3),
    ('Hamstrings', 'Single-Leg Deadlifts', 12, 3),
    ('Hamstrings', 'Swiss Ball Hamstring Curls', 15, 3),

    ('Glutes', 'Squats', 12, 3),
    ('Glutes', 'Hip Thrusts', 12, 3),
    ('Glutes', 'Lunges', 10, 3),
    ('Glutes', 'Deadlifts', 12, 3),
    ('Glutes', 'Glute Bridges', 20, 3),
    ('Glutes', 'Cable Kickbacks', 15, 3)
]


# Insert sample data into the table
sample_data = [


    # Breakfast
    ('Oatmeal with fruit', '', 187, 33.8, 5.2, 2.4, 'Balanced'),
    ('Toast with eggs and orange juice', 'eggs', 508, 46.23, 10.98, 10.73, 'Balanced'),
    ('Toast with sausage and orange juice', 'meat', 447, 59, 13, 18, 'High-protein'),
    ('English muffin with sausage', 'meat', 322, 27, 12.1, 18, 'High-protein'),
    ('Granola with fruit and yogurt', 'dairy', 125, 23.6, 5, 1.5, 'Balanced'),
    ('Whole-wheat pancakes with syrup', 'eggs', 324, 37.6, 10.6, 14.1, 'Balanced'),
    ('Green Smoothie', '', 120, 30, 3, 0, 'Low-carb'),
    ('Açaí Bowl', '', 70, 4, 1, 5, 'Low-carb'),
    ('Avocado toast', '', 179.4, 15.5, 4.2, 13.6, 'Low-carb'),
    ('Mixed Berries and Banana Smoothie', '', 168, 38, 0.1, 1, 'Balanced'),
    ('Mango Smoothie', '', 120, 22, 4.5, 2.1, 'Balanced'),
    ('Egg and cheese omelet', 'eggs, dairy', 177, 1.1, 9.5, 14.8, 'High-protein'),
    ('Veggie omelet', 'eggs', 620, 19, 37, 44, 'Vegetarian'),
    ('English muffin with veggie-sausage', '', 202, 29, 14.1, 3.5, 'Low-carb'),
    ('Toast with veggie-sausage and orange juice', '', 327, 61, 15, 3.5, 'Low-carb'),
    ('Yogurt with banana', 'dairy', 113, 20.6, 5.1, 1.9, 'Vegan'),
    ('bagel with peanut butter and sliced bananas', 'peanuts', 385, 73.95, 12.79, 9.89, 'Vegan'),
    ('bagel with cream cheese and sliced bananas', 'dairy', 114.4, 18.4, 10.7, 0.3, 'Vegan'),
    ('bagel with cream cheese and yogurt', 'dairy', 528, 68.4, 21.5, 19, 'High-protein'),
    ('Breakfast burrito w/ eggs and sausage', 'eggs, meat', 277, 21.4, 10.5, 16.3, 'Vegetarian'),


    # Lunch & Dinner
    ('Taco Salad', 'meat, cheese', 400, 25, 25, 20, 'High-Protein'),
    ('Baked salmon', 'meat, seafood', 250, 0, 30, 15, 'Low-carb'),
    ('Grilled shrimp with rice and veggies', 'meat, seafood', 350, 40, 25, 10, 'Balanced'),
    ('Cauliflower fried rice', 'eggs', 200, 15, 5, 10, 'Low-carb'),
    ('Vegetarian Enchiladas', 'cheese', 350, 30, 20, 15, 'Balanced'),
    ('Pizza with Tomato, Mozzarella and Basil', 'cheese', 300, 30, 15, 15, 'Balanced'),
    ('Sweet and Tangy Chicken Burgers', 'Poultry', 350, 30, 25, 15, 'High-Protein'),
    ('Kale and Apple Salad', '', 200, 20, 5, 10, 'Vegan'),
    ('Chicken Ranch Salad', 'Poultry, dairy', 300, 15, 25, 20, 'High-Protein'),
    ('Chicken Caesar Salad', 'Poultry, dairy', 350, 20, 25, 25, 'High-Protein'),
    ('Caesar Salad', 'dairy', 250, 15, 10, 20, 'Balanced'),
    ('Asian Chopped Chicken Salad', 'peanuts', 300, 25, 20, 15, 'Low-carb'),
    ('Tuscan kale salad', '', 200, 20, 5, 10, 'Vegan'),
    ('Turkey Tacos', 'meat', 300, 20, 20, 15, 'High-Protein'),
    ('Healthy BBQ Salmon Sheet Pan Dinner', 'meat', 350, 30, 25, 15, 'High-Protein'),
    ('Hummus and Grilled Vegetable Wrap', '', 300, 35, 10, 15, 'Vegan'),
    ('Grilled Chicken and veggie wrap', 'meat', 350, 30, 20, 15, 'Balanced'),
    ('Chicken noodle soup', 'meat, poultry', 250, 20, 15, 10, 'Balanced'),
    ('Asian Chicken Rice Bowl', 'meat, poultry', 400, 40, 25, 15, 'Balanced'),
    ('Tuna Salad Sandwich', 'meat, seafood, dairy', 350, 25, 20, 20, 'High-Protein'),
    ('Ham & cheese sandwhich on wheat bread w/light mayo, lettice & tomato', 'meat, dairy', 350, 30, 20, 15, 'Balanced'),
    ('Chili', 'meat', 300, 25, 20, 15, 'Balanced'),
    ('Veggie Chili', '', 250, 20, 15, 10, 'Vegan'),
    ('Vegetable Soup', '', 200, 20, 10, 5, 'Vegan'),
    ('Green Smoothie', '', 150, 25, 5, 5, 'Vegan'),
    ('Açaí Bowl', '', 300, 40, 10, 10, 'Vegan'),
    ('Energy Bars', '', 250, 30, 15, 10, 'Low-carb'),
    ('Beefly Baked Potatoes', 'meat, dairy', 400, 30, 20, 20, 'Balanced'),
    ('Baked Potatoes', 'dairy', 250, 40, 5, 5, 'Balanced'),
    ('Turkey Burgers', '', 300, 20, 25, 15, 'High-Protein'),
    ('Beyond Burgers', '', 300, 20, 20, 20, 'Vegan'),
    ('Chicken, rice, and veggie bowl', '', 400, 35, 25, 10, 'Balanced'),
    ('Vegan Pasta', '', 350, 40, 15, 15, 'Vegan'),
    ('Chicken pasta with bread', 'meat, poultry', 450, 50, 20, 20, 'Balanced'),
    ('pasta with veggies', '', 300, 40, 10, 10, 'Vegan'),
    ('Homemade mac & cheese', 'dairy', 400, 30, 15, 20, 'Low-carb'),
    ('Orange chicken and veggie stir fry', 'eggs', 350, 30, 20, 15, 'Balanced'),
    ('“ants on a log”', 'peanuts', 150, 15, 5, 5, 'Balanced'),
    ('Stir-fried brown rice with chicken', 'meat, poultry, eggs', 350, 40, 20, 15, 'Balanced'),
    ('Salmon with Kale and Apple Salad', 'seafood, meat', 350, 25, 25, 20, 'Balanced'),
    ('Tai Basil Chicken', 'meat, poultry', 350, 30, 25, 15, 'Balanced'),
    ('Vegetable Noodle Soup', '', 200, 25, 10, 5, 'Vegan'),
    ('Turkey and cheese wrap with mayo, lettuce and tomato in a flour tortilla', 'meat', 400, 30, 20, 20, 'Balanced'),
    ('Turkey & cheese sandwhich on wheat bread w/light mayo, lettice & tomato', 'meat', 350, 30, 20, 15, 'Balanced'),
    ('Beans, rice, and veggie bowl', '', 350, 50, 15, 5, 'Vegan'),
    ('Turkey meatballs', 'meat', 300, 10, 25, 15, 'High-Protein'),
    ('Veggie meatballs', '', 250, 20, 15, 10, 'Vegan'),
    ('Vegetable and tofu stir-fry', 'eggs', 250, 25, 15, 10, 'Balanced'),
    ('Egg salad lettuce wraps', 'eggs', 250, 10, 15, 20, 'Low-carb'),
    ('Grilled turkey panini on wheat', 'meat', 400, 30, 25, 20, 'Balanced'),
    ('Grilled veggie panini on wheat', '', 350, 40, 10, 15, 'Vegan'),
    ('Whole wheat pita pizzas with veggies', '', 300, 35, 15, 10, 'Vegan'),
    ('Thai peanut tofu with rice.', 'peanuts', 400, 45, 20, 15, 'Balanced'),
    ('Lentil and vegetable curry', '', 300, 40, 15, 10, 'Vegan'),
    ('Beef stew', 'meat', 350, 20, 25, 15, 'Balanced'),
    ('Fruit salad (strawberries, blueberries, bananas, etc)', '', 150, 35, 2, 0, 'Vegan'),
    ('Fruit salad w/granola & yogurt (strawberries, blueberries, bananas, etc)', 'dairy', 250, 40, 10, 5, 'Balanced'),
    ('Turkey and greens', 'meat', 300, 15, 25, 15, 'High-Protein'),
    ('Caprese salad with grilled chicken', 'meat, poultry', 350, 10, 30, 20, 'High-Protein'),
    ('Whole wheat pita pizzas with veggies and grilled chicken', 'meat, poultry', 400, 40, 25, 15, 'Balanced'),
    ('Sushi (California Roll)', 'seafood, meat', 300, 45, 15, 5, 'Low-carb'),
    ('Veggie sushi rolls', '', 250, 40, 10, 5, 'Vegan'),
    ('Mediterranean-style tuna salad', 'seafood, meat', 350, 10, 20, 25, 'High-Protein'),
    ('Spaghetti and turkey meatballs', 'meat', 400, 40, 25, 15, 'Balanced'),
    ('Spaghetti and veggie meatballs', '', 350, 45, 15, 10, 'Vegan'),
    ('Shepherd\'s pie', 'meat, poultry', 400, 30, 20, 20, 'Balanced'),
    ('Veggie shepherd\'s pie', '', 350, 35, 15, 15, 'Vegan'),
    ('Vegetable stir-fry with tofu and brown rice', 'eggs', 300, 40, 15, 10, 'Balanced')

]

cursor.executemany('''
    INSERT INTO FOOD ('name', 'allergies', calories, carbohydrates, proteins, fats, 'food_group')
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', sample_data)

#('Shoulders', 'Military Press', 10, 3)

cursor.executemany('''
    INSERT INTO EXERCISES (BODY_PART, EXERCISE_NAME, REPS, SETS)
    VALUES (?, ?, ?, ?)
''', exercise_data)

'''cursor.execute("INSERT INTO EXERCISES (BODY_PA, EXERCISE_NAME, REPS, SETS) VALUES (0101, 'Standing Military Press', 12, 3)")

cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0102, ‘Lateral Raises, 15, 3)")
cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0103, ‘Front Raises’, 15, 3)")
cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0104, ‘Bent-Over Reverse Flyes’, 15, 3)")
cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0105, ‘Arnold Press’, 12, 3)")
cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0106, ‘Upright Row', 12, 3)")'''

# Side abs  
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0501, ‘Russian Twists', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0502, ‘SidePlanks', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0503, 'Side Plank Hip Dips', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0504, ‘Oblique V-ups’, 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0505, ‘Bicycle Crunches', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0506, ‘Woodchoppers', 12, 3)")

# Abdominal
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0701, ‘Crunches', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0702, ‘Leg Raises', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0703, ‘Planks', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0704, ‘Mountain Climbers', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0705, ‘Russian Twists', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0706, ‘Bicycle Crunches', 12, 3)")

# Quads
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0801, ‘Barbell Squats', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0802, ‘Leg Press', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0803, ‘Walking Lunges', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0804, ‘Leg Extensions', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0805, ‘Split Squats', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0806, ‘Step-Ups’, 12, 3)")

# Calves
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0901, 'Standing Calf Raises', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0902, 'Seated Calf Raises', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0903, ‘Calf Raises on Leg Press Machine', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0904, ‘Jump Rope’, 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0905, ‘Box Jumps', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (0906, ‘Single-Leg Calf Raises’, 12, 3)")

# Tibial Anterior
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1001, ‘Toe Raises', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1002, ‘Dorsiflexion  with Resistance Band', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1003, ’Tibialis Raises on Leg Press Machine’, 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1004, ‘Resistance Band Dorsiflexion', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1005, ’Tibialis Anterior Stretch', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1006, ‘Calf and Shin Raises', 12, 3)")


# Upper back
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1101, ‘Pull-Ups’, 15, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1102, ‘Bent-Over Rows’, 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1103, ‘Lat Pulldowns', 12, 3)")
###cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1104, ’T-Bar Row’, 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1105, ‘Seated Cable Rows', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1106, ‘Face Pulls', 15, 3)")

# Middle back
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1201, ‘One-Arm Dumbbell Rows’, 12, 3)")
###cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1202, ’T-Bar Rows’, 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1203, 'Seated Cable Rows with Wide Grip’, 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1204, ‘Barbell Bent-Over Rows (Underhand Grip)’, 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1205, ‘Chest-Supported Dumbbell Row’, 15, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1206, ‘Reverse Flyes', 15, 3)")

# Triceps
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1301, ‘Tricep Dips', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1302, ‘Skull Crushers (Lying Triceps Extensions)’, 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1303, ’Tricep Pushdowns', 15, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1304, ‘Close-Grip Bench Press’, 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1305, ‘Overhead Tricep Extension', 15, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1306, ‘Diamond Push-Ups’, 12, 3)")

# Hamstrings
###cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1401, ‘Romanian Deadlifts', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1402, ‘Lying Leg Curls', 15, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1403, ‘Stiff-Legged Deadlifts’, 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1404, ’Glute-Ham Raises’, 10, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1405, ‘Single-Leg Deadlifts’, 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1406, 'Swiss Ball Hamstring Curls', 15, 3)")

# Lower back
###cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1501, ‘Deadlifts', 10, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1502, ‘Hyperextensions (Back Extensions)’, 15, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1503, ‘Good Mornings', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1504, ‘Supermans', 15, 3)")
###cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1505, ‘Romanian Deadlifts', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1506, ‘Bird Dogs', 10, 3)")

# Glutes
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1601, 'Squats', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1602, ‘Hip Thrusts', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1603, ‘Lunges', 10, 3)")
###cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1604, ‘Deadlifts', 12, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1605, ‘Glute Bridges', 20, 3)")
#cursor.execute("INSERT INTO EXERCISES (EXERCISE_ID, EXERCISE_NAME, REPS, SETS) VALUES (1606, ‘Cable Kickbacks', 15, 3)")


# Commit changes and close the connection
conn.commit()
conn.close()
