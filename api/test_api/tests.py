from fastapi import APIRouter
from database.testservice import get_question_db, add_question_db, get_10_leaders_db


test_router = APIRouter(prefix='/test', tags=["API for tests"])


@test_router.get('/top-10-leaders')
async def get_10_leaders():
    return get_10_leaders_db()


@test_router.get("/question")
async def get_question():
    return get_question_db()


@test_router.get("/add-question")
async def add_question(main_question: str, v1: str, v2: str, v3: str, v4: str, correct_answer: int):
    add_q = add_question_db(main_question, v1, v2, v3, v4, correct_answer)
    return add_q
