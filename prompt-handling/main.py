from models import PC

import argparse

def main():
    parser = argparse.ArgumentParser(description="Handle memory and CPU flags")
    parser.add_argument("--ram", type=int, help="Specify memory in MB")
    parser.add_argument("--price", type=int, help="Cost in USD")
    parser.add_argument("--memory", type=int, help="Specify memory in MB")
    parser.add_argument("--cpu", type=int, help="Specify number of CPU cores")
    parser.add_argument("--gpu-series", type=int, help="GPU series from Nvidia (i.e. 3070, 3080, etc.)")

    args = parser.parse_args()
    if args.gpu_series:
        gpu = f"NVIDIA {args.gpu_series}"
    my_pc = PC(args.cpu, args.ram, args.memory, args.price, args.gpu_series)

if __name__ == "__main__":
    main()