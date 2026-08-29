workers = 4
bind = 'unix:/tmp/gunicorn.sock'
loglevel = 'info'
accesslog = "./logs/access.log"
errorlog = "./logs/error.log"

