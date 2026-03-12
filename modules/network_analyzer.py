from scapy.all import rdpcap
from database.db_manager import DBManager
from config import PCAP_FILE

db = DBManager()

def analyze_pcap():

    try:

        packets = rdpcap(PCAP_FILE)

        for pkt in packets:

            if pkt.haslayer("IP"):

                src = pkt["IP"].src
                dst = pkt["IP"].dst
                proto = pkt["IP"].proto
                length = len(pkt)

                db.insert(
                "INSERT INTO network(src_ip,dst_ip,protocol,length) VALUES(?,?,?,?)",
                (src,dst,str(proto),length))

    except:
        pass