import sqlite3
import threading

class DatabaseConnectionSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(DatabaseConnectionSingleton, cls).__new__(cls)
                    cls._instance.connection = None
        return cls._instance
    
    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect("app.db",check_same_thread=False)
        return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.connection = None