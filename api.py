from fastapi import UploadFile, File, APIRouter
import shutil


image_router = APIRouter()


@image_router.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(...)):
    try:
        with open(f"{file.filename}", 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception:
        return {'message': 'Файл не загрузился!'}
    finally:
        file.file.close()

    return {"message": f'Файл {file.filename} успешно загружен!'}

