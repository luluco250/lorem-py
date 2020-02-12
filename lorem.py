import argparse, random

WORDS = [
	"consequat", "congue", "arcu", "culpa", "varius", "ut", "luctus",
	"pharetra", "etiam", "sed", "dictumst", "eu", "neque", "excepteur",
	"nullam", "id", "est", "laoreet", "ea", "tempor", "elit", "aute", "tellus",
	"quis", "quam", "aliquet", "platea", "sunt", "velit", "ac", "mollis",
	"integer", "nisl", "labore", "maecenas", "sem", "aliqua", "lobortis",
	"augue", "minim", "gravida", "magna", "lacus", "vehicula", "qui",
	"tincidunt", "faucibus", "enim", "nulla", "eiusmod", "sollicitudin",
	"bibendum", "nostrud", "malesuada", "felis", "nec", "eros", "cillum",
	"cupidatat", "in", "dolore", "mi", "anim", "cras", "laborum", "nunc",
	"lorem", "ullamco", "consectetur", "nibh", "fermentum", "et", "occaecat",
	"a", "risus", "nisi", "scelerisque", "veniam", "pellentesque", "diam",
	"laboris", "odio", "ex", "fugiat", "pariatur", "curabitur", "euismod",
	"ipsum", "duis", "ad", "commodo", "dolor", "sapien", "donec", "aliquam",
	"officia", "feugiat", "aliquip", "pretium", "eget", "hac", "adipiscing",
	"esse", "do", "sit", "habitasse", "sint", "turpis", "voluptate", "orci",
	"reprehenderit", "incididunt", "deserunt", "aenean", "erat", "proident",
	"ullamcorper", "irure", "vulputate", "non", "dictum", "amet", "ligula",
	"mollit", "molestie", "dapibus", "mauris", "exercitation"
]

def main():
	args = parse_args()

	for i in range(args.line_count):
		print(" ".join(random.choices(WORDS, k=args.word_count)).capitalize() + ".")

def parse_args():
	parser = argparse.ArgumentParser(description="A lorem ipsum generator.")

	parser.add_argument("-w", "--word-count", type=int, default=random.randint(7, 13))
	parser.add_argument("-l", "--line-count", type=int, default=1)

	return parser.parse_args()

if __name__ == "__main__": main()