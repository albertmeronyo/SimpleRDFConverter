#!/usr/bin/env python

from rdflib import Graph
import argparse

# Argument parsing

parser = argparse.ArgumentParser(description="Converts the RDF input file to the specified serialization format.")
parser.add_argument('--input', '-i',
                    help = "Input RDF file", 
                    required = True)
parser.add_argument('--input-format', '-if',
                    help = "Serialization format of the input file",
                    choices = ['html', 'hturtle', 'mdata', 'microdata', 'n3', 'nquads', 'nt', 'rdfa', 'rdfa1.0', 'rdfa1.1', 'trix', 'turtle', 'xml'],
                    required = True)
parser.add_argument('--output', '-o',
                    help = "Output RDF file", 
                    required = True)
parser.add_argument('--output-format', '-of',
                    help = "Serialization format of the output file",
                    choices = ['html', 'hturtle', 'mdata', 'microdata', 'n3', 'nquads', 'nt', 'rdfa', 'rdfa1.0', 'rdfa1.1', 'trix', 'turtle', 'xml'],
                    required = True)

args = parser.parse_args()

g = Graph()
g.parse(args.input, format = args.input_format)
g.serialize(args.output, format = args.output_format)
