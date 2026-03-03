import json
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

# === ABSOLUTE IMPORTS (fixed for easy running) ===
from database import engine, get_db
from models import Base, Form, Response
from schemas import FormCreate, FormUpdate, FormResponse, ResponseCreate, ResponseResponse

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Pseudo Google Forms API")

# CORS (allows frontend to call backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/forms", response_model=FormResponse)
def create_form(form: FormCreate, db: Session = Depends(get_db)):
    db_form = Form(
        title=form.title,
        form_json=json.dumps(form.form_json)
    )
    db.add(db_form)
    db.commit()
    db.refresh(db_form)
    db_form.form_json = json.loads(db_form.form_json)
    return db_form

@app.get("/api/forms", response_model=list[FormResponse])
def list_forms(db: Session = Depends(get_db)):
    forms = db.query(Form).all()
    for f in forms:
        f.form_json = json.loads(f.form_json)
    return forms

@app.get("/api/forms/{form_id}", response_model=FormResponse)
def get_form(form_id: int, db: Session = Depends(get_db)):
    form = db.query(Form).filter(Form.id == form_id).first()
    if not form:
        raise HTTPException(status_code=404, detail="Form not found")
    form.form_json = json.loads(form.form_json)
    return form

@app.put("/api/forms/{form_id}", response_model=FormResponse)
def update_form(form_id: int, form_update: FormUpdate, db: Session = Depends(get_db)):
    form = db.query(Form).filter(Form.id == form_id).first()
    if not form:
        raise HTTPException(status_code=404, detail="Form not found")
    form.title = form_update.title
    form.form_json = json.dumps(form_update.form_json)
    db.commit()
    db.refresh(form)
    form.form_json = json.loads(form.form_json)
    return form

@app.post("/api/forms/{form_id}/responses", status_code=status.HTTP_201_CREATED)
def submit_response(form_id: int, response: ResponseCreate, db: Session = Depends(get_db)):
    form = db.query(Form).filter(Form.id == form_id).first()
    if not form:
        raise HTTPException(status_code=404, detail="Form not found")
    db_response = Response(
        form_id=form_id,
        answers_json=json.dumps(response.answers_json)
    )
    db.add(db_response)
    db.commit()
    return {"message": "Response submitted successfully"}

@app.get("/api/forms/{form_id}/responses", response_model=list[ResponseResponse])
def get_responses(form_id: int, db: Session = Depends(get_db)):
    responses = db.query(Response).filter(Response.form_id == form_id).all()
    for r in responses:
        r.answers_json = json.loads(r.answers_json)
    return responses