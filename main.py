import face_recognition
import os
import shutil

known_image = face_recognition.load_image_file("1.png")
known_encoding = face_recognition.face_encodings(known_image)[0]


for f in os.listdir("images"):
    try:
        unknown_image = face_recognition.load_image_file("images\\" + f)
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
        results = face_recognition.compare_faces([known_encoding], unknown_encoding, 0.5)
        if (results == [True]):
            shutil.copy2("images\\" + f, 'SameFace')
        else:
            shutil.copy2("images\\" + f, 'OtherFaces')
    except Exception as e:
        shutil.copy2("images\\" + f, 'NoFace') # complete target filename given
        results = e

    print("{}: {}".format(f,results))