# DISCLAIMER
- A lot of the stuff I've done here I had to learn on the fly. There will, doubtlessly, be some *(possibly many many)* errors but I tried to focus a lot on infrastructure and architecture.

- I've given some justifications for my choices in the last section.

# RUNNING THE APP 

## Running on Jenkins

To run this on Jenkins, you can add parameters to Jenkins secrets and run the `create_env_file.sh` to create a .env file with secrets before the build, test and deploy stages

## Running on docker container in local machine

### Loading secrets
To load all secrets, create a `.env` file like below. This file should go in the same directory as this README. This should contain all the app secrets. I didn't have time to so sth detailed so I only used the bare minimum to run the application ie:

```
####################################
#   ELASTIC SEARCH
####################################
ELASTIC_PASSWORD="root"
ELASTIC_PORT="9200"
ELASTIC_HOST="elasticsearch"
ELASTIC_INDEX_NAME="identity"
ELASTIC_APM_SERVER_URL="http://apm-server:8200"

####################################
#   TESTS
####################################
TEST_INDEX_NAME="test_identity"
TEST_ELASTIC_PORT="9200"
TEST_ELASTIC_HOST="localhost"
TEST_ELASTIC_APM_SERVER_URL="http://localhost:8200"
```

### Loading the test Elasticsearch instance
In the `scripts` folder in the `backend`, there is a `create_db.sh` file that can be run to create an elastic search instance. I used random names and IDs so creating an instance manually under the name test_identity should work fine as well.


### Exposed ports
The exposed ports are `3000` for the front end, `8000` for the backend, `5601` for kibana and `9200` for elastic search.


### Running the container
To run the app, install [Docker Compose](https://docs.docker.com/compose/install/) and run the command:
```
docker-compose up --build -d
```

If you want the logs printed out, you can run
```
docker-compose up --build
```

### Running Tests
You may have to create a `log` folder in the scripts folder to run the backend. This seems to be a weird feature when testing apps with logs on FastAPI. Would love to look into it but I'm not sure what more I could do.

## Some justification for choices

### Devops
 **1) Jenkins**
 - I wanted to build a full pipeline. Granted, I've probably made some errors but I at least wanted to do something fully self-contained and usable out of the box.

**2) Using .env file for config**
- I should probably have looked more into security but seeing how many different parts I wanted to include, I just didn't have the time. I went with the simplest thing I could find.

- I don't know how secure this is in an actual production environment considering the prod environment variables can be kept as secrets on Jenkins and loaded during the build.

**3) Docker compose settings**
- I got these from the official elastic recommendations for [FastAPI](https://github.com/elastic/elasticsearch-py/tree/main/examples/fastapi-apm). A lot of the configs I understand but would not have been able to do on my own from scratch if I'm completely honest.

### Backend

 **1) Elastic Search**
 - We spoke a bit about this in the interview so I decided to try it out. I've seen that there were other options like FTS in PostgreSQL but I wanted to remain consistent with the stack used at FRISS for this specific part.

 **2) Poetry over pip**
 - I wanted to try to use poetry in Docker as opposed to pip just to be sure that I could handle it. I have never used poetry and was looking for an opportunity to do so.

**3) FastAPI over Django**
- Newer, faster and more lightweight framework. Also have never really used dependencies and I think this was a great intro to the former.

**4) ES Caching**
- I didn't really have time to look for anything else. Also, during the interview, I asked about this and Mindo & Andre explained that Redis wasn't heavily used so I went with ES default caching. It seems fairly powerful but I guess I would have to ask the guy that did it at Friss :) 

**5) Config JSON**
- This was a first attempt at having dynamic matching rules. First principles thinking would mean defining the parameters we intend to modify before implementation. Going with JSON inherently means selecting mongodb as the choice for storing configs.

**6) Logging**
- I only used the loggers to catch errors. Maybe not the best approach but I honestly would love to learn more about this.

### Frontend
 **1) React over Vue**
 - I was already having to learn Elastic Search and poetry in docker(which turned out to be a bit of a pain.) By the time the weekend was over I didn't have time to start learning Vue. Also, my front end is atrocious. (Please don't judge me!) I just didn't have time to do everything I would have wanted to do.


## Stuff I couldn't finish

**1) Dynamic elastic `rescore` algorithm and UI matching rules**

I wanted to finish this but it was late and I knew I would have trouble so I just did the first part to indicate that I could and left it at that.

As mentionned I was much more worried about the infrastructure and architecture than the implementation of the code itself. Might be a bad thing in hindsight but I really did want to have an app that could run independently without fail.
