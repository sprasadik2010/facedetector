import face_recognition
import os
import shutil
import uuid

from multiprocessing import Pool


def finddups(img):
    try:
        known_image = face_recognition.load_image_file("images\\" + img)
        known_encoding = face_recognition.face_encodings(known_image)[0]
        foldername = str(uuid.uuid4())
        os.makedirs(foldername)
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
                    shutil.move("images\\" + g, 'NoFace')  # complete target filename given
                except:
                    results = e
    except:
        results = ""

#for f in os.listdir("images"):
#    asyncio.run(finddups(f))

if __name__ == '__main__':
    imglist = os.listdir("images")
    pool = Pool(os.cpu_count())
    pool.map(finddups, imglist)  # process data_inputs iterable with pool
