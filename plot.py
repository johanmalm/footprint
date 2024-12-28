#!/usr/bin/env python3

import argparse
import sys
import matplotlib.pyplot as plt

class Graph():
    def __init__(self):
        """
        blame_lines will become something like this for labwc:
        {
            'Johan Malm': [],
            'Consolatis': [],
        }
        """
        self.refs = []
        self.blame_lines = dict()

    def add_ref(self, ref):
        self.refs.append(ref)

    def add_blame_lines(self, who, nr_lines):
        if who not in self.blame_lines:
            if self.blame_lines:
                # When adding new users we need to pad out with zeros for all the refs
                # for which they had not yet contributed
                size = max(len(v) for v in self.blame_lines.values()) - 1
                self.blame_lines[who] = [0] * size
            else:
                self.blame_lines[who] = list()
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
        # -1 to reverse; 15 to show top 15 entries
        self.blame_lines = dict((k, v) for _, k, v in sorted((sum(v), k, v) for k, v in self.blame_lines.items())[::-1][:15])
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
