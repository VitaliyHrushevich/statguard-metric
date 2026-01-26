import sqlite3
import os
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_DIR, "..", "data", "experiments.db")


class StatMetricDB:
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        # Create a data folder if there is no data folder
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS experiment_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp DATETIME,
                    test_name TEXT,
                    p_value REAL,
                    lift REAL,
                    test_type TEXT,  
                    is_significant INT
                )
            ''')

            conn.commit()

    def log_experiment(self, name: str, p_val: float, lift: float, test_type: str):  # ДОБАВИЛИ test_type
        is_sig = 1 if p_val < 0.05 else 0
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO experiment_logs (timestamp, test_name, p_value, lift, test_type, is_significant)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (datetime.now(), name, p_val, lift, test_type, is_sig))  # И ЗДЕСЬ ДОБАВИЛИ
            conn.commit()
            print(f"💾 [DB] Результат '{name}' ({test_type}) успешно залогирован.")



