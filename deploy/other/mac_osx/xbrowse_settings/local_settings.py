from xbrowse.reference import Reference
from xbrowse.annotation import VariantAnnotator
from xbrowse.datastore.population_datastore import PopulationDatastore
from xbrowse.datastore.project_datastore import ProjectDatastore
from xbrowse.coverage import CoverageDatastore
from xbrowse.datastore import MongoDatastore
from xbrowse.cnv import CNVStore

import os
import pymongo
import imp

#from xbrowse_server.xbrowse_annotation_controls import CustomAnnotator

# django stuff



XBROWSE_CODE_DIR = os.path.abspath(os.path.join(__file__, "../../../../../"))
if not os.path.isdir(XBROWSE_CODE_DIR):
    raise Exception("Directory doesn't exist: %s" % XBROWSE_CODE_DIR)


REFERENCE_DATA_DIR = os.path.join(XBROWSE_CODE_DIR, "xbrowse-laptop-downloads")

DEBUG = True
#COMPRESS_ENABLED = False
BASE_URL = 'http://localhost:8000/'
URL_PREFIX = '/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(XBROWSE_CODE_DIR, 'xbrowse_db.sqlite'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


STATICFILES_DIRS = (
    os.path.join(XBROWSE_CODE_DIR, 'xbrowse_server/staticfiles/'),
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


#
# xbrowse stuff
#

COMMON_SNP_FILE = os.path.join(REFERENCE_DATA_DIR, "markers.txt")

HGMD_OMIM_FILE = os.path.join(REFERENCE_DATA_DIR, 'hgmd_omim_genes.txt')

REFERENCE_SETTINGS = imp.load_source(
    'reference_settings',
    os.path.dirname(os.path.realpath(__file__)) + '/reference_settings.py'
)
CUSTOM_ANNOTATOR_SETTINGS = None

ANNOTATOR_SETTINGS = imp.load_source(
    'annotator_settings',
    os.path.dirname(os.path.realpath(__file__)) + '/annotator_settings.py'
)

_conn = pymongo.Connection()
DATASTORE_DB = _conn['xbrowse_datastore']
POPULATION_DATASTORE_DB = _conn['xbrowse_pop_datastore']

DEFAULT_CONTROL_COHORT = 'controls'
CONTROL_COHORTS = [
    {
        'slug': 'controls',
        'vcf': '',
    },
]

COVERAGE_DB = _conn['xbrowse_coverage']

PROJECT_DATASTORE_DB = _conn['xbrowse_proj_store']

CNV_STORE_DB_NAME = 'xbrowse_cnvs'

CUSTOM_POPULATIONS_DB = _conn['xcustom_refpops']