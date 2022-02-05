## Description

This project is used for storing information about houseplants, with all basic CRUD operations for database implemented. 
Application was developed using python django, HTML5 and CSS. Docker image of the app has been built and deployed to dockerhub. The project has been deployed as Azure App service using built image. All steps of deployment are described later in this document.

![image](https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/various-beautiful-green-plants-in-pots-on-white-royalty-free-image-931824676-1565950537.jpg?crop=0.825xw:0.620xh;0.0785xw,0.132xh&resize=1200:*)

## Tools and software :hammer:
- [Visual Studio Code](https://code.visualstudio.com/)
- [Python 3.9.7] (https://www.python.org/downloads/)
- [Django 2+] (https://www.djangoproject.com/)
- [Docker](https://www.docker.com/) 🐋
- [Azure CLI] (https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)


## Build and deployment steps :rocket:
1. Get app from https://github.com/SailorMoonCrystal/cloud_wsb
2. Be sure you have files as showed on picture

![image](https://i.ibb.co/fH249Wx/project-structure.png)
3. Create docker image from the project. After -t give your repository/image name
```bash
docker build -f Dockerfile -t  kristina12131415/flowershop:latest 
```
4. Push image to your dockerhub repository
```bash
docker push kristina12131415/flowershop:latest
```
5. Login to azure. The login page will open in your default browser
```bash
az login
```
6. Create resource group
```bash
az group create --name wsb-cloud --location "West Europe"
```
7. Create app service plan
```bash
az appservice plan create --name wsb-cloud-project --resource-group wsb-cloud --sku S1 --is-linux
```
8. Create Azure App Service from your docker image
```bash
az webapp create --resource-group wsb-cloud --plan wsb-cloud-project --name flowers-alekseyenko --deployment-container-image-name kristina12131415/flowershop:latest
```
9. Modify app to ensure gunicorn is listening on port 8000
```bash
az webapp config appsettings set --resource-group wsb-cloud --name flowers-alekseyenko --settings WEBSITES_PORT=8000
```

Server should be available at https://flowers-alekseyenko.azurewebsites.net/plants/ :globe_with_meridians:

## Environment variables
### Application
- `SECRET_KEY` - `str` - defaults to `secret` (unused)
- `DATABASE_URL` - `str` - defaults to `project.sqlite3` in the root project path.
- `DEBUG` - `bool` - `True` for development, `False` for production (default).
- `ALLOWED_HOSTS` - `list` - is set to wildcard.