# batchPDFcert package

This is a simple tool built in python and that uses [Inkscape](https://inkscape.org/) to generate PDF certificates replacing the texts automatically, from:

1. A predefined certificate template in the `.svg` format, stored in the `template/` folder. The template file can be created with Inkscape, containing text including `[tags]` brackets, which will be replaced by the script.

2. A list of contents to be replaced in the scripts, in the `.csv`' format using the `;` character as separator. The first line represents the header of the data and must contain the tags to be replaced. The following lines must contain the entries that will produce the certificates (each line will produce a certificate). At least the `[name]` field defined in the header is expected in the template file, which will also be used as the file name.

## Setting up the environment with Anaconda

Python 3.9 is required to run this code.

```
conda create --name batchPDFcert python=3.9
conda activate batchPDFcert
```

## Preparing files

You need to define the paths for Inkscape binary, templates (`.csv` data table and `.svg` certificate model) and output files. Those paths must be defined in the `config.ini` file.

## Running

Just run:

```
python batchPDFcert.py
```


