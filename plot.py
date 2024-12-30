#!/usr/bin/env python3

import argparse
import sys
import matplotlib.pyplot as plt
import os

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
        who = {
            'Hiroaki Yamamoto': 'tokyo4j',
            'Simon Ser': 'emersion',
        }.get(who, who)

        if who not in self.blame_lines:
            # When adding new users we need to pad out with zeros
            # for all the refs for which they had not yet contributed
            self.blame_lines[who] = [0] * (len(self.refs) - 1)

        if len(self.blame_lines[who]) == len(self.refs):
            # Multiple aliases have ownership within this tag
            self.blame_lines[who][-1] += int(nr_lines)
        else:
            self.blame_lines[who].append(int(nr_lines))

    def add_zeros_for_dormant_contributors(self):
        """
        All data series have to be the same length, so if a contributor did not
        have any tally against a particular ref, we just add a 0
        """
        for i in self.blame_lines.values():
            if len(i) != len(self.refs):
                i.append(0)

    def plot(self):
        # -1 to reverse; 15 to show top 15 entries
        blame_lines = dict((k, v) for _, k, v in sorted((sum(v), k, v) for k, v in self.blame_lines.items())[::-1][:15])
        #blame_lines = dict(sorted(self.blame_lines.items(), key=lambda kv : sum(kv[1]))[::-1][:15])
        _, ax = plt.subplots()
        ax.stackplot(self.refs, blame_lines.values(),
            labels=blame_lines.keys(), alpha=0.8)
        ax.legend(loc='upper left', reverse=True)
        ax.set_title('Footprint')
        ax.set_xlabel('Ref')
        ax.set_ylabel('Count in src/ and incluce/')
        plt.show()

    def plot_shell(self):
        blame_lines = dict(
            sorted(self.blame_lines.items(),
                # sort by contributions to the last tag, favors current devs
                #key=lambda kv : kv[1][-1],
                # sort by sum of contributions over all tags, favors early devs
                key=lambda kv : sum(kv[1]),
                reverse=True
            )[:35]
        )
        print()
        print(f'  \x1b[1m{"Author":<25s} ' + ' '.join(f'{tag:>6s}' for tag in self.refs) + '\x1b[m')
        print(f'  {"":-<25s} ' + ' '.join(f'{"":->6s}' for _ in self.refs))
        for name, values in blame_lines.items():
            print(f'  {name:<25s} ' + ' '.join(f'{val:>6d}' for val in values))
        print()

    def debug(self):
        print(self.refs)
        print(self.blame_lines)

def main():
    """ main """
    parser = argparse.ArgumentParser(prog="plot.py")
    parser.add_argument("--tags", help="tags")
    parser.add_argument("--debug", help="debug", action='store_true')
    parser.add_argument("--shell-plot", help="shell-plot", action='store_true')
    args = parser.parse_args()

    if args.tags is None:
        parser.print_help(sys.stderr)
        sys.exit(1)

    graph = Graph()

    tags = args.tags.split(' ')
    for t in sorted(tags[::-1]):
        if not t:
            continue
        graph.add_ref(t)
        cache_dir = os.getenv("CACHE_DIR")
        with open(cache_dir + '/' + t, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
        for line in lines:
            parts = line.split(maxsplit=2)
            graph.add_blame_lines(parts[2], parts[0])
        graph.add_zeros_for_dormant_contributors()

    if args.debug:
        graph.debug()
    if args.shell_plot:
        graph.plot_shell()
    else:
        graph.plot()

if __name__ == '__main__':
    main()
