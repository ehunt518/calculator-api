from fastapi import FastAPI, status, HTTPException

app = FastAPI()
# test


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

    try:                 #check for correct inputs
        a = float(a)
        b = float(b)

    except ValueError:   #raise an expception if inputs are not integers or floats
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="both inputs must be numeric, you can even add a decimal!")

    return {"result": a + b}

@app.get("/subtract/{a}/{b}", status_code=200)
def subtract(a : str, b : str):
    """
    subtract two numbers.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """

    try:                 #check for correct inputs
        a = float(a)
        b = float(b)

    except ValueError:   #raise an expception if inputs are not integers or floats
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="both inputs must be numeric, you can even add a decimal!")

    return {"result": a - b}


@app.get("/multiply/{a}/{b}", status_code=200)
def multiply(a : str, b : str):
    """
    multiply two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """

    try:                 #check for correct inputs
        a = float(a)
        b = float(b)

    except ValueError:   #raise an expception if inputs are not integers or floats
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="both inputs must be numeric, you can even add a decimal!")

    return {"result": a * b}

@app.get("/divide/{a}/{b}", status_code=200)
def divide(a : str, b : str):
    """
    divide two numbers.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """

    try:                 #check for correct inputs
        a = float(a)
        b = float(b)

    except ValueError:   #raise an expception if inputs are not integers or floats
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="both inputs must be numeric, you can even add a decimal!")

    return {"result": a / b}


@app.get("/double/{a}", status_code = 200)
def double(a : str):
    """

    Take one number and double it

    Parameters:
        a: number to double
    
    returns:
    Json object as the result

    """

    try:    #check for correct inputs
        a = float(a)

    except ValueError:  #if inputs not correct explain the problem and ask user to try again
        raise HTTPException(status_code = status.HTTP_422_UNPROCESSABLE_ENTITY, detail = "the input must be a number, please try again")

    return {"result": a * 2}


@app.get("/power/{a}/{b}", status_code = 200)
def power(a : str, b : str):

    """

    This is going to take a and put it to the power of b

    parameter:
    -   a: first number(base)
    -   b: second number(power)

    """

    try:    #check for correct inputs
        a = float(a)
        b = float(b)

    except ValueError:  #if incorrect inputs explain what happened and tell them to try again

        raise HTTPException(status_code = status.HTTP_422_UNPROCESSABLE_ENTITY, detail = "both inputs must be numbers, decimals count! try again.")

    return {a ** b}

@app.get("/mean/{a}/{b}/{c}/{d}")
def notnice(a : str, b : str, c : str, d : str):

    """
    This operation will take the mean of four numbers
        not more and not less
    
    parameters:
    -   a: number 1
    -   b: number 1
    -   c: number 1
    -   d: number 1

    """

    try:

        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)

    except:
        
        raise HTTPException(status_code = status.HTTP_422_UNPROCESSABLE_ENTITY, detail = "All four inputs must be numbers, decimals are allowed, try again." )

    #create the product of all numbers for shorter return line
    M = a + b + c + d

    return {M / 4}
    