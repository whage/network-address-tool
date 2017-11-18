A tiny command line utility for querying IP addresses of the host machine.

To run, just execute the main script:  
`./get-ips`

Supported flags:
- `--with-prefix`: prints addressess with CIDR notation
- `--overlapping`: prints overlapping pairs of addresses, each pair separated by an empty line

Tested with:
- python 3.5.2  
- pip 9.0.1

To run tests:
- install nosetests: `pip install nose`
- run `./testrunner` in the root dir of this package