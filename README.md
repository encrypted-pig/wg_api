**wg_api** – Python модуль для удобной работы с Wargaming API.

*Доступны методы для работы с API игры WOT Blitz.*

* [Wargaming Developer Room](https://developers.wargaming.net/)

```python
import wg_api

#id вашего приложения можно посмотреть здесь https://developers.wargaming.net/applications
app = wg_api.WOTBlitz("228053609b02258f94c78c79bd6c3971")
print(app.get_player_info_by_name("player12345"))
```

Установка
------------
    $ python -m pip install wg_api

__Список доступных методов методов:__
- get_player_id_by_name(name: str, language: str = 'ru') -> int
- search_players(search: str, language: str = "ru", limit: int = 100, type: str = "startswith") -> list
- get_player_name_by_id(account_id: int, language: str = "ru") -> str
- get_player_info_by_id(account_id: int, language: str = "ru") -> dict
- get_player_info_by_name(name: str, language: str = "ru") -> dict
- get_player_achievements_by_id(account_id: int, language: str = "ru") -> dict
- get_player_achievements_by_name(name: str, language: str = "ru") -> dict
- get_player_max_series_by_id(account_id: int, language: str = "ru") -> dict
- get_player_max_series_by_name(name: str, language: str = "ru") -> dict
- get_clan_id_by_name(clan_name: str, language: str = "ru") -> int
- get_clan_info_by_id(clan_id: int, language: str = "ru") -> dict
- get_clan_info_by_name(clan_name: str, language: str = "ru")
- get_tanks_list() -> dict