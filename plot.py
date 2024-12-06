#!/usr/bin/env python3

import argparse
import sys
import matplotlib.pyplot as plt

class Graph():
    def __init__(self):
        self.refs = []
        self.blame_lines = {
            'Johan Malm': [],
            'ARDiDo': [],
            'bi4k8': [],
            'Joshua Ashton': [],
            'Consolatis': [],
            'John Lindgren': [],
            'Consus': [],
            'Ph42oN': [],
            'Tomi Ollila': [],
            'tokyo4j': [],
            'Hiroaki Yamamoto': [],
            'Andrew J. Hesford': [],
            'Jens Peters': [],
            'Simon Long': [],
            'Christopher Snowhill': [],
            'David Turner': [],
            'Tobias Bengfort': [],
            'droc12345': [],
            'Orfeas': [],
        }

    def add_ref(self, ref):
        self.refs.append(ref)

    def add_blame_lines(self, who, nr_lines):
        if who in self.blame_lines:
            self.blame_lines[who].append(int(nr_lines))

    def add_zeros_for_dormant_contributors(self):
        """
        All data series have to be the same length, so if a contributor did not
        have any tally against a particular ref, we just add a 0
        """
        for _, i in self.blame_lines.items():
            if len(i) != len(self.refs):
                i.append(0)

    def plot(self):
        _, ax = plt.subplots()
        ax.stackplot(self.refs, self.blame_lines.values(),
            labels=self.blame_lines.keys(), alpha=0.8)
        ax.legend(loc='upper left', reverse=True)
        ax.set_title('Footprint')
        ax.set_xlabel('Ref')
        ax.set_ylabel('Count in src/ and incluce/')
        plt.show()

    def debug(self):
        print(self.refs)
        print(self.blame_lines)

def main():
    """ main """
    parser = argparse.ArgumentParser(prog="plot.py")
    parser.add_argument("--tags", help="tags")
    parser.add_argument("--debug", help="debug", action='store_true')
    args = parser.parse_args()

    if args.tags is None:
        parser.print_help(sys.stderr)
        sys.exit(1)

    print('Generating graph...')
    graph = Graph()

    tags = args.tags.split(' ')
    for t in tags[::-1]:
        graph.add_ref(t)
        with open('.cache/' + t, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
        for line in lines:
            parts = line.split(maxsplit=2)
            graph.add_blame_lines(parts[2], parts[0])
        graph.add_zeros_for_dormant_contributors()

    if args.debug:
        graph.debug()
    graph.plot()

if __name__ == '__main__':
    main()
