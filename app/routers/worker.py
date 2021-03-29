from fastapi import APIRouter
from fastapi import BackgroundTasks
from starlette.responses import JSONResponse

from app.schemas.worker import Task
from app.worker import Worker

router = APIRouter()

worker = Worker()


@router.post('/create', tags=['worker'])
async def create_task(task: Task, background_tasks: BackgroundTasks):
    if not worker.run:
        worker.run = True
        background_tasks.add_task(worker.start_worker)

    await worker.add_task(num=task.num, timeout=task.timeout)

    return JSONResponse(
        {'message': 'Task added'},
        status_code=201
    )


@router.get('/results', tags=['worker'])
async def get_results():
    return JSONResponse(
        {'results': worker.results},
        status_code=200
    )


@router.get('/tasks', tags=['worker'])
async def get_tasks():
    return JSONResponse(
        {'tasks': await worker.get_tasks()},
        status_code=200
    )
