from fastapi import FastAPI
from pydantic import BaseModel
import geo
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

class input2(BaseModel):
    s : str
    d : str

@app.post("/routeDetails")
def route(inp : input2):
    cost, dist, ntolls, geometry = geo.get_toll_geo(inp.s, inp.d)

    print(geometry)
    return {
        "cost" : cost,
        "dist" : dist,
        "ntolls": int(ntolls),
        "geometry":geometry
    }

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=4000)

