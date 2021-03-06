from sanic import Sanic
from sanic.response import text

app = Sanic("My Hello, world app")


@app.get("/")
async def hello_world(request):
    return text("Hello, world.")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
