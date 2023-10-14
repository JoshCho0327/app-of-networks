# Plots results for input file of form
# event_number  queue_len   dropped_packets

import sys
import argparse
#import matplotlib
#import matplotlib.pyplot as plt
#import matplotlib.dates as mdates
from matplotlib import pyplot as plt 
from matplotlib import dates as mdates


def get_args(argv):
    parser = argparse.ArgumentParser(description="Program for plotting simulator results")
    parser.add_argument('-i', '--input-file', required=True)
    parser.add_argument('-o', '--output-file', required=True)
    parser.add_argument('-t', '--title', required=False)
    return parser.parse_args()

def main(argv):
    args = get_args(argv)

    # Read points from file
    event_seq_points = []
    queue_len_points = []
    dropped_count_points = []
    with open(args.input_file, 'r') as f:
        for line in f:
            parts = line.split()
            event_seq = int(parts[0])
            pkt_in_q = int(parts[1])
            pkt_dropped = int(parts[2])
            event_seq_points.append(event_seq)
            queue_len_points.append(pkt_in_q)
            dropped_count_points.append(pkt_dropped)

    # Create plot
    plt.plot(event_seq_points, queue_len_points, label = "Packets in the queue")
    plt.plot(event_seq_points, dropped_count_points, label = "Packets dropped from the queue", linewidth = 5, linestyle='--', color = 'r')
    plt.legend()
    if args.title:
        plt.title(args.title)
    plt.savefig(args.output_file)

if __name__ == "__main__":
    main(sys.argv[1:])
