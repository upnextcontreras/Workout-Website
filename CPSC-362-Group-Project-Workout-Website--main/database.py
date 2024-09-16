import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('gym.db')
cursor = conn.cursor()

# Create a table to store food items
cursor.execute('''
    CREATE TABLE IF NOT EXISTS FOOD (
        id INTEGER PRIMARY KEY,
        name TEXT,
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
    ('Legs', 'Squats', 10, 3),
    ('Chest', 'Bench Press', 8, 4),
    ('Back', 'Deadlifts', 12, 3),
    ('Shoulders', 'Military Press', 10, 3)
    # Additional exercises can be added here
]

# Insert sample data into the table
sample_data = [


    # Breakfast
    ('Oatmeal w/ friut', 1001, 187, 34, 2, 5, 4, 'Balanced'),
    ('Toast w/ eggs & OJ', 1002, 508, 46, 11, 11, 2, 'Balanced'),
    ('Toast w/ sausage & OJ', 1003, 447, 59, 18, 13, 2, 'Hight-protein'),
    ('English muffin w/ sausage', 1004, 322, 27, 18, 12, 2, 'High-protein'),
    ('Granola w/ fruit & yogurt', 1005, 125, 24, 2, 5, 2, 'Balanced'),
    ('Whole-wheat pancakes w/ syrup', 1006, 324, 38, 14, 11, 5, 'Balanced'),
    ('Green smoothie', 1007, 120, 30, 0, 3, 5, 'Low-carb'),
    ('Açaí bowl', 1008, 70, 4, 5, 1, 3, 'Low-carb'),
    ('Avocado toast', 1009, 179, 16, 14, 4, 8, 'Low-carb'),
    ('Mixed berries & banana smoothie', 1010, 168, 38, 1, 0, 3, 'Balanced'),
    ('Mango smoothie', 1011, 120, 22, 2, 5, 2, 'Balanced')
    ('Egg & cheese omelet', 1012, 177, 1, 15, 10, 0, 'Hight-protein')
    ('Veggie omelet', 1013, 620, 19, 44, 37, 3, 'Vegetarian')
    ('English muffin w/ veggie4-sausage', 1014, 202, 29, 4, 14, 2, 'Low-carb'),
    ('Toast w/ veggie-sausage & OJ', 1015, 327, 61, 4, 15, 2, 'Low-carb'),
    ('Yogurt w/ banana', 1016, 113, 21, 2, 5, 0, 'Vegan'),
    ('Bagel w/ peanut butter & sliced banana', 1017, 385, 74, 10, 13, 10, 'Vegan'),
    ('Bagel w/ cream cheese & sliced banana', 1018, 114, 18, 0, 11, 2, 'Vegan'),
    ('Begel w/ cream cheese & yogurt', 1019, 528, 68, 19, 22, 2, 'High-protein'),
    ('Breakfast burrito w/ eggs & sausage', 1020, 277, 21, 16, 11, 1, 'Vegetarian'),
    ('Breakfast burrito w/ eggs & veggie-sausage', 1021, 157, 23, 2, 13, 1, 'Vegetarian'),


    # Lunch & Dinner
    ('Taco salad', 1022, 400, 25, 20, 25, 8, 'High-protein'),
    ('Baked salmon', 1023, 250, 0, 15, 30, 0, 'Low-carb'),
    ('Grilled shrimp w/ rice & veggies', 1024, 350, 0, 15, 30, 0, 'Balanced'),
    ('Cauliflower fried rice', 1025, 200, 15, 10, 5, 5, 'Low-carb'),
    ('Vegetarian enchiladas', 1026, 350, 30, 15, 20, 8, 'Balanced'),
    ('Pizza w/ tomato, mozzarella & basil', 1027, 300, 30, 15, 15, 3, 'Balanced'),
    ('Sweet & tangy chicken burger', 1028, 350, 30, 15, 25, 4, 'High-protein'),
    ('Kale & apple salad', 1029, 200, 20, 10, 5, 5, 'Vegan'),
    ('Chicken ranch salad', 1030, 300, 15, 20, 25, 4, 'High-protein'),
    ('Chicken caesar salad', 1031, 350, 20, 25, 25, 3, 'High-protein'),
    ('Caesar salad', 1032, 250, 15, 20, 10, 3, 'Balanced'),
    ('Asian chopped chicken salad', 1033, 300, 25, 15, 20, 6, 'Low-carb'),
    ('Tuscan kale salad', 1034, 200, 20, 10, 5, 7, 'Vegan'),
    ('Turkey tacos', 1035, 300, 20, 15, 20, 5, 'High-protein'),
    ('Healthy BBQ salmon sheet pan dinner', 1036, 350, 30, 15, 25, 4, 'High-protein'),
    ('Hummus & grilled Veggie wrap', 1037, 300, 35, 15, 10, 8, 'Vegan'),
    ('Grilled chicken and veggie wrap', 1038, 350, 30, 15, 20, 6, 'Balanced'),
    ('Chicken noodle soup', 1039, 250, 20, 10, 15, 3, 'Balanced'),
    ('Asian chicken rice bowl', 1040, 400, 40, 15, 25, 5, 'Balanced'),
    ('Tuna salad sandwich', 1041, 350, 25, 20, 20, 4, 'High-protein'),
    ('Ham & cheese sandwich on wheat w/ light mayo, lettuce & tomato', 1042, 350, 30, 15, 20, 4, 'Balanced'),
    ('Chili', 1043, 300, 25, 15, 20, 8, 'Balanced'),
    ('Veggie chili', 1044, 250, 20, 10, 15, 10, 'Vegan'),
    ('Vegetable soup', 1045, 200, 20, 5, 10, 8, 'Vegan'),
    ('Green smoothie', 1046, 150, 25, 5, 5, 5, 'Vegan'),
    ('Açaí bowl', 1047, 300, 40, 10, 10, 8, 'Vegan'),
    ('Energy bar', 1048, 250, 30, 10, 15, 5, 'Low-carb'),
    ('Beefy baked potato', 1049, 400, 30, 20, 20, 6, 'Balanced'),
    ('Baked potato', 1050, 250, 40, 5, 5, 6, 'Balanced'),
    ('Turkey burger', 1051, 300, 20, 15, 25, 4, 'High-protein'),
    ('Beyond burger', 1052, 300, 20, 20, 20, 5, 'Vegan'),
    ('Chicken, rice, & veggie stir-fry', 1053, 400, 35, 10, 25, 6, 'Balanced'),
    ('Vegan pasta', 1054, 350, 40, 15, 15, 6, 'Vegan'),
    ('Chicken pasta w/ bread', 1055, 450, 50, 20, 20, 5, 'Balanced'),
    ('Pasta w/ veggies', 1056, 300, 40, 10, 10, 8, 'Vegan'),
    ('Homemade mac & cheese', 1057, 400, 30, 20, 15, 2, 'Low-carb'),
    ('Orange chicken & veggie stir-fry', 1058, 350, 30, 15, 20, 5, 'Balanced'),
    ('Ants on a log', 1059, 150, 15, 5, 5, 3, 'Balanced'),
    ('Stir-fried brown rice w/ chicken', 1060, 350, 40, 15, 20, 5, 'Balanced'),
    ('Salmon w/ kale & apple salad', 1061, 350, 25, 20, 25, 6, 'Balanced'),
    ('Tai basil chicken', 1062, 350, 30, 15, 25, 4, 'Balanced'),
    ('Vegetable noodle soup', 1063, 200, 25, 5, 10, 6, 'Vegan'),
    ('Turkey & cheese wrap w/ mayo, lettuce & tomato in a flour tortilla', 1064, 400, 30, 20, 20, 4, 'Balanced'),
    ('Turkey & cheese sandwich on wheat w/ light mayo, lettuce & tomato', 1065, 350, 30, 15, 20, 4, 'Balanced'),
    ('Beans, rice, & veggie bowl', 1066, 350, 50, 5, 15, 10, 'Vegan'),
    ('Turkey meatballs', 1067, 300, 10, 15, 25, 2, 'High-protein'),
    ('Veggie meatballs', 1068, 250, 20, 10, 15, 8, 'Vegan'),
    ('Vegetable & tofu stir-fry', 1069, 250, 25, 10, 15, 8, 'Balanced'),
    ('Egg salad lettuce wrap', 1070, 250, 10, 20, 15, 3, 'Low-carb'),
    ('Grilled turkey panini on wheat', 1071, 400, 30, 20, 25, 4, 'Balanced'),
    ('Grilled veggie panini on wheat', 1072, 350, 40, 15, 10, 6, 'Vegan'),
    ('Whole wheat pita pizza w/ veggies', 1073, 300, 35, 10, 15, 5, 'Vegan'),
    ('Thai peanet tofu w/ rice', 1074, 400, 45, 15, 20, 6, 'Balanced'),
    ('Lentil & vegetable curry', 1075, 300, 40, 10, 15, 10, 'Vegan'),
    ('Beef stew', 1076, 350, 20, 15, 25, 5, 'Balanced'),
    ('Fruit salad (strawberries, blueberries, banana, etc)', 1077, 150, 35, 0, 2, 5, 'Vegan'),
    ('Fruit salad w/ granola & yogurt (strawberries, blueberries, banana, etc)', 1078, 250, 40, 5, 10, 6, 'Balanced'),
    ('Turkey & greens', 1079, 300, 15, 15, 25, 5, 'High-protein'),
    ('Caprese salad w/ grilled chicken', 1080, 350, 10, 20, 30, 3, 'High-protein'),
    ('Whole wheat pita pizza w/ grilled chicken & veggies', 1081, 400, 40, 15, 25, 6, 'Balanced'),
    ('Sushi (Califfornia roll)', 1082, 300, 45, 5, 15, 3, 'Low-carb'),
    ('Vegetable shushi roll', 1083, 250, 40, 5, 10, 6, 'Vegan'),
    ('Mediterranean-style meatballs', 1084, 350, 10, 25, 20, 5, 'High-protein'),
    ('Spaghetti & turkey meatballs', 1085, 400, 40, 15, 25, 6, 'Balanced')


]

cursor.executemany('''
    INSERT INTO FOOD ('name', calories, carbohydrates, proteins, fats, 'food_group')
    VALUES (?, ?, ?, ?, ?, ?)
''', sample_data)



cursor.executemany('''
    INSERT INTO EXERCISES (BODY_PART, EXERCISE_NAME, REPS,SETS)
    VALUES (?, ?, ?, ?)
''', exercise_data)

# Commit changes and close the connection
conn.commit()
conn.close()
