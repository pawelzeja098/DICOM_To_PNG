from flask import Blueprint
from flask_restx import Api

from .file_upload import api as file_upload


# Initialize Blueprint and Api
blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint,
          title='Dicom tool',
          version='0.1',
          description='Extract images from Dicom file'
          )

# Add namespace to api
api.add_namespace(file_upload)
# ...
# api.add_namespace(ns_...)


