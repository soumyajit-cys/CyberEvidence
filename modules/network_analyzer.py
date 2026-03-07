from scapy.all import rdpcap
from database.db_manager import DBManager

db = DBManager()

def analyze_pcap(file):

    packets = rdpcap(file)

    for pkt in packets:

        try:
            src = pkt[0][1].src
            dst = pkt[0][1].dst
            proto = pkt[0][1].name
            length = len(pkt)

            db.insert_network((src,dst,proto,length))

        except:
            continue