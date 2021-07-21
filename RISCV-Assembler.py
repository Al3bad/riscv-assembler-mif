# To setup the virtual environment
# execute: py -3 -m venv .venv
# then   : .venv\scripts\activate

# To install packages
# execute: python -m pip install <package-name>

# To deactivate the virtual environment
# execute: deactivate
# ==================================

import argparse
import os.path
from riscv_assembler.convert import AssemblyConverter

WIDTH = 32
DEPTH = 256

parser = argparse.ArgumentParser(description='Conver RISC-V instruction to machine code')
parser.add_argument("--src", type=str)

args = parser.parse_args()

if not args.src:
    raise Exception("Please provide the input file for the instructions using '--src' option.")

if not os.path.isfile(args.src):
    raise Exception("There is not file with this name in this directory.")

cnv = AssemblyConverter(output_type="-", filename=args.src, hexMode=True)
machineCode = cnv.convert(args.src)
lines = machineCode.split("\n")
numOfLines = len(lines) - 1

f = open("program.mif", "w")

f.write("WIDTH=%d;\n" % (WIDTH))
f.write("DEPTH=%d;\n" % (DEPTH))
f.write("ADDRESS_RADIX=HEX;\n")
f.write("DATA_RADIX=HEX;\n\n")
f.write("CONTENT BEGIN\n")

for i in range(numOfLines):
    address     = hex(i).split("x")[1]
    instruction = lines[i].split("x")[1]
    f.write("\t%s : %s;\n" % (address, instruction))

if numOfLines != DEPTH:
    f.write("\t[%s..%s] : 000000;\n" % (hex(numOfLines).split("x")[1], hex(DEPTH - 1).split("x")[1]))

f.write("END;\n")
f.close()

