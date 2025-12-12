from dataclasses import dataclass, asdict
import json, uuid, datetime

@dataclass
class DataEmployee:
    id: str
    first_name: str
    last_name: str
    position: str
    email: str = ""
    phone: str = ""
    hired_date: str = ""

class EmployeeManagment:
    def __init__(self, path="employees.json"):
        self.path = path
        self._employees = []
        self.load()

    def save(self):
        data = []
        for emp in self._employees:
            data.append(asdict(emp))
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self):
        emps = []
        if not self.path.exists():
            self._employees = []
            return
        with open(self.path, "r", encoding="utf-8") as f:
            inf = json.load(f)
        for emp in inf:
            emps.append(DataEmployee(**emp))
        self._employees = emps

    def add(self, emp: DataEmployee):
        self._employees.append(emp)
        self.save()

    def find_by_last_name(self, last_name):
        result = []
        for emp in self._employees:
            if emp.last_name.lower() == last_name.lower():
                result.append(emp)
        return result

    def update(self, emp_id, **fields):
        emp = self.get(emp_id)
        if not emp:
            return False
        for i, j in fields.items():
            if hasattr(emp, i):
                setattr(emp, i, j)
        self.save()
        return True
    
    def delete(self, emp_id):
        length = len(self._employees)
        self._employees = []
        for employee in self._employees:
            if employee.id != emp_id:
                self._employees.append(employee)
        if (len(self._employees) < length):
            self.save()
            return True
        return False
    
    def get(self, emp_id):
        for emp in self._employees:
            if emp.id == emp_id:
                return emp
        return None
