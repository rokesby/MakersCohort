# Class Friends
# Dictionary['name'] = Friend
# Methods:
#  Add a friend
#  Edit(friend)
#  list_upcoming_bdays (base it on timenow)
#  
# Child class => Friend --> attributes  DOB, name, card
# Set friend_bday 
# Set friend_name
# Get age
# get next_bdy


import pytest
from lib.complex import *
import datetime


# Test the child 
@pytest.fixture
def create_friend1():
    friend = Friend('Rez','28/05/1992')
    return friend

@pytest.fixture
def create_friend2():
    friend = Friend('George', '29/05/1998')
    friend.set_name('David')
    friend.set_dob('29/06/1993')

def test_name_valid():
    with pytest.raises(Exception) as err:
        friend  = Friend('','')
    assert str(err.value) == 'Invalid input, please double check'

def test_name(create_friend):
    assert create_friend.name == 'Rez'

def test_dob(create_friend):
    assert create_friend.dob == '08/05/1992'


def test_set_name(create_friend2):
    assert create_friend2.name == 'David'

def test_set_name_invalid_input(create_friend1):
    with pytest.raises(Exception) as err:
        create_friend1.set_name('')
    assert str(err.value) == 'Invalid name, please type a string'

def test_set_dob(create_friend2):
    assert create_friend2.dob == '06/06/1993'

def test_set_dob_invalid_input(create_friend1):
    with pytest.raises(Exception) as err:
        create_friend1.set_dob('')
    # exception --> input and validate as correct date 
    assert str(err.value) == 'Invalid name, please type a string'

def test_get_age(create_friend1):
    assert create_friend1.age() == 32

def test_get_next_bday(create_friend1):
    assert create_friend1.next_bday() == '28/05/2025'

# Friends class tests

@pytest.fixture
def create_friends():
    friends = Friends()
    friends.add(Friend('George', '29/05/1998'))
    friends.add(Friend('Rez', '29/05/1998'))


def test_add_friend(create_friends):
    assert create_friends[0].name == 'George'

def test_upcoming_bdays(create_friends):
    assert create_friends.upcoming_bdays == [('George','29/05/1998'),('Rez','29/05/1998')]
