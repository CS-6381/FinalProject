import pyshark
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--interface", default="s1-eth1")
parser.add_argument("--net_size", default=1)
parser.add_argument("--sample_size", "--samples", default=500)

args = parser.parse_args()
intf = args.interface
sample_size = int(args.sample_size)
net_size = int(args.net_size)


def capture_and_plot(intf):
    print(f"begining live capture on {intf}")

    capture = pyshark.LiveCapture(interface=intf)
    packet_map = {}
    for packet in capture.sniff_continuously(packet_count=sample_size):
        # print(packet)

        if "ip" not in packet or "tcp" not in packet:
            continue

        ip = packet.ip
        tcp = packet.tcp

        port = tcp.dstport

        # Filter for traffic in the appropriate port-range of the given Pub/Sub server
        # try:
        #     port = int(port)
        #     if port > 5600:
        #         continue
        # except Exception:
        #     continue

        src = ip.src
        dst = ip.dst

        flags = tcp.flags
        time_delta = tcp.time_delta

        # Store time data for given connection identifier
        key = f'{src}/{dst}:{port}'
        if key in packet_map:
            data_points = packet_map[key]
            data_points.append(float(time_delta))
        else:
            data_points = [float(time_delta), ]
            packet_map[key] = data_points

        # Contents can be printed to file instead of stored in memory for plotting data...
        # print( f' source: {src} dest: {dst} port: {port} time_lapse(RTT):{time_delta} flags:{flags}')
        # print(f'{src}|{dest}|{port}|{time_delta|{flags}')
        # print(f'{src},{dest},{port},{time_delta,{flags}')

    map_len = len(packet_map)
    fig, axs = plt.subplots(map_len)
    fig.suptitle('RTTs (round trip time) of Packets')

    i = 0
    for k, v in packet_map.items():
        if map_len > 1:
            axs[i].plot(range(len(v)), v)
            axs[i].set_title(f'(src/dest:port) - {k}')
            axs[i].set_ylabel("Delta Time (Pub - Sub)")
            axs[i].set_xlabel("Number of Samples")
        else:
            axs.plot(range(len(v)), v)
            axs.set_title(f'(src/dest:port) - {k}')
            axs.set_ylabel("Delta Time (Pub - Sub)")
            axs.set_xlabel("Number of Samples")

        i = i+1
    plt.show()

# not in use.. attempting parallel Matplots to no avail.
# p = Pool(net_size)
# with p:
#     p.map(capture_and_plot, range(net_size))

# Run capture either over single Interface, or range
if net_size == 1:
    capture_and_plot(intf)
else:
    for i in range(net_size):
        intf = f"s1-eth{i+1}"
        capture_and_plot(intf)

plt.show()