db = {
    'user' : 'mariadm',
    'password' : 'dLR91wsFK9T07Tf0tkKY',
    'host' : 'dev-insw-pay.clggrr8q6ibc.ap-northeast-2.rds.amazonaws.com',
    'port' : '3306',
    'database' : 'INSWAVE_PAY'
}

DEBUG = True
SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
SQLALCHEMY_TRACK_MODIFICATIONS = False
