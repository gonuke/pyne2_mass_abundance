import sys
sys.path.append("../../config")
import write_common_headers

# NMA for nuclide mass & abundance
P2_NMA_NAME = 'mass_abundance'
P2_NMA_MAJOR_VERSION = 0
P2_NMA_MINOR_VERSION = 1
P2_NMA_PATCH_VERSION = 0

stub_version = write_common_headers.write_version_header(P2C_NAME,
                                                         P2_NMA_MAJOR_VERSION,
                                                         P2_NMA_MINOR_VERSION,
                                                         P2_NMA_PATCH_VERSION)
