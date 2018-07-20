from scapy import *

def main():
    """
    """
    packet = IP(dst="192.168.100.123")/TCP()/"from scapy packet"
    send(packet)


def packet_with_seq_n():
    packet = IP(dst="192.168.100.123", src="192.168.100.144")/TCP(sport=333, dport=222, seq=112344)/"Sequence number 112344"
    send(packet)
    # we can use sendp to choose different network interface
    sendp(packet, iface="lo")
    # lsc() can see functions descriptions.

if __name__ == "__main__":
    main()
    packet_with_seq_n()
