from app import app, n, w
import threading

if __name__ == '__main__':
    cr_th = threading.Thread(target=n.do_crawling)
    cr_th.daemon = True
    cr_th.start()
    wt_th = threading.Thread(target=w.get_weather_data_thread)
    wt_th.daemon = True
    wt_th.start()
    app.run(host='127.0.0.1', debug=True, use_reloader=False)#, port=5000)

# suggested way
'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
'''
## server on http://0.0.0.0:5000/
## visible across the network
## BaseUrl for Android http://<your ip address>:5000/blah/blah