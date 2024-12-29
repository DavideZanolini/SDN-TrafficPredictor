import csv
import os
from scapy.all import rdpcap

# Define the output CSV file
output_csv = 'output.csv'

# Open the CSV file for writing
with open(output_csv, mode='w', newline='') as csv_file:
    fieldnames = ['timestamp', 'src_ip', 'dst_ip', 'protocol']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Process each pcap file in the extracted folder
    for root, dirs, files in os.walk('extracted_files'):
        for file in files:
            if file.endswith('.pcap'):
                pcap_file = os.path.join(root, file)
                packets = rdpcap(pcap_file)
                for packet in packets:
                    if packet.haslayer('IP'):
                        timestamp = packet.time
                        src_ip = packet['IP'].src
                        dst_ip = packet['IP'].dst
                        protocol = packet['IP'].proto
                        # Write the data to the CSV file
                        writer.writerow({
                            'timestamp': timestamp,
                            'src_ip': src_ip,
                            'dst_ip': dst_ip,
                            'protocol': protocol
                        })