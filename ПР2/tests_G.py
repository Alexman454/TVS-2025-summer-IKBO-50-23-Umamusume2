import pytest
from unittest.mock import patch
import module_G as a

@patch("random.random",return_value=0)
@patch("random.choice",return_value="Сидоров")
def test_cmn_gs(mock_random,mock_choice):
    assert a.generate_surname(False) == "Сидоров"
    assert a.generate_surname(True) == "Сидорова"

@patch("random.random",return_value=0.6)
@patch("random.choice",side_effect=["Бело","бор","ов"])
def test_bsm_m_gs(mock_random,side_effect):
    assert a.generate_surname(False) == "Белоборов"

@patch("random.random",return_value=0.6)
@patch("random.choice",side_effect=["Бело","бор","ова"])
def test_bsm_f_gs(mock_random,side_effect):
    assert a.generate_surname(True) == "Белоборова"

@patch("random.randint",return_value=1)
@patch("random.random",return_value=0)
@patch("random.choice",side_effect=["А","Сидоров"])
def test_f2_gfn(mock_randint,mock_random,mock_choice):
    names = ["София", "Анна", "Мария", "Ева", "Виктория", "Полина", "Алиса", "Варвара", "Василиса", "Александра", "Елизавета", "Арина", "Ксения", "Екатерина", "Дарья", "Милана", "Анастасия", "Мирослава", "Вероника", "Кира", "Михаил", "Александр", "Максим", "Артем", "Марк", "Лев", "Иван", "Матвей", "Даниил", "Дмитрий", "Тимофей", "Роман", "Мирон", "Мухаммад", "Кирилл", "Егор", "Илья", "Алексей", "Константин", "Федор"]
    assert a.generate_full_name() == "Анна А. Сидорова"
    
@patch("random.randint",return_value=20)
@patch("random.random",return_value=0)
@patch("random.choice",side_effect=["А","Сидоров"])
def test_m1_gfn(mock_randint,mock_random,mock_choice):
    names = ["София", "Анна", "Мария", "Ева", "Виктория", "Полина", "Алиса", "Варвара", "Василиса", "Александра", "Елизавета", "Арина", "Ксения", "Екатерина", "Дарья", "Милана", "Анастасия", "Мирослава", "Вероника", "Кира", "Михаил", "Александр", "Максим", "Артем", "Марк", "Лев", "Иван", "Матвей", "Даниил", "Дмитрий", "Тимофей", "Роман", "Мирон", "Мухаммад", "Кирилл", "Егор", "Илья", "Алексей", "Константин", "Федор"]
    assert a.generate_full_name() == "Михаил А. Сидоров"

@patch("random.randint",side_effect = [1991,31,2])
def test_2_and_big_gbd(mock_randint):
    assert a.generate_born_date() == "28.2.1991"

@patch("random.randint",side_effect = [2009,31,4])
def test_4_and_big_gbd(mock_randint):
    assert a.generate_born_date() == "30.4.2009"

@patch("random.randint",side_effect = [2004,30,2])
def test_vesokosny_gbd(mock_randint):
    assert a.generate_born_date() == "29.2.2004"

@patch("random.randint")
def test_gpn(mock_randint):
    mock_randint.side_effect = [20,15,2000]
    assert a.generatepasnum() == "20 15 002000"
    mock_randint.side_effect = [50,20,999999]
    assert a.generatepasnum() == "26 12 199100"
    mock_randint.side_effect = [26,12,199100]
    assert a.generatepasnum() == "26 12 199100"

def test_dpi(capsys):
    res = a.displaypasinfo("LEEROOOOY JENKINS!","88 00 5553535","11.09.2001")
    cap =  capsys.readouterr()
    assert "ФИО - LEEROOOOY JENKINS!" in cap.out
    assert "Дата рождения - 11.09.2001" in cap.out
    assert "Серия и Номер - 88 00 5553535" in cap.out

def test_vc():
    assert a.validitycheck(["LEEROOOOY JENKINS!","88 00 5553535","11.9.2001"]) == False
    assert a.validitycheck(["LEEROOOOY JENKINS!","50 20 999999","11.9.2001"]) == True

