try:
    import requests
except ModuleNotFoundError:
    raise NameError("The requests module was not found")

class WOTBlitz():
    def __init__(self, application_id: str) -> None:
        '''
            Object initialization.
        params:
            :application_id: str - is the id of your application in Wargaming developer room.
            (https://developers.wargaming.net/applications)
        '''
        if requests.get("https://api.wotblitz.ru/wotb/account/list/?application_id=%s&search=test&limit=1" % (application_id)).json()["status"] == "ok":
            self.application_id = application_id
        else:
            raise NameError("INVALID_APPLICATION_ID")
    
    def get_player_id_by_nickname(self, nickname: str, language: str = 'ru') -> int:
        '''
            this method returns the id of the player with this nickname, 
            if there is no player with this nickname, 0 will be returned.
        params:
            *:nickname: str - player nickname.
            :language: str - the localized language. Default: "ru".
        '''
        data = requests.get("https://api.wotblitz.ru/wotb/account/list/?application_id=%s&search=%s&language=%s&limit=1" % (self.application_id, nickname, language)).json()
        if data["meta"]["count"] == 1:
            if data["data"][0]["nickname"] == nickname:
                return data["data"][0]["account_id"]
        return 0

    def search_players(self, search: str, language: str = "ru", limit: int = 100, type: str = "startswith") -> list:
        '''
            The method returns a part of the list of players filtered by the first characters of the name and sorted alphabetically.
            If the search fails an empty list will be returned.
        params:
            *:search: str - the search string the names of the players.
            :language: str - the localized language. Default: "ru".
            :limit: int - number of records returned (may return fewer records, but not more than 100).
            :type: str - type of search. Default: "startswith". Valid value: "startswith", "exact".
        '''
        data = requests.get("https://api.worldoftanks.ru/wot/account/list/?application_id=%s&search=%s&language=%s&limit=%s&type=%s" % (self.application_id, search, lang, limit, type)).json()
        return data["data"]
    def get_player_nickname_by_id(self, account_id: int, language: str = "ru") -> str:
        '''
            This method returns nickname of id's owner.
            If id is invalid, None will be returned.
        params:
            *:account_id: int - id of the player account.
            :language: str - the localized language. Default: "ru".
        '''
        data = requests.get("https://api.wotblitz.ru/wotb/account/info/?application_id=%s&account_id=%s&language=%s" % (self.application_id, account_id, language)).json()
        if data["meta"]["count"] == 1:
            return data["data"][str(account_id)]["nickname"]
        return None
    
    def get_player_info_by_id(self, account_id: int, language: str = "ru") -> dict:
        '''
            This method returns player's personal data.
            If id is invalid, None will be returned.
        params:
            *:account_id: int - id of the player account.
            :language: str - the localized language. Default: "ru".
        '''
        data = requests.get("https://api.wotblitz.ru/wotb/account/info/?application_id=%s&account_id=%s&language=%s" % (self.application_id, account_id, language)).json()
        if data["data"][str(account_id)] == None:
            return None
        return data["data"][str(account_id)]["statistics"]["all"]

    def get_player_info_by_nickname(self, nickname: str, language: str = "ru") -> dict:
        '''
            This method returns player's personal data.
            If nickname is invalid, None will be returned.
        params:
            *:nickname: str - id nickname the player account.
            :language: str - the localized language. Default: "ru".
        '''
        account_id = self.get_player_id_by_nickname(nickname, language = language)
        if account_id == 0:
            return None
        return self.get_info_about_plyer_by_id(account_id, language = language)
    def get_player_achievements_by_id(self, account_id: int, language: str = "ru") -> dict:
        '''
            This method returns the player achievement.
            If id is invalid, None will be returned.
        params:
            *:id: str - id of the player account.
            :language: str - the localized language. Default: "ru".
        '''
        data = requests.get("https://api.wotblitz.ru/wotb/account/achievements/?application_id=%s&account_id=%s&language=%s" % (self.application_id, account_id, language)).json()
        if data["data"][str(account_id)] == None:
            return None
        return data["data"][str(account_id)]["achievements"]

    def get_player_achievements_by_nickname(self, nickname: str, language: str = "ru") -> dict:
        '''
            This method returns the player achievement.
            If nickname is invalid, None will be returned.
        params:
            *:nickname: str - nickname of the player account.
            :language: str - the localized language. Default: "ru".
        '''
        account_id = self.get_player_id_by_nickname(nickname, language = language)
        if account_id == 0:
            return None
        return self.get_player_achievements_by_id(account_id, language = language)
    def get_player_max_series_by_id(self, account_id: int, language: str = "ru") -> dict:
        '''
            This method returns the player max series.
            If id is invalid, None will be returned.
        params:
            *:id: int - id of the player account.
            :language: str - the localized language. Default: "ru".
        '''
        data = requests.get("https://api.wotblitz.ru/wotb/account/achievements/?application_id=%s&account_id=%s&language=%s" % (self.application_id, account_id, language)).json()
        if data["data"][str(account_id)] == None:
            return None
        return data["data"][str(account_id)]["max_series"]

    def get_player_max_series_by_nickname(self, nickname: str, language: str = "ru") -> dict:
        '''
            This method returns the player max series.
            If nickname is invalid, None will be returned.
        params:
            *:nickname: str - nickname of the player account.
            :language: str - the localized language. Default: "ru".
        '''
        account_id = self.get_player_id_by_nickname(nickname, language = language)
        if account_id == 0:
            return None
        return self.get_player_max_series_by_id(account_id)

    def get_clan_id_by_name(self, clan_name: str, language: str = "ru") -> int:
        '''
            This method returns the clan_id.
            If name is invalid, None will be returned.
        params:
            *:clan_name: str - the name or tag of the clan.
            :language: str - the localized language. Default: "ru".
        '''
        data = requests.get("https://api.wotblitz.ru/wotb/clans/list/?application_id=%s&search=%s&language=%s&limit=1" % (self.application_id, clan_name, language)).json()
        if data["data"] == list():
            return None
        return data["data"][0]["clan_id"]
    
    def get_tanks_list(self) -> dict:
        '''
            This method returns a list that contains ids and names of all tanks in the game.
        '''
        from tanks_list_wot_blitz import TANKS_LIST
        return TANKS_LIST