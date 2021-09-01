#!/usr/bin/env python3
import os
import sys
import argparse


def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('GithubLink', help="Github link for custom script and dockerfile, ex: https://github.com/TerrySunTW/TestAITask1.git")
    parser.add_argument('DockerFilePath', help="dockerfile filename for runtime environment, system will using the docker environment to run your script")
    parser.add_argument('TaskCommand', help="The commnad you need to run on the disribution system. (ex: python /scripts/test.py p1 p2 p3 )")
    parser.add_argument('ArchiveFolderPath', help="Archive folderpath(default: ./out)")
    parser.add_argument('ReportFilePath', help="Report filename(text file in json format)")

    args = parser.parse_args(arguments)

    print(args)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
