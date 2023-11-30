import os
import time
from platform import architecture
from deb_pkg_tools import control, package

def throw_exception(tgt):
    raise Exception(f"{tgt} is a required option.")

src_dir =  os.getenv("INPUT_SRC_DIR") or throw_exception('src_dir')
out_dir =  os.getenv("INPUT_BINARY_DIR")
depends = os.getenv("INPUT_PACKAGE_DEPENDS")
version = os.path.basename(os.getenv("INPUT_PACKAGE_VERSION")) or throw_exception('package_version')
package_name = os.getenv("INPUT_PACKAGE_NAME") or throw_exception('package_name')
description = os.getenv("INPUT_PACKAGE_DESCRIPTION") or throw_exception('package_description')
maintainer = os.getenv("INPUT_PACKAGE_MAINTAINER") or throw_exception('package_maintainer')
arch = os.getenv("INPUT_PACKAGE_ARCH") or throw_exception('package_arch')

#Let's change the version to a string or conjour one up if not a release number
#if not version[0].isdigit():
#    version=f"{str(int(time.time()))}-{version}"

#The default control_fields
control_fields={
    "architecture": arch,
    "package": package_name,
    "version": version,
    "description": description,
    "maintainer": maintainer,
    "replaces": package_name
}

#Add depends list if it was set
if depends:
    control_fields.update({ "depends": depends})

#Create the control file
control.create_control_file(control_file=f"{src_dir}/DEBIAN/control",control_fields=control_fields)

#If the output directory doesn't exist, let's create it
if not os.path.isdir(f"{out_dir}"): 
    os.mkdir(f"{out_dir}")

#Build the package
package.build_package(directory=src_dir,repository=out_dir)