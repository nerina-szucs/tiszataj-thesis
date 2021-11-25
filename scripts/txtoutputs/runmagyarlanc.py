import subprocess
import glob
import os


def run_command(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')


def generate_output(inputfile, outputfile):
    for output_line in run_command(
            f'java -Xmx2g -jar magyarlanc-3.0.jar -mode parse -input "{inputfile}" -output "mloutputs/{outputfile}" -encoding WINDOWS-1250'):
        print(output_line)

    with open(f'mloutputs/{outputfile}', 'r') as original: data = original.read()
    with open(f'mloutputs/{outputfile}', 'w') as modified: modified.write(
        "SZO_ID	SZO	LEMMA	SZOFAJ	MORPH	PARENT_ID	DEP_LABEL	CONST_LABEL\n" + data)


files_list = []

# for root, dirs, files in os.walk('.'):
#     for file in files:
#         if file.endswith('.txt'):
#             files_list.append(file)
#
# for file in files_list:
#     myInput = file
#     myOutput = file.removesuffix(".txt") + '_out' + '.txt'
#     print(myInput)
#     print(myOutput)
    # generate_output(myInput, myOutput)

myInput = input("Elemezni kívánt fájl:\n")
myOutput = myInput.split('.txt')[0].strip() + "_out" + ".txt"
generate_output(myInput, myOutput)
