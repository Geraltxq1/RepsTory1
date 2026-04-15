from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import database

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


def redirect(url: str, msg: str | None = None, error: str | None = None):
    if msg:
        url += f"?msg={msg}"
    if error:
        url += f"?error={error}"
    return RedirectResponse(url=url, status_code=303)


# 🏠 HOME
@app.get("/", response_class=HTMLResponse)
def home(request: Request, msg: str | None = None, error: str | None = None):
    return templates.TemplateResponse(
        name="index.html",
        context={
            "request": request,
            "msg": msg,
            "error": error
        }
    )


# 👨‍🎓 ESTUDIANTES
@app.get("/estudiantes", response_class=HTMLResponse)
def estudiantes_list(request: Request, msg: str | None = None, error: str | None = None):
    estudiantes = database.listar_estudiantes()

    return templates.TemplateResponse(
        name="estudiantes_list.html",
        context={
            "request": request,
            "estudiantes": estudiantes,
            "msg": msg,
            "error": error
        }
    )


@app.get("/estudiantes/nuevo", response_class=HTMLResponse)
def estudiantes_form(request: Request, error: str | None = None):
    return templates.TemplateResponse(
        name="estudiantes_form.html",
        context={
            "request": request,
            "error": error
        }
    )


@app.post("/estudiantes/nuevo")
def estudiantes_crear(nombre: str = Form(...), documento: str = Form(...)):
    nombre = nombre.strip()
    documento = documento.strip()

    if not nombre or not documento:
        return redirect("/estudiantes/nuevo", error="Campos vacíos")

    ok = database.crear_estudiante(nombre, documento)

    if ok:
        return redirect("/estudiantes", msg="Estudiante creado")
    else:
        return redirect("/estudiantes/nuevo", error="No se pudo crear")


# 📋 ASISTENCIA
@app.get("/asistencia", response_class=HTMLResponse)
def asistencia_list(request: Request, msg: str | None = None, error: str | None = None):
    asistencias = database.listar_asistencias()

    return templates.TemplateResponse(
        name="asistencia_list.html",
        context={
            "request": request,
            "asistencias": asistencias,
            "msg": msg,
            "error": error
        }
    )


@app.get("/asistencia/nueva", response_class=HTMLResponse)
def asistencia_form(request: Request, error: str | None = None):
    estudiantes = database.listar_estudiantes()

    return templates.TemplateResponse(
        name="asistencia_form.html",
        context={
            "request": request,
            "estudiantes": estudiantes,
            "error": error
        }
    )


@app.post("/asistencia/nueva")
def asistencia_crear(
    id_estudiante: int = Form(...),
    fecha: str = Form(...),
    estado: str = Form(...)
):
    ok = database.registrar_asistencia(id_estudiante, fecha, estado)

    if ok:
        return redirect("/asistencia", msg="Asistencia registrada")
    else:
        return redirect("/asistencia/nueva", error="No se pudo registrar")


# 📊 REPORTES
@app.get("/reportes", response_class=HTMLResponse)
def reportes(request: Request):
    resumen = database.resumen_asistencia()

    return templates.TemplateResponse(
        name="reportes.html",
        context={
            "request": request,
            "resumen": resumen
        }
    )