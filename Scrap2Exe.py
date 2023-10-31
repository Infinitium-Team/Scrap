import sys
import re
import subprocess

def convert_scrap_to_cpp(input_file):
    output_file = "tocpp.cpp"
    with open(input_file, 'r') as f:
        scrap_code = f.read()

    cpp_code = re.sub(r'def (\w+)\(\)\s+printT\("(.+)"\)\s+END', r'int \1() {\n    std::cout << "\2";\n}\n', scrap_code)

    with open(output_file, 'w') as f:
        f.write('#include <iostream>\n\n')
        f.write(cpp_code)
        f.write('\n\nint main() {\n')
        function_names = re.findall(r'int (\w+)\(\)', cpp_code)
        for function_name in function_names:
            f.write(f'    {function_name}();\n')
        f.write('    return 0;\n}\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Using: python Scrap2Exe.py input_file.scrap")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        convert_scrap_to_cpp(input_file, output_file)
        print(f"Succesful converted to C++ and saved to {output_file}.")

        try:
            subprocess.run(['./g++', output_file, '-o', 'Build'])
            print("Compiled to: Build.exe")
        except subprocess.CalledProcessError as e:
            print(f"Ошибка компиляции: {e}")
