# will parse the data inside the postgres_database.ini and will return here in the form of dictionary
# so Connect_to_a_Postgres_Database.py can read from this postgres_config.py

from configparser import ConfigParser   # ConfigParser is the class

def config(filename="postgres_database.ini", section="postgresql"):
    # create a parser
    parser = ConfigParser()
    # read the config file
    parser.read(filename)
    db = {}  # need to reiterate over the filename, and return each element inside that file and put it inside a dictionary. so create an empty dictionary
    if parser.has_section(section):  # verification step to check for header/section
        params = parser.items(section)  # params would have everything inside postgres_database.ini. 
        #print(params)       # a list of Tuples - [('host', 'localhost'), ('database', 'test'), ('user', 'postgres'), ('password', 'riki')]
        for param in params:
            # print(param[1])
            db[param[0]] = param[1]     # since db is an empty dictionary, this way you are trying to create a key : value pair
    else:
        raise Exception('Section {0} is not found in the {1} file.'.format(section, filename))
    #print(db)       # {'host': 'localhost', 'database': 'test', 'user': 'postgres', 'password': 'riki'}
    return db
params = config()
#print(params)


