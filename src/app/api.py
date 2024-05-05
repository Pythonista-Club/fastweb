from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def get_root():
    """_summary_
    Baseline method of the application
    """

    return {"resp":"Welcome for the Pythonista Club! "} 
