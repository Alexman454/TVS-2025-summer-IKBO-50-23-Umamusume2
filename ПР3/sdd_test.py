from dataclasses import dataclass, asdict
from employee_managment import EmployeeManagment, DataEmployee
import tempfile, pathlib, os, uuid
import pytest

SDD_SPECIFICATIONS = [
    {
        "action": "add",
        "input": {"first_name": "Ivan", "last_name": "Ivanov", "position": "Engineer", "email": "", "phone": ""},
        "expected": {
            "fields": ["id", "first_name", "last_name", "position", "email", "phone", "hired_date"],
            "first_name": "Ivan",
            "last_name": "Ivanov"
        }
    },
    {
        "action": "find_by_last_name",
        "input": {"last_name": "Ivanov"},
        "expected": {"count": 1, "first_name": "Ivan"}
    },
    {
        "action": "update",
        "input": {"fields": {"position": "Senior Engineer"}},
        "expected": {"updated": True, "position": "Senior Engineer"}
    },
    {
        "action": "delete",
        "expected": {"deleted": True}
    }
]

@pytest.mark.parametrize("spec", SDD_SPECIFICATIONS)
def test_sdd_new_version(spec):
    fd, path = tempfile.mkstemp(prefix="sdd_", suffix=".json")
    os.close(fd)
    db_path = pathlib.Path(path)
    db_path.write_text("[]", encoding="utf-8")
    mgr = EmployeeManagment(path=db_path)
    try:
        if spec["action"] == "add":
            inp = spec["input"]
            emp = DataEmployee(id=str(uuid.uuid4()), **inp, hired_date="")
            mgr.add(emp)
            for field in spec["expected"]["fields"]:
                assert hasattr(emp, field)
            assert emp.first_name == spec["expected"]["first_name"]
            assert emp.last_name == spec["expected"]["last_name"]

        elif spec["action"] == "find_by_last_name":
            emp = DataEmployee(id=str(uuid.uuid4()), first_name="Ivan", last_name="Ivanov", position="Engineer")
            mgr.add(emp)
            results = mgr.find_by_last_name(spec["input"]["last_name"])
            assert len(results) == spec["expected"]["count"]
            if results:
                assert results[0].first_name == spec["expected"]["first_name"]

        elif spec["action"] == "update":
            emp = DataEmployee(id=str(uuid.uuid4()), first_name="Ivan", last_name="Ivanov", position="Engineer")
            mgr.add(emp)
            updated = mgr.update(emp.id, **spec["input"]["fields"])
            assert updated == spec["expected"]["updated"]
            for k, v in spec["input"]["fields"].items():
                assert getattr(emp, k) == v

        elif spec["action"] == "delete":
            emp = DataEmployee(id=str(uuid.uuid4()), first_name="Ivan", last_name="Ivanov", position="Engineer")
            mgr.add(emp)
            deleted = mgr.delete(emp.id)
            assert deleted == spec["expected"]["deleted"]
            assert mgr.get(emp.id) is None

    finally:
        try:
            db_path.unlink()
        except PermissionError:
            pass

if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__]))
