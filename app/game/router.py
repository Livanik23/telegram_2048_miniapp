from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.game.dao import UserDAO
from app.game.schemas import TelegramIDModel, SetBestScoreRequest, SetBestScoreResponse

router = APIRouter(prefix='', tags=['ИГРА'])
templates = Jinja2Templates(directory='app/templates')

@router.get("/", response_class=HTMLResponse)
async def game_page(request: Request):
    """Главная страница с игрой 2048"""
    return templates.TemplateResponse("pages/index.html", {"request": request})

@router.get("/records", response_class=HTMLResponse)
async def records_page(request: Request, session: AsyncSession = Depends(get_session)):
    """Страница с рекордами"""
    # Получаем топ-20 игроков
    top_players = await UserDAO.get_top_scores(session=session, limit=20)
    return templates.TemplateResponse("pages/records.html", {
        "request": request,
        "top_players": top_players
    })

@router.put("/api/bestScore/{user_id}", response_model=SetBestScoreResponse, summary="Set Best Score")
async def set_best_score(
    user_id: int,
    request: SetBestScoreRequest,
    session: AsyncSession = Depends(get_session)
):
    """
    Установить лучший счет пользователя.
    Обновляет значение `best_score` в базе данных для текущего `user_id`.
    """
    score = request.score

    user = await UserDAO.find_one_or_none(session=session, filters=TelegramIDModel(telegram_id=user_id))

    if not user:
        return SetBestScoreResponse(status="error", best_score=0)

    # Обновляем только если новый результат лучше текущего
    if score > user.best_score:
        user.best_score = score
        await session.commit()

    return SetBestScoreResponse(status="success", best_score=user.best_score)

@router.get("/api/user/{user_id}/rank")
async def get_user_rank(user_id: int, session: AsyncSession = Depends(get_session)):
    """Получить ранг пользователя"""
    rank_info = await UserDAO.get_user_rank(session=session, telegram_id=user_id)
    return rank_info if rank_info else {"rank": 0, "best_score": 0}

@router.get("/api/top-scores")
async def get_top_scores(session: AsyncSession = Depends(get_session)):
    """Получить топ игроков"""
    return await UserDAO.get_top_scores(session=session, limit=20)
