import argparse
import os


def parse_option():
	parser = argparse.ArgumentParser('get twitter image', add_help=False)
	parser.add_argument('--consumer_key', type=str, default="******", help='consumer key')
	parser.add_argument('--consumer_secret', type=str, default="******", help='consumer secret')
	parser.add_argument('--access_token_key', type=str, default="******", help='access token key')
	parser.add_argument('--access_token_secret', type=str, default="******", help='access token secret')
	parser.add_argument('--output_dir', type=str, default="./sample", help='path to config file')
	parser.add_argument('--image_dir', type=str, default="image_dir", help='path to config file')
	parser.add_argument('--sample_file', type=str, default="sample.csv", help='path to config file')
	parser.add_argument("--class_txt", type=str, default="./imagenet1000_clsidx_to_labels.txt", help="search name")
	parser.add_argument("--search_name", type=str, default="French bulldog", help="search name")
	parser.add_argument("--batch_size", type=int, default=1, help="search name")
	parser.add_argument("--search_pages_number", type=int, default=20, help="search pages number")
	parser.add_argument("--per_page_number", type=int, default=10, help="per pages number")
	args, _ = parser.parse_known_args()
	return args

def config(args):

	args.image_dir = os.path.join(args.output_dir, args.search_name, args.image_dir)
	args.sample_file = os.path.join(args.output_dir, args.search_name, args.sample_file)
	os.makedirs(args.image_dir, exist_ok=True)

	return args