
import typing
import enum

from HakariUtils import LogLevel, ErrorCode, log



# Data Classes
class Character:
    def __init__(self):
        """[Constructor] Default Constructor for Character"""
        self.id : int = -1
        self.name : str = ""
        self.series : str = ""
        self.gender : str = ""
        self.alias : typing.List[str] = []
        self.value : int = -1
        self.claim_rank : int = -1
        self.like_rank : int = -1
        self.image_urls : typing.List[str] = []
        self.about : str = ""

    def SetFromDict(self, data : typing.Dict[str, typing.Any]) -> ErrorCode:
        """[Method] Move data values from dictionary into the Character class"""
        try:
            for key in data:
                match key:
                    case "id":
                        self.id = data[key]
                    case "name":
                        self.name = data[key]
                    case "series":
                        self.series = data[key]
                    case "gender":
                        self.gender = data[key]
                    case "alias":
                        self.alias = data[key]
                    case "value":
                        self.value = data[key]
                    case "claim_rank":
                        self.claim_rank = data[key]
                    case "like_rank":
                        self.like_rank = data[key]
                    case "image_urls":
                        self.image_urls = data[key]
                    case "about":
                        self.about = data[key]
            return ErrorCode(1)
        except Exception as exc:
            return ErrorCode(0)
    
    def GetAsDict(self) -> typing.Dict[str, typing.Any]:
        """[Method] Move Data from Class into Dictionary"""
        try:
            data = {}
            data["id"] = self.id
            data["name"] = self.name
            data["series"] = self.series
            data["gender"] = self.gender
            data["alias"] = self.alias
            data["value"] = self.value
            data["claim_rank"] = self.claim_rank
            data["like_rank"] = self.like_rank
            data["image_urls"] = self.image_urls
            data["about"] = self.about
            return data
        except Exception as exc:
            return {}

class Player:
    def __init__(self):
        """[Constructor] Default Constructor for player"""
        self.id : int = -1
        self.guild_id : int = -1
        self.balance : int = -1
        self.lifetime_losses : int = -1
        self.daily_allowance : int = -1
        self.image_url : str = ""

        self.owned_characters : typing.List[int]
        self.liked_characters : typing.List[int]

        self.unused_rolls : int = -1
        self.unused_claims : int = -1

        self.coin_toss_bonus : int = -1
        self.rock_paper_scissors_bonus : int = -1
        self.blackjack_bonus : int = -1
    
    def SetFromDict(self, data : typing.Dict[str, typing.Any]) -> ErrorCode:
        """[Method] Move data values from dictionary into the Player class"""
        try:
            for key in data:
                match key:
                    case "id":
                        self.id = data[key]
                    case "guild_id":
                        self.guild_id = data[key]
                    case "balance":
                        self.balance = data[key]
                    case "lifetime_losses":
                        self.lifetime_losses = data[key]
                    case "daily_allowance":
                        self.daily_allowance = data[key]
                    case "image_url":
                        self.image_url = data[key]
                    case "owned_characters":
                        self.owned_characters = data[key]
                    case "liked_characters":
                        self.liked_characters = data[key]
                    case "unused_rolls":
                        self.unused_rolls = data[key]
                    case "unused_claims":
                        self.unused_claims = data[key]
                    case "coin_toss_bonus":
                        self.coin_toss_bonus = data[key]
                    case "rock_paper_scissors_bonus":
                        self.rock_paper_scissors_bonus = data[key]
                    case "blackjack_bonus":
                        self.blackjack_bonus = data[key]
            return ErrorCode(1)
        except Exception as exc:
            return ErrorCode(0)

    def GetAsDict(self) -> typing.Dict[str, typing.Any]:
        """[Method] Move Data from Class into Dictionary"""
        try:
            data = {}
            data["id"] = self.id
            data["guild_id"] = self.guild_id
            data["balance"] = self.balance
            data["lifetime_losses"] = self.lifetime_losses
            data["daily_allowance"] = self.daily_allowance
            data["image_url"] = self.image_url
            data["owned_characters"] = self.owned_characters
            data["liked_characters"] = self.liked_characters
            data["unused_rolls"] = self.unused_rolls
            data["unused_claims"] = self.unused_claims
            data["coin_toss_bonus"] = self.coin_toss_bonus
            data["rock_paper_scissors_bonus"] = self.rock_paper_scissors_bonus
            data["blackjack_bonus"] = self.blackjack_bonus
            return data
        except Exception as exc:
            return {}


class Series:
    def __init__(self):
        self.id : int = -1
        self.name : str = ""
        self.alias : typing.List[str] = []
        self.series_rank : int = -1
        self.about : str = ""
        self.image_urls : typing.List[str] = []

    def SetFromDict(self, data : typing.Dict[str, typing.Any]) -> ErrorCode:
        return
    def GetAsDict(self) -> typing.Dict[str, typing.Any]:
        return

class BlackMarket:
    def __init__(self):
        self.guild_id : int = -1
        self.available_characters : typing.List[int]
        self.market_bonus : int = -1
    
    def SetFromDict(self, data : typing.Dict[str, typing.Any]) -> ErrorCode:
        return
    def GetAsDict(self) -> typing.Dict[str, typing.Any]:
        return
    




# Command Classes
    
class HakariCommands():
    ROLL = 0
    DIVORCE = 1
    SEARCH = 2
    COIN_TOSS = 3
    ROCK_PAPER_SCISSORS = 4
    HELP = 5
    DAILY_ALLOWANCE = 6
    TOP_CHARACTERS = 7
    OWNED_CHARACTERS = 8



    
class HakariCommand:
    def __init__(self):
        self.command_id : int = -1
        self.command_parameters : typing.List[str] = []



