# Imagine you are developing a food delivery app
# The application can run in three envs
# Dev
# Test
# Prod

#Define configuration class

class DevConfig:
    database ="sqlite.db"
    debug = True
class TestConfig:
    database = "test.db"
    debug = True
class ProdConfig:
    database = "mysql://food_app"
    debug = False

#Step2: Define a config Factory 

def get_config(env):
    if env == "dev":
        return DevConfig()
    elif env == "test":
        return TestConfig
    else:
        return ProdConfig()

#Step3: Use the factory

env = "Production"

config = get_config(env)

print(config.database)
print(config.debug)