import unittest
from employee_managment import EmployeeManagment, DataEmployee
import tempfile, pathlib, os, uuid

class TestEmployeeCRUD(unittest.TestCase):
    def setUp(self):
        fd, path = tempfile.mkstemp(prefix="tdd_", suffix=".json")
        os.close(fd)
        self.temp = pathlib.Path(path)
        self.temp.write_text("[]", encoding="utf-8")
        self.mgr = EmployeeManagment(path=self.temp)

    def tearDown(self):
        try:
            self.temp.unlink()
        except PermissionError:
            pass

    def test_create(self):
        emp = DataEmployee(
            id=str(uuid.uuid4()),
            first_name="Drake",
            last_name="Drobov",
            position="Engineer"
        )
        self.mgr.add(emp)
        found = self.mgr.get(emp.id)
        self.assertIsNotNone(found)
        self.assertEqual(found.first_name, "Drake")
        self.assertEqual(found.last_name, "Drobov")

    def test_update(self):
        emp = DataEmployee(
            id=str(uuid.uuid4()),
            first_name="Grigory",
            last_name="Grobov",
            position="Analyst"
        )
        self.mgr.add(emp)
        updated = self.mgr.update(emp.id, position="Analyst")
        self.assertTrue(updated)
        self.assertEqual(self.mgr.get(emp.id).position, "Analyst")

    def test_delete(self):
        emp = DataEmployee(
            id=str(uuid.uuid4()),
            first_name="Lena",
            last_name="Varkinovna",
            position="Designer"
        )
        self.mgr.add(emp)
        deleted = self.mgr.delete(emp.id)
        self.assertTrue(deleted)
        self.assertIsNone(self.mgr.get(emp.id))

    def test_find_by_last_name(self):
        emp1 = DataEmployee(
            id=str(uuid.uuid4()),
            first_name="Alexander",
            last_name="Alexandrov",
            position="Manager"
        )
        emp2 = DataEmployee(
            id=str(uuid.uuid4()),
            first_name="Igor",
            last_name="Igorev",
            position="Developer"
        )
        self.mgr.add(emp1)
        self.mgr.add(emp2)
        results = self.mgr.find_by_last_name("Alexandrov")
        self.assertEqual(len(results),1)
        self.assertEqual(results[0].first_name, "Alexander")

if __name__ == "__main__":
    unittest.main()
