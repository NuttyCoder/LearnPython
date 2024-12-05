import scapy.all as scapy
import datetime
import sqlite3
import time
from threading import Thread
import socket
import netifaces

class NetworkMonitor:
    def __init__(self, db_path="network_data.db"):
        self.db_path = db_path
        self.setup_database()
        self.known_devices = {}
        
    def setup_database(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        # Create tables for devices and network events
        c.execute('''CREATE TABLE IF NOT EXISTS devices
                    (mac TEXT PRIMARY KEY, ip TEXT, hostname TEXT, 
                     first_seen TIMESTAMP, last_seen TIMESTAMP)''')
        
        c.execute('''CREATE TABLE IF NOT EXISTS events
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     mac TEXT, event_type TEXT, timestamp TIMESTAMP,
                     details TEXT)''')
        
        conn.commit()
        conn.close()
    
    def get_network_info(self):
        # Get default gateway interface
        gateways = netifaces.gateways()
        default_gateway = gateways['default'][netifaces.AF_INET][1]
        
        # Get interface IP and subnet
        interface_info = netifaces.ifaddresses(default_gateway)[netifaces.AF_INET][0]
        ip = interface_info['addr']
        netmask = interface_info['netmask']
        
        return f"{ip}/{self.netmask_to_cidr(netmask)}"
    
    @staticmethod
    def netmask_to_cidr(netmask):
        return sum([bin(int(x)).count('1') for x in netmask.split('.')])
    
    def scan_network(self):
        network = self.get_network_info()
        arp_request = scapy.ARP(pdst=network)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
        
        devices = []
        for element in answered_list:
            device = {
                'ip': element[1].psrc,
                'mac': element[1].hwsrc
            }
            try:
                device['hostname'] = socket.gethostbyaddr(device['ip'])[0]
            except:
                device['hostname'] = 'Unknown'
            devices.append(device)
        
        return devices
    
    def update_device_status(self, device):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        # Check if device exists
        c.execute("SELECT * FROM devices WHERE mac=?", (device['mac'],))
        existing_device = c.fetchone()
        
        current_time = datetime.datetime.now()
        
        if existing_device is None:
            # New device
            c.execute("""INSERT INTO devices (mac, ip, hostname, first_seen, last_seen)
                        VALUES (?, ?, ?, ?, ?)""",
                     (device['mac'], device['ip'], device['hostname'], 
                      current_time, current_time))
            
            self.log_event(c, device['mac'], 'NEW_DEVICE', 
                          f"New device discovered: {device['hostname']} ({device['ip']})")
        else:
            # Update existing device
            c.execute("""UPDATE devices 
                        SET ip=?, hostname=?, last_seen=?
                        WHERE mac=?""",
                     (device['ip'], device['hostname'], current_time, device['mac']))
        
        conn.commit()
        conn.close()
    
    def log_event(self, cursor, mac, event_type, details):
        cursor.execute("""INSERT INTO events (mac, event_type, timestamp, details)
                         VALUES (?, ?, ?, ?)""",
                      (mac, event_type, datetime.datetime.now(), details))
    
    def monitor_loop(self):
        while True:
            try:
                devices = self.scan_network()
                for device in devices:
                    self.update_device_status(device)
                time.sleep(60)  # Scan every minute
            except Exception as e:
                print(f"Error in monitor loop: {e}")
                time.sleep(5)
    
    def start_monitoring(self):
        monitor_thread = Thread(target=self.monitor_loop)
        monitor_thread.daemon = True
        monitor_thread.start()
        return monitor_thread

    def get_device_history(self, mac=None):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        if mac:
            c.execute("""SELECT devices.*, COUNT(events.id) as event_count
                        FROM devices 
                        LEFT JOIN events ON devices.mac = events.mac
                        WHERE devices.mac=?
                        GROUP BY devices.mac""", (mac,))
        else:
            c.execute("""SELECT devices.*, COUNT(events.id) as event_count
                        FROM devices 
                        LEFT JOIN events ON devices.mac = events.mac
                        GROUP BY devices.mac""")
        
        results = c.fetchall()
        conn.close()
        return results

if __name__ == "__main__":
    monitor = NetworkMonitor()
    monitor_thread = monitor.start_monitoring()
    
    try:
        while True:
            print("\nCurrent network status:")
            for device in monitor.get_device_history():
                print(f"MAC: {device[0]}")
                print(f"IP: {device[1]}")
                print(f"Hostname: {device[2]}")
                print(f"First seen: {device[3]}")
                print(f"Last seen: {device[4]}")
                print(f"Event count: {device[5]}")
                print("-" * 50)
            time.sleep(300)  # Update display every 5 minutes
    except KeyboardInterrupt:
        print("\nStopping network monitor...")
