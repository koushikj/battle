#!/usr/bin/env python
"""
1. validation of avro schema and data(json).
2. creation(encode) of avro from json data.
3. decode of avro to json format.
"""

from __future__ import print_function
import sys
import os
import argparse
import boto
import boto3
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import LONG_MIN_VALUE, LONG_MAX_VALUE, INT_MIN_VALUE, INT_MAX_VALUE
from avro.io import DatumReader, DatumWriter
from json import loads, dump

if sys.version_info[0] < 3:
    from avro.schema import parse as Parse
else:
    from avro.schema import Parse
    from past.builtins import long, basestring

# CONSTANTS
cur_file = ""

def checkType(datum, fieldTypeList, name, isPrint=True):
    """ Check if type of the datum matches fieldTypeList
    """
    #print ("-----------------")
    #print (datum)
    #print (fieldTypeList)
    #print ("-----------------")
    global cur_file
    match = False
    for fieldType in fieldTypeList:
        if isinstance(datum, fieldType):
            match = True
            break

    if not match and isPrint:
        print(cur_file, ": Type mismatch: ", name, "   Expected: ", fieldTypeList, "  Got: ", type(datum))

    return match

def validate_PrintErrorField(expected_schema, datum, name, isPrint=True):
    """Determine if a python datum is an instance of a schema.
    """
    schema_type = expected_schema.type

    if schema_type == 'null':
        return datum is None
    elif schema_type == 'boolean':
        return checkType(datum, [bool], name, isPrint)
    elif schema_type == 'string':
        return checkType(datum, [basestring], name, isPrint)
    elif schema_type == 'bytes':
        return checkType(datum, [str], name, isPrint)
    elif schema_type == 'int':
        return checkType(datum, [int, long], name, isPrint) and INT_MIN_VALUE <= datum <= INT_MAX_VALUE
    elif schema_type == 'long':
        return checkType(datum, [int, long], name, isPrint) and LONG_MIN_VALUE <= datum <= LONG_MAX_VALUE
    elif schema_type in ['float', 'double']:
        return checkType(datum, [int, long, float], name, isPrint)
    elif schema_type == 'fixed':
        return checkType(datum, [str], name, isPrint) and len(datum) == expected_schema.size
    elif schema_type == 'enum':
        return datum in expected_schema.symbols
    elif schema_type == 'array':
        return (checkType(datum, [list], name, isPrint) and
                False not in [validate_PrintErrorField(expected_schema.items, d, name) for d in datum])
    elif schema_type == 'map':
        return (checkType(datum, [dict], name, isPrint) and
                False not in [checkType(k, [basestring], name, isPrint) for k in datum.keys()] and
                False not in [validate_PrintErrorField(expected_schema.values, v, datum.name) for v in datum.values()])
    elif schema_type in ['union', 'error_union']:
        res = True in [validate_PrintErrorField(s, datum, name, isPrint=False) for s in expected_schema.schemas]
        if res is False:
            print(cur_file, ": Type mismatch 2: ", name, \
                            " Expected: ", [str(s) for s in expected_schema.schemas], \
                            " Got: ", type(datum))

        return res

    elif schema_type in ['record', 'error', 'request']:
        return (checkType(datum, [dict], name, isPrint) and
                False not in [validate_PrintErrorField(f.type, datum.get(f.name), f.name) for f in expected_schema.fields])


def validateAvro(schemaFileName, dataFileList):
    """ validates the file names provided in the dataFileList matches the schema
    """
    global cur_file
    valid = set()
    invalid_avro = set()
    invalid_json = set()

    try:
        schema = Parse(open(schemaFileName).read())
        for arg in dataFileList:
            try:
                cur_file = arg
                json = loads(open(arg, 'r').read())
                if validate_PrintErrorField(schema, json, schema.name):
                    valid.add(arg)
                else:
                    invalid_avro.add(arg)
            except ValueError:
                invalid_json.add(arg)

        print('\nCompliant data files:\n\t' + '\n\t'.join(valid))
        print('Non-compliant data files:\n\t' + '\n\t'.join(invalid_avro))
        print('Invalid json:\n\t' + '\n\t'.join(invalid_json))
    except Exception as ex:
        print('1Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(ex).__name__)

def createAvro(schemaFileName, dataFileName, outputAvroFileName):
    """This function creates avro
    """
    try:
        # create the handle for the avro creation
        schema = Parse(open(schemaFileName, "rb").read())
        writer = DataFileWriter(open(outputAvroFileName, "wb"), DatumWriter(), schema)

        # load the json data
        with open(dataFileName, "r") as myfile:
            data = myfile.read()
            jData = loads(data)
            writer.append(jData)

        writer.close()
    except Exception as ex:
        print('2Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(ex).__name__)

def decodeAvroFile(listAvroFileName, outputDirectory):
    """ This function decodes the avro and store in the local directory
        Format of the file names is <cur-dir>/<outputDirectory>/<avro file name>_<id>.json
    """

    try:
        os.makedirs(outputDirectory+"/Output", mode=0o777)
    except OSError:
        print("Output directory already exists")

    try:
        for avroFileName in listAvroFileName:
            i = 0
            # Decode the avro file and read the data
            reader = DataFileReader(open(avroFileName, "rb"), DatumReader())
            for user in reader:
                with open(outputDirectory+"/Output/" + os.path.splitext(avroFileName)[0]+'_'+str(i)+".json", 'w') as outputFile:
                    dump(user, outputFile)
                    i += 1
            reader.close()
    except Exception as ex:
        print('3Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(ex).__name__, ex)

def fetchAvroFromS3(region, buckname, prefixname, timestamp, outputDirectory):
    """ Fetch the avro from the s3 and filter it based on the timestamp
        and store it at the output directory specified
    """
    try:
        s3Client = boto3.client('s3')
        conn = boto.s3.connect_to_region(region, is_secure=False)
        bucket = conn.get_bucket(buckname)
        val = list(bucket.list(prefix=prefixname))

        avroFileNames = [x.key for x in val if x.last_modified >= timestamp]
        for keyname in avroFileNames:
            'trim the name and downalod the files'
            filename = keyname.split('/')[-1]
            s3Client.download_file(buckname, keyname, outputDirectory+"/"+filename)
    except Exception as ex:
        print('4Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(ex).__name__, ex)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='avro operations', title="Operations", dest='operationName')
    subparsers.required = True

    validate_parser = subparsers.add_parser("validate", help="Validate avro schema with data files")
    create_parser = subparsers.add_parser("encode", help="Create the avro file")
    decode_parser = subparsers.add_parser("decode", help="Decode the avro file")
    fetch_parser = subparsers.add_parser("fetch", help="fetch the avro files from s3")

    validate_parser.add_argument("-s", "--schema", required=True, help='Schema File Name', dest="schema")
    validate_parser.add_argument("-d", "--data", required=True, nargs="+", help='One or more data files', dest="data")

    create_parser.add_argument("-s,", "--schema", required=True, help='Schema File Name', dest="schema")
    create_parser.add_argument("-d", "--data", required=True, help='Data File Name', dest="data")
    create_parser.add_argument("-o", "--output", required=True, help='Avro File Name (*.avro)', dest="output")

    dir_path = os.getcwd()
    group = decode_parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-a", "--avro", help='Avro File Name', dest="avro_file_name")
    group.add_argument("-d", "--dir", help='Directory of all avro files', dest="avro_dir_name")
    decode_parser.add_argument("-o", "--output", default=dir_path, dest="output_dir_name",
                               help='Directory to store decoded json files (default: ./Output)')

    # Fetching avro from s3 parser
    fetch_parser.add_argument("-t", "--timestamp",dest="ts", default="",
                             help="timestamp in IS8601 format (2017-10-31T23:10:54.000Z). Filter to get files after TS")
    fetch_parser.add_argument("-d", "--dir", help="directpry to store avro (default: avro)", dest="outputDirectory", default="Avro")
    fetch_parser.add_argument("-b", "--bucketname", help="Bucket Name of S3 Avro File location", dest="bucketname")
    fetch_parser.add_argument("-p", "--prefix", help="Prefix Name of S3 File Location", dest="prefixname")
    fetch_parser.add_argument("-r", "--region", help="AWS region", dest="regionName", required=True)

    argument = parser.parse_args()
    if argument.operationName == 'validate':
        validateAvro(argument.schema, argument.data)
    elif argument.operationName == 'encode':
        createAvro(argument.schema, argument.data, argument.output)
    elif argument.operationName == 'decode':
        if argument.avro_file_name:
            decodeAvroFile([argument.avro_file_name], argument.output_dir_name)
        elif argument.avro_dir_name:
            # Filter only files with avro extension.
            results = [os.path.join(argument.avro_dir_name, each) for each in os.listdir(argument.avro_dir_name) if each.endswith('.avro')]
            decodeAvroFile(results, argument.output_dir_name)
    elif argument.operationName == 'fetch':
        try:
            os.makedirs(argument.outputDirectory, mode=0o777)
        except OSError:
            # print("Output directory already exists")
            pass
        fetchAvroFromS3(argument.regionName, argument.bucketname, argument.prefixname, argument.ts, argument.outputDirectory)
    else:
        print("Error: ")
