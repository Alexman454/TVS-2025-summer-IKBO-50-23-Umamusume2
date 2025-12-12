from employee_managment import EmployeeManagment, DataEmployee
import tempfile, pathlib, os, uuid

def create_temp_manage():
    fd, path = tempfile.mkstemp(prefix="atdd_", suffix=".json")
    os.close(fd)
    temp = pathlib.Path(path)
    temp.write_text("[]", encoding="utf-8")
    mgr = EmployeeManagment(path=temp)
    return temp, mgr

def test_add_and_find_employee_acceptance():
    temp, mgr = create_temp_manage()
    try:
        emp = DataEmployee(
            id=str(uuid.uuid4()),
            first_name="Frax",
            last_name="Klak",
            position="Manager"
        )
        mgr.add(emp)

        results = mgr.find_by_last_name("Klak")
        assert len(results) == 1
        assert results[0].first_name == "Frax"
    finally:
        try:
            temp.unlink()
        except PermissionError:
            pass

def test_update_and_delete_employee_acceptance():
    temp, mgr = create_temp_manage()
    try:
        emp = DataEmployee(
            id=str(uuid.uuid4()),
            first_name="Rodion",
            last_name="Raskolnikov",
            position="Student"
        )
        mgr.add(emp)
        updated = mgr.update(emp.id, position="Student")
        assert updated
        assert mgr.get(emp.id).position == "Student"
        deleted = mgr.delete(emp.id)
        assert deleted
        assert mgr.get(emp.id) is None
    finally:
        try:
            temp.unlink()
        except PermissionError:
            pass
