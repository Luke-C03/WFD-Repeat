import unittest
from PartA import Athlete, swimmer

class TestAthlete(unittest.TestCase):
    def setUp(self):
        self.athlete = Athlete(
            name="James",
            sex="male",
            age=25,
            qualifications=["National Champion"],
            records=[{"event": "200m backstroke", "time": "1:48.10"}]
        )
        self.swimmer = swimmer(
            name="Amy",
            sex="Female",
            age=23,
            qualifications=["Regional Champion"],
            records=[{"event": "100m butterfly", "time": "53.50"}],
            event="100m butterfly",
            personal_best="53.50"
        )

        self.same_athelte = self.athlete
        self.different_athlete = Athlete(
            name="James",
            sex="male",
            age=25,
            qualifications=["National Champion"],
            records=[{"event": "200m backstroke", "time": "1:48.10"}]
        )

    def test_instance_of_class(self):
        self.assertIsInstance(self.athlete,Athlete)
        self.assertIsInstance(self.swimmer,swimmer)
        self.assertIsInstance(self.swimmer,Athlete)

    def test_not_instance_of_class(self):
        self.assertNotIsInstance(self.athlete, swimmer)

    def test_objects_identity(self):
        self.assertIs(self.athlete, self.same_athelte)
        self.assertIsNot(self.athlete, self.different_athlete)

    def test_update_name(self):
        self.athlete.update_name("James Morgan")
        self.assertEqual(self.athlete.name, "James Morgan")

if __name__ == '__main__':
    unittest.main
       