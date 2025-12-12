import sys, os, json, tempfile, pathlib, uuid
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from behave import given, when, then
from employee_managment import EmployeeManagment, DataEmployee

@given('сотрудник "{first_name} {last_name}" с должностью "{position}" добавлен в систему')
def step_add_employee(context, first_name, last_name, position):
    fd, path = tempfile.mkstemp(prefix="bdd_", suffix=".json")
    os.close(fd)
    context.temp = pathlib.Path(path)
    context.temp.write_text("[]", encoding="utf-8")
    context.mgr = EmployeeManagment(path=context.temp)
    emp = DataEmployee(
        id=str(uuid.uuid4()),
        first_name=first_name,
        last_name=last_name,
        position=position
    )
    context.mgr.add(emp)

@when('я выполняю поиск сотрудника по фамилии "{last_name}"')
def step_search(context, last_name):
    context.results = context.mgr.find_by_last_name(last_name)

@then('я нахожу одного сотрудника с именем "{expected}"')
def step_check(context, expected):
    assert len(context.results) == 1
    assert context.results[0].first_name == expected
    try:
        context.temp.unlink(missing_ok=True)
    except PermissionError:
        pass
