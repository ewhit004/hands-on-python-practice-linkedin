import os

#defining variables for enviornment
DEVELOPMENT = "development"
PRODUCTION = "production"
STAGING = "staging"
CODE_SPACE = "code_space"
LOCAL = "local"

#"os.environ.get()" allows us to access the enviornment that we are 
#running on and grab things from there, used for keys and modes; 
#if no specified environment name use "DEVELOPMENT"
current_env = os.environ.get("ENV_NAME", DEVELOPMENT)

#check statements for variables
if current_env == DEVELOPMENT:
    print("Development environment")
elif current_env == PRODUCTION:
    print("Production environment")
elif current_env == STAGING:
    print("Staging environment")
#Note: you can also check if a substring is in a larger string
elif current_env in [CODE_SPACE, LOCAL]:
    print("Codespace or local environment")
else:
    print("Unknown environment")
