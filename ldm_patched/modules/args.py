import argparse



parser = argparse.ArgumentParser()

parser.add_argument("--cuda-malloc", action="store_true")
parser.add_argument("--cuda-stream", action="store_true")
parser.add_argument("--pin-shared-memory", action="store_true")

args = parser.parse_known_args()[0]


cuda_stream = args.cuda_stream
