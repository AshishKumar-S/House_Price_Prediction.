step-1: we need to install the Docker desktop

I Upload the file in doogle classroom
            Download

step-2: we need to create a Dockerfile for guidelines
    1. install the python
      we will give the python image with version
    2. we will create a folder
    3. we will copy all the files
        at a time or one by one
    4. we will install the requirements.txt
    5. Last we will write how to run command 

step-3:
        Open Docker desktop
        skip email
        if you get wsl error
        run below command in CMD 

wsl --update
wsl --set-default-version 2
wsl --version

step-4: In your CMD first go to your CWD
        docker build -t california-app .

        docker build -t <app_name>

        It will run all the commands 5-10mins

step-5: If image successfully available we can check
        in cmd type
        docker images (then we can able to see california-app)


step=6: docker run -p 8000:8000 <app_name>
        docker run -p 8000:8000 california-app


docker run -d -p 8000:8000 fastapi-app



step-7: http://127.0.0.1:8000/predict