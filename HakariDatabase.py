

import typing
import sqlite3

import multiprocessing
import threading

from HakariUtils import LogLevel, ErrorCode, log
from HakariClasses import Character, Player


class Database:
    def __init__(self, dbfilename : str):
        """[Initializer] Default Initializer for Database"""
        self.__connection : sqlite3.Connection = sqlite3.connect(dbfilename)
        self.__cursor : sqlite3.Cursor = self.__connection.cursor()

    def __initialize_table(self, tablename : str, columns : typing.List[str]) -> ErrorCode:
        """"""
        try:
            col_str = ", ".join(columns)
            query = f"CREATE TABLE IF NOT EXISTS {tablename}({col_str})"
            self.__cursor.execute(query)
            self.__connection.commit()
            log(f"Initialized Table [{tablename}]", LogLevel.DEBUG)
            log(f"\tColumns: {columns}", LogLevel.DEBUG)
            return ErrorCode(1)
        except Exception as exc:
            log(f"Exception when Initializing {tablename} [{exc.args}]", LogLevel.WARNING)
            log(f"\tColumns: {columns}", LogLevel.DEBUG)
            return ErrorCode(0)

    def __insert(self, tablename : str, data : dict[str, typing.Any]) -> ErrorCode:
        try:
            col_str = ", ".join(["?" for i in range(len(data))])
            entry = (data[val] for val in data)
            query = f"INSERT INTO {tablename} VALUES ({col_str})"
            self.__cursor.execute(query, entry)
            self.__connection.commit()
            log(f"Inserted into {tablename}", LogLevel.DEBUG)
            log(f"\tColumns: {data.keys()}", LogLevel.DEBUG)
            return ErrorCode(1)
        except Exception as exc:
            log(f"Exception when Inserting into {tablename} [{exc.args}]", LogLevel.WARNING)
            log(f"\tColumns: {data.keys()}", LogLevel.DEBUG)
            log(f"\tValues: {data.values()}", LogLevel.DEBUG)
            return ErrorCode(0)


class HakariDatabase(Database):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create Tables in the Database
        self.__initialize_tables()

        # Define Database Insertion Queue
        self.DatabaseInsertionQueue : multiprocessing.Queue[typing.Tuple[str, dict[str, typing.Any]]] = multiprocessing.Queue(maxSize=999)
        
        # Start Database Insertion Thread
        self.__insertion_thread : threading.Thread = threading.Thread(target=self.__run_insertion_queue, name="InsertionThread")
        self.__insertion_thread.start()

    def __initialize_tables(self):
        # Create SERVERS Table
        columns = ["id INTEGER PRIMARY KEY"]
        self.__initialize_table("SERVERS", columns)

        # Create SERVER_PLAYERS Table
        columns = ["guild_id INTEGER",
                   "player_id INTEGER",
                   "FOREIGN KEY (guild_id) REFERENCES SERVERS(id) ON DELETE CASCADE"]

        # Create CHARACTERS Table
        columns = ["id INTEGER PRIMARY KEY",
                   "name TEXT",
                   "series TEXT",
                   "gender TEXT",
                   "value INTEGER",
                   "claim_rank INTEGER",
                   "like_rank INTEGER",
                   "about TEXT"]
        self.__initialize_table("CHARACTERS", columns)

        # Create CHAR_ALIASES Table
        columns = ["character_id INTEGER",
                   "alias TEXT",
                   "FOREIGN KEY (character_id) REFERENCES CHARACTERS(id) ON DELETE CASCADE"]
        self.__initialize_table("CHAR_ALIASES", columns)

        # Create CHAR_IMAGE_URLS Table
        columns = ["character_id INTEGER",
                   "image_urls TEXT",
                   "FOREIGN KEY (character_id) REFERENCES CHARACTERS(id) ON DELETE CASCADE"]
        self.__initialize_table("CHAR_IMAGE_URLS", columns)

        # Create PLAYERS Table
        columns = ["id INTEGER PRIMARY KEY",
                   "guild_id INTEGER",
                   "balance INTEGER",
                   "lifetime_losses INTEGER",
                   "daily_allowance INTEGER",
                   "image_url TEXT",
                   "unused_rolls INTEGER",
                   "unused_claims INTEGER",
                   "coin_toss_bonus INTEGER",
                   "rock_paper_scissors_bonus INTEGER",
                   "blackjack_bonus INTEGER",
                   "FOREIGN KEY (guild_id) REFERENCES SERVERS(id) ON DELETE CASCADE"]
        self.__initialize_table("PLAYERS", columns)

        # Create OWNED_CHARACTERS Table
        columns = ["guild_id INTEGER",
                   "player_id INTEGER",
                   "character_id INTEGER",
                   "FOREIGN KEY (guild_id) REFERENCES SERVERS(id) ON DELETE CASCADE",
                   "FOREIGN KEY (player_id) REFERENCES PLAYERS(id) ON DELETE CASCADE",
                   "FOREIGN KEY (character_id) REFERENCES CHARACTERS(id) ON DELETE CASCADE"]
        self.__initialize_table("OWNED_CHARACTERS", columns)

        # Create LIKED_CHARACTERS Table
        columns = ["guild_id INTEGER",
                   "player_id INTEGER",
                   "character_id INTEGER",
                   "FOREIGN KEY (guild_id) REFERENCES SERVERS(id) ON DELETE CASCADE",
                   "FOREIGN KEY (player_id) REFERENCES PLAYERS(id) ON DELETE CASCADE",
                   "FOREIGN KEY (character_id) REFERENCES CHARACTERS(id) ON DELETE CASCADE"]
        self.__initialize_table("LIKED_CHARACTERS", columns)

        # Create SERIES Table
        columns = ["id INTEGER PRIMARY KEY",
                   "name TEXT",
                   "series_rank INT",
                   "about TEXT"]
        self.__initialize_table("SERIES", columns)

        # Create SERIES_IMAGE_URLS Table
        columns = ["series_id INTEGER",
                   "image_urls TEXT",
                   "FOREIGN KEY (series_id) REFERENCES SERIES(id) ON DELETE CASCADE"]
        self.__initialize_table("SERIES_IMAGE_URLS", columns)

        # Create SERIES_ALIASES Table
        columns = ["series_id INTEGER",
                   "alias TEXT",
                   "FOREIGN KEY (series_id) REFERENCES SERIES(id) ON DELETE CASCADE"]
        self.__initialize_table("SERIES_ALIASES", columns)

        # Create BLACK_MARKET Table
        columns = ["market_bonus INTEGER",
                   "guild_id INTEGER",
                   "FOREIGN KEY (guild_id) REFERENCES SERVERS(id) ON DELETE CASCADE"]
        self.__initialize_table("BLACK_MARKET", columns)

        # Create AVAILABLE_CHARACTERS Table
        columns = ["character_id INTEGER",
                   "guild_id INTEGER",
                   "FOREIGN KEY (guild_id) REFERENCES SERVERS(id) ON DELETE CASCADE",
                   "FOREIGN KEY (character_id) REFERENCES CHARACTERS(id) ON DELETE CASCADE"]
        self.__initialize_table("AVAILABLE_CHARACTERS", columns)

    def __run_insertion_queue(self):
        """[Threaded Method] Take the first insertion command in the queue and inserts into the database"""
        while True:
            try:
                # Get next object to insert in Queue
                tn, data = self.DatabaseInsertionQueue.get()
                self.__insert(tn, data)
            except Exception as exc:
                log(f"Exception When Inserting into Database [{exc}]", LogLevel.ERROR)
        

    # public functions
    def GetAllCharactersFromSeries(self, series : str) -> typing.Tuple[ErrorCode, typing.List[Character]]:
        return (ErrorCode(1), [])
    def GetAllCharactersFromGenre(self, genre : str) -> typing.Tuple[ErrorCode, typing.List[Character]]:
        return (ErrorCode(1), [])
    def GetTopCharacters(self) -> typing.Tuple[ErrorCode, typing.List[Character]]:
        return (ErrorCode(1), [])
    
    def GetCharacterWithName(self, name : str) -> typing.Tuple[ErrorCode, Character]:
        return (ErrorCode(1), {})
    def GetCharacterWithId(self, id : int) -> typing.Tuple[ErrorCode, Character]:
        return (ErrorCode(1), {})
    
    def GetPlayerOwnedCharacters(self, playerid : int) -> typing.Tuple[ErrorCode, typing.List[Character]]:
        return (ErrorCode(1), [])
    




if __name__ == "__main__":
    # db = HakariDatabase("test_database.db")
    # db.InitializeTables()

    print("Main()")