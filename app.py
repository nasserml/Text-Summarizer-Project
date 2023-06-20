""" 
from fastapi import FastAPI: Imports the FastAPI class from the fastapi module.

import uvicorn: Imports the uvicorn module, which is a server that can run the FastAPI application.

import sys: Imports the sys module, which provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter.

import os: Imports the os module, which provides a way of using operating system dependent functionality.

from fastapi.templating import Jinja2Templates: Imports the Jinja2Templates class from the fastapi.templating module, which allows using Jinja2 templates in FastAPI.

from starlette.responses import RedirectResponse: Imports the RedirectResponse class from the starlette.responses module, which represents an HTTP redirect response.

from fastapi.responses import Response: Imports the Response class from the fastapi.responses module, which represents an HTTP response.

from textSummarizer.pipeline.prediction import PredictionPipeline: Imports the PredictionPipeline class from the textSummarizer.pipeline.prediction module.

text:str = "What is Text Summarization?": Initializes a string variable text with the value "What is Text Summarization?".

app = FastAPI(): Creates an instance of the FastAPI class and assigns it to the variable app.

@app.get("/", tags=["authentication"]): Decorator that defines a route for the root URL ("/") with the HTTP GET method. The route is associated with the "authentication" tag.

async def index():: Defines an asynchronous function named index.

return RedirectResponse(url="/docs"): Returns a redirect response to the "/docs" URL.

@app.get("/train"): Decorator that defines a route for the "/train" URL with the HTTP GET method.

async def training():: Defines an asynchronous function named training.

try:: Starts a try block.

os.system("python main.py"): Executes the command "python main.py" in the operating system's shell.

return Response("Training successful !!"): Returns an HTTP response with the message "Training successful !!".

except Exception as e:: Handles any exception that occurs in the try block and assigns it to the variable e.

return Response(f"Error Occurred! {e}"): Returns an HTTP response with an error message that includes the exception information.

@app.post("/predict"): Decorator that defines a route for the "/predict" URL with the HTTP POST method.

async def predict_route(text):: Defines an asynchronous function named predict_route that takes a text parameter.

try:: Starts a try block.

obj = PredictionPipeline(): Creates an instance of the PredictionPipeline class and assigns it to the variable obj.

text = obj.predict(text): Calls the predict method of the obj instance, passing the text parameter, and assigns the result back to the text variable.

return text: Returns the predicted text.

except Exception as e:: Handles any exception that occurs in the try block and assigns it to the variable e.

raise e: Raises the exception again.

if __name__=="__main__":: Checks if the script is being executed as the main module.

uvicorn.run(app, host="0.0.0.0", port=8080): Starts the UVicorn server to run the FastAPI application on the specified host and port.

In summary, this code sets up a FastAPI application with routes for the root URL ("/"), a "/train" URL, and a "/predict" URL. It defines functions to handle requests to these routes, including redirecting to the documentation page, running a training process, and predicting text summaries using the PredictionPipeline class. Finally, it starts the UVicorn server to run the FastAPI application.

"""

from fastapi import FastAPI , Request
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummarizer.pipeline.prediction import PredictionPipeline
from fastapi.staticfiles import StaticFiles



text: str = "What is Text Summarization?"

app = FastAPI()
templates = Jinja2Templates(directory="swagger")

# Mount the static files directory to serve the Swagger UI assets
app.mount("/static", StaticFiles(directory="swagger/static"), name="static")

@app.get("/", tags=["authentication"])
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful !!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")

@app.post("/predict")
async def predict_route(text):
    try:
        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
    

""" 
Imports the necessary dependencies:

FastAPI: A web framework for building APIs quickly.
uvicorn: A lightning-fast ASGI server for running the FastAPI application.
sys: Provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter.
os: Provides a way of using operating system-dependent functionality.
Jinja2Templates: Templating engine for FastAPI to render HTML templates.
RedirectResponse: A response class for redirecting requests to a different URL.
Response: A response class for returning plain text or HTML responses.
Defines a string variable text with the value "What is Text Summarization?".

Creates an instance of the FastAPI application.

Defines an endpoint for the root URL ("/") with the "authentication" tag. This endpoint redirects to the "/docs" URL, which is the FastAPI documentation page.

Defines an endpoint for the "/train" URL. When accessed with a GET request, it attempts to run the command "python main.py" to trigger the training process. It returns a response indicating whether the training was successful or an error occurred.

Defines an endpoint for the "/predict" URL. When accessed with a POST request, it creates an instance of the PredictionPipeline class and calls the predict method to generate a text summary based on the provided text. It returns the generated summary as the response.

Checks if the script is being run directly and starts the FastAPI application using the uvicorn.run function with the host set to "0.0.0.0" and the port set to 8080.

This code sets up a FastAPI application with endpoints for redirecting, training a model, and making predictions. The application listens on the specified host and port when run directly.
"""