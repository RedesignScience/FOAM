"""
FOAM
Package for performing adaptive sampling of biomolecular systems
"""

# Add imports here
from .model import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
