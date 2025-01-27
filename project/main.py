import fastapi
app = fastapi.FastAPI()

@app.get('/')
async def hello():
    return 'hello api'

@app.get('/score/{score}')
async def grade(score):
    score = int(score)
    if score >= 50:
        return 'สอบผ่าน'
    else:
        return 'สอบตก'