SimpleRDFConverter
==================

A simple, command-line, RDFLib based RDF serialization format converter

**Author**: [Albert Meroño-Peñuela](https://github.com/albertmeronyo)

## Usage

`./simpleRDFConverter.py -i inputfile -if inputfileformat -o outputfile -of outputfileformat`

e.g. to convert an OWL/XML file to an N-Triples file

`./simpleRDFConverter.py -i myontology.owl -if xml -o myontology.nt -of nt`

Parameters:
- `--input / -i` to specify the input RDF file
- `--input-format / -if` to specify the serialization format of the input file
- `--output / -o` to specify the output RDF file
- `--output-format / -of` to specify the serialization format of the output file
- `--help / -h` to display usage info

## Dependencies

Python 2.7.5, RDFLib 4.1.0