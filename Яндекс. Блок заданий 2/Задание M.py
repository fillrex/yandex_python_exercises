elf = int(input())
dwarf = int(input())
man = int(input())

elf_1 = elf // 10
elf_2 = elf % 10

dwarf_1 = dwarf // 10
dwarf_2 = dwarf % 10

man_1 = man // 10
man_2 = man % 10

if elf_1 == dwarf_1 and dwarf_1 == man_1:
    print(elf_1)
elif elf_2 == dwarf_2 and dwarf_2 == man_2:
    print(elf_2)