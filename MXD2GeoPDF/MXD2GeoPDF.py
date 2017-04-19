#! python
"""MXD2GeoPDF.py

Create GeoPDF documents from ArcPy/PubPy.

Copyright 2015 TerraGo Technologies Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import os
import sys

# import arcpy equired to "wake up" ArcGIS from outside ArcMap

import arcpy

from pubpy.geopdf_export.api import ExportMXDToGeoPDF

def throw(msg):
    """Raise a simple exception"""
    raise BaseException(msg)

def usage():
    """usage: MXD2GeoPDF.py mxd [pdf]

where:
    mxd: name of MDX
    pdf: optional name of GeoPDF document
"""
    print usage.__doc__

def validate_inputs(mxd, pdf):
    """Make sure we have an MXD and no PDF which might get clobbered"""
    base, ext = os.path.splitext(mxd)
    if not ext:
        mxd += '.mxd'
    if not os.path.exists(mxd):
        throw('Cannot find MXD ' + mxd)
    if not pdf:
        pdf = base + '.pdf'
    base, ext = os.path.splitext(pdf)
    if not ext:
        pdf += '.pdf'
    if os.path.exists(pdf):
        throw('Output file {0} exists'.format(pdf))
    return mxd, pdf

def parse_args():
    """deal with command line arguments"""
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)
    else:
        mxd = sys.argv[1]
        pdf = ''
        if len(sys.argv) > 2:
            pdf = sys.argv[2]
    return validate_inputs(mxd, pdf)

if __name__ == '__main__':
    try:
        mxd, pdf = parse_args()
        ExportMXDToGeoPDF(mxd, pdf)
    except:
        print "Error: {0}".format(sys.exc_info()[1])
        sys.exit(1)
