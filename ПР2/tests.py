import pytest
from unittest.mock import patch
import tests as a #Название модуля, мы обменивались кодом, а не файлами, поэтому тут мое рандомное

@patch('builtins.input',return_value="Heads")
@patch("random.choice",return_value="Heads")
def test_hh_head_or_tails(mock_input, mock_choice):
    assert a.head_or_tails() == "Correct!"

@patch('builtins.input',return_value="Heads")
@patch("random.choice",return_value="Tails")
def test_ht_head_or_tails(mock_input, mock_choice):
    assert a.head_or_tails() == "You Lost!"

@patch('builtins.input',return_value="Tails")
@patch("random.choice",return_value="Heads")
def test_th_head_or_tails(mock_input, mock_choice):
    assert a.head_or_tails() == "You Lost!"

@patch('builtins.input',return_value="Tails")
@patch("random.choice",return_value="Tails")
def test_tt_head_or_tails(mock_input, mock_choice):
    assert a.head_or_tails() == "Correct!"

@patch('builtins.input',return_value="tails")
@patch("random.choice",return_value="Tails")
def test_cc_head_or_tails(mock_input, mock_choice): #Check capitalize
    assert a.head_or_tails() == "Correct!"

@patch('builtins.input',return_value="ITSPIKACHU")
def test_rr_head_or_tails(mock_input):
    assert a.head_or_tails() == "...Huh? Anyway..You Lost!"

@patch("random.randint",return_value=10)
@patch('builtins.input',return_value="10")
def test_ft_guess_number(mock_input, mock_randint, capsys): #First try
    res = a.guess_number()
    cap =  capsys.readouterr()
    assert res == "Correct! Good job!"
    assert "Can you guess a number?" in cap.out
    assert "Too much! Try lesser number." not in cap.out
    assert "Not enough! Try bigger number." not in cap.out

@patch("random.randint",return_value=10)
@patch('builtins.input',side_effect=["2","10"])
def test_lt_guess_number(mock_input, mock_randint, capsys): #Less try
    res = a.guess_number()
    cap = capsys.readouterr()
    assert res == "Correct! Good job!"
    assert "Can you guess a number?" in cap.out
    assert "Too much! Try lesser number." not in cap.out
    assert "Not enough! Try bigger number." in cap.out

@patch("random.randint",return_value=10)
@patch('builtins.input',side_effect=["12","10"])
def test_bt_guess_number(mock_input, mock_randint, capsys): #Big try
    res = a.guess_number()
    cap = capsys.readouterr()
    assert res == "Correct! Good job!"
    assert "Can you guess a number?" in cap.out
    assert "Too much! Try lesser number." in cap.out
    assert "Not enough! Try bigger number." not in cap.out

@patch("random.randint",return_value=10)
@patch('builtins.input',side_effect=["100","1","10"])
def test_bt_guess_number(mock_input, mock_randint, capsys): #Big try
    res = a.guess_number()
    cap = capsys.readouterr()
    assert res == "Correct! Good job!"
    assert cap.out.splitlines()[1] == "Too much! Try lesser number."
    assert cap.out.splitlines()[2] == "Not enough! Try bigger number."

#rps = rock paper scissorgshfk Ножницы короче
@patch('builtins.input',return_value="rock")
@patch('random.choice',return_value=('2','Paper'))
def test_cc_rps(mock_input,mock_choice):
    assert a.rock_paper_scissors()=="You Lost!"

@patch('builtins.input',return_value="Rock")
@patch('random.choice',return_value=('2','Paper'))
def test_l_rps(mock_input,mock_choice):
    assert a.rock_paper_scissors()=="You Lost!"

@patch('builtins.input',return_value="Scissors")
@patch('random.choice',return_value=('2','Paper'))
def test_w_rps(mock_input,mock_choice):
    assert a.rock_paper_scissors()=="You Win!"

@patch('builtins.input',return_value='Paper')
@patch('random.choice',return_value=('2','Paper'))
def test_d_rps(mock_input,mock_choice):
    assert a.rock_paper_scissors()=="Draw!"

@patch('builtins.input',return_value="Эскперимент не был провальным")
@patch('random.choice',return_value=('2','Paper'))
def test_ri_rps(mock_input,mock_choice):
    assert a.rock_paper_scissors()=="No..."

@patch('builtins.input',return_value="qxzcdwu")
@patch('random.choice',return_value="bravery")
def test_l_hangman(mock_input,mock_choice,capsys):
    res = a.hangman()
    cap = capsys.readouterr()
    assert res == "You couldn't guess word... Correct answer was bravery"
    assert "Can you guess a word?" in cap.out
    assert "Wrong letter..." in cap.out

@patch('builtins.input',side_effect=["a","b","v","e","r","y"])
@patch('random.choice',return_value="bravery")
def test_w_hangman(mock_choice,mock_input,capsys):
    res = a.hangman()
    cap = capsys.readouterr()
    assert res == "You Win!\nCorrect word is bravery"
    assert "Can you guess a word?" in cap.out
    assert "Wrong letter..." not in cap.out

@patch('builtins.input',side_effect=["Выкидываем игру","5","f","c","d","q","a","b","v","e","r","y"])
@patch('random.choice',return_value="bravery")
def test_cl_hangman(mock_choice,mock_input,capsys):
    res = a.hangman()
    cap = capsys.readouterr()
    assert res == "You Win!\nCorrect word is bravery"
    assert "Can you guess a word?" in cap.out
    assert "Wrong letter..." in cap.out
    assert "Correct letter!" in cap.out
    assert "_ _ a _ _ _ _" in cap.out

@patch('builtins.input',return_value="")
@patch('random.randint',side_effect=[6,1])
def test_w_dice_battle(mock_input,mock_choice, capsys):
    res = a.dice_battle()
    cap = capsys.readouterr()
    assert res == "Congratulations! Hp left... 1"
    assert "You Won!" in cap.out
    assert "Ready to throw a dice?" in cap.out
    assert "You both had 5 hp!" in cap.out

@patch('builtins.input',return_value="")
@patch('random.randint',side_effect=[1,6])
def test_l_dice_battle(mock_input,mock_choice, capsys):
    res = a.dice_battle()
    cap = capsys.readouterr()
    assert res == "You died...Game over!"
    assert "You Lost.." in cap.out
    assert "Ready to throw a dice?" in cap.out
    assert "You both had 5 hp!" in cap.out

@patch('builtins.input',return_value="")
@patch('random.randint',side_effect=[1,1,6,1])
def test_dw_dice_battle(mock_input,mock_choice, capsys):
    res = a.dice_battle()
    cap = capsys.readouterr()
    assert res == "Congratulations! Hp left... 1"
    assert "You Won!" in cap.out
    assert "Ready to throw a dice?" in cap.out
    assert "You both had 5 hp!" in cap.out
    assert "Draw!" in cap.out