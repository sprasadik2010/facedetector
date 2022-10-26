import face_recognition
import os
import shutil
import uuid


for f in os.listdir("images"):
    foldername = str(uuid.uuid4())
    os.makedirs(foldername)
    known_image = face_recognition.load_image_file("images\\" + f)
    known_encoding = face_recognition.face_encodings(known_image)[0]
    for g in os.listdir("images"):
        try:
            unknown_image = face_recognition.load_image_file("images\\" + g)
            unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
            results = face_recognition.compare_faces([known_encoding], unknown_encoding, 0.5)
            if (results == [True]):
                shutil.move("images\\" + g, foldername)
            # else:
            #     shutil.copy2("images\\" + f, 'OtherFaces')
        except Exception as e:
            try:
                shutil.move("images\\" + g, 'NoFace') # complete target filename given
            except:
                results = e


        # print("{}: {}".format(f,results))
