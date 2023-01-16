import sys
import argparse
from traceroute import Traceroute

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('destination_server')
    parser.add_argument('-c', '--count', required=False, nargs='?', default=3, type=int, metavar='Count of packets')
    parser.add_argument('-t', '--timeout', required=False, nargs='?', default=1000, type=int, metavar='Timeout in ms')
    parser.add_argument('-m', '--maxhops', required=False, nargs='?', default=64, type=int, metavar='Max hops')
    parser.add_argument('-p', '--packet_size', required=False, nargs='?', default=55, type=int, metavar='Packet size in bytes')

    return parser


def traceroute(destination_server, count_of_packets=3, packet_size=52, max_hops=64, timeout=1000):
    t = Traceroute(destination_server, count_of_packets, packet_size, max_hops, timeout)
    t.start_traceroute()

def main():
    parser = create_parser()
    args = parser.parse_args(sys.argv[1:])
    destination_server = args.destination_server
    timeout = args.timeout
    packet_size = args.packet_size
    count = args.count
    max_hops = args.maxhops
    traceroute(destination_server, count, packet_size, max_hops, timeout)

if __name__ == '__main__':
    main()