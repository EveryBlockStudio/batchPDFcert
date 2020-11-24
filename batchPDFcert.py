import os
import subprocess
import csv
import configparser

def convert_to_pdf_inkscape(svg, filename, output_dir, inkscape_dir, work_dir):
    """
    Convert SVG file to PDF using Inkscape.
    """

    cmd = f'{inkscape_dir} -o {work_dir+output_dir+filename}.pdf {work_dir}temp.svg'

    subprocess.run(cmd, capture_output=True, shell=True)
    subprocess.run(f'rm {work_dir}temp.svg', shell=True)


def modify_svg(fields_to_change, svg_template_file):
    """
    Replace each field in the SVG template with the correspondent value of a dictionary of strings.
    """

    with open(svg_template_file, 'r') as svg_arq:
        svg_str = svg_arq.read()

        for key in fields_to_change:
            try:
                if key != '' and fields_to_change[key] != None:
                    svg_str = svg_str.replace(f'[{key}]', fields_to_change[key])
            except KeyError:
                print(f'There is no [{key}] in the SVG file!')
            except Exception as e:
                print(f'Another error: \n\t{e}')

    with open('temp.svg','w') as temp_arq:
        temp_arq.write(svg_str)

def build_certificates(inkscape_dir, output_dir, work_dir, svg_template_file, data_table):
    """
    Build PDF certificates using a SVG template file. The Inkscape director must be specified.
    """

    with open(data_table, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')

        for row in reader:
            filename = row['name'].replace(' ','_')
            print(f'[{reader.line_num-1}]\tBuilding {filename}.pdf...', end='\t\t')

            modify_svg(row, svg_template_file)
            convert_to_pdf_inkscape(svg_template_file, filename, output_dir, inkscape_dir, work_dir)
            print('OK')


if __name__ == '__main__':
    work_dir = os.getcwd()+'/'

    conf = configparser.ConfigParser()
    conf.read('config.ini')

    build_certificates(
        conf['Paths']['inkscape_dir'],
        conf['Paths']['output_dir'],
        work_dir,
        conf['Paths']['svg_template_file'],
        conf['Paths']['data_table']
    )
