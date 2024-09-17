import unittest
import sqlite3

class TestDatabase(unittest.TestCase):
    def setUp(self):
        # Establish connection to the database
        self.conn = sqlite3.connect('gym.db')
        self.cursor = self.conn.cursor()

    def tearDown(self):
        # Close the connection
        self.conn.close()

    def test_food(self):
        self.cursor.execute("SELECT * FROM FOOD WHERE name=?", ('Avocado toast',))
        result = self.cursor.fetchone()
        self.assertIsNotNone(result, "Value 'Avocado toast' should be present in the database")
    
    def test_workout(self):
        self.cursor.execute("SELECT * FROM EXERCISES WHERE CWID = ?", (1,))
        result = self.cursor.fetchone()
        self.assertIsNotNone(result, "Value '1' should be present in the database")

    #no inbuilt users in the database rn so
    def test_user(self):
        self.cursor.execute("SELECT * FROM USER WHERE CWID = ?", (1,))
        result = self.cursor.fetchone()
        self.assertIsNotNone(result,"Value '1' should be present in the database")

if __name__ == '__main__':
    unittest.main()
