# Train your memory by remembering your memory map.
# Copyright (C) 2020 Eugene Efimenko

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Full notice in file LICENSE
# email - mailforcoolmail@yandex.ru


import random
import sys
from collections import OrderedDict
filename = 'memory_map.txt'
memory_dict = OrderedDict()
with open(filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        number, memory_point = line.split('.')
        memory_dict[number] = memory_point.strip()
last_memory_point = int(list(memory_dict.keys())[-1])
score = 0
print("""    Memory trainer  Copyright (C) 2020 Eugene Efimenko
    This program comes with ABSOLUTELY NO WARRANTY; for details type `tell w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `tell c' for details.""")
print("Welcome to memory trainer!")
max_training_number = int(sys.argv[1])
correct_anwser = False
while True:
    random_memory_point = random.randint(0, max_training_number)
    if correct_anwser:
        user_number_guess = input(f"+{score} How number {random_memory_point} looks? ")
    else:
        user_number_guess = input(f"-{score} How number {random_memory_point} looks? ")
    if user_number_guess.lower() == memory_dict[str(random_memory_point)].lower():
        score += 1
        correct_anwser = True
    elif user_number_guess.lower() == "tell w":
        print("""THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM “AS IS” WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.""")
    elif user_number_guess.lower() == "tell c":
        print("""4. Conveying Verbatim Copies.

You may convey verbatim copies of the Program's source code as you receive it, in any medium, provided that you conspicuously and appropriately publish on each copy an appropriate copyright notice; keep intact all notices stating that this License and any non-permissive terms added in accord with section 7 apply to the code; keep intact all notices of the absence of any warranty; and give all recipients a copy of this License along with the Program.

You may charge any price or no price for each copy that you convey, and you may offer support or warranty protection for a fee.
5. Conveying Modified Source Versions.

You may convey a work based on the Program, or the modifications to produce it from the Program, in the form of source code under the terms of section 4, provided that you also meet all of these conditions:

    a) The work must carry prominent notices stating that you modified it, and giving a relevant date.
    b) The work must carry prominent notices stating that it is released under this License and any conditions added under section 7. This requirement modifies the requirement in section 4 to “keep intact all notices”.
    c) You must license the entire work, as a whole, under this License to anyone who comes into possession of a copy. This License will therefore apply, along with any applicable section 7 additional terms, to the whole of the work, and all its parts, regardless of how they are packaged. This License gives no permission to license the work in any other way, but it does not invalidate such permission if you have separately received it.
    d) If the work has interactive user interfaces, each must display Appropriate Legal Notices; however, if the Program has interactive interfaces that do not display Appropriate Legal Notices, your work need not make them do so.

A compilation of a covered work with other separate and independent works, which are not by their nature extensions of the covered work, and which are not combined with it such as to form a larger program, in or on a volume of a storage or distribution medium, is called an “aggregate” if the compilation and its resulting copyright are not used to limit the access or legal rights of the compilation's users beyond what the individual works permit. Inclusion of a covered work in an aggregate does not cause this License to apply to the other parts of the aggregate.""")
    else:
        correct_anwser = False
        score -= 1
        print(f"{random_memory_point} is {memory_dict[str(random_memory_point)].lower()}")
    

