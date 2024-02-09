from fastapi import APIRouter


router = APIRouter(
    tags=["Test"],
)

@router.get('/test')
def get_test():
    return {'test': 'test'}
