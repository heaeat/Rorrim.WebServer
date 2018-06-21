from app import app, n, w, connector, host, face_classification
import threading
#om tensorflow.python.client import graph_util

if __name__ == '__main__':
    '''
    face_classification = FaceID.FaceID()
    face_classification.start_training("rorrim1234567890")
    file_name = 'test12313.jpg'
    uid = 'lion'
    uid_label, accuracy = face_classification.get_accrucy("rorrim1234567890", 'test12313.jpg')
    if uid_label.__contains__(uid) and accuracy >= 0.9:
        print('Login Success')
    else:
        print('Login Fail')
    '''
    connector.start()
    '''
    face_th = threading.Thread(target=face_classification.start_training)  # , args=('rorrim1234567890'))#('rorrim1234567890'))
    face_th.daemon = True
    face_th.start()
    '''
    cr_th = threading.Thread(target=n.do_crawling)
    cr_th.daemon = True
    cr_th.start()
    wt_th = threading.Thread(target=w.get_weather_data_thread)
    wt_th.daemon = True
    wt_th.start()



    app.run(host=host, debug=True, use_reloader=False, port=5000)
    #app.run(host='192.168.0.126', debug=True, use_reloader=False)#, port=5000)
    #app.run(host='172.16.28.163', debug=True, use_reloader=False)#, port=5000)

# suggested way
'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
'''
## server on http://0.0.0.0:5000/
## visible across the network
## BaseUrl for Android http://<your ip address>:5000/blah/blah