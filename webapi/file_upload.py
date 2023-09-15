import os
from dicom_converter import clear_tmp, get_names,convert_dcm_jpg
from flask_restx import Namespace , Resource
from flask import request, jsonify


from werkzeug.utils import secure_filename

from flask import current_app

import pydicom


from pydicom import dcmread
import pylibjpeg

import tempfile


#TO CHANGE:
api = Namespace('kangaroo', 'Description kangaroo Web API url prefix')
#______



                

@api.route('/file-upload')
class UploadFile(Resource):
    clear_tmp()
    ALLOWED_EXTENSIONS = set(['png','dcm'])
    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS

    
    def post(self):
        if 'file' not in request.files:
            resp = jsonify({'message': 'No file part in the request'})
            resp.status_code = 400
            return resp

        file = request.files['file']
        if file.filename == '':
            resp = jsonify({'message': 'No file selected for uploading'})
            resp.status_code = 400
            return resp

        if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

            upload_folder = current_app.config['UPLOAD_FOLDER']
           
            #TODO test dicom
            #if dicom call analise m
            #dcm_to_png(filename)
            inputdir = upload_folder
            #outdir = './unpacked'
            #os.mkdir(outdir)

            #test_list = [ f for f in  os.listdir(inputdir)]

            #for f in test_list:   # remove "[:10]" to convert all images 
            #    ds = pydicom.read_file(inputdir + '/'+f) # read dicom image
            #    img = ds.pixel_array # get image array
            #    cv2.imwrite(outdir + f.replace('.dcm','.png'),img) # write png image
                
            names = get_names(upload_folder)
            folder_path = "./tmp"
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            #temp = tempfile.TemporaryFile()
            
            if names[0].endswith('.dcm'):
                for name in names:
                
                    images = convert_dcm_jpg(upload_folder, name)
                
                i = 0
                a = len(images)
                clear_tmp()
            
                for i in range(0,a):
             
                    image = images[i]
                    image.save(folder_path + "/" + f'image{i:02d}' + '.png')
            
                
            resp = jsonify({'message': 'File successfully uploaded'})
            resp.status_code = 201
            return resp
            
        else:
            resp = jsonify({'message': 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
            resp.status_code = 400
            return resp






        
         


















