from fastapi import Depends, FastAPI, HTTPException
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.utils import get_openapi

from sqlalchemy.orm import Session

from database import SessionLocal, engine
import models, schemas, crud


app = FastAPI(docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Race Tracker",
        version="1.0.0",
        summary="API for my typing speed tracker",
        description="this is a leveling system I made to take my minimum typing speed",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.put("/", response_model=schemas.GetSpeedLevel)
async def calc_speed(speed_obj: schemas.UpdateSpeed, db: Session = Depends(get_db)):
    level = db.query(models.Speed).first()

    if not speed_obj.is_ghost:
        if speed_obj.speed >= level.speed:
            level.state, checkpoint = crud.update_state(True, level.state)

        else:
            level.state, checkpoint = crud.update_state(False, level.state)

    else:
        level.state = crud.update_state_ghost(level.state, speed_obj.ghost_level, level.speed, speed_obj.speed)


    level.speed, level.state = crud.update_speed(level.speed, level.state)

    db.commit()

    return {
        'speed': level.speed,
        'state': level.state
    }

    # if score > curr_speed:

    
