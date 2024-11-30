import psutil
import time
import sqlite3
from datetime import datetime, timedelta
import platform
import subprocess

class InternetUsageTracker:
    def __init__(self, children):
        """
        Initialize the Internet Usage Tracker
        
        :param children: List of children's names to track
        """
        self.children = children
        # Initialize database connection
        self.conn = sqlite3.connect('internet_usage.db')
        self.create_database()
    
    def create_database(self):
        """
        Create SQLite database to store internet usage data
        """
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usage_log (
                id INTEGER PRIMARY KEY,
                child_name TEXT,
                start_time DATETIME,
                end_time DATETIME,
                duration INTEGER,
                total_bytes_sent INTEGER,
                total_bytes_recv INTEGER,
                website TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS daily_limits (
                child_name TEXT PRIMARY KEY,
                daily_limit_minutes INTEGER
            )
        ''')
        self.conn.commit()
    
    def set_daily_limit(self, child_name, limit_minutes):
        """
        Set daily internet usage limit for a child
        
        :param child_name: Name of the child
        :param limit_minutes: Maximum allowed internet time per day
        """
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO daily_limits (child_name, daily_limit_minutes)
            VALUES (?, ?)
        ''', (child_name, limit_minutes))
        self.conn.commit()
    
    def get_network_usage(self):
        """
        Retrieve current network usage statistics
        
        :return: Dictionary of network statistics
        """
        net_io = psutil.net_io_counters()
        return {
            'bytes_sent': net_io.bytes_sent,
            'bytes_recv': net_io.bytes_recv
        }
    
    def track_usage(self, child_name, duration=60):
        """
        Track internet usage for a specific child
        
        :param child_name: Name of the child being tracked
        :param duration: Tracking duration in seconds
        """
        start_time = datetime.now()
        start_usage = self.get_network_usage()
        
        # Sleep for specified duration
        time.sleep(duration)
        
        end_time = datetime.now()
        end_usage = self.get_network_usage()
        
        # Calculate network usage
        bytes_sent = end_usage['bytes_sent'] - start_usage['bytes_sent']
        bytes_recv = end_usage['bytes_recv'] - start_usage['bytes_recv']
        
        # Log usage to database
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO usage_log 
            (child_name, start_time, end_time, duration, total_bytes_sent, total_bytes_recv)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (child_name, start_time, end_time, duration, bytes_sent, bytes_recv))
        self.conn.commit()
    
    def check_daily_limit(self, child_name):
        """
        Check if child has exceeded daily internet usage limit
        
        :param child_name: Name of the child
        :return: Boolean indicating if limit is exceeded
        """
        cursor = self.conn.cursor()
        # Get daily limit
        cursor.execute('SELECT daily_limit_minutes FROM daily_limits WHERE child_name = ?', (child_name,))
        limit = cursor.fetchone()
        
        if not limit:
            return False
        
        # Calculate total usage for today
        today = datetime.now().date()
        cursor.execute('''
            SELECT SUM(duration) 
            FROM usage_log 
            WHERE child_name = ? AND date(start_time) = ?
        ''', (child_name, today))
        
        total_usage = cursor.fetchone()[0] or 0
        return total_usage > (limit[0] * 60)  # Convert minutes to seconds
    
    def generate_report(self, child_name, days=7):
        """
        Generate usage report for a child
        
        :param child_name: Name of the child
        :param days: Number of days to include in report
        :return: Dictionary with usage statistics
        """
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT 
                SUM(duration) as total_time,
                SUM(total_bytes_sent + total_bytes_recv) as total_data
            FROM usage_log
            WHERE child_name = ? AND start_time >= date('now', ?)
        ''', (child_name, f'-{days} days'))
        
        report = cursor.fetchone()
        return {
            'total_time_seconds': report[0] or 0,
            'total_data_bytes': report[1] or 0
        }
    
    def close(self):
        """
        Close database connection
        """
        self.conn.close()

def main():
    # Example usage
    tracker = InternetUsageTracker(['Alice', 'Bob'])
    
    # Set daily limits
    tracker.set_daily_limit('Alice', 120)  # 2 hours
    tracker.set_daily_limit('Bob', 90)     # 1.5 hours
    
    # Track usage for Alice
    tracker.track_usage('Alice', duration=300)  # 5 minutes tracking
    
    # Check if daily limit is exceeded
    if tracker.check_daily_limit('Alice'):
        print("Alice has exceeded her daily internet limit!")
    
    # Generate report
    report = tracker.generate_report('Alice')
    print(f"Alice's 7-day usage: {report['total_time_seconds']/60:.2f} minutes")
    
    tracker.close()

if __name__ == '__main__':
    main()
