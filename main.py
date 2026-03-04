from fastapi import FastAPI, status, HTTPException

app = FastAPI()


@app.get("/", status_code=200)
def read_root():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/add/{a}/{b}", status_code=200)
def add(a : str, b : str):
    """
    Add two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """

    try:                 #make sure user isn't stupid
        a = float(a)
        b = float(b)

    except ValueError:   #raise an expception if user is not smart
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="both inputs must be numeric, you can even add a decimal!")

    return {"result": a + b}
