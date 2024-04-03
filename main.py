from fastapi import FastAPI, Request
from returns.maybe import Maybe
from starlette.responses import RedirectResponse

app = FastAPI()


@app.get("/")
def redirect_form(request: Request, form: str, entry: str):
    ip_param = (
        Maybe.from_optional(request.client)
        .map(lambda client: client.host)
        .map(lambda ip: f"&entry.{entry}={ip}")
        .value_or("")
    )
    return RedirectResponse(
        f"https://docs.google.com/forms/d/e/{form}/viewform?usp=pp_url{ip_param}"
    )
