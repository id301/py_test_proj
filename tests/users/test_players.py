import requests
import pytest

from src.generators.player_localization import PlayerLocalization

@pytest.mark.parametrize("status", [
    "ACTIVE",
    "BANNED",
    "DELETED",
    "INACTIVE"
])
def test_players(status, get_player_generator):
    print(get_player_generator.build())

#Проверка баланса
@pytest.mark.parametrize("balance_value", [
    "100",
    "0",
    "-10",
    "adasd"
])
def test_players(balance_value, get_player_generator):
    print(get_player_generator.set_balance(balance_value).build())

#проверка обязательности полей
@pytest.mark.parametrize("delete_key", [
    "account_status",
    "balance",
    "localize",
    "avatar"
])
def test_players(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)

#апдейт внутренних генераторов
def test_players(get_player_generator):
    object_to_send = get_player_generator.update_inner_generator(
        "localize", PlayerLocalization('fr_FR')
    ).build()
    print(object_to_send)