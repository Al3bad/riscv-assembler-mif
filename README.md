# RISCV Assembler

This project converts the base 32-bit RISCV instructions set into machine code in .mif file format that can be used in Intel Quartus Prime software

> NOTE: This project is still under development and it was only tested on Windows OS using git bash as the command-line

## Project setup

- Create & active the virtual environment:

```bash
# Create the virutal environement
py -3 -m venv .venv
# Activate the virtual environement (should be executed only in git bash)
source .venv\scripts\activate
```

- Install the dependencies:

```bash
pip install -r requirements.txt
```

- Copy `py-files/convert.py` to `.venv/Lib/site-packages/riscv_assembler` folder. You can either do it through the file explorer or running this command from the root of the project:

```bash
cp -f py-files/conver.py .venv/Lib/site-packages/riscv_assembler/.
```

## Usage

```bash
python RISCV-Assembler.py --src RISCV-INSTRUCTIONS
```

where `RISCV-INSTRUCTION` is the file where the actual instructions are written, and the file extension must be `.s`.

- Example:

If we have RISCV instructions written in this file called `code.s` with the following content:

```asm
addi x1, x0, 7
nop
nop
add  x2, x1, x0
nop
nop
beq  x1, x2, shift
addi  x2, x1, 3
nop
nop
shift:
slli x3, x2, 1
nop
nop
```

And we run this command:

```bash
python RISCV-Assembler.py --src code.s
```

A file will be generated called `program.mif` with the following content:

```txt
WIDTH=32;
DEPTH=256;
ADDRESS_RADIX=HEX;
DATA_RADIX=HEX;

CONTENT BEGIN
	0 : 00700093;
	1 : 00000013;
	2 : 00000013;
	3 : 00008133;
	4 : 00000013;
	5 : 00000013;
	6 : 00208863;
	7 : 00308113;
	8 : 00000013;
	9 : 00000013;
	a : 00111193;
	b : 00000013;
	c : 00000013;
	[0xd..0xff] : 000000;
END;
```

## Build & package this project

You can create executable file by simply run this command (ONLY IN GIT BASH):

```bash
./build.sh
```

The generated executable file can be found in `dist` folder. You should now be able to use this `.exe` file anywhere in your system.

## Credit

This project is based on [riscv-assembler package](https://github.com/kcelebi/riscv-assembler)
