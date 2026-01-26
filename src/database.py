import sqlite3
import os
from datetime import datetime


class StatMetricDB:
    """Designed for managing A/B test history"""

    def __init__(self, db_path: str = "data/experiments.db"):
        self.db_path = db_path
        # os.makedirs creates a folder if it is missing and 'exist_ok=True'  will not issue an error if the folder
        # already exists.
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._init_db()

    def _init_db(self):
        """Creates a table if it is not already created (Impotence)"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            # Creates a table logs, where we will store verdicts
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS experiment_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp DATETIME,
                    test_name TEXT,
                    p_value REAL,
                    lift REAL,          -- На сколько % группа B лучше A
                    is_significant INT  -- 1 (True) или 0 (False)
                )
            ''')
            conn.commit()

    def log_experiment(self, name: str, p_val: float, lift: float):
        """Records test result in database"""
        is_sig = 1 if p_val < 0.05 else 0
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO experiment_logs (timestamp, test_name, p_value, lift, is_significant)
                VALUES (?, ?, ?, ?, ?)
            ''', (datetime.now(), name, p_val, lift, is_sig))
            conn.commit()
            print(f"💾 [DB] Результат '{name}' успешно залогирован.")
