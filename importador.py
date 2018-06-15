import pandas as pd
import argparse


def main():
    parser = argparse.ArgumentParser("%prog -f <file>")
    parser.add_argument("-f", dest="file", help="ruta del file")
    args = parser.parse_args()

    if (args.file == None):
        print
        parser.usage
        exit(0)
    else:
        file = args.file

    titulares = pd.read_excel(file,sheet_name=0,index_col=0)
    familiares = pd.read_excel(file,sheet_name=1,index_col=0)

    joined = titulares.join(familiares,lsuffix='_titular', rsuffix='_familiar')
    writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
    joined.to_excel(writer, sheet_name='report')
    workbook = writer.book
    worksheet = writer.sheets['report']
    header_fmt = workbook.add_format({'bold': True})
    worksheet.set_row(0, None, header_fmt)
    writer.save()

    # print(joined.head())



if __name__ == "__main__":
    main()

