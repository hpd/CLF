#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Print information about a Clip Metadata file
"""

import array
import os
import sys

import clip

def main():
    import optparse

    p = optparse.OptionParser(description='Print information about a Clip Metadata file',
                                prog='clipinfo',
                                version='0.01',
                                usage='%prog [options]')

    p.add_option('--clip', '-c', default='')

    options, arguments = p.parse_args()

    #
    # Get options
    # 
    clipPath = options.clip

    try:
        argsStart = sys.argv.index('--') + 1
        args = sys.argv[argsStart:]
    except:
        argsStart = len(sys.argv)+1
        args = []

    print( "command line : \n%s\n" % " ".join(sys.argv) )
 
    #
    # Run 
    #
    if clipPath:
        clp = clip.ClipMetadata(clipPath)
        clp.printInfo()

# main

if __name__ == '__main__':
    main()