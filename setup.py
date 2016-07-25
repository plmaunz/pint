#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

try:
    from subprocess import check_output, check_call
except ImportError:
    import subprocess as sp
    def check_output(*args, **kwds):
        kwds['stdout'] = sp.PIPE
        proc = sp.Popen(*args, **kwds)
        output = proc.stdout.read()
        proc.wait()
        if proc.returncode != 0:
            ex = Exception("Process had nonzero return value %d" % proc.returncode)
            ex.returncode = proc.returncode
            ex.output = output
            raise ex
        return output

try:
    reload(sys).setdefaultencoding("UTF-8")
except:
    pass

try:
    from setuptools import setup
except ImportError:
    print('Please install or upgrade setuptools or pip to continue')
    sys.exit(1)

import codecs


def read(filename):
    return codecs.open(filename, encoding='utf-8').read()


long_description = '\n\n'.join([read('README'),
                                read('AUTHORS'),
                                read('CHANGES')])

__doc__ = long_description


def getGitVersion(tagPrefix=None):
    """Return a version string with information about this git checkout.
    If the checkout is an unmodified, tagged commit, then return the tag version.
    If this is not a tagged commit, return the output of ``git describe --tags``.
    If this checkout has been modified, append "+" to the version.
    """
    path = os.getcwd()
    if not os.path.isdir(os.path.join(path, '.git')):
        return None

    gitVersion = check_output(['git', 'describe', '--tags']).strip().decode('utf-8')

    # any uncommitted modifications?
    modified = False
    status = check_output(['git', 'status', '--porcelain'], universal_newlines=True).strip().split('\n')
    for line in status:
        if line != '' and line[:2] != '??':
            modified = True
            break

    if modified:
        gitVersion = gitVersion + '+'

    return gitVersion


setup(
    name='Pint',
    version=getGitVersion(),
    description='Physical quantities module',
    long_description=long_description,
    keywords='physical quantities unit conversion science',
    author='Hernan E. Grecco',
    author_email='hernan.grecco@gmail.com',
    url='https://github.com/hgrecco/pint',
    test_suite='pint.testsuite.testsuite',
    zip_safe=True,
    packages=['pint'],
    package_data={
        'pint': ['default_en.txt',
                 'constants_en.txt']
      },
    include_package_data=True,
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ])
