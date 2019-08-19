from os.path import dirname, basename, isfile, join
import glob
import sys
dir_name = dirname(__file__)
sys.path.append(dir_name)
modules = glob.glob(join(dir_name, "*.py"))
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]