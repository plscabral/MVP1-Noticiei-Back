from fastapi import FastAPI, APIRouter, Depends
from dtos.request import TermReqModel
from dtos.response import UserResModel
from entities import Term, UserTerm, Session
from utils import auth

router = APIRouter(prefix='/terms', tags=["Termos"])

@router.get("")
def get_terms(user: UserResModel = Depends(auth.get_user_logged)):
    session = Session()
    user_terms: list[UserTerm] = session.query(UserTerm).filter(UserTerm.user_id == user.id).all()
    users = [user.term for user in user_terms]
    session.close()
    return users


@router.delete("/{id}")
def delete_term_by_id(id: int, user: UserResModel = Depends(auth.get_user_logged)):
    session = Session()
    term = session.query(Term).filter(Term.id == id).first()
    user_term = session.query(UserTerm).filter(UserTerm.term_id == id).first()
    session.delete(user_term)
    session.commit()
    session.delete(term)
    session.commit()
    session.close()
    return {"success": True, "message": "Termo deletado com sucesso!"}


@router.post("", status_code=201)
def create_term(model: TermReqModel, user: UserResModel = Depends(auth.get_user_logged)):
    session = Session()
    term = session.query(Term).filter(Term.description == model.description).first()

    if not term:
        term = Term(description=model.description)
        session.add(term)
        session.commit()

    user_term = session.query(UserTerm).filter(UserTerm.term_id == term.id).first()

    if not user_term:
        user_term = UserTerm(user.id, term.id)
        session.add(user_term)
        session.commit()

    session.close()
    return {"success": True, "message": "Termo criado com sucesso!"}


def include_route(app: FastAPI):
    app.include_router(router)
