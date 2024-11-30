import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog
import psutil
import time
import sqlite3
from datetime import datetime, timedelta
import threading
import logging
import subprocess
import platform
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import re
import socket
import ipaddress
import json

# Machine Learning Libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

# Network and Geolocation Libraries
import geoip2.database
import dns.resolver
import netifaces

class AdvancedInternetUsageTracker:
    def __init__(self, master):
        """
        Initialize the advanced application with enhanced tracking
        """
        self.master = master
        master.title("Advanced Intelligent Internet Usage Tracker")
        master.geometry("1200x900")
        master.configure(bg='#f0f0f0')

        # Enhanced database setup
        self.conn = sqlite3.connect('intelligent_internet_usage.db', check_same_thread=False)
        self.create_advanced_database()

        # Logging configuration
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s',
            handlers=[
                logging.FileHandler('intelligent_tracker.log'),
                logging.StreamHandler()
            ]
        )

        # Machine Learning Classifiers
        self.website_classifier = self.train_website_classifier()
        self.device_fingerprint_db = {}

        # Geolocation and Network Tracking
        try:
            self.geoip_reader = geoip2.database.Reader('GeoLite2-Country.mmdb')
        except Exception as e:
            logging.warning(f"Geolocation database not found: {e}")
            self.geoip_reader = None

        # Advanced tracking configurations
        self.tracking_config = {
            'network_interfaces': self.get_network_interfaces(),
            'vpn_detection': True,
            'device_tracking': True
        }

        # Initialize UI
        self.create_advanced_ui()

    def create_advanced_database(self):
        """
        Create an enhanced database schema with additional tracking tables
        """
        cursor = self.conn.cursor()
        
        # Enhanced children table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS children (
                name TEXT PRIMARY KEY,
                daily_limit INTEGER,
                email TEXT,
                phone TEXT,
                device_fingerprint TEXT
            )
        ''')
        
        # Comprehensive network and location tracking
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS network_log (
                id INTEGER PRIMARY KEY,
                child_name TEXT,
                timestamp DATETIME,
                ip_address TEXT,
                country TEXT,
                network_interface TEXT,
                is_vpn BOOLEAN,
                total_bandwidth INTEGER
            )
        ''')
        
        # Machine learning enhanced website categorization
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS website_classification (
                domain TEXT PRIMARY KEY,
                primary_category TEXT,
                confidence REAL,
                last_updated DATETIME
            )
        ''')
        
        # Threat and anomaly detection log
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS security_log (
                id INTEGER PRIMARY KEY,
                child_name TEXT,
                timestamp DATETIME,
                event_type TEXT,
                description TEXT,
                severity INTEGER
            )
        ''')
        
        self.conn.commit()

    def train_website_classifier(self):
        """
        Train a machine learning model for website categorization
        """
        # Sample training data (you'd want a much larger dataset in real-world)
        websites = [
            ("facebook.com", "Social Media"),
            ("youtube.com", "Video"),
            ("wikipedia.org", "Educational"),
            ("netflix.com", "Entertainment"),
            ("github.com", "Programming"),
            # More training data would be added here
        ]
        
        domains, categories = zip(*websites)
        
        # Prepare features
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(domains)
        
        # Train classifier
        classifier = MultinomialNB()
        classifier.fit(X, categories)
        
        return {
            'vectorizer': vectorizer,
            'classifier': classifier
        }

    def classify_website(self, domain):
        """
        Classify website using machine learning
        """
        try:
            vectorized_domain = self.website_classifier['vectorizer'].transform([domain])
            prediction = self.website_classifier['classifier'].predict(vectorized_domain)
            confidence = self.website_classifier['classifier'].predict_proba(vectorized_domain).max()
            
            # Store classification
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT OR REPLACE INTO website_classification 
                (domain, primary_category, confidence, last_updated)
                VALUES (?, ?, ?, ?)
            ''', (domain, prediction[0], confidence, datetime.now()))
            self.conn.commit()
            
            return prediction[0], confidence
        except Exception as e:
            logging.error(f"Website classification error: {e}")
            return "Uncategorized", 0.5

    def get_network_interfaces(self):
        """
        Detect and return network interfaces
        """
        try:
            return netifaces.interfaces()
        except Exception as e:
            logging.error(f"Network interface detection error: {e}")
            return []

    def detect_vpn(self, ip_address):
        """
        Detect potential VPN usage
        """
        try:
            # Check against known VPN IP ranges or services
            vpn_indicators = [
                'digitalocean.com',
                'aws.amazon.com',
                'azure.microsoft.com'
            ]
            
            # Resolve IP to hostname
            hostname = socket.gethostbyaddr(ip_address)[0]
            
            return any(indicator in hostname for indicator in vpn_indicators)
        except Exception:
            return False

    def log_network_activity(self, child_name, ip_address):
        """
        Log comprehensive network activity
        """
        try:
            # Geolocation detection
            country = "Unknown"
            if self.geoip_reader:
                try:
                    response = self.geoip_reader.country(ip_address)
                    country = response.country.name
                except Exception:
                    pass

            # VPN Detection
            is_vpn = self.detect_vpn(ip_address)

            # Network interface
            network_interface = netifaces.gateways()['default'][netifaces.AF_INET][1]

            # Bandwidth calculation
            net_io = psutil.net_io_counters()
            total_bandwidth = net_io.bytes_sent + net_io.bytes_recv

            # Log to database
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO network_log 
                (child_name, timestamp, ip_address, country, 
                network_interface, is_vpn, total_bandwidth)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                child_name, datetime.now(), ip_address, country, 
                network_interface, is_vpn, total_bandwidth
            ))
            self.conn.commit()

            # Potential security event logging
            if is_vpn:
                self.log_security_event(
                    child_name, 
                    "VPN Detection", 
                    f"Potential VPN usage detected from {ip_address}", 
                    severity=3
                )

        except Exception as e:
            logging.error(f"Network activity logging error: {e}")

    def log_security_event(self, child_name, event_type, description, severity=1):
        """
        Log potential security events or anomalies
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO security_log 
                (child_name, timestamp, event_type, description, severity)
                VALUES (?, ?, ?, ?, ?)
            ''', (child_name, datetime.now(), event_type, description, severity))
            self.conn.commit()
        except Exception as e:
            logging.error(f"Security event logging error: {e}")

    def advanced_tracking_report(self):
        """
        Generate a comprehensive tracking report
        """
        report = {
            'total_network_events': 0,
            'vpn_events': 0,
            'countries_accessed': set(),
            'security_events': []
        }

        try:
            cursor = self.conn.cursor()
            
            # Network events
            cursor.execute('SELECT COUNT(*) FROM network_log')
            report['total_network_events'] = cursor.fetchone()[0]

            # VPN events
            cursor.execute('SELECT COUNT(*) FROM network_log WHERE is_vpn = 1')
            report['vpn_events'] = cursor.fetchone()[0]

            # Countries accessed
            cursor.execute('SELECT DISTINCT country FROM network_log')
            report['countries_accessed'] = {row[0] for row in cursor.fetchall()}

            # Security events
            cursor.execute('SELECT * FROM security_log ORDER BY severity DESC LIMIT 10')
            report['security_events'] = cursor.fetchall()

        except Exception as e:
            logging.error(f"Report generation error: {e}")

        return report

def main():
    root = tk.Tk()
    app = AdvancedInternetUsageTracker(root)
    root.mainloop()

if __name__ == '__main__':
    main()
