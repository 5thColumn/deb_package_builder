import os
import time
from platform import architecture
from deb_pkg_tools import control, package

src_dir =  os.getenv("INPUT_SRC_DIR")
out_dir =  os.getenv("INPUT_BINARY_DIR")
depends = os.getenv("INPUT_PACKAGE_DEPENDS")
version = os.path.basename(os.getenv("INPUT_PACKAGE_VERSION"))
package_name = os.getenv("INPUT_PACKAGE_NAME")
description = os.getenv("INPUT_PACKAGE_DESCRIPTION")
maintainer = os.getenv("INPUT_PACKAGE_MAINTAINER")
arch = os.getenv("INPUT_PACKAGE_ARCH")

if not version.isnumeric():
    version=time.time()

    # # Binary control file fields.
    # CaseInsensitiveKey('Breaks'),
    # CaseInsensitiveKey('Conflicts'),
    # CaseInsensitiveKey('Depends'),
    # CaseInsensitiveKey('Enhances'),
    # CaseInsensitiveKey('Pre-Depends'),
    # CaseInsensitiveKey('Provides'),
    # CaseInsensitiveKey('Recommends'),
    # CaseInsensitiveKey('Replaces'),
    # CaseInsensitiveKey('Suggests'),
    # # Source control file fields.
    # CaseInsensitiveKey('Build-Conflicts'),
    # CaseInsensitiveKey('Build-Conflicts-Arch'),
    # CaseInsensitiveKey('Build-Conflicts-Indep'),
    # CaseInsensitiveKey('Build-Depends'),
    # CaseInsensitiveKey('Build-Depends-Arch'),
    # CaseInsensitiveKey('Build-Depends-Indep'),
    # CaseInsensitiveKey('Built-Using'),
# Package: revolver
# Priority: Required
# Version: 1.0.17
# Section: admin
# Maintainer: Ryan Pisani <rpisani@5thcolumn.net>
# Depends: sudo, nginx, python3-pip, libldap2-dev, libsasl2-dev, git, curl, cron, dialog, libsystemd-dev
# Architecture: all
# Description: Provides 5thColumn's Revolver configuration & management utility 
# Replaces: revolver
    # CaseInsensitiveKey('Architecture'),
    # CaseInsensitiveKey('Description'),
    # CaseInsensitiveKey('Maintainer'),
    # CaseInsensitiveKey('Package'),
    # CaseInsensitiveKey('Version'),
control_fields={
    "architecture": arch,
    "package": package_name,
    "version": version,
    "description": description,
    "maintainer": maintainer
}
control.create_control_file(control_file=f"{src_dir}/DEBIAN/control",control_fields=control_fields)
if os.path.isdir(f"{src_dir}/DEBIAN/control"):
    print('exists')

if not os.path.isdir(f"{out_dir}"): 
    os.mkdir(f"{out_dir}")


print(package_name)
print(version)
print(src_dir)
print(depends)
print(os.listdir())
if os.path.isdir(src_dir):
    print("Path exists")
print("hello")
package.build_package(directory=src_dir,repository=out_dir)